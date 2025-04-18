a = int(input())
for i in range (1,11):
    print(a,'x',i,'=?')
    tra_loi = input()
    if tra_loi == 'dừng': break
    if tra_loi == 'Không nhớ':
        print("không nhớ,bỏ qua")
        continue
    dap_an = i * a
    if int(tra_loi) == dap_an:
        print("Đúng")
    else:
        print("Sai,đáp án là:",dap_an)
print("ok")

