import random

def rAn():
    choices = ["Kéo", "Búa", "Bao"]  # Chữ in hoa đầu để đồng bộ với capitalize()
    
    # Người chơi nhập lựa chọn
    player = input("Chọn (Kéo, Búa, Bao): ").capitalize()
    while player not in choices:
        print("Vui lòng chọn đúng!")
        player = input("Chọn (Kéo, Búa, Bao): ").capitalize()

    # Máy chọn ngẫu nhiên
    bot_p = random.choice(choices)
    print(f"Máy chọn: {bot_p}")

    # Xác định kết quả
    if bot_p == player:
        print("Hòa!")
    elif (player == "Kéo" and bot_p == "Bao") or \
         (player == "Búa" and bot_p == "Kéo") or \
         (player == "Bao" and bot_p == "Búa"):  # Sửa lỗi dấu `or /` thành `or \`
        print("Bạn thắng!")
    else:
        print("Bạn thua!")

# Chạy trò chơi
rAn()
