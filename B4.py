t=int(input("Nhập số dòng :"))
if t>0 and t<=100:
    for i in range (1, t+1):
        c=input()
        print(c.replace("\t", " "))