import unittest
mx = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def test_true(self):
        true_grid = [0,0,True]
        self.assertEqual(mx(true_grid), True)

    def test_false(self):
        false_grid = [-1,-1,False]
        self.assertEqual(mx(false_grid), False)

    def test_one(self):
        one_grid = [1]
        self.assertEqual(mx(one_grid), 1)

    def test_decimal(self):
        decimal_grid = [0.9,0.9999,0.99999999999999]
        self.assertEqual(mx(decimal_grid), 0.99999999999999)

    def test_one_max(self):
        one_grid = [1, 2, 3, 9, 1]
        self.assertEqual(mx(one_grid), 9)

    def test_two_max(self):
        two_grid = [9, 2, 3, 9, 1]
        self.assertEqual(mx(two_grid), 9)

    def test_all_max(self):
        all_grid = [9, 9, 9, 9, 9]
        self.assertEqual(mx(all_grid), 9)

    def test_large_max(self):
        inf_grid = [float("inf"), 9, 9, 9, 9]
        self.assertEqual(mx(inf_grid), float('inf'))

    def test_sign_max(self):
        sign_grid = [-9, 0, 9]
        self.assertEqual(mx(sign_grid), 9)

    def test_string_max(self):
        string = "Monty Python"
        self.assertEqual(mx(string), "y")

    def test_list_max(self):
        list = [[1,2,3,4],[12, 12, 23, 23]]
        self.assertEqual(mx(list), [12, 12, 23, 23])


    def test_raise_error(self):

        with self.assertRaises(TypeError):
            mx(None)

        with self.assertRaises(TypeError):
            mx(["string", 1, [1, 2]])

        self.assertIsNone(mx([]))



if __name__ == "__main__":
    unittest.main()
