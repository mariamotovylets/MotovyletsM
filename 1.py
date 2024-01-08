
import math

def calculate_rectangle_area(length, width):
    """Обчислює площу прямокутника."""
    return length * width

def calculate_circle_area(radius):
    """Обчислює площу кола."""
    return math.pi * radius ** 2

def calculate_triangle_area(base, height):
    """Обчислює площу трикутника."""
    return 0.5 * base * height

def calculate_square_area(side):
    """Обчислює площу квадрата."""
    return side ** 2

def calculate_parallelogram_area(base, height):
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
    length_rect = float(input("Введіть довжину прямокутника: "))
    width_rect = float(input("Введіть ширину прямокутника: "))
    area = calculate_rectangle_area(length_rect, width_rect)

elif choice == 2:
    radius_circle = float(input("Введіть радіус кола: "))
    area = calculate_circle_area(radius_circle)

elif choice == 3:
    base_triangle = float(input("Введіть основу трикутника: "))
    height_triangle = float(input("Введіть висоту трикутника: "))
    area = calculate_triangle_area(base_triangle, height_triangle)

elif choice == 4:
    side_square = float(input("Введіть сторону квадрата: "))
    area = calculate_square_area(side_square)

elif choice == 5:
    base_parallelogram = float(input("Введіть основу паралелограма: "))
    height_parallelogram = float(input("Введіть висоту паралелограма: "))
    area = calculate_parallelogram_area(base_parallelogram, height_parallelogram)

else:
    print("Невірний вибір фігури.")
    area = None

# Виведення даних
if area is not None:
    print(f"Площа обраної фігури: {area}")
