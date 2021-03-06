# pylint: disable=E1101
"""
Tests for Custom Metaclass
"""
from dataclasses import dataclass
from homework2.task2.custom_meta import CustomMeta
import pytest


class TestTicTac:
    """
    Test class for Custom Metaclass
    """
    @staticmethod
    def test_custom_value():
        """
        Test for custom value in class
        """
        @dataclass
        class Test1(metaclass=CustomMeta):
            """
            Class with x and p variables
            """
            x = 10
            p = 42

        test_class = Test1()
        assert 'x' not in test_class.__dict__
        assert 'p' not in test_class.__dict__
        assert test_class.custom_x == 10
        assert test_class.custom_p == 42
        with pytest.raises(AttributeError):
            assert test_class.x == 10
        with pytest.raises(AttributeError):
            assert test_class.p == 10

    @staticmethod
    def test_custom_methods():
        """
        Test for custom methods names
        """
        @dataclass
        class Test2(metaclass=CustomMeta):
            """
            Class with x variable and size method
            """
            x = 42

            def size(self):
                """
                :return: x * 10
                """
                return self.custom_x * 10

        test_class = Test2()
        assert 'x' not in test_class.__dict__
        assert 'size' not in test_class.__dict__
        assert test_class.custom_size() == 420
        with pytest.raises(AttributeError):
            assert test_class.size() == 420
        with pytest.raises(AttributeError):
            assert test_class.x == 10

    @staticmethod
    def test_custom_value_in_init():
        """
        Test for custom value in init
        """
        @dataclass
        class Test3(metaclass=CustomMeta):
            """
            Class with x and arg variables
            """
            x = 10

            def __init__(self, arg=42):
                self.arg = arg

            def size(self):
                """
                :return: x * arg
                """
                return self.custom_x * self.custom_arg

        test_class = Test3()
        assert 'x' not in test_class.__dict__
        assert 'size' not in test_class.__dict__
        assert 'arg' not in test_class.__dict__
        assert test_class.custom_arg == 42
        assert test_class.custom_size() == 420
        with pytest.raises(AttributeError):
            assert test_class.size() == 10
        with pytest.raises(AttributeError):
            assert test_class.arg == 10

        test_class = Test3(10)
        assert test_class.custom_arg == 10
        assert test_class.custom_size() == 100

    @staticmethod
    def test_custom_name():
        """
        Test for custom name with "custom_"
        """
        @dataclass
        class Test4(metaclass=CustomMeta):
            """
            Class with custom variable
            """
            custom = 10

        test_class = Test4()
        assert 'custom' not in test_class.__dict__
        assert test_class.custom_custom == 10
        with pytest.raises(AttributeError):
            assert test_class.custom == 10
