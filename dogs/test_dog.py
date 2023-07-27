import unittest
import unittest.mock
from unittest.mock import call, patch
from dog import Dog, side_effect

# class DogTestCase extends unittest.TestCase
class DogTestCase(unittest.TestCase):

    # @patch('dog.side_effect')
    def test_set_color(self):
        # mock_side_effect.return_value = None

        testDog = Dog('test', 'mixed', 1, 'white')
        newColor = 'brown'
        testDog.set_color(newColor)
        self.assertEqual(testDog.color, newColor)






    # # Testing a simple math function (basic example of assertEqual)
    # def test_age_in_dog_years(self):
    #     # Arrange
    #     testDog = Dog('test', 'mixed', 5, 'white')

    #     # Act
    #     age_in_dog_years = testDog.age_in_dog_years()

    #     # Assert -- with mathematical calculations like this I will just do this myself
    #     self.assertEqual(age_in_dog_years, 35)

    # # Testing constructor
    # def test_constructor_initializes_breed(self):
    #     # Arrange
    #     breed = 'mixed'

    #     # Act
    #     testDog = Dog('test', breed, 1, 'blue')

    #     # Assert
    #     self.assertEqual(breed, testDog.breed)
    
    # # Testing that the correct exception is thrown in a particular situation
    # # When working in a larger code base, it is important to understand what you're expected output is (or expected Error)
    # def test_constructor_throws_exception(self):
    #     # Arrange
    #     breed = ''

    #     # Act / Assert
    #     with self.assertRaises(Exception):
    #         testDog = Dog('test', breed, 1, 'blue')
    
    # # If we look at the side_effect function in dog.py we see that it has a parameter color
    # # So let's write a test to make sure that the side_effect function is called with the correct argument 

    # # @patch('{module_name}.{function_name}') -- remember module is generally the file name (minus the .py at the end)
    # @patch('dog.side_effect') 
    # def test_set_color_side_effect(self, mock_side_effect):
    #     # Arrange
    #     testDog = Dog('test', 'mixed', 1, 'white')
    #     newColor = 'brown'

    #     # Act
    #     testDog.set_color(newColor)

    #     # Assert
    #     call1 = call('brown')
    #     mock_side_effect.assert_has_calls([call1])
    
    # # Secondary syntax for mocks
    # # instead of creating the mock function using the @patch decorator, we can use patch within our function
    # def test_set_color_side_effect_2(self):
    #     # Arrange
    #     testDog = Dog('test', 'mixed', 1, 'white')
    #     newColor = 'brown'

    #     # this patch syntax allows for the mock_side_effect to be used and tested within the "with" code block
    #     with patch('dog.side_effect') as mock_side_effect:
    #         # Act
    #         testDog.set_color(newColor)
    #         # Assert
    #         mock_side_effect.assert_called_once_with('brown')

    # # This @patch.object syntax works with classes and their methods 
    # # First, import the class that contains the method you want to mock then use the below syntax
    # # @patch.object({ClassName}, '{method_name}')
    # @patch.object(Dog, 'get_info_side_effect')
    # def test_get_info_side_effect(self, mock_get_info_side_effect):
    #     # Arrange
    #     expectedResult = 'something new'

    #     # in order to remove an external dependency (or a bad side_effect), we can mock return values of our side_effect functions
    #     # this allows us to test one function at a time, without side_effects potentially messing with our test
    #     mock_get_info_side_effect.return_value = expectedResult
    #     testDog = Dog('test', 'mixed', 1, 'white')

    #     # Act / Assert
    #     actualResult = testDog.get_info()

    #     # Assert
    #     self.assertEqual(expectedResult, actualResult)


if __name__ == '__main__':
    unittest.main()