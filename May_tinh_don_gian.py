def calculator():
    while True:
        try:
            a = int(input("Nhap so nguyen thu nhat: ")) 
            b = int(input("Nhap so nguyen thu hai: "))
            math = input("Moi lua chon phep toan (+, -, *, /): ")
            if math == "+":
              print(f"Ket qua cua {a} + {b} = {a+b}")
            elif math == "-":
              print(f"Ket qua cua {a} - {b} = {a-b}")
            elif math == "*":
              print(f"Ket qua cua {a} * {b} = {a*b}")
            elif math == "/":
                if b == 0:
                    print("Loi khong the chia cho 0!")
                else:
                    print(f"Ket qua cua {a} / {b} = {a/b}")
            else:
              print("Loi phep toan!")
            tieptuc = input("Ban co muon tiep tuc khong? (y/n): ").lower()
            if tieptuc != "y":
              print("Cam on vi da su dung may tinh :3")
              break

        except ValueError:
            print("Vui long nhap so nguyen!")

calculator()