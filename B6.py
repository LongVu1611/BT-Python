def thay_the(s1, s2, s3):
    if s2 in s1:
        print("Thay thế chuỗi 1 vào chuỗi 2 :",s1.replace(s2, s3))
    else :
        print("Chuỗi 2 không có trong chuỗi 1 để thay thế !")

m = int(input("Nhập số dòng : "))
if 0 < m <= 100:
    for i in range(m):
        s1 = input("Nhập chuỗi vào đây: ")
        s2 = input("Nhập chuỗi thay thế cũ: ")
        s3 = input("Nhập chuỗi thay thế mới: ")
        print(f"Test {i + 1}:", end="\n")
        thay_the(s1,s2,s3)