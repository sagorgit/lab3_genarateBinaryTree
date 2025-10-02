# gen_bin_tree.py

from typing import Optional, Dict, Any

def gen_bin_tree(height: Optional[int] = None, root: Optional[int] = None) -> Optional[Dict[str, Any]]:
    """
    Рекурсивная функция для построения бинарного дерева.

    Если root и height не заданы, берутся значения по варианту №14:
    root = 14, height = 4
    left = 2 - (root - 1)
    right = root * 2
    """

    # Если пользователь не ввёл значения → берём вариант 14
    if height is None:
        height = 4
    if root is None:
        root = 14

    # Базовый случай: если высота дерева = 0 → дальше нет узлов
    if height == 0:
        return None

    # Вычисляем значения потомков (формулы варианта 14)
    left_val = 2 - (root - 1)
    right_val = root * 2

    # Возвращаем узел в виде словаря
    return {
        "value": root,
        "left": gen_bin_tree(height - 1, left_val),
        "right": gen_bin_tree(height - 1, right_val),
    }


if __name__ == "__main__":
    print("=== Генератор бинарного дерева (Вариант 14) ===")

    # Ввод значений от пользователя
    root_in = input("Введите значение корня (Enter — по умолчанию 14): ").strip()
    height_in = input("Введите высоту дерева (Enter — по умолчанию 4): ").strip()

    # Если введено число → преобразуем в int, иначе None (тогда возьмём дефолт)
    root_val = int(root_in) if root_in else None
    height_val = int(height_in) if height_in else None

    # Строим дерево
    tree = gen_bin_tree(height=height_val, root=root_val)

    print("\nСгенерированное бинарное дерево:\n")
    print(tree)
