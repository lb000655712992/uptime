# uptime
The system will check the vm uptime and send email to user
## step1:資料庫準備
準備名為db的資料庫\n
並且執行database.create_table.py
## step2:python執行
請執行三個檔案
server.py           #網頁\n
Threshold_check.py  #確認資料庫內的time是否超出Threshold\n
update_uptime.py    #更新資料庫的uptime欄位\n
