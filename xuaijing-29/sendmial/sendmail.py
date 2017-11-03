import smtplib
import email.mime.multipart
import email.mime.text

msg=email.mime.multipart.MIMEMultipart()
msg['from']='xuaijingwendy@163.com'
msg['to']='2018933125@qq.com'
msg['subject']='test'
content='''''
     你好，
              这是一封自动发送的邮件。


'''
txt=email.mime.multipart.MIMEMultipart(content)
msg.attach(txt)

smtp=smtplib.SMTP()
smtp.connect('smtp.163.com','25')
smtp.login('xuaijingwendy@163.com','15251356767xy')
smtp.sendmail('xuaijingwendy@163.com','2018933125@qq.com',str(msg))
smtp.quit()