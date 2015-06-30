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

##Backend

* 採用Django做為後端的Web應用框架，由Python寫成
* 整個後端的資料夾分為<br/>
  │<br/>
  └dataProcessing_not_in_Django<br/>
  └queryChinese<br/>
  └queryClosePronounce<br/>
  └taigiGameDB<br/>

* dataProcessing_not_in_Django<br/>
  -是用來儲存處理資料庫中罕見中文字以及重複字詞所用到的程式
* queryChinese & queryClosePronounce<br/>
  -資料夾底下的model.py是用來建立儲存資料格式的模型<br/>
  -而views.py是用來處理文字的查詢、將題目打包丟給前端(前者)以及相似發音的查詢(後者)
* taigiGameDB<br/>
  -主要是利用底下的urls.py來提供對應的查詢

* 執行步驟
  1. 確認已經安裝Django套件
  2. 如果沒安裝請先安裝Django套件，執行pip install Django -U
  3. 進入Backend的資料夾中啟動後端server，執行python manage.py runserver
  4. 到 http://127.0.0.1:8000/hello/ 確認是否成功啟動
  

## API
  * http://127.0.0.1:8000/q/get_question/                 取得題目
  * http://127.0.0.1:8000/q/chinese_word/工夫/            取得"工夫"的音標
  * http://127.0.0.1:8000/q/close_pronounce/hu/           取得發音為"hu"的相似字

## License

[MIT License](http://g0v.mit-license.org/)
  
