"""Fantini 蝦皮短影音資產與成片自動驗證工具
用法：
  python validate_assets.py --images d:/蝦皮/assets/F002/verified
  python validate_assets.py --video d:/蝦皮/work/F002/final.mp4
"""
import argparse, json, subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image


def check_images(folder: Path):
    print(f"=== 檢查商品圖片目錄: {folder} ===")
    files = list(folder.glob("*.jpg")) + list(folder.glob("*.png"))
    if not files:
        print("[ERROR] 目錄下找不到任何圖片！")
        sys.exit(1)
    for f in files:
        im = Image.open(f)
        arr = np.array(im.convert("RGB"))
        mean_val = float(arr.mean())
        status = "OK"
        if im.mode == "RGBA":
            status = "WARNING: RGBA 透明圖 (直接轉碼會變黑底，請改用 RGB 實拍圖)"
        elif mean_val < 40:
            status = "ERROR: 圖片過暗或黑底"
        print(f"  - {f.name}: size={im.size}, mode={im.mode}, mean_brightness={mean_val:.1f} -> [{status}]")


def check_video(video_path: Path):
    print(f"=== 檢查成片品質與防重複: {video_path} ===")
    if not video_path.exists():
        print(f"[ERROR] 找不到影片: {video_path}")
        sys.exit(1)

    raw = subprocess.check_output([
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_streams", "-show_format", str(video_path)
    ])
    meta = json.loads(raw)
    v_stream = [s for s in meta["streams"] if s["codec_type"] == "video"][0]
    dur = float(meta["format"]["duration"])
    w, h = int(v_stream["width"]), int(v_stream["height"])
    fps = v_stream["r_frame_rate"]
    print(f"  規格: {w}x{h} | FPS: {fps} | 時長: {dur:.2f}s")

    if w != 1080 or h != 1920:
        print("[ERROR] 解析度不符 1080x1920！")
    if dur < 20.0 or dur > 60.5:
        print(f"[WARNING] 影片長度 ({dur:.2f}s) 不在 20~60s 建議區間內！")

    # 依每 8 秒一段抽樣中心幀 (4s, 12s, 20s, 28s...)
    num_segments = int(round(dur / 8.0))
    frames = []
    for i in range(num_segments):
        t = i * 8 + 4
        if t >= dur:
            break
        tmp_png = video_path.parent / f"_qa_frame_{t}s.png"
        subprocess.run([
            "ffmpeg", "-y", "-ss", str(t), "-i", str(video_path),
            "-frames:v", "1", str(tmp_png)
        ], capture_output=True)
        im = Image.open(tmp_png).convert("RGB")
        arr = np.array(im, dtype=np.float32)
        mean_val = float(arr.mean())
        print(f"  段落 S{i+1} ({t}s): 平均亮度 = {mean_val:.1f} {'[OK]' if mean_val > 50 else '[ERROR: 疑似黑畫面!]'}")
        frames.append((i + 1, t, arr))
        tmp_png.unlink(missing_ok=True)

    # 比對相鄰段落是否重複或過度相似 (裁切中段無字幕區域 Y: 300~1300)
    for idx in range(len(frames) - 1):
        s_a, t_a, arr_a = frames[idx]
        s_b, t_b, arr_b = frames[idx + 1]
        crop_a = arr_a[300:1300, :, :]
        crop_b = arr_b[300:1300, :, :]
        diff = float(np.mean(np.abs(crop_a - crop_b)))
        print(f"  段落差異度 S{s_a} vs S{s_b}: MAE = {diff:.1f} {'[OK: 場景不同]' if diff > 25 else '[WARNING: 畫面疑似重複或過度雷同!]'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--images", type=Path, help="檢查圖片資料夾")
    parser.add_argument("--video", type=Path, help="檢查輸出 MP4 影片")
    args = parser.parse_args()
    if args.images:
        check_images(args.images)
    if args.video:
        check_video(args.video)
