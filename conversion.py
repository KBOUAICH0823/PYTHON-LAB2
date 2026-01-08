choix = input("اختار التحويل (1: Celsius → F/K ، 2: Fahrenheit → C): ")

try:
    if choix == "1":
        c = float(input("دخل الدرجة بالـ Celsius: "))
        f = c * 9/5 + 32
        k = c + 273.15
        print(f"{c}°C = {f}°F = {k}K")

    elif choix == "2":
        f = float(input("دخل الدرجة بالـ Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c}°C")

    else:
        print("اختيار غير صحيح")

except ValueError:
    print("خطأ: دخل قيمة عددية")
