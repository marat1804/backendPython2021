"""
Tests for CustomList class
"""
from homework2.task1.custom_list import CustomList
import pytest


class TestTicTac:
    """
    Test class for CustomList
    """
    @staticmethod
    def test_list_creation():
        """
        Test for CustomList creation
        """
        first_list = CustomList()
        with pytest.raises(IndexError):
            first_list[0] = 0
        first_list.append(0)
        assert first_list[0] == 0
        first_list[0] = 1
        assert first_list[0] == 1
        assert len(first_list) == 1

        second_list = CustomList(1, 2, 3)
        assert second_list[0] == 1
        second_list[2] = 4
        assert second_list[2] == 4
        assert len(second_list) == 3

    @staticmethod
    def test_add_custom_lists():
        """
        Test for CustomList addition
        """
        first_list = CustomList(1, 2)
        second_list = CustomList(3, 3)
        result_list = first_list + second_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == 4
        assert result_list[1] == 5

        first_list = CustomList(1, 2)
        second_list = CustomList(3, 3, 3)
        result_list = first_list + second_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == 4
        assert result_list[1] == 5
        assert result_list[2] == 3

        first_list = CustomList(1, 2, 3)
        second_list = CustomList(3, 3)
        result_list = first_list + second_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == 4
        assert result_list[1] == 5
        assert result_list[2] == 3

    @staticmethod
    def test_add_with_usual_list():
        """
        Test for CustomList and list addition
        """
        first_list = CustomList(1, 2)
        second_list = [3, 3]
        result_list = first_list + second_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == 4
        assert result_list[1] == 5

        first_list = CustomList(1, 2)
        second_list = [3, 3, 3]
        result_list = first_list + second_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == 4
        assert result_list[1] == 5
        assert result_list[2] == 3

        first_list = CustomList(1, 2, 3)
        second_list = [3, 3]
        result_list = first_list + second_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == 4
        assert result_list[1] == 5
        assert result_list[2] == 3

        result_list = second_list + first_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == 4
        assert result_list[1] == 5
        assert result_list[2] == 3

    @staticmethod
    def test_add_and_assign():
        """
        Test for += operator
        """
        first_list = CustomList(1, 2)
        second_list = CustomList(3, 3)
        first_list += second_list
        assert first_list[0] == 4
        assert first_list[1] == 5

        first_list = CustomList(1, 2)
        second_list = [3, 3, 3]
        first_list += second_list
        assert first_list[0] == 4
        assert first_list[1] == 5
        assert first_list[2] == 3

        first_list = CustomList(1, 2, 3)
        second_list = [3, 3]
        first_list += second_list
        assert first_list[0] == 4
        assert first_list[1] == 5
        assert first_list[2] == 3

    @staticmethod
    def test_custom_list_sub():
        """
        Test for CustomList subtraction
        """
        first_list = CustomList(1, 2)
        second_list = CustomList(3, 3)
        result_list = first_list - second_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == -2
        assert result_list[1] == -1

        first_list = CustomList(1, 2)
        second_list = CustomList(3, 3, 3)
        result_list = first_list - second_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == -2
        assert result_list[1] == -1
        assert result_list[2] == -3

        first_list = CustomList(1, 2, 3)
        second_list = CustomList(3, 3)
        result_list = first_list - second_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == -2
        assert result_list[1] == -1
        assert result_list[2] == 3

    @staticmethod
    def test_sub_with_usual_list():
        """
        Test for CustomList and list subtraction
        """
        first_list = CustomList(1, 2)
        second_list = [3, 3]
        result_list = first_list - second_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == -2
        assert result_list[1] == -1

        first_list = CustomList(1, 2)
        second_list = [3, 3, 3]
        result_list = first_list - second_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == -2
        assert result_list[1] == -1
        assert result_list[2] == -3

        first_list = CustomList(1, 2, 3)
        second_list = [3, 3]
        result_list = first_list - second_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == -2
        assert result_list[1] == -1
        assert result_list[2] == 3

        result_list = second_list - first_list
        assert isinstance(result_list, CustomList)
        assert result_list[0] == -2
        assert result_list[1] == -1
        assert result_list[2] == 3

    @staticmethod
    def test_sub_and_assign():
        """
        Test for -= operator
        """
        first_list = CustomList(1, 2)
        second_list = CustomList(3, 3)
        first_list -= second_list
        assert first_list[0] == -2
        assert first_list[1] == -1

        first_list = CustomList(1, 2)
        second_list = [3, 3, 3]
        first_list -= second_list
        assert first_list[0] == -2
        assert first_list[1] == -1
        assert first_list[2] == -3

        first_list = CustomList(1, 2, 3)
        second_list = [3, 3]
        first_list -= second_list
        assert first_list[0] == -2
        assert first_list[1] == -1
        assert first_list[2] == 3

    @staticmethod
    def test_lt_custom_list():
        """
        Test for < operator
        """
        first_list = CustomList(1, 2, 3)
        second_list = CustomList(4, 5)
        assert first_list < second_list

        third_list = [0, 0, 1]
        assert not first_list < third_list

    @staticmethod
    def test_le_custom_list():
        """
        Test for <= operator
        """
        first_list = CustomList(1, 2, 3)
        second_list = CustomList(4, 5)
        assert first_list <= second_list

        third_list = [0, 0, 1]
        assert not first_list <= third_list

        first_list = CustomList(0, 0)
        second_list = CustomList(0)
        assert first_list <= second_list

        third_list = [0, 0, 0]
        assert first_list <= third_list

    @staticmethod
    def test_gt_custom_list():
        """
        Test for gt operator
        """
        first_list = CustomList(1, 2, 3)
        second_list = CustomList(4, 5)
        assert not first_list > second_list
        third_list = [0, 0, 1]
        assert first_list > third_list

    @staticmethod
    def test_ge_custom_list():
        """
        Test for >= operator
        """
        first_list = CustomList(1, 2, 3)
        second_list = CustomList(4, 5)
        assert not first_list >= second_list

        third_list = [0, 0, 1]
        assert first_list >= third_list

        first_list = CustomList(0, 0)
        second_list = CustomList(0)
        assert first_list >= second_list

        third_list = [0, 0, 0]
        assert first_list >= third_list

    @staticmethod
    def test_eq_custom_list():
        """
        Test for == operator
        """

        first_list = CustomList(2, 3, 4)
        second_list = CustomList(4, 5)
        assert first_list == second_list

        third_list = [0, 0, 1]
        assert not first_list == third_list

    @staticmethod
    def test_ne_custom_list():
        """
        Test for != operator
        """

        first_list = CustomList(2, 3, 4)
        second_list = CustomList(4, 5)
        assert not first_list != second_list

        third_list = [0, 0, 1]
        assert first_list != third_list
