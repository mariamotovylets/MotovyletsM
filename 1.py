import math

def rectangle_area(length, width):
    """Обчислює площу прямокутника."""
    return length * width

def circle_area(radius):
    """Обчислює площу кола."""
    return math.pi * radius ** 2

def triangle_area(base, height):
    """Обчислює площу трикутника."""
    return 0.5 * base1 * height1

def square_area(side):
    """Обчислює площу квадрата."""
    return side ** 2

def parallelogram_area(base, height):
    """Обчислює площу паралелограма."""
    return base2 * height2

# Вибір фігури 
while True:
    # Вибір фігури
    print("0. Вихід")
    print("Виберіть фігуру:")
    print("1. Прямокутник")
    print("2. Коло")
    print("3. Трикутник")
    print("4. Квадрат")
    print("5. Паралелограм")
    

    choice = int(input("Введіть номер вибраної фігури (або 0 для виходу): "))

    if choice == 0:
        break  # Вихід з циклу при виборі 0

    # Введення даних
    if choice == 1:
        length = float(input("Введіть довжину прямокутника: "))
        width = float(input("Введіть ширину прямокутника: "))
        area = rectangle_area(length, width)

    elif choice == 2:
        radius = float(input("Введіть радіус кола: "))
        area = circle_area(radius)

    elif choice == 3:
        base = float(input("Введіть основу трикутника: "))
        height = float(input("Введіть висоту трикутника: "))
        area = triangle_area(base, height)

    elif choice == 4:
        side = float(input("Введіть сторону квадрата: "))
        area = square_area(side)

    elif choice == 5:
        base = float(input("Введіть основу паралелограма: "))
        height = float(input("Введіть висоту паралелограма: "))
        area = parallelogram_area(base, height)

    else:
        print("Невірний вибір фігури.")
        area = None

    # Виведення даних
    if area is not None:
        coma = int(input("Введіть кількість знаків після коми: "))
        print(f"Площа обраної фігури: {area:.{coma}f}")
