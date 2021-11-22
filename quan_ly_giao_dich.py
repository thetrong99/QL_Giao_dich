import giao_dich_tien_te as tiente
import giao_dich_vang as vang
gold = []
money = []
def outp():
    code = input("Nhap ma GD: ")
    day = input("Nhap Ngay GD: ")
    sl = int(input("Nhap So luong GD: "))
    typ = int(input("Nhap loai giao dich (1-vang 2-Tiente): "))
    if typ == 1:
        loai = input("chon loai: 18k / 24k / 9999: ")
        don_gia = int(input("Nhap don gia: "))
        x = vang.vang(code,day,sl,loai,don_gia)
        gold.append(x)
        sumg = 0
        for i in gold:
            sumg += i.tinhtien()
            print(i.in_kq())
        print("Tong Tien : ", sumg)
    else:
        loai_gd = input("nhap loai: USD / EUR / AUD: ")
        ty_gia = int(input("Nhap ty gia: "))
        mua_ban = int(input("mua hay ban? (1-mua 0-ban): "))
        t = tiente.tien_te(code,day,sl,ty_gia,loai_gd,mua_ban)
        money.append(t)
        sumt = 0
        for i in money:
            sumt += i.tinhtien()
            print(i.in_kq())
        print("Tong Tien: ", sumt)
def main():
    print("Quan Ly Giao Dich")
    outp()
    while True:
        tt = int(input("nhap tiep tuc (1-co 0-khong): "))
        if tt == 1:
            outp()
        else:
            break;
if __name__ == "__main__":
    main()

        