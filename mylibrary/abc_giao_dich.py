import abc

class giaodich(abc.ABC):

    @abc.abstractclassmethod
    def __init__(self,code,day,sl):
        pass
    @abc.abstractclassmethod
    def tinhtien(self):
        pass
    @abc.abstractclassmethod
    def in_kq(self):
        pass