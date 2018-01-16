#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .base import BaseMessage
class Msg(BaseMessage):
    def __init__(self):
        pass

    def send(self,subject,body,to,name):
        print('短信发送成功')

