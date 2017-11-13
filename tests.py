import unittest

from routing import *

class scenario:
    def scenario1(self):
        """Single operator"""
        ops = operators()
        op = operator()
        op.name = "Operator 1"
        op.dictionary = {1: 2.23, 79: 3.3, 43: 1.82, 173: 3.94, 143: 1.15, 146: 4.44, 51: 2.55, 149: 3.53, 54: 4.45,
                    23: 3.5,
                    89: 4.5, 187: 2.1, 53: 4.27}
        ops.append(op)

        ops = ops.iterate("128548")
        if ops.getCheapest(ops,"128548") == None:
            return False
        else:
            return True

    def scenario2(self):
        """Single operator compare value"""
        ops = operators()
        op = operator()
        op.name = "Operator 1"
        op.dictionary = {1: 2.23, 79: 3.3, 43: 1.82, 173: 3.94, 143: 1.15, 146: 4.44, 51: 2.55, 149: 3.53, 54: 4.45,
                    23: 3.5,
                    89: 4.5, 187: 2.1, 53: 4.27}
        ops.append(op)

        ops = ops.iterate("128548")
        if ops.getCheapest(ops,"128548")[0].name == "Operator 1":
            return True
        else:
            return False

    def scenario3(self):
        """Single operator compare value"""
        ops = operators()
        op = operator()
        op.name = "Operator 1"
        op.dictionary = {1: 2.23, 79: 3.3, 43: 1.82, 173: 3.94, 143: 1.15, 146: 4.44, 51: 2.55, 149: 3.53, 54: 4.45,
                    23: 3.5,
                    89: 4.5, 187: 2.1, 53: 4.27}
        ops.append(op)

        ops = ops.iterate("128548")
        if ops.getCheapest(ops,"128548")[1] == 2.32:
            return True
        else:
            return False

    def scenario1_1(self):
        """Multiple operators"""
        ops = operators()
        op = operator()
        op.name = "Operator 1"
        op.dictionary = {1: 2.23, 79: 3.3, 43: 1.82, 173: 3.94, 143: 1.15, 146: 4.44, 51: 2.55, 149: 3.53, 54: 4.45,
                    23: 3.5,
                    89: 4.5, 187: 2.1, 53: 4.27}
        ops.append(op)

        op = operator()
        op.name = "Operator 2"
        op.dictionary = {193: 3.13, 2: 3.37, 4: 2.63, 101: 4.09, 177: 2.79, 107: 1.74, 13: 3.97, 14: 3.13, 77: 1.08,
                         113: 3.23, 50: 3.07, 117: 4.14, 118: 3.12, 25: 4.77, 154: 2.86, 191: 4.19}
        ops.append(op)

        op = operator()
        op.name = "Operator 3"
        op.dictionary = {96: 4.57, 131: 2.61, 100: 2.99, 166: 3.87, 38: 2.88, 199: 2.36, 72: 1.83, 105: 2.01, 10: 4.46,
                         50: 3.88, 153: 3.9, 4: 1.41, 27: 3.11, 101: 4.93, 94: 3.3, 159: 4.81}
        ops.append(op)

        op = operator()
        op.name = "Operator 4"
        op.dictionary = {1: 4.07, 2: 2.01, 165: 2.38, 161: 4.69, 75: 4.19, 47: 2.33, 113: 2.93, 178: 2.25, 19: 4.17,
                         180: 4.59, 150: 1.18, 103: 4.36, 61: 3.91}
        ops.append(op)

        ops = ops.iterate("128548")
        if ops.getCheapest(ops,"128548") == None:
            return False
        else:
            return True

    def scenario2_1(self):
        """Multiple operators compare value"""
        ops = operators()
        op = operator()
        op.name = "Operator 1"
        op.dictionary = {1: 2.23, 79: 3.3, 43: 1.82, 173: 3.94, 143: 1.15, 146: 4.44, 51: 2.55, 149: 3.53, 54: 4.45,
                         23: 3.5,
                         89: 4.5, 187: 2.1, 53: 4.27}
        ops.append(op)

        op = operator()
        op.name = "Operator 2"
        op.dictionary = {193: 3.13, 2: 3.37, 4: 2.63, 101: 4.09, 177: 2.79, 107: 1.74, 13: 3.97, 14: 3.13, 77: 1.08,
                         113: 3.23, 50: 3.07, 117: 4.14, 118: 3.12, 25: 4.77, 154: 2.86, 191: 4.19}
        ops.append(op)

        op = operator()
        op.name = "Operator 3"
        op.dictionary = {96: 4.57, 131: 2.61, 100: 2.99, 166: 3.87, 38: 2.88, 199: 2.36, 72: 1.83, 105: 2.01, 10: 4.46,
                         50: 3.88, 153: 3.9, 4: 1.41, 27: 3.11, 101: 4.93, 94: 3.3, 159: 4.81}
        ops.append(op)

        op = operator()
        op.name = "Operator 4"
        op.dictionary = {1: 4.07, 2: 2.01, 165: 2.38, 161: 4.69, 75: 4.19, 47: 2.33, 113: 2.93, 178: 2.25, 19: 4.17,
                         180: 4.59, 150: 1.18, 103: 4.36, 61: 3.91}
        ops.append(op)

        ops = ops.iterate("128548")
        if ops.getCheapest(ops,"128548")[0].name == "Operator 1":
            return True
        else:
            return False

    def scenario3_1(self):
        """Multiple operators compare value"""
        ops = operators()
        op = operator()
        op.name = "Operator 1"
        op.dictionary = {1: 2.23, 79: 3.3, 43: 1.82, 173: 3.94, 143: 1.15, 146: 4.44, 51: 2.55, 149: 3.53, 54: 4.45,
                         23: 3.5,
                         89: 4.5, 187: 2.1, 53: 4.27}
        ops.append(op)

        op = operator()
        op.name = "Operator 2"
        op.dictionary = {193: 3.13, 2: 3.37, 4: 2.63, 101: 4.09, 177: 2.79, 107: 1.74, 13: 3.97, 14: 3.13, 77: 1.08,
                         113: 3.23, 50: 3.07, 117: 4.14, 118: 3.12, 25: 4.77, 154: 2.86, 191: 4.19}
        ops.append(op)

        op = operator()
        op.name = "Operator 3"
        op.dictionary = {96: 4.57, 131: 2.61, 100: 2.99, 166: 3.87, 38: 2.88, 199: 2.36, 72: 1.83, 105: 2.01, 10: 4.46,
                         50: 3.88, 153: 3.9, 4: 1.41, 27: 3.11, 101: 4.93, 94: 3.3, 159: 4.81}
        ops.append(op)

        op = operator()
        op.name = "Operator 4"
        op.dictionary = {1: 4.07, 2: 2.01, 165: 2.38, 161: 4.69, 75: 4.19, 47: 2.33, 113: 2.93, 178: 2.25, 19: 4.17,
                         180: 4.59, 150: 1.18, 103: 4.36, 61: 3.91}
        ops.append(op)

        ops = ops.iterate("128548")
        if ops.getCheapest(ops,"128548")[1] == 2.32:
            return True
        else:
            return False

class TestStringMethods(unittest.TestCase):

    def test_single_operator(self):
        scenario().scenario1()

    def test_single_operator2(self):
        scenario().scenario2()

    def test_single_operator3(self):
        scenario().scenario3()

    def test_multiple_operator1(self):
        scenario().scenario1_1()

    def test_multiple_operator2(self):
        scenario().scenario2_1()

    def test_multiple_operator3(self):
        scenario().scenario3_1()


if __name__ == '__main__':
    unittest.main()