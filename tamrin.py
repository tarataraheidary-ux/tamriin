import sys
sys.stdout.reconfigure(encoding='utf-8')
import random

play_again = "بله"

while play_again == "بله":
    num = random.randint(1, 100)
    count = 0
    win = False

    print()
    print("یک عدد بین 1 تا 100 حدس بزن. 5 فرصت داری!")

    while count < 5:
        print()
        print("تلاش", count + 1, "از 5")
        print("جان باقی‌مانده:", 5 - count)

        try:
            guess = int(input("حدس شما: "))
        except ValueError:
            print("ورودی نامعتبر است! فقط عدد وارد کن.")
            continue

        if guess < 1 or guess > 100:
            print("عدد باید بین 1 تا 100 باشد!")
            continue

        count += 1

        if guess == num:
            print()
            print("آفرین! درست حدس زدی.")
            if count == 1:
                print("رتبه: نمونه ای")
            elif count == 2:
                print("رتبه: بسیار خوبی")
            elif count == 3:
                print("رتبه: خوب")
            elif count == 4:
                print("رتبه: قبول")
            else:
                print("رتبه: با شانس بردی!")
            win = True
            break

        if guess < num:
            print("بزرگ‌تر وارد کن")
        else:
            print("کوچک‌تر وارد کن")

        diff = abs(num - guess)
        if diff <= 5:
            print("خیلی نزدیکی!")
        elif diff <= 15:
            print("نزدیکی، ولی هنوز فاصله داری!")
        else:
            print("خیلی دوری!")

    if not win:
        print()
        print("باختی! فرصت‌هایت تمام شد.")
        print("عدد مخفی", num, "بود.")

    while True:
        answer = input("دوباره بازی می‌کنی؟ (بله/خیر): ").strip()
        if answer == "بله" or answer == "خیر":
            break
        print("فقط «بله» یا «خیر» وارد کن.")
    play_again = answer

print("خداحافظ!")
