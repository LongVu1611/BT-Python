# # -- Bài 3-- Đếm số từ trong test--------------------
def count_word():
    string = input()
    words = string.split()
    return len(words)

t = int(input("Nhập số dòng : "))
for i in range (1,t+1):
    result =count_word()
    print(f"Test {i} : {result}")
