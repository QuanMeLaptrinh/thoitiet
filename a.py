W = int(input("Dung lượng của đĩa (chỉ nhập số): "))
print(f"Dung lượng của đĩa: {W} KB")  # Hiển thị "KB" sau số đã nhập

d = [int(i) for i in input().split()]
dem = 0
for a in range(len(d)):
    for i in range(len(d) - 1):  
        if d[i] > d[i+1]:
            b = d[i]
            d[i] = d[i+1]
            d[i+1] = b
print(d)
for i in range(len(d)):
    if W - d[i] >= 0:
        dem += 1
        W  -= d[i]
print("Số ảnh đĩa có thể lưu là:",dem,"( còn dư",W,"kb)")



