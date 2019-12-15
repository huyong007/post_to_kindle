from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase
import smtplib
from email.mime.text import MIMEText

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

# 输入Email地址和口令
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址：
to_addr = input('To: ')
# 输入SMTP服务器地址
smtp_server = input('SMTP server: ')

# 邮件对象
msg  = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者<%s>'%from_addr)
msg['To'] = _format_addr('管理员<%s>'%to_addr)
msg['Subject'] = Header('来自SMTP的问候...','utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('this file sent by huyong`s Python script','plain','utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open('/Users/smart/python/book/七周七语言.pdf','rb') as f:
    # 设置附件的MIME和文件名字，这里是jpg类型：
    mime = MIMEBase('application','pdf',fileName='七周七语言.pdf')
    # 加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='七周七语言.pdf')
    mime.add_header('Content_ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    # 把附件的内容读进来：
    mime.set_payload(f.read())
    # 用Base64编码：
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server,25) # SMTP 默认端口是25
server.set_debuglevel(1)

server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()