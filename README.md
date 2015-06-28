新臺語運動之遊戲分支

##資料處理 (using Python)

* 讀取csv檔
* 建立 中文字->發音 的map

##發音資料處理 (using Julia)

* 讀取csv檔
* 切割發音音節與對應中文字
* 將對應中文字們unigue
* 藉由分組建立 音節->中文字們 的map

##相似發音對應 (using Python in viewer)

* 單次問句為一個音節
* 尋找音節相似度，藉由羅馬拼音的單字距離，例如ling與lin很接近
* 回傳相似度大於門檻的中文字們

##語音

* AJAX 賽微
* 工研院語音 crawler
