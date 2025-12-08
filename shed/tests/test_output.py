class TestOutput:
    def test_tmp_path(self, tmp_path):
        assert "/" in str(tmp_path)
