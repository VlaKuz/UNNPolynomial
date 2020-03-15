import unittest
from polynomial import Polynomial


class TestPolynomialMethods(unittest.TestCase):
    #init
    def test_init_list_1(self):
        self.assertEqual([5, 3, -10, 0, 2], Polynomial([5, 3, -10, 0, 2]).coeffs)

    def test_init_list_2(self):
        self.assertEqual([0], Polynomial([0, 0, 0, 0, 0]).coeffs)

    def test_init_list_3(self):
        with self.assertRaises(AttributeError):
            Polynomial([])

    def test_init_list_4(self):
        with self.assertRaises(TypeError):
            Polynomial()

    def test_init_list_5(self):
        with self.assertRaises(TypeError):
            Polynomial(['1', '2', '3'])

    def test_init_list_6(self):
        with self.assertRaises(TypeError):
            Polynomial([True, False])

    def test_init_list_7(self):
        with self.assertRaises(TypeError):
            Polynomial(15)

    def test_init_list_8(self):
        with self.assertRaises(TypeError):
            Polynomial([2, 1, False, 3])

    def test_init_list_9(self):
        self.assertEqual([1, 3], Polynomial([0, 0, 0, 0, 0, 0, 1, 3]).coeffs)

    def test_init_list_10(self):
        self.assertEqual([1, 0, 3], Polynomial([0, 0, 0, 0, 0, 0, 1, 0, 3]).coeffs)

    def test_init_list_11(self):
        self.assertEqual([1], Polynomial([1]).coeffs)

    def test_init_list_12(self):
        with self.assertRaises(TypeError):
            Polynomial([2.1, 1, -3.33])

    def test_init_tuple_1(self):
        self.assertEqual([5, 3, -10, 0, 2], Polynomial((5, 3, -10, 0, 2)).coeffs)

    def test_init_tuple_2(self):
        self.assertEqual([0], Polynomial((0, 0, 0, 0, 0)).coeffs)

    def test_init_tuple_3(self):
        with self.assertRaises(AttributeError):
            Polynomial(())

    def test_init_tuple_4(self):
        with self.assertRaises(TypeError):
            Polynomial(('1', '2', '3'))

    def test_init_tuple_5(self):
        with self.assertRaises(TypeError):
            Polynomial((True, False))

    def test_init_tuple_6(self):
        with self.assertRaises(TypeError):
            Polynomial((2, 1, False, 3))

    def test_init_tuple_7(self):
        self.assertEqual([1, 3], Polynomial((0, 0, 0, 0, 0, 0, 1, 3)).coeffs)

    def test_init_tuple_8(self):
        self.assertEqual([1, 0, 3], Polynomial((0, 0, 0, 0, 0, 0, 1, 0, 3)).coeffs)

    def test_init_tuple_9(self):
        with self.assertRaises(TypeError):
            Polynomial((2.1, 1, -3.33))

    def test_init_copy_1(self):
        polynom_test_1 = Polynomial([3, 3, 1])
        polynom_test_2 = Polynomial(polynom_test_1)
        self.assertEqual(polynom_test_1.coeffs, polynom_test_2.coeffs)

    def test_init_copy_2(self):
        polynom_test_1 = Polynomial([3, 3, 1])
        polynom_test_2 = Polynomial(polynom_test_1)
        polynom_test_2.coeffs[1] = 5
        self.assertEqual([3, 5, 1], polynom_test_2.coeffs)

    def test_init_copy_3(self):
        polynom_test_1 = Polynomial([3, 3, 1])
        polynom_test_2 = Polynomial(polynom_test_1)
        polynom_test_2.coeffs.append(5)
        self.assertEqual([3, 3, 1, 5], polynom_test_2.coeffs)
    #equal
    def test_eq_1(self):
        polynom_test_1 = Polynomial([3, 3, 1])
        polynom_test_2 = Polynomial(polynom_test_1)
        self.assertEqual(True, polynom_test_1 == polynom_test_2)

    def test_eq_2(self):
        polynom_test_1 = Polynomial([3, 3, 1])
        polynom_test_2 = Polynomial([-2, 1])
        self.assertEqual(True, polynom_test_1 != polynom_test_2)

    def test_eq_3(self):
        polynom_test_1 = Polynomial([3, 3, 1])
        polynom_test_2 = Polynomial([-2, 1])
        self.assertEqual(False, polynom_test_1 == polynom_test_2)

    def test_eq_4(self):
        polynom_test_1 = Polynomial([3, 3, 1])
        polynom_test_2 = Polynomial(polynom_test_1)
        self.assertEqual(False, polynom_test_1 != polynom_test_2)

    def test_eq_5(self):
        polynom_test_1 = Polynomial([3, 3, 1])
        with self.assertRaises(TypeError):
            polynom_test_1 == True

    def test_eq_6(self):
        polynom_test_1 = Polynomial([1, 2, 3])
        with self.assertRaises(TypeError):
            polynom_test_1 == '123'

    def test_eq_7(self):
        polynom_test_1 = Polynomial([1, 2, 4])
        with self.assertRaises(TypeError):
            polynom_test_1 != '123'

    #add
    def test_add_pol_1(self):
        self.assertEqual(Polynomial([5, 3, -10, 0, 102]), Polynomial([5, 3, -10, 0, 2]) + 100)

    def test_add_pol_2(self):
        self.assertEqual(Polynomial([5, 3, -10, 0, 102]), 100 + Polynomial([5, 3, -10, 0, 2]))

    def test_add_pol_3(self):
        self.assertEqual(Polynomial([20, 9, -20, 0, 0]), Polynomial([5, 6, -10, 0, -2]) + Polynomial([15, 3, -10, 0, 2]))

    def test_add_pol_4(self):
        self.assertEqual(Polynomial([15, 3, -20, 0, 0]), Polynomial([-10, 0, -2]) + Polynomial([15, 3, -10, 0, 2]))

    def test_add_pol_5(self):
        self.assertEqual(Polynomial([15, 3, -20, 0, 0]), Polynomial([15, 3, -10, 0, 2]) + Polynomial([-10, 0, -2]))

    def test_add_pol_6(self):
        self.assertEqual(Polynomial([0]), Polynomial([-5, -3, 10, 0, 2]) + Polynomial([5, 3, -10, 0, -2]))

    def test_add_pol_7(self):
        self.assertEqual(Polynomial([4]), Polynomial([-5, -3, 10, 0, 2]) + Polynomial([5, 3, -10, 0, 2]))

    def test_add_pol_8(self):
        self.assertEqual(Polynomial((5, 3, -10, 0, 102)), Polynomial((5, 3, -10, 0, 2)) + 100)

    def test_add_pol_9(self):
        self.assertEqual(Polynomial((5, 3, -10, 0, 102)), 100 + Polynomial((5, 3, -10, 0, 2)))

    def test_add_pol_10(self):
        self.assertEqual(Polynomial((20, 9, -20, 0, 0)), Polynomial((5, 6, -10, 0, -2)) + Polynomial((15, 3, -10, 0, 2)))

    def test_add_pol_11(self):
        self.assertEqual(Polynomial((15, 3, -20, 0, 0)), Polynomial((-10, 0, -2)) + Polynomial((15, 3, -10, 0, 2)))

    def test_add_pol_12(self):
        self.assertEqual(Polynomial([15, 3, -20, 0, 0]), Polynomial((15, 3, -10, 0, 2)) + Polynomial([-10, 0, -2]))

    def test_add_pol_13(self):
        self.assertEqual(Polynomial([0]), Polynomial([-5, -3, 10, 0, 2]) + Polynomial((5, 3, -10, 0, -2)))

    def test_add_pol_14(self):
        self.assertEqual(Polynomial([4]), Polynomial((-5, -3, 10, 0, 2)) + Polynomial([5, 3, -10, 0, 2]))

    def test_add_15(self):
        with self.assertRaises(TypeError):
            Polynomial([-5, -3, 10, 0, 2]) + '12'

    def test_add_16(self):
        with self.assertRaises(TypeError):
           '12' + Polynomial([-5, -3, 10, 0, 2])

    #sub
    def test_sub_pol_1(self):
        self.assertEqual(Polynomial([5, 3, -10, 0, -98]), Polynomial([5, 3, -10, 0, 2]) - 100)

    def test_sub_pol_2(self):
        self.assertEqual(Polynomial([-5, -3, 10, 0, 98]), 100 - Polynomial([5, 3, -10, 0, 2]))

    def test_sub_pol_3(self):
        self.assertEqual(Polynomial([0]), Polynomial([-5, 3, 7]) - Polynomial([-5, 3, 7]))

    def test_sub_pol_4(self):
        self.assertEqual(Polynomial([2, 3]), Polynomial([5, 6, -7, 2, 3]) - Polynomial([5, 6, -7, 0, 0]))

    def test_sub_pol_5(self):
        with self.assertRaises(TypeError):
            Polynomial([-2]) - '123'

    def test_sub_pol_5(self):
        with self.assertRaises(TypeError):
            '123' - Polynomial([-2])

    def test_sub_pol_6(self):
        self.assertEqual(
            Polynomial([-5, -6, 3]), -Polynomial([5, 6, -3]))

    #mul
    def test_mul_pol_1(self):
        self.assertEqual(Polynomial([10, 6, -20, 0, 4]), Polynomial([5, 3, -10, 0, 2]) * 2)

    def test_mul_pol_2(self):
        self.assertEqual(Polynomial([10, 6, -20, 0, 4]), 2 * Polynomial([5, 3, -10, 0, 2]))

    def test_mul_pol_3(self):
        self.assertEqual(Polynomial([25, 30, -41, -30, 10, 6]), Polynomial([5, 3]) * Polynomial([5, 3, -10, 0, 2]))

    def test_mul_pol_4(self):
        self.assertEqual(Polynomial([25, 30, -41, -30, 10, 6]), Polynomial([5, 3, -10, 0, 2]) * Polynomial([5, 3]))

    def test_mul_pol_5(self):
        self.assertEqual(Polynomial([0]), Polynomial([5, 3, -10, 0, 2]) * 0)

    def test_mul_pol_6(self):
        self.assertEqual(Polynomial([0]), 0 * Polynomial([5, 3, -10, 0, 2]))

    def test_mul_pol_7(self):
        with self.assertRaises(TypeError):
            Polynomial([5, 3, -10, 0, 2]) * '123'

    def test_mul_pol_8(self):
        with self.assertRaises(TypeError):
            '123' * Polynomial([5, 3, -10, 0, 2])

    #str
    def test_str_pol_1(self):
        self.assertEqual('x^3 + 4x - 3', str(Polynomial([1, 0, 4, -3])))

    def test_str_pol_2(self):
        self.assertEqual('-3', str(Polynomial([-3])))

    def test_str_pol_3(self):
        self.assertEqual('0', str(Polynomial([0])))

    def test_str_pol_4(self):
        self.assertEqual('4x^2 + 5', str(Polynomial([0, 0, 0, 4, 0, 5])))

    def test_str_pol_5(self):
        self.assertEqual('-4x^2 - 5x', str(Polynomial([-4, -5, 0])))
    #repr
    def test_repr_pol_1(self):
        self.assertEqual('Polynomial([-4, -5, 0])', repr(Polynomial([-4, -5, 0])))

    def test_repr_pol_2(self):
        self.assertEqual('Polynomial([0])', repr(Polynomial([0, 0, 0, 0, 0])))

    def test_full_pol_1(self):
        self.assertEqual('-8x^7 - 12x^6 + 38x^5 - 28x^4 + 6x^3 + 28x^2 - 15x - 4', str(Polynomial([4, 0, -3, 5]) * Polynomial([-2, 6, 8, 0, 0]) + 5 - 3 * Polynomial([12, 0, 0, 0, 4, 5, 3])))

    def test_bool_exc_1(self):
        with self.assertRaises(TypeError):
            True * Polynomial([5, 3, -10, 0, 2])

    def test_bool_exc_2(self):
        with self.assertRaises(TypeError):
            Polynomial([5, 3, -10, 0, 2]) * False

    def test_bool_exc_3(self):
        with self.assertRaises(TypeError):
            True + Polynomial([5, 3, -10, 0, 2])

    def test_bool_exc_4(self):
        with self.assertRaises(TypeError):
            Polynomial([5, 3, -10, 0, 2]) + False

    def test_bool_exc_5(self):
        with self.assertRaises(TypeError):
            True - Polynomial([5, 3, -10, 0, 2])

    def test_bool_exc_6(self):
        with self.assertRaises(TypeError):
            Polynomial([5, 3, -10, 0, 2]) - False

if __name__ == '__main__':
    unittest.main()