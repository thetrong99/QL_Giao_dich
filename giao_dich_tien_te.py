from mylibrary.abc_giao_dich import *

class tien_te(giaodich):
    def __init__(self,code,day,sl,ty_gia,loai_gd,mua_ban):
        self.code = code
        self.day = day
        self.sl = sl
        self.loai_gd = loai_gd
        self.ty_gia = ty_gia
        self.mua_ban = mua_ban
    def tinhtien(self):
        if int(self.mua_ban) == 1:
            return self.sl * self.ty_gia
        else:
            return self.sl * self.ty_gia * 1.05
    def in_kq(self):
        if int(self.mua_ban) == 1:
            result = "GD Mua: "
        else:
            result = "GD Ban: "
        result += str(self.code) + " - " + str(self.day) + " - " + str(self.loai_gd) + " - "
        result += str(self.sl) + " - " + str(self.ty_gia) + " - "
        result += "Thanh Tien: " + str(self.tinhtien())
        return result
if __name__ == "__main__":
    x = tien_te("gd123","27/10/1999",10,235,"USD",0)
    print(x.in_kq())
