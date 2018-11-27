# Line_BOT_Flask


使用Python Flask搭配Google Cloud Platform的App Engine完成

使用的是Line 的[Message API](https://developers.line.biz/en/services/messaging-api/)

官網的tutorial建議是使用Heroku架設所需的HTTPS server
因為GCP的App Engine也可以架設HTTPS 所以我將Flask架設在GCP上

同時把Chat Bot會用到的圖片也放在GCP的static資料夾內
這樣就可以透過

https://{app_engine_url}/static/{圖片名稱}

拿到圖片, 不用另外把圖片上傳到免費空間

在main中有宣告一個 /newMenu 的路徑

是為了更新richmenu方便所以在這裡定義,
而且沒有另外做驗證

如果是有打算透過Messaage API建立客製化Richmenu的話,

把對用戶跟對開發者兩邊的server分開,
Line@ manager也提供相當足夠的功能可以透過網頁建立RichMenu 

如果只需要基本的功能的話可以透過網頁完成即可

qr code
http://qr-official.line.me/L/OUsW1FO-jc.png
