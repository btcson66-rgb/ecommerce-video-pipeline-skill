---
name: fantini-shopee-video-pipeline
description: >-
  MANDATORY standard operating procedure (SOP) for producing vertical commercial
  short videos (9:16, 1080x1920, 30fps CFR) for multi-brand products (Fantini
  Pelletteria leather bags, ESPNER eyewear/sunglasses, etc.). Every video MUST be
  composed of 3 distinct real AI videos: S1 (Gemini App Veo lifestyle action), S2
  (Gemini/Flow ambient close-up push-in), and S3 (Google Flow Omni 1.1 Flash 3D
  turntable rotation showcase). Pure static image slideshows or single-scene videos
  are STRICTLY PROHIBITED.
---

# 精品短影音自動化製片標準作業流程 (SOP) — 多品牌通用旗艦版

> ⚠️ **【鐵律：絕對禁止偷懶與拼湊】**  
> 1. **每部成片必須且只能由 3 段截然不同的真實 AI 影片組成**：  
>    - **S1（Gemini App）**：生活實穿動態（歐風街拍、商務走廊、網球場漫步）。  
>    - **S2（Gemini / Flow）**：精品休憩置放與平滑推鏡特寫（咖啡座木桌、場邊長椅）。  
>    - **S3（Google Flow 3D 轉盤）**：360° 旋轉展示特寫（最短 5 秒省點數 + Asset Chips 真品標籤）。  
> 2. **嚴禁純靜態圖片運鏡（Ken Burns / Zoompan）冒充主片**！  
> 3. **嚴禁只做 1 段或 2 段就草率結案，S3 轉盤特寫鏡頭絕不可缺席**！

---

## 一、標準 3 段式鏡頭分工與純廣告規範

### 1. 標準 3 段式鏡頭分工架構（S1 + S2 + S3）
- **S1（Gemini App 實穿動態，8 秒 9:16）**：
  - **包款**：都會街頭漫步、商務走廊步入，展示肩背/手提自然擺動（只拍外觀穿搭，**絕不拍零錢包內部掀蓋或拉鍊微距結構**）。
  - **運動墨鏡**：陽光網球場、運動賽道漫步與單手扶鏡特寫。
  - **復古墨鏡**：海濱棕櫚大道漫步、陽光街頭穿搭。
- **S2（Gemini / Flow 特寫推軌，5～8 秒 9:16）**：
  - **包款**：露天咖啡座木桌置放，陽光灑落皮革紋理與五金細節。
  - **墨鏡**：精品露天咖啡座木桌搭配冰咖啡，平滑推鏡特寫手工金屬鏡框與 G-15 鏡片；或場邊長椅搭配球拍特寫。
- **S3（Google Flow 3D 轉盤旋轉，5 秒 9:16 最短秒數省點數）**：
  - 在展示台上 360° 旋轉展示，搭配多色切換介紹或單色完整環繞。

### 2. 純商品官方廣告模式（預設「去蝦皮化」Pure Brand Commercial）
- 除非使用者特別要求標註蝦皮，否則一律採用**純品牌官方形象廣告模式**。
- 頂部膠囊、底部字幕卡、導購 CTA 按鈕、旁白配音與 `caption.txt` **嚴禁出現任何「蝦皮」字樣**，統一標註「官方旗艦限定 / 現貨」、「點擊下方探索 / 選購」。

---

## 二、Step 1：真品圖片抓取、AI 友善預處理與雙重驗證

1. **抓取高畫質真品原圖與核對特徵**：
   - 記錄真實品牌（`FANTINI`、`ESPNER` 等）、型號、價格、現貨色系與細節特徵。
2. **預先整理 AI 友善識別參考圖（Pre-processing Reference Image）**：
   - 使用 [`scripts/preprocess_ai_ref.py`](./scripts/preprocess_ai_ref.py) 將商品主圖去除促銷文字邊框，置中並輸出為乾淨純背景的 1024×1024 RGB 圖像（`*_gemini_studio.jpg` 或 `*_gemini_hero.jpg`），防止 AI 辨識尺寸失真。
3. **雙重驗證（防錯配 + 防黑屏）**：
   - 必須使用 `read_file` 親眼檢視參考圖，確認 100% 吻合真實商品。
   - 執行 [`scripts/validate_assets.py`](./scripts/validate_assets.py) 確認圖片為 `RGB` 模式（嚴禁直接使用 `RGBA` 透明去背圖）。

---

## 三、Step 2：Gemini (Veo) 與 Google Flow (Omni 1.1 Flash) 雙引擎生成規範

### 1. 防範 Gemini 多輪對話快取汙染（Session Isolation 鐵律）
- 更換商品時，在 Gemini App **必須開啟全新對話（New Chat）**，防止後端快取誤用前一款商品的圖片。
- 影片下載後，**必須立即使用 `ffmpeg` 抽取影格並以 `read_file` 親眼查驗**。若款式被舊對話汙染或細節不符，立即改用 Google Flow 重新生成。

### 2. Google Flow 最短秒數省點數 + Asset Chips 精準控制
- **S3 片尾 3D 轉盤 360° 旋轉展示（必用 Google Flow）**：
  - 上傳真品圖後，**必須在輸入框下方點擊「在提示詞輸入框新增素材」，勾選真品圖插入為條件標籤（Asset Chips）**。
  - **設定最短秒數（5 秒）** 以節省點數消耗，後製透過 FFmpeg `setpts` 平滑慢動作展延至配音所需長度。
- **Gemini 額度用盡或需精準特寫時無縫接力**：
  - 若 Gemini 達每輪 3 部上限（冷卻 5 小時），S1 / S2 直接由 Google Flow 接力生成，無須空等。

---

## 四、Step 3：沉穩男聲配音與 FFmpeg「零截斷、零定格」雙版本壓製

標準自動化壓製腳本：[`scripts/render_video_template.py`](./scripts/render_video_template.py)

1. **配音標準（語音零截斷）**：
   - 統一使用 `edge-tts` 正式沉穩台灣男聲：**`zh-TW-YunJheNeural`**（`rate="-1%"`, `pitch="-2Hz"`）。
   - **完全解除 24 秒硬性限制**：段落長度由完整句長動態決定（`target_dur = audio_dur + 0.8s`，含 `adelay=350|350` 與句尾呼吸留白），嚴禁使用 `atrim` 截斷配音。
2. **畫面平滑延伸（絕不定格 Zero Freeze Frame）**：
   - **嚴禁使用 `tpad=stop_mode=clone` 尾幀定格**！
   - 當原始影片秒數（如 5s 或 8s）短於段落目標秒數時，一律採用 **`setpts=(seg_dur/v_dur)*PTS`** 平滑動態慢動作延伸，或搭配平滑推鏡放大，確保鏡頭全程動態運鏡。
   - 強制輸出規格：`1080x1920`、`-r 30`（30.0 fps CFR 恆定幀率）、`libx264`、`yuv420p`。
3. **雙版本同步產出（多色版 + 單色 360° 旋轉版）**：
   - **`final.mp4`**：S1 + S2 + S3（多色款式切換圖卡）。
   - **`final_single_color.mp4`**：S1 + S2 + S3（單一主打色 360° 旋轉展示圖卡）。
4. **成片視覺抽檢**：
   - 抽取 `final_check_s1.jpg`、`final_check_s2.jpg`、`final_check_s3.jpg`，使用 `read_file` 親眼查驗。

---

## 五、Step 4：Google Drive 雲端硬碟 7 件組白名單交付

1. **標準 7 件組清單**：
   - `final.mp4`（多色介紹版）
   - `final_single_color.mp4`（單色 360° 旋轉版）
   - `cover.jpg`（1080×1920 高質感封面）
   - `caption.txt`（官方社群文案與 Hashtags，去蝦皮化）
   - `title.txt`（SEO 標題）
   - `product_url.txt`（商品網址）
   - `qa.json`（品質檢驗通過紀錄）
2. **白名單上傳流程**：
   - 複製 7 個檔案至 `C:\Users\User\AppData\Local\Temp\<Product_ID>\`。
   - 於 Google Drive `02_手機待發布` 建立子資料夾（`<編號>_<品牌>_<商品簡稱>`）並完成上傳。
