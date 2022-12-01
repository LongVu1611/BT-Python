def count_word():
    nguyenam = 0
    phuam = 0
    str = input('Test : ')
    for i in str:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
                or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            nguyenam = nguyenam + 1
        else:
            phuam = phuam + 1
    print(f"{nguyenam}", end="\n")
    print(f"{phuam}", end="\n")

t=int(input('Nhập số dòng: '))
for i in range(1, t+1):
    print(f"test {i}", end="\t")
    result = count_word()