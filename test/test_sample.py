import pytest

from python_repository_template import sample


@pytest.mark.parametrize(  # type: ignore[misc]
    "number, flg",
    [
        (1, True),
        (2, False),
        (3, True),
        (5, True),
        (8, False),
        (13, True),
        (21, True),
        (34, False),
    ],
)
def test_odd(number: int, flg: bool) -> None:
    assert sample.is_odd(number) == flg
