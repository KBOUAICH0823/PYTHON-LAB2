try:
    a = float(input("دخل العدد الأول: "))
    b = float(input("دخل العدد الثاني: "))
    op = input("اختار العملية (+, -, *, /): ")

    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        if b == 0:
            print("خطأ: القسمة على صفر غير ممكنة")
            exit()
        res = a / b
    else:
        print("عملية غير صالحة")
        exit()

    print(f"{a} {op} {b} = {res}")

except ValueError:
    print("خطأ: خاص تدخل أعداد صحيحة أو عشرية")
