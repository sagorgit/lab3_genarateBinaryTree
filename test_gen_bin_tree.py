# test_bin_tree.py
# Простые тесты для начинающих: проверяем, что генерируется бинарное дерево,
# параметры по умолчанию берутся из варианта №14, пользовательские параметры работают,
# глубина (высота) корректная, базовый случай при height=0, и формулы выполняются.

import unittest
from typing import Optional, Dict, Any
from gen_bin_tree import gen_bin_tree  # импортируем функцию из gen_bin_tree.py

class TestBinaryTreeBeginner(unittest.TestCase):
    """Тесты для функции gen_bin_tree (вариант №14)."""

    def test_defaults_variant_14(self):
        """
        Если параметры не переданы, должны использоваться значения варианта №14:
        root=14, height=4.
        """
        tree = gen_bin_tree()  # без аргументов
        self.assertIsInstance(tree, dict)
        self.assertEqual(tree["value"], 14)
        # проверяем наличие потомков-ключей
        self.assertIn("left", tree)
        self.assertIn("right", tree)

    def test_custom_params_used(self):
        """
        Если параметры переданы, используются они (а не значения варианта).
        Для варианта 14 формулы:
          left = 2 - (root - 1)
          right = root * 2
        """
        tree = gen_bin_tree(height=2, root=5)
        self.assertEqual(tree["value"], 5)
        # считаем ожидаемые значения потомков на 1-й уровень
        expected_left = 2 - (5 - 1)   # = -2
        expected_right = 5 * 2        # = 10
        self.assertEqual(tree["left"]["value"], expected_left)
        self.assertEqual(tree["right"]["value"], expected_right)

    def test_zero_height_returns_none(self):
        """Базовый случай: если height == 0, должно вернуться None (пустое дерево)."""
        self.assertIsNone(gen_bin_tree(height=0, root=14))

    def test_tree_depth_matches_height(self):
        """
        Проверяем, что фактическая глубина дерева равна height.
        Глубина считается как число уровней узлов (None не считается).
        """
        def depth(node: Optional[Dict[str, Any]]) -> int:
            if node is None:
                return 0
            return 1 + max(depth(node["left"]), depth(node["right"]))

        h = 3
        tree = gen_bin_tree(height=h, root=7)
        self.assertEqual(depth(tree), h)

    def test_all_nodes_are_dict_or_none(self):
        """
        Проверяем структуру: каждый узел — это словарь с ключами 'value', 'left', 'right' или None.
        (Для начинающих: это гарантирует, что мы действительно строим дерево-словарь.)
        """
        def check(node) -> bool:
            if node is None:
                return True
            if not isinstance(node, dict):
                return False
            # ключи должны быть
            for k in ("value", "left", "right"):
                if k not in node:
                    return False
            return check(node["left"]) and check(node["right"])

        tree = gen_bin_tree(height=3, root=4)
        self.assertTrue(check(tree))

    def test_formulas_hold_on_each_level(self):
        """
        Дополнительная простая проверка формул на нескольких уровнях.
        Для каждого узла x:
          left_value = 2 - (x - 1)
          right_value = x * 2
        Проверим это для первых двух уровней.
        """
        tree = gen_bin_tree(height=3, root=10)

        # уровень 0 (корень)
        x0 = tree["value"]
        self.assertEqual(tree["left"]["value"], 2 - (x0 - 1))
        self.assertEqual(tree["right"]["value"], x0 * 2)

        # уровень 1 (дети корня)
        left1 = tree["left"]
        right1 = tree["right"]

        xL = left1["value"]
        xR = right1["value"]

        # Формулы должны выполняться и для следующего уровня
        self.assertEqual(left1["left"]["value"],  2 - (xL - 1))
        self.assertEqual(left1["right"]["value"], xL * 2)
        self.assertEqual(right1["left"]["value"], 2 - (xR - 1))
        self.assertEqual(right1["right"]["value"], xR * 2)


if __name__ == "__main__":
    # Универсальный запуск (включая Google Colab/Jupyter):
    unittest.main(argv=[''], verbosity=2, exit=False)
    # Если запускаете как обычный скрипт локально, эта строка тоже корректно отработает.
