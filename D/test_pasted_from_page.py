#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        print('------------')
        print(out)
        print('------------')
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """7
100 120 130 130 115 115 150"""
        output = """1685"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
100 200 200 200 200 200"""
        output = """2000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
100 100"""
        output = """1216"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
