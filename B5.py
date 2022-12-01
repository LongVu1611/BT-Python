def kiem_tra_chuoi_con(s1, s2):
   #Su dung toan tu in de kiem tra su xuat hien cua chuoi con
   if s2 in s1:
       #Su dung phuong thuc count() de dem so lan xuat hien cua chuoi con
       print(s1.count(s2))
   else:
       # format() được tích hợp sẵn trong Python  để định dạng một giá trị truyền vào thành một định dạng cụ thể
       print('chuỗi "{}" không xuất hiện trong chuỗi "{}"'.format(s2, s1))


p = int(input("Nhập số dòng : "))
if 0 < p <= 100:
    for i in range(p):
        s1 = input("Nhập chuỗi 1: ")
        s2 = input("Nhập chuỗi 2: ")
        print(f"test {i + 1}:", end="\n")
        kiem_tra_chuoi_con(s1, s2)