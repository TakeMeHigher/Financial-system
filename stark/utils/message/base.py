# from abc import ABCMeta
# from abc import abstractmethod
#
# class BaseMessage(metaclass=ABCMeta):
#
#     @abstractmethod
#     def send(self,subject,body,to,name):
#         pass


class BaseMessage(object):
    def send(self, subject, body, to, name):
        raise NotImplementedError('未实现send方法')