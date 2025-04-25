import os
import math

def menu():
    print("\n--------------------MENU--------------------")
    print("1. In ra danh sách vừa tạo.")
    print("2. In đảo ngược danh sách.")
    print("3. Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).")
    print("4. Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.")
    print("5. Đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.")
    print("6. In ra vị trí các phần tử là số nguyên tố.")
    print("7. Tìm các số duy nhất (không trùng lặp) trong danh sách.")
    print("8. Liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó")
    print("9 .In ra các đoạn con trong danh sách giảm liên tiếp.")
    print("10. Thoat")

def res_4(list):
    max_num = max(list)
    pos = 0
    for x in range(len(list)):
        if list[x] == max_num:
            pos = x
    print(f"Max = {max_num}")
    print(f"Vi tri cuoi cung: {pos}")

def res_5(list):
    os.system("cls")
    n = int(input("Nhap 1 so: "))
    count = 0
    appear = []
    for x in range(len(list)):
        if list[x] == n:
            count += 1
            appear.append(x)
    if count == 0:
        print(f"Khong ton tai so {n} trong mang")
    else:
        print(f"So luong phan tu {n}: {count}")
        print(f"Vi tri xuat hien: {appear}")

def res_6(list):
    pos = []
    for x in range(len(list)):
        if list[x] == 2:
            pos.append(x)
        if list[x] > 2:
            for i in range(2,list[x]):
                if list[x] % i == 0:
                    break
                if i == list[x] - 1:
                    pos.append(x)
    print(f"Vi tri cac phan tu la so nguyen to: {pos}")
def res_7(list):
    result = []
    for i in range(len(list)):
        x = list[i]
        count = 0
        for j in list:
            if j == x:
                count += 1
        if count == 1:
            result.append(x)
    print(f"{result}")

def res_08(list):
    result = {}
    for x in list:
        if x in result:
            result[x] += 1
        else:
            result[x] =1
    print(result)

def res_09(arr):
    result = []
    current = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] - 1:
            current.append(arr[i])
        else:
            if len(current) > 1:
                result.append(current)
            current = [arr[i]]
    for x in result:
        print(x)

if __name__ == "__main__":
    # Nhập phần tử
    my_list = [7,2,1,4,8,7,6,5,1]
    """len_list = int(input("Nhap so luong phan tu (1-100): "))
    for x in range(len_list):
        a = int(input(f"Nhap gia tri thu {x+1}: "))
        my_list.append(a)"""

    os.system("cls")
    while True:
        my_menu = menu()
        choice = int(input("Nhap lua chon cua ban: "))

        if choice == 1:
            print(my_list)
            os.system('cls')

        if choice == 2:
            b = reversed(my_list)
            print(list(b))

        if choice == 3:
            b = sorted(my_list)
            print(list(b))

        if choice == 4:
            res_4(my_list)

        if choice == 5:
            res_5(my_list)

        if choice == 6:
            res_6(my_list)

        if choice == 7:
            res_7(my_list)

        if choice == 8:
            res_08(my_list)

        if choice == 9:
            res_09(my_list)

        if choice == 10:
            break
