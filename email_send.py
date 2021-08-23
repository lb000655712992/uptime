from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def email_send(to, Text):
    content = MIMEMultipart()  # 建立MIMEMultipart物件
    content["subject"] = "Threshold warning"  # 郵件標題
    content["from"] = "lb000655712992@gmail.com"  # 寄件者
    content["to"] = to              # 收件者
    content.attach(MIMEText(Text))  # 郵件內容

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("lb000655712992@gmail.com", "password")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)