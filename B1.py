t = int(input("Nhập số dòng : "))
if 0 < t and t<= 100:
    for i in range (1,t+1):
        c=input()
        print(f"Test {i}:\n{c.title()}")