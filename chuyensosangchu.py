


def so_sang_chu(so):
    chu_so_don = {
        "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", 
        "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
    }

    chu_so_muoi = {
        "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", 
        "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"
    }

    chu_so_chuc = {
        "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", 
        "7": "seventy", "8": "eighty", "9": "ninety"
    }

    so = str(int(so))  # Loại bỏ số 0 ở đầu, nếu có

    if so in chu_so_don:
        return chu_so_don[so]
    elif so in chu_so_muoi:
        return chu_so_muoi[so]
    elif len(so) == 2:
        return chu_so_chuc[so[0]] + ("-" + chu_so_don[so[1]] if so[1] != "0" else " ")
    else:
        return "Invalid input"

# Nhập vào một số từ 0 đến 99
so = input("Nhập một số từ 0 đến 99: ")
# Chuyển đổi và in ra chữ tương ứng
print(so_sang_chu(so))
