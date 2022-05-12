from random import random
import unittest
from unittest.mock import patch


def fun():
    data = getData()
    data.update({
        'company': 'Pursuit'
    })
    return data

def getData():
    return dict({
        'name': 'Billy',
        'lastName': 'Taggart',
        'phoneNumber': random(10)
    })

class DataTestCase(unittest.TestCase):

    # Testing fun() should not be reliant on the implementation of the get data function
    @patch('testing.getData')
    def test_data_obj_company(self, mock_get_data):
        # Arrange
        # We hard code the return value of the getData function so that we can see an end result
        mock_get_data.return_value = dict({
            'name': 'Jamee',
            'lastName': 'Hengari',
            'phoneNumber': '00000000000'
        })

        # Act
        data = fun()

        # Assert
        self.assertEqual(data['company'], 'Pursuit')

if __name__ == '__main__':
    unittest.main()