
import math

def rectangle_area(length, width):
    """Обчислює площу прямокутника."""
    return length * width

def circle_area(radius):
    """Обчислює площу кола."""
    return math.pi * radius ** 2

def triangle_area(base=None, height=None, side_a=None, side_b=None, side_c=None):
    """Обчислює площу трикутника залежно від вхідних даних."""
    if base is not None and height is not None:
        return 0.5 * base * height
    elif side_a is not None and side_b is not None and side_c is not None:
        # За правилом Герона для обчислення площі трикутника
        s = (side_a + side_b + side_c) / 2
        return math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    else:
        print("Невірні вхідні дані для обчислення площі трикутника.")
        return None

def square_area(side):
    """Обчислює площу квадрата."""
    return side ** 2

def parallelogram_area(base, height):
    """Обчислює площу паралелограма."""
    return base2 * height2

def rhombus_area(diagonal1, diagonal2):
    """Обчислює площу ромба."""
    return 0.5 * diagonal1 * diagonal2

def trapezoid_area(base1, base2, height):
    """Обчислює площу трапеції."""
    return 0.5 * (base1 + base2) * height

# Вибір фігури 
while True:
    # Вибір фігури
    print("0. Вихід")
    print("Виберіть фігуру:")
    print("1. Прямокутник")
    print("2. Коло")
    print("3. Трикутник, коли відомо висоту та основу, або відомо три сторони")
    print("4. Квадрат")
    print("5. Паралелограм")
    print("6. Ромб")
    print("7. Трапеція")
    

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
        base_str = input("Введіть основу трикутника (або залиште порожнім): ")
        height_str = input("Введіть висоту трикутника (або залиште порожнім): ")
        side_a_str = input("Введіть довжину сторони A (або залиште порожнім): ")
        side_b_str = input("Введіть довжину сторони B (або залиште порожнім): ")
        side_c_str = input("Введіть довжину сторони C (або залиште порожнім): ")

        base = float(base_str) if base_str.strip() else None
        height = float(height_str) if height_str.strip() else None
        side_a = float(side_a_str) if side_a_str.strip() else None
        side_b = float(side_b_str) if side_b_str.strip() else None
        side_c = float(side_c_str) if side_c_str.strip() else None

        area = triangle_area(base=base, height=height, side_a=side_a, side_b=side_b, side_c=side_c)
        
    elif choice == 4:
        side = float(input("Введіть сторону квадрата: "))
        area = square_area(side)

    elif choice == 5:
        base = float(input("Введіть основу паралелограма: "))
        height = float(input("Введіть висоту паралелограма: "))
        area = parallelogram_area(base, height)
        
    elif choice == 6:
        diagonal1 = float(input("Введіть першу діагональ ромба: "))
        diagonal2 = float(input("Введіть другу діагональ ромба: "))
        area = rhombus_area(diagonal1, diagonal2)

    elif choice == 7:
        base1 = float(input("Введіть верхню основу трапеції: "))
        base2 = float(input("Введіть нижню основу трапеції: "))
        height_trap = float(input("Введіть висоту трапеції: "))
        area = trapezoid_area(base1, base2, height_trap)
    else:
        print("Невірний вибір фігури.")
        area = None

    # Виведення даних
    if area is not None:
        coma = int(input("Введіть кількість знаків після коми: "))
        print(f"Площа обраної фігури: {area:.{coma}f}")
