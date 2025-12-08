import pytest

class TestDummy:
    @pytest.mark.skipif("f" not in "duck", reason="This test exists only to be skipped")
    def test_f_in_duck(self):
        x = "duck"
        assert "f" in x

    def test_c_in_duck(self):
        x = "duck"
        assert "c" in x