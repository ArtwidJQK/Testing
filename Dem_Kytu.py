from collections import Counter
def dem_kytu():
    chuoi = input("Mời nhập chuỗi ký tự: ").lower()
    tan_suat = Counter(chuoi)
    for ky_tu in sorted(tan_suat):
        print(f"'{ky_tu}': {tan_suat[ky_tu  ]} ")
dem_kytu()