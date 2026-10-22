---
name: fantini-shopee-video-pipeline
description: >-
  End-to-end standard operating procedure (SOP) for producing vertical commercial
  short videos (9:16, 1080x1920, 30fps CFR) for multi-brand products (Fantini
  Pelletteria leather bags, ESPNER eyewear/sunglasses, etc.) using pre-processed
  real product photos, Gemini App (Veo) & Google Flow (Omni 1.1 Flash) AI video
  generation, formal male TTS narration (zero cut-off), FFmpeg smooth dynamic
  extension (zero freeze-frame), dual-version rendering (multi-color + single-color
  360 rotation), pure brand commercial styling (Shopee-free mode), and Google Drive
  7-piece package delivery. Activate this skill whenever creating, editing, or
  troubleshooting product short videos in this workspace.
---

# 精品短影音自動化製片標準作業流程 (SOP) — 多品牌通用旗艦版

本技能淬鍊自 **Fantini Pelletteria 義大利真皮包款（F002～F012）** 與 **ESPNER 專業運動/時尚偏光太陽眼鏡（E001～E005）** 全系列實戰經驗，旨在 100% 落實：
- **純商品官方形象廣告模式（預設去蝦皮化，跨平台通用）**
- **預處理 AI 友善識別真品圖 + 親眼雙重視覺驗證（零錯配、零黑屏、比例精準）**
- **解除秒數硬限制 + 語音零截斷 + 畫面絕不定格（`setpts` 平滑慢動作 / `zoompan` 動態推鏡）**
- **Gemini 跨商品對話隔離 + Google Flow 最短秒數省點數 3D 旋轉換色雙引擎接力**
- **雙版本 7 件組（`final.mp4` + `final_single_color.mp4`）Google Drive 自動化交付**

---

## 一、黃金 3 段式架構、多品牌定位與「去蝦皮化」純廣告規範

### 1. 標準 3 段式黃金結構（S1 + S2 + S3）
- **S1（動態實穿 / 生活氣場）**：
  - **包款（Fantini）**：都會街頭漫步、挑高商務大樓步入、歐風石板路肩背/手提自然擺動（只拍外觀穿搭，**絕不拍零錢包內部掀蓋或拉鍊微距結構**）。
  - **運動墨鏡（ESPNER 運動系列）**：陽光網球場、戶外運動賽道自信漫步與單手扶鏡特寫。
  - **復古/時尚墨鏡（ESPNER 都會/海濱系列）**：歐洲海濱棕櫚林蔭大道漫步、陽光街頭自信穿搭。
- **S2（靜態休憩置放 / 材質工藝特寫）**：
  - **包款**：露天咖啡座優雅將包款置於木桌，陽光灑落皮革紋理與五金。
  - **運動墨鏡**：場邊木質長椅搭配網球拍與運動毛巾，微風吹拂下近距離推軌特寫鏡片 REVO 鍍膜光澤。
  - **復古/時尚墨鏡**：精品露天咖啡座木桌搭配冰拿鐵，平滑推鏡特寫手工微弧金屬鏡框與 G-15 偏光鏡片。
- **S3（Google Flow 3D 轉盤旋轉展示 + 規格導購 CTA）**：
  - 360° 柔和光影展示台旋轉，搭配多色系切換介紹或單色完整環繞展示。

### 2. 純商品官方廣告模式（預設「去蝦皮化」Pure Brand Commercial）
- **核心原則**：除非使用者特別指定要標註蝦皮，否則一律採用**純品牌官方形象廣告模式**，不出現任何「蝦皮」字樣。
- **視覺與文案規範**：
  - **頂部膠囊（Top Capsule）**：標註品牌與系列定位（例如：`ESPNER 專業運動光學系列`、`ESPNER 義式復古工藝系列`、`FANTINI 義大利手工皮件`）。
  - **底部 CTA 按鈕**：使用 `【官方旗艦限定】限時 7 折 NT$1,750` 或 `【官方旗艦現貨】立即探索選購`，**嚴禁出現「蝦皮優惠價」、「點擊蝦皮購買」**。
  - **旁白與 `caption.txt`**：口播結尾統一使用「官方旗艦現貨供應，立即探索選購」；文案與 Hashtags 聚焦品牌與產品機能，方便直接投放於 IG Reels、TikTok、YouTube Shorts、FB 與蝦皮短影音。

---

## 二、Step 1：真品圖片抓取、AI 友善預處理與雙重驗證

在進入 AI 生成前，必須針對商品頁完成以下準備：

1. **抓取高畫質真品原圖與核對特徵**：
   - 記錄商品真實品牌名稱（`FANTINI`、`ESPNER` 等）、型號、定價/折扣價、現貨色系與結構細節（如：鏡框形狀、鼻橋金屬、鏡片顏色、皮革紋理）。
2. **預先整理 AI 友善識別參考圖（Pre-processing Reference Image）**：
   - 針對墨鏡或精細配件，若原圖帶有促銷文字邊框、多圖拼貼或過小比例，直接餵給 AI 容易導致生成的墨鏡尺寸過大或框型失真。
   - **必做預處理**：使用 Python PIL 將商品主圖去蕪存菁，裁切並置中於乾淨高質感灰白背景或純淨特寫畫布（輸出為 `*_gemini_studio.jpg` 或 `*_gemini_hero.jpg`，確保 `mode == 'RGB'`）。
3. **雙重驗證（防錯配 + 防黑屏）**：
   - **親眼檢視**：必須使用 `read_file` 親眼檢視預處理後的參考圖，確認與商品標題 100% 吻合。
   - **RGB 驗證**：執行 [`scripts/validate_assets.py`](./scripts/validate_assets.py) 確認 `im.mode == 'RGB'` 且平均亮度 `mean > 50`（嚴禁直接使用 `RGBA` 透明去背圖以免 FFmpeg 轉碼產生全黑背景）。

---

## 三、Step 2：Gemini (Veo) 與 Google Flow (Omni 1.1 Flash) 雙引擎生成規範

### 1. 防範 Gemini 多輪對話快取汙染（Session Isolation 鐵律）
- **問題根源**：在同一個 Gemini App 對話串中連續生成不同商品時，Gemini 後端極易沿用該對話最初上傳的舊商品圖（例如把前一款白框運動眼鏡套用到新款金屬圓框墨鏡上）。
- **強制對策**：
  - 每切換一個新商品，在 Gemini App **必須開啟全新對話（New Chat）**。
  - 每次上傳僅限 **1 張**預處理後的真品參考圖（先複製至 `C:\Users\User\AppData\Local\Temp\` 白名單目錄再上傳）。
  - 影片下載後，**必須立即使用 `ffmpeg` 抽取影格並以 `read_file` 親眼查驗**：確認影片中人物穿戴的商品款式、顏色、框型與真品 100% 一致。若發生款式錯置，立即改用 **Google Flow** 重新生成。

### 2. Google Flow 最短秒數省點數 + Asset Chips 精準控制
- **何時使用 Google Flow (`flow.google.com`)**：
  1. 製作 **S3 片尾 3D 轉盤 360° 旋轉展示**（必用）。
  2. 當 Gemini 達到每輪 3 部影片額度上限（冷卻約 5 小時）時，直接以 Google Flow（Omni 1.1 Flash）接力生成 S1 / S2 生活場景，**無須空等 5 小時**。
  3. 當商品細節極為精細（如金屬細框墨鏡），需要透過 Flow 的獨立素材標籤（Asset Chips）強制鎖定外觀時。
- **Google Flow 操作鐵律**：
  - **強制掛載真品圖條件標籤（Asset Chips）**：上傳真品圖後，點擊輸入框下方「在提示詞輸入框新增素材」，選取該商品真品圖插入為條件標籤，絕不無圖盲生。
  - **設定最短秒數（5 秒）節省點數**：在 Flow 生成時一律設定為最短秒數（5 秒），減少點數消耗；下載後於 FFmpeg 透過 `setpts` 平滑動態慢動作延伸至配音所需秒數。

### 3. 提示詞（Prompt）精準度與品牌動態標註規範
- **動態指定真實品牌名稱**：
  - 提示詞中必須明確指定該商品的真實品牌英文字樣（例如 `FANTINI PELLETTERIA` 或 `ESPNER`），嚴禁寫錯品牌或讓 AI 隨機發明亂碼字母。
- **完整詳盡描述**：
  - 必須包含：直向 `Vertical 9:16`、人物穿搭與動作、光影環境、以及產品精確結構（例如：`wearing these exact ESPNER round gold metal sunglasses with dark green G-15 lenses` 或 `carrying this exact FANTINI dark brown grained leather handbag`）。

---

## 四、Step 3：沉穩男聲配音與 FFmpeg「零截斷、零定格」雙版本壓製

標準自動化壓製範本腳本位於：[`scripts/render_video_template.py`](./scripts/render_video_template.py)

1. **配音標準（語音零截斷）**：
   - 統一使用 `edge-tts` 正式沉穩台灣男聲：**`zh-TW-YunJheNeural`**（`rate="-1%"`, `pitch="-2Hz"`）。
   - **完全解除 24 秒硬性限制**：每段目標時長由配音實際長度動態決定：`target_dur = audio_dur + 0.8s`（含 `adelay=350|350` 與句尾自然留白）。
   - **嚴禁使用 `atrim` 截斷配音**，確保每一句旁白完整、從容說完。
2. **畫面平滑延伸（絕不定格 Zero Freeze Frame）**：
   - **嚴格禁止使用 `tpad=stop_mode=clone` 尾幀定格**（定格會造成畫面卡死停頓感）。
   - 當 AI 原始影片秒數（`v_dur`，如 5s 或 8s）異於段落目標秒數（`seg_dur`，如 8.8s）時，統一使用 **`setpts=(seg_dur/v_dur)*PTS`** 進行絲滑慢動作延伸，或搭配平滑微幅推鏡（Smooth Zoom-in），確保鏡頭從頭到尾持續流暢運動。
   - 強制輸出規格：`1080x1920`、`-r 30`（30.0 fps CFR 恆定幀率）、`libx264`、`yuv420p`。
3. **雙版本同步產出（多色版 + 單色 360° 旋轉版）**：
   - **`final.mp4`**：S1 + S2 + S3（多色款式介紹 / 雙色切換說明圖卡）。
   - **`final_single_color.mp4`**：S1 + S2 + S3（單一主打色 360° 旋轉展示圖卡）。
4. **成片視覺抽檢（必做）**：
   - 壓製完成後，從 `final.mp4` 抽取 `final_check_s1.jpg`、`final_check_s2.jpg`、`final_check_s3.jpg`，並使用 `read_file` 親眼確認字幕排版、膠囊標題、商品外觀與畫面亮度一切完美。

---

## 五、Step 4：Google Drive 雲端硬碟 7 件組白名單交付

1. **標準 7 件組清單**：
   - `final.mp4`：多色介紹版正式成片
   - `final_single_color.mp4`：單色 360° 旋轉版成片
   - `cover.jpg`：1080×1920 高質感封面圖（由 S1 最佳瞬間擷取）
   - `caption.txt`：品牌官方社群文案與 Hashtags（去蝦皮化）
   - `title.txt`：SEO 產品標題
   - `product_url.txt`：商品網址
   - `qa.json`：品質檢驗通過紀錄（記錄解析度、秒數、零定格、語音完整、去蝦皮化狀態）
2. **白名單上傳流程**：
   - 先將 7 個檔案複製至 `C:\Users\User\AppData\Local\Temp\<Product_ID>\`（確保 Chrome 檔案上傳器可直接讀取，避免跨磁碟權限阻擋）。
   - 在 Chrome 開啟 Google Drive `02_手機待發布`（`https://drive.google.com/drive/folders/159V39Zk3TfLkyvyHxwrHgLryjBxl56lA`）。
   - 建立專屬子資料夾（命名格式：`<編號>_<品牌>_<商品簡稱>`，如 `E004_Espner_BASELINE運動太陽眼鏡`、`E005_Espner_MARBELLA復古偏光墨鏡`）。
   - 將 7 個檔案全數上傳，確認上傳完成後取得資料夾與 `final.mp4` 分享連結回報使用者。

---

## 六、異常重試與 Discord 緊急警報機制

1. **自動喚醒與間隔重試**：
   - 當遇到連線逾時或額度冷卻時，優先切換 Google Flow 雙引擎接力，或使用 `schedule` 定時器等待重置後自動繼續。
2. **連續 3 次失敗觸發 Discord @mention 警報**：
   - 連續測試重試達 **3 次**仍無法排除阻礙時，立即停止無效空轉並執行：
     `python d:\蝦皮\scripts\send_discord_alert.py "<詳細異常原因>"`
   - 透過 `D:\notify-bot` 在 Discord `shopee-alerts` 頻道發送緊急通知提醒使用者。
