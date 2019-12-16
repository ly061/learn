import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "605402932@qq.com"
mail_pass = "tjctffbccqkzbcdd"           # 服务端授权码，不是邮箱的密码
sender = mail_user
receivers = ["yan.liu@mullenloweprofero.com"]  # 接收邮件
mail_msg = """
<p>Python 邮件测试</p>
<p><a href="http://www.baidu.com">百度链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')   # 发送html邮件
message['From'] = Header("测试邮件标题", 'utf-8')
message['To'] = ";".join(receivers)

subject = "Python SMTP 邮件测试"
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()
    print("邮件发送成功")
except Exception as e:
    print("Error: 无法发送邮件")
    print(str(e))
