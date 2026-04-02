import pytest
from calculator import add


# ─── 덧셈 ────────────────────────────────
class TestAdd:
    def test_add_positive(self):
        assert add(2, 3) == 5

  