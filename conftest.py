# -*- coding: utf-8 -*-
import pytest
from fixture.application import Applicaton
fixture = None

@pytest.fixture(scope='class')
def app(request):
    global fixture
    #operator=request.config.getoption("--target")
    fixture = Applicaton()
    yield fixture
    fixture.destroy()