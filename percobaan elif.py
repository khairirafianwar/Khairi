

nilai = int(input("Masukkan nilai kamu: "))

if nilai >= 90:
    print("Nilai kamu A (Sangat Baik) 🎉")
elif nilai >= 75:
    print("Nilai kamu B (Baik) 👍")
elif nilai >= 60:
    print("Nilai kamu C (Cukup)")
elif nilai >= 50:
    print("Nilai kamu D (Kurang)")
else:
    print("Nilai kamu E (Sangat Kurang) ❌")