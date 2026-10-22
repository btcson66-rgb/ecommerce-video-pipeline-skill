# 🎬 AI E-Commerce Short Video Pipeline Skill (精品電商短影音自動化製片技能)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Antigravity / Agents](https://img.shields.io/badge/Platform-Antigravity%20%7C%20Agentic%20AI-orange.svg)](#)
[![Format: 9:16 Vertical Video](https://img.shields.io/badge/Format-9%3A16%201080x1920%2030fps%20CFR-green.svg)](#)

> **生產級「純品牌形象短影音」全自動化製片 SOP 與渲染引擎**  
> 專為精品包款（皮件、托特包、馬鞍包）、太陽眼鏡/偏光墨鏡、鐘錶飾品等電商產品打造的直向短影音（9:16, 1080x1920, 30fps CFR）自動化技能。  
> 支援 **Google Antigravity**、**Claude Code**、**Cursor**、**Codex** 及任何通用 AI Agent 系統。

---

## 🌟 核心特色 (Key Features)

### 1. 🔕 純商品官方形象廣告模式 (Default Pure Brand Commercial Mode)
- **跨平台一鍵通用**：預設為**去蝦皮化/無第三方平台標籤**的純品牌廣告規格。
- 頂部質感膠囊、底部字幕卡、導購 CTA 按鈕、口播配音及發布文案一律採用「官方旗艦限定 / 現貨」設計，影片產出後可直接投放於 **Instagram Reels**、**TikTok**、**YouTube Shorts**、**Facebook**、**品牌官網**及**蝦皮短影音**。

### 2. 🎞️ 畫面絕不定格 (Zero Freeze Frame)
- **告別僵硬停頓**：嚴格拋棄傳統 `tpad=stop_mode=clone` 尾幀凍結做法。
- 當 AI 生成之生活影片（5 秒或 8 秒）與配音所需長度不一致時，引擎統一採用 **`setpts=(target_dur/in_dur)*PTS`** 進行平滑動態慢動作展延或 **`zoompan`** 慢速推鏡放大，確保鏡頭全程動態運鏡不卡頓。

### 3. 🎙️ 語音零截斷 (TTS Zero Cut-off)
- **解除固定秒數限制**：完全打破 24 秒或 30 秒等僵硬時間限制。
- 影片時長由配音完整句長動態決定（`target_dur = audio_dur + 0.8s`，預留 0.35s 啟動延遲與 0.45s 句尾呼吸留白），嚴禁使用 `atrim` 硬切音訊，保證正式沉穩台灣男聲（`zh-TW-YunJheNeural`）每句話完整、從容地說完。

### 4. 🔄 Google Flow 3D 轉盤旋轉片尾 (Cost Optimization & Turntable Showcase)
- **極致節省點數消耗**：在 Google Flow（Omni 1.1 Flash）以最短可用秒數（5 秒）生成 360° 轉盤展示，後製透過 FFmpeg 平滑補幀延展，避免高昂點數消耗。
- **真品圖強制掛載（Asset Chips）**：生成時強制插入真品參考圖條件標籤，100% 還原真品五金與輪廓，徹底防止 AI 憑空捏造假產品。

### 5. 📦 雙版本 7 件組發布包 (Dual-Version Packaging)
每個產品自動產生並交付 7 件規格化檔案：
1. `final.mp4`：多色款式切換介紹成片
2. `final_single_color.mp4`：單一主打色 360° 完整旋轉展示成片
3. `cover.jpg`：1080×1920 高質感封面圖（擷取自黃金生活瞬間）
4. `caption.txt`：官方社群發布文案與精準 Hashtags
5. `title.txt`：高點擊率 SEO 標題
6. `product_url.txt`：原廠商品頁網址
7. `qa.json`：成片規格與品質檢驗通過紀錄（解析度、CFR 幀率、無凍結幀檢驗）

### 6. 🖼️ 真品圖 AI 友善預處理 (Pre-processing Studio Cards)
- 內建 [`preprocess_ai_ref.py`](./scripts/preprocess_ai_ref.py)，自動將促銷圖去邊框、轉 RGB、置中於 1024×1024 純淨背景，徹底解決墨鏡尺寸過大、鏡框失真與 RGBA 轉碼黑屏問題。

---

## 📐 黃金 3 段式架構 (Golden 3-Scene Structure)

| 段落 | 鏡頭類型 | 視覺重點 | 音訊與文案定位 |
| :--- | :--- | :--- | :--- |
| **S1** | 動態實穿 / 生活氣場 | 模特兒街頭漫步、商務走廊、球場動態 | 品牌系列定位、痛點情境切入 |
| **S2** | 休憩置放 / 特寫推軌 | 露天咖啡座木桌特寫、場邊長椅推鏡 | 材質細節（全粒面牛皮 / G-15偏光鏡片 / 五金） |
| **S3** | 3D 轉盤旋轉展示 | 360° 環繞、多色切換或單色全貌展示 | 官方旗艦限時優惠、引導下單 CTA |

---

## 🚀 如何在各 AI Agent 系統中使用 (Installation)

### 方案 A：在 Google Antigravity 中安裝（推薦）
將此儲存庫 Clone 至您的專案目錄下的 `.agents/skills/`：
```bash
# 進入您的專案根目錄
cd /path/to/your/workspace

# Clone 至技能目錄
git clone https://github.com/btcson66-rgb/ecommerce-video-pipeline-skill.git .agents/skills/fantini-shopee-video-pipeline
```
安裝後，在對話中呼叫或指定產品連結，Antigravity 將自動啟動此技能！

### 方案 B：在 Claude Code / Cursor / Codex / Custom Agents 中使用
直接將本儲存庫的 [`SKILL.md`](./SKILL.md) 內容載入至您的 Agent 系統提示詞（System Prompt）或自訂 Rules/Runbook 中。

### 方案 C：以獨立 Python 腳本執行合成
本專案腳本亦可直接作為 CLI 工具使用：

#### 1. 預處理參考圖：
```bash
python scripts/preprocess_ai_ref.py path/to/raw_product.jpg assets/studio_ref.jpg
```

#### 2. 驗證素材規格（防黑屏與色彩空間檢測）：
```bash
python scripts/validate_assets.py assets/
```

#### 3. 執行成片渲染（依設定檔批次輸出）：
```bash
python scripts/render_video_template.py [PRODUCT_CODE]
```

---

## 🛠️ 環境需求 (Prerequisites)

- **Python** $\ge$ 3.10
- **FFmpeg** $\ge$ 6.0（需加入系統 `PATH`，支援 `libx264` 與 `aac`）
- **Python 套件**：
  ```bash
  pip install Pillow edge-tts
  ```
- **字型檔**：腳本預設採用繁體中文標準微軟正黑體粗體（`msjhbd.ttc`），亦可於設定檔中自訂字型路徑。

---

## 📁 專案目錄結構 (Repository Structure)

```text
ecommerce-video-pipeline-skill/
├── SKILL.md                      # Antigravity / Agent 標準技能說明與 SOP 規範
├── README.md                     # 專案中文與英文指南
├── LICENSE                       # MIT 授權條款
├── .gitignore                    # Git 忽略設定
├── examples/
│   └── example_product_config.json # 範例商品設定檔（包款/墨鏡文案與樣式）
└── scripts/
    ├── preprocess_ai_ref.py      # 真品圖片 AI 友善預處理腳本 (1024x1024 RGB)
    ├── render_video_template.py  # FFmpeg 零定格平滑延伸與雙版本壓製引擎
    └── validate_assets.py        # 素材 RGB / 亮度 / 防黑畫面品質檢驗工具
```

---

## 📄 授權條款 (License)

本專案基於 [MIT License](LICENSE) 條款開源，歡迎自由使用、修改與二次開發！
