#tạo hàm đếm từ
def dem_tu(s1):
    #str: Đây là bất kỳ phân chia chuỗi - delimeter nào, mặc định là khoảng trống
    str = s1.split(" ")
    count = {}
    for i in str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
#hàm sorted(dict, key=dict.get, reverse=False) sẽ trả về một list các giá trị đã được sắp xếp
    for i in sorted(count, key=count.get, reverse=False):
        print(f"{i}-{count[i]}")

r = int(input("Nhập số dòng : "))
if 0 < r <= 100:
    for i in range(r):
        s1 = input("Mời nhập chuỗi: ")
        print(f"Test {i + 1}:", end="\n")
        dem_tu(s1)