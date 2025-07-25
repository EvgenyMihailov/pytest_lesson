import  pytest

from src.string_utils import StringUtils


class TestStringUtils:
    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("abc", "cba"),
            ("",""),
            ("123","321"),
            (1234, pytest.raises(TypeError)),
            (None, pytest.raises(TypeError))
        ]
    )
    def test_reverse_string(self,input_str,expected):
        utils = StringUtils()
        if isinstance(expected, str):
            assert utils.reverse_string(input_str) == expected
        else:
            with expected:
                utils.get_initials(input_str)



    @pytest.mark.parametrize(
        "full_name, expected",
        [
            ("Daniil Nikolaev", "DN"),
            ("Ivan Ivanov", "II"),
            ("", pytest.raises(ValueError))
        ]
    )
    def test_get_initials(self,full_name, expected):
        utils = StringUtils()
        if isinstance(expected, str):
            assert utils.get_initials(full_name) == expected
        else:
            with expected:
                utils.get_initials(full_name)


