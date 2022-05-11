import unittest
import unittest.mock
from unittest.mock import patch
from dog import Dog

class DogTestCase(unittest.TestCase):

    def test_age_in_dog_years(self):
        # Arrange
        testDog = Dog('test', 'mixed', 5, 'white')

        # Act
        age_in_dog_years = testDog.age_in_dog_years()

        # Assert -- with mathematical calculations like this I will just do this myself
        self.assertEqual(age_in_dog_years, 35)

    def test_constructor_initializes_breed(self):
        # Arrange
        breed = 'mixed'

        # Act
        testDog = Dog('test', breed, 1, 'blue')

        # Assert
        self.assertEqual(breed, testDog.breed)
    
    def test_constructor_throws_exception(self):
        # Arrange
        breed = ''

        # Act / Assert
        with self.assertRaises(Exception):
            testDog = Dog('test', breed, 1, 'blue')
    

    # THIS WILL BREAK -- side_effect cannot call assert_called_once_with, this is where mocks come in
    # def test_set_color_side_effect(self):
    #     # Arrange
    #     testDog = Dog('test', 'mixed', 1, 'white')
    #     newColor = 'brown'

    #     # Act
    #     testDog.set_color(newColor)

    #     # Assert
    #     side_effect.assert_called_once_with()

    @patch('dog.side_effect')
    def test_set_color_side_effect(self, mock_side_effect):
        # Arrange
        testDog = Dog('test', 'mixed', 1, 'white')
        newColor = 'brown'

        # Act
        testDog.set_color(newColor)

        # Assert
        mock_side_effect.assert_called_once_with()
    
    # Secondary syntax for mocks
    def test_set_color_side_effect_2(self):
        # Arrange
        testDog = Dog('test', 'mixed', 1, 'white')
        newColor = 'brown'

        with patch('dog.side_effect') as mock_side_effect:
            # Act
            testDog.set_color(newColor)
            # Assert
            mock_side_effect.assert_called_once_with()

    @patch.object(Dog, 'get_info_side_effect')
    def test_get_info_side_effect(self, mock_get_info_side_effect):
        # Arrange
        expectedResult = 'something new'
        mock_get_info_side_effect.return_value = expectedResult
        testDog = Dog('test', 'mixed', 1, 'white')

        # Act / Assert
        actualResult = testDog.get_info()

        # Assert
        self.assertEqual(expectedResult, actualResult)


if __name__ == '__main__':
    unittest.main()