# import time
# start_time = time.time()
n = int(input("Nhập n:"))
for i in range(2, n + 1):
    is_prime = True
    for a in range(2, (i//2) + 1):
        if i % a == 0:
            is_prime = False
            break
    if is_prime == True:
        print(i)
# # Đoạn mã cần kiểm tra thời gian chạy
# for i in range(1000000):
#     pass

# # Kết thúc đo thời gian
# end_time = time.time()

# # Tính toán và in ra thời gian chạy
# elapsed_time = end_time - start_time
# print(f"Thời gian chạy: {elapsed_time} giây")

