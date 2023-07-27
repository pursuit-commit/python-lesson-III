from unittest.mock import patch
from _ import ClassA, ClassB

@patch.object(ClassB, 'method_3')
@patch.object(ClassB, 'method_2')
@patch('classb.method_1')
def test_same_method_multi_return_value(self, method_1, method_2, method_3):
    method_1.return_value = 0
    method_2.return_value = 1

    # execute code that relies on Class1 and Class2 and method_1 and method_2

    # assert that the return values are correct