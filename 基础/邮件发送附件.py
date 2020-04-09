import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_email_att():
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "605402932@qq.com"
    mail_pass = "dxoazqcymofabfgi"           # 服务端授权码，不是邮箱的密码
    sender = mail_user
    receivers = ["yan.liu@mullenloweprofero.com"]  # 接收邮件
    mail_msg = """
    <p>Python 邮件测试</p>
    <p><a href="http://www.baidu.com">百度链接</a></p>
    """

    message = MIMEMultipart()   # 创建一个带附件的实例
    message['From'] = Header("测试邮件标题", 'utf-8')
    message['To'] = ";".join(receivers)
    subject = "Python SMTP 邮件测试"
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    # 构造附件1
    att1 = MIMEText(open('../正则表达式/report.html').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename = "report.html"'
    message.attach(att1)

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


send_email_att()
