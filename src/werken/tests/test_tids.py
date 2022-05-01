from werken import tids
import pytest


@pytest.mark.parametrize("value, expected", [
    (0, "0000000000"),
    (9, "0000000009"),
    (10, "000000000A"),
    (36, "000000000a"),
    (61, "000000000z"),
    (62, "0000000010"),
    (tids.MAX_ID, "zzzzzzzzzz")])
def test_id_from_int(value, expected):
    assert tids.id_from_int(value) == expected


def test_id_from_int_min():
    with pytest.raises(ValueError, match="id must not be negative"):
        tids.id_from_int(-1)


def test_id_from_int_max():
    with pytest.raises(ValueError, match="id too large"):
        tids.id_from_int(tids.MAX_ID + 1)
