from unittest import TestCase
from CodingProject import CodingProject


class TestCodingProject(TestCase):
    cp = CodingProject()

    def test_handle_string_number_1(self):

        print("Input: I am n0thing m0r3 than a string. I t00 hav3 a "
                               "lexic0graphoc 0rd3r")
        print("--------------------------------------------")

        self.cp.set_user_input("I am n0thing m0r3 than a string. I t00 hav3 a "
                               "lexic0graphoc 0rd3r")
        self.cp.handle_string()
        self.assertEqual(self.cp.string_result, ".: 1 0: 6 3: 3 I: 2 a: 6 c: 2 d: 1 e: 1 g: 3 h: 4 i: 3 l: 1 m: 2 "
                                                "n: 4 o: 1 p: 1 r: 5 s: 1 t: 4 v: 1 x: 1")

    def test_handle_string_number_2(self):

        print("Input: sunsoutgunsout")
        print("--------------------------------------------")

        self.cp.set_user_input("sunsoutgunsout")
        self.cp.handle_string()
        self.assertEqual(self.cp.string_result, "g: 1 n: 2 o: 2 s: 3 t: 2 u: 4")

    def test_handle_string_number_3(self):

        print("Input: quit quit")
        print("--------------------------------------------")

        self.cp.set_user_input("quit quit")
        self.cp.handle_string()
        self.assertEqual(self.cp.string_result, "i: 2 q: 2 t: 2 u: 2")

    def test_numeric_sequence_number_1(self):

        print("Input: 1 2 13 45 99 0 0 0 1")
        print("--------------------------------------------")

        self.cp.set_user_input("1 2 13 45 99 0 0 0 1")
        self.cp.handle_numeric()
        self.mean("17.88888888888889")
        self.median("1.0")
        self.mode("0.0")
        self.range("99.0")

    def test_numeric_sequence_number_2(self):

        print("Input: 0")
        print("--------------------------------------------")

        self.cp.set_user_input("0")
        self.cp.handle_numeric()
        self.mean("0.0")
        self.median("0.0")
        self.mode("none")
        self.range("0.0")

    def mean(self, result):
        self.assertEqual(self.cp.mean, result, "Mean failed")

    def median(self, result):
        self.assertEqual(self.cp.median, result, "median failed")

    def mode(self, result):
        self.assertEqual(self.cp.mode, result, "Mode failed")

    def range(self, result):
        self.assertEqual(self.cp.range, result, "Range failed")

    def tearDown(self):
        self.cp.clean_up()
