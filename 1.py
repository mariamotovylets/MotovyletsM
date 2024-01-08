
import math

def rectangle_area(length, width):
    """Обчислює площу прямокутника."""
    return length * width

def circle_area(radius):
    """Обчислює площу кола."""
    return math.pi * radius ** 2

def triangle_area(base, height):
    """Обчислює площу трикутника."""
    return 0.5 * base * height

def square_area(side):
    """Обчислює площу квадрата."""
    return side ** 2

def parallelogram_area(base, height):
    """Обчислює площу паралелограма."""
    return base * height

# Вибір фігури 
print("Виберіть фігуру:")
print("1. Прямокутник")
print("2. Коло")
print("3. Трикутник")
print("4. Квадрат")
print("5. Паралелограм")

choice = int(input("Введіть номер вибраної фігури: "))

# Введення даних
if choice == 1:
    length = float(input("Введіть довжину прямокутника: "))
    width = float(input("Введіть ширину прямокутника: "))
    area = rectangle_area(length, width)

elif choice == 2:
    radius = float(input("Введіть радіус кола: "))
    area = circle_area(radius)

elif choice == 3:
    base1 = float(input("Введіть основу трикутника: "))
    height1 = float(input("Введіть висоту трикутника: "))
    area = triangle_area(base1, height)

elif choice == 4:
    side = float(input("Введіть сторону квадрата: "))
    area = square_area(side)

elif choice == 5:
    base2 = float(input("Введіть основу паралелограма: "))
    height2 = float(input("Введіть висоту паралелограма: "))
    area = parallelogram_area(base2, height2)

else:
    print("Невірний вибір фігури.")
    area = None

# Виведення даних
if area is not None:
    print(f"Площа обраної фігури: {area}")
