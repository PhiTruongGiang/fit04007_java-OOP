total = 0

# Biến đếm số lượng số chẵn đã tìm thấy
count = 0

# Số bắt đầu
n = 0

# Vòng lặp cho đến khi tìm đủ 10 số chẵn
while count < 10:
    if n % 2 == 0:
        total += n
        count += 1
    n += 1

print("Tổng của 10 số chẵn đầu tiên là:", total)

