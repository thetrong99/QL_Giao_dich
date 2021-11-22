from mylibrary.abc_giao_dich import *

class vang(giaodich):
    def __init__(self,code,day,sl,loai,don_gia):
        self.code = code
        self.day = day
        self.sl = sl
        self.loai = loai
        self.don_gia = don_gia

    def tinhtien(self):
        return self.sl * self.don_gia
    def in_kq(self):
        result = ""
        result += str(self.code) + " - " + str(self.day) + " - " + str(self.loai) + " - "
        result += str(self.sl) + " - " + str(self.don_gia) + " - "
        result += "Thanh Tien: " + str(self.tinhtien())
        return result
if __name__ == "__main__":
    x = vang("gd345","09/10/1980",100,"18K",2345)
    print(x.in_kq())