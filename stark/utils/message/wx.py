from .base import BaseMessage

class WeChat(BaseMessage):
    def __init__(self):
        pass

    def send(self,subject,body,to,name):
        print('微信发送成功')

