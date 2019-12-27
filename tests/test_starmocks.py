import os
from unittest import mock

from starmocks import starmocks


def _dummy_caller():
    return os.path.join(os.path.pardir, "world")


class TestDecorator:
    @mock.patch("os.path.join", return_value="lero")
    @starmocks
    def test_single_mock(self, mocks):
        assert isinstance(mocks.join, mock.Mock)
        res = _dummy_caller()
        assert res == "lero"

    @mock.patch("os.path.join", return_value="lero")
    @mock.patch("os.path.pardir")
    @mock.patch("os.path.exists", return_value=True)
    @starmocks
    def test_multiple_mocks(self, mocks):
        assert isinstance(mocks.join, mock.Mock)
        res = _dummy_caller()
        assert res == "lero"
