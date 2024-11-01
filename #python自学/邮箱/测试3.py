import cv2

# cap = cv2.VideoCapture(0)
# # 把拍摄到的内容读取出来
# _, frame = cap.read()
# # 把照片数据保存成文件
# cv2.imwrite('img.jpg', frame)

# cap.release()
'''
这里针对smtplib做了一系列封装，可以完成以下四种场景：
发送纯文本的邮件
发送html页面的邮件
发送带附件文件的邮件
发送能展示图片的邮件
以上四种场景，已经做好了二次封装，经测试OK，使用时直接传入对应参数即可，直接上代码
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


class SendEMail(object):
    """封装发送邮件类"""

    def __init__(self, host, port, msg_from, pwd):

        self.msg_from = msg_from
        self.password = pwd

        # 邮箱服务器地址和端口
        self.smtp_s = smtplib.SMTP_SSL(host=host, port=port)

        # 发送方邮箱账号和授权码
        self.smtp_s.login(user=msg_from, password=pwd)

    def send_text(self, to_user, content, subject, content_type='plain'):
        """
        发送文本邮件
        :param to_user: 对方邮箱
        :param content: 邮件正文
        :param subject: 邮件主题
        :param content_type: 内容格式：'plain' or 'html'
        :return:
        """
        msg = MIMEText(content, _subtype=content_type, _charset="utf8")

        msg["From"] = self.msg_from
        msg["To"] = to_user
        msg["subject"] = subject

        self.smtp_s.send_message(msg, from_addr=self.msg_from, to_addrs=to_user)

    def send_file(self, to_user, content, subject, reports_path, filename, content_type='plain'):
        """
        发送带文件的邮件
        :param to_user: 对方邮箱
        :param content: 邮件正文
        :param subject: 邮件主题
        :param reports_path: 文件路径
        :param filename: 邮件中显示的文件名称
        :param content_type: 内容格式
        """

        file_content = open(reports_path, "rb").read()

        msg = MIMEMultipart()

        text_msg = MIMEText(content, _subtype=content_type, _charset="utf8")
        msg.attach(text_msg)

        file_msg = MIMEApplication(file_content)
        file_msg.add_header('content-disposition', 'attachment', filename=filename)
        msg.attach(file_msg)

        msg["From"] = self.msg_from
        msg["To"] = to_user
        msg["subject"] = subject

        self.smtp_s.send_message(msg, from_addr=self.msg_from, to_addrs=to_user)

    def send_img(self, to_user, content ,subject,  filename, content_type='html'):
        '''
        发送带图片的邮件
        :param to_user: 对方邮箱
        :param content: 邮件正文
        :param subject: 邮件主题
        :param filename: 图片路径
        :param content_type: 内容格式
        '''
        subject = subject
        msg = MIMEMultipart('related')
        # Html正文必须包含<img src="cid:imageid" alt="imageid" width="100%" height="100%>
        content = MIMEText(content, _subtype=content_type, _charset="utf8")
        msg.attach(content)
        msg['Subject'] = subject
        msg['From'] = self.msg_from
        msg['To'] = to_user

        with open(filename, "rb") as file:
            img_data = file.read()

        img = MIMEImage(img_data)
        img.add_header('Content-ID', 'imageid')
        msg.attach(img)

        self.smtp_s.sendmail(self.msg_from, to_user, msg.as_string())


sendemail=SendEMail('smtp.qq.com',465,'970586718@qq.com','uwlakdflhlbxbcig')
# sendemail.send_text('对方邮箱','正文','主题：测试发送文本')
sendemail.send_img('3181314768@qq.com','正文','主题：测试发送图片','img.jpg')
# sendemail.send_file('对方邮箱','正文','主题：测试发送文件','文件地址','对方接收时显示的文件名')

