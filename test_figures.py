import unittest
import math

import circle
import square
import rectangle
import triangle


class TestCircle(unittest.TestCase):
    '''
    Набор модульных тестов для проверки корректности работы функций модуля circle.

    Проверяются:
        • вычисление площади круга;
        • вычисление длины окружности;
        • работа функции при нулевом радиусе;
        • большие значения радиуса;
        • дробные значения радиуса;
        • отрицательные значения радиуса (проверяется фактическое поведение формулы).

    Все тесты построены по принципу:
        1. передача входных параметров;
        2. вычисление результата с помощью функции;
        3. сравнение результата с ожидаемым значением.
    '''

    def test_circle_area(self):
        '''
        Проверяет корректность вычисления площади круга радиуса 1.

        Ожидаемое значение:
            π * 1²
        '''
        self.assertAlmostEqual(circle.area(1), math.pi * 1 * 1)

    def test_circle_perimeter(self):
        '''
        Проверяет вычисление длины окружности радиуса 1.

        Ожидаемое значение:
            2 * π * 1
        '''
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi * 1)

    def test_circle_zero(self):
        '''
        Проверяет работу функций при радиусе равном 0.

        Ожидаемые значения:
            площадь = 0
            длина окружности = 0
        '''
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.perimeter(0), 0)

    def test_circle_large(self):
        '''
        Проверяет работу функций при большом значении радиуса.

        Пример:
            r = 1000
        '''
        self.assertAlmostEqual(circle.area(1000), math.pi * 1000**2)

    def test_circle_float_radius(self):
        '''
        Проверяет корректность работы функций при дробном значении радиуса.

        Пример:
            r = 0.5
        '''
        self.assertAlmostEqual(circle.area(0.5), math.pi * 0.5 * 0.5)
        self.assertAlmostEqual(circle.perimeter(0.5), 2 * math.pi * 0.5)

    def test_circle_negative_radius_math_result(self):
        '''
        Проверяет фактическое поведение формул при отрицательном радиусе.

        Функции не запрещают отрицательные значения,
        поэтому проверяется чистый математический результат.
        '''
        self.assertAlmostEqual(circle.area(-2), math.pi * 4)
        self.assertAlmostEqual(circle.perimeter(-2), -4 * math.pi)


class TestSquare(unittest.TestCase):
    '''
    Набор тестов для проверки функций модуля square.

    Проверяются:
        • корректность вычисления площади и периметра квадрата;
        • работа с нулевыми, большими и дробными значениями;
        • математическое поведение формул при отрицательных значениях.
    '''

    def test_square_area(self):
        '''Проверяет площадь квадрата со стороной 5 (ожидается 25).'''
        self.assertEqual(square.area(5), 25)

    def test_square_perimeter(self):
        '''Проверяет периметр квадрата со стороной 5 (ожидается 20).'''
        self.assertEqual(square.perimeter(5), 20)

    def test_square_zero(self):
        '''Проверяет работу функций при нулевой длине стороны.'''
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.perimeter(0), 0)

    def test_square_large(self):
        '''Проверяет функции при большой стороне (a = 1000).'''
        self.assertEqual(square.area(1000), 1000000)

    def test_square_float_side(self):
        '''Проверяет работу функций при дробной длине стороны.'''
        self.assertAlmostEqual(square.area(2.5), 6.25)
        self.assertAlmostEqual(square.perimeter(2.5), 10.0)

    def test_square_negative_side(self):
        '''
        Проверяет математическое поведение формул при отрицательной стороне.
        Функции не запрещают отрицательные значения.
        '''
        self.assertEqual(square.area(-3), 9)
        self.assertEqual(square.perimeter(-3), -12)


class TestRectangle(unittest.TestCase):
    '''
    Набор тестов для проверки функций модуля rectangle.

    Проверяются:
        • вычисление площади;
        • вычисление периметра;
        • случаи с нулевыми сторонами;
        • дробные значения сторон;
        • проверка коммутативности умножения (a*b == b*a).
    '''

    def test_rectangle_area(self):
        '''Проверяет площадь прямоугольника 5×3 (ожидается 15).'''
        self.assertEqual(rectangle.area(5, 3), 15)

    def test_rectangle_perimeter(self):
        '''Проверяет периметр прямоугольника 5×3 (ожидается 16).'''
        self.assertEqual(rectangle.perimeter(5, 3), 16)

    def test_rectangle_zero(self):
        '''Проверяет поведение функций при нулевой стороне.'''
        self.assertEqual(rectangle.area(5, 0), 0)
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_rectangle_square_case(self):
        '''Проверка случая, когда прямоугольник становится квадратом.'''
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_rectangle_float_sides(self):
        '''Проверяет вычисления при дробных сторонах.'''
        self.assertAlmostEqual(rectangle.area(2.5, 4.0), 10.0)
        self.assertAlmostEqual(rectangle.perimeter(2.5, 4.0), 13.0)

    def test_rectangle_commutativity_of_sides(self):
        '''Проверяет, что порядок сторон не влияет на результат.'''
        self.assertEqual(rectangle.area(2, 7), rectangle.area(7, 2))
        self.assertEqual(rectangle.perimeter(2, 7), rectangle.perimeter(7, 2))


class TestTriangle(unittest.TestCase):
    '''
    Тестовый набор для функций модуля triangle.

    Проверяются:
        • площадь по основанию и высоте;
        • периметр по трём сторонам;
        • нулевые значения параметров;
        • большие числа;
        • дробные значения;
        • вырожденные случаи.
    '''

    def test_triangle_area(self):
        '''Проверяет площадь треугольника (основание 10, высота 5).'''
        self.assertEqual(triangle.area(10, 5), 25.0)

    def test_triangle_perimeter(self):
        '''Проверяет периметр классического треугольника 3–4–5.'''
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_triangle_zero(self):
        '''Проверяет вычисление площади при нулевом основании или высоте.'''
        self.assertEqual(triangle.area(0, 10), 0)
        self.assertEqual(triangle.area(10, 0), 0)

    def test_triangle_large(self):
        '''Проверяет работу функций при больших значениях сторон.'''
        self.assertEqual(triangle.perimeter(100, 200, 300), 600)

    def test_triangle_float_values(self):
        '''Проверяет вычисление площади и периметра при дробных входных данных.'''
        self.assertAlmostEqual(triangle.area(2.5, 4.0), 2.5 * 4.0 / 2)
        self.assertAlmostEqual(
            triangle.perimeter(1.5, 2.5, 3.5), 1.5 + 2.5 + 3.5
        )

    def test_triangle_degenerate(self):
        '''Проверяет поведение формулы периметра в вырожденных случаях.'''
        self.assertEqual(triangle.perimeter(0, 4, 5), 9)
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)


if __name__ == '__main__':
    '''
    Точка входа для запуска всех тестов данного модуля.

    Запускается командами:
        python test_figures.py
        python -m unittest test_figures.py
        python -m unittest discover
    '''
    unittest.main()
