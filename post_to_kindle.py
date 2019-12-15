from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase
import smtplib
from email.mime.text import MIMEText
import os 

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

# 输入Email地址和口令
# 检查是否使用默认邮箱
def check_email(email,type):
    if email != '':
        return email
    if (type =='from') and (email == ''):
        print('当前发送邮箱为空，将使用默认邮箱:1341696804@qq.com')
        return  '1341696804@qq.com'
    if (type =='to') and (email == ''):
        print('当前收件邮箱为空使用默认邮箱:huyong_huawei_kindle@kindle.cn')
        return 'huyong_huawei_kindle@kindle.cn'
    if (type =='server') and (email == ''):
        print('SMTP server为空将使用默认qqSMTP协议')
        return 'smtp.qq.com'
# 输入发送邮箱
from_addr = input('From: ')
from_addr =check_email(from_addr,'from')
def input_pwd():
    password = input('Password: ')
    if password == '':
        return input_pwd()
    else:
        return password
password = input_pwd()

# 输入收件人地址：
to_addr = input('To: ')
to_addr = check_email(to_addr,'to')
# 输入SMTP服务器地址
smtp_server = input('SMTP server: ')
smtp_server = check_email(smtp_server,'server')
# 邮件对象
msg  = MIMEMultipart()
msg['From'] = _format_addr('胡永的python脚本<%s>'%from_addr)
msg['To'] = _format_addr('管理员<%s>'%to_addr)
msg['Subject'] = Header('来自SMTP的问候...','utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('this file sent by huyong`s Python script','plain','utf-8'))
# 列出book文件中的所有文件
filePath = '/Users/smart/python/book'
def list_dir_file(now_dir):
    print('book文件中的文件名\n',[x for x in os.listdir(now_dir) if os.path.isfile(x)])
list_dir_file(filePath)
fileName = input('输入book文件夹中要post到kindle的文件名: ')
print('您要上传的文件名是：',fileName)
# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open(os.path.join(filePath,fileName),'rb') as f:
    # 设置附件的MIME和文件名字，这里是jpg类型：
    mime = MIMEBase('application','pdf',fileName=str(fileName))
    # 加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename = str(fileName))
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