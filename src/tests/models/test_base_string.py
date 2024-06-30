import pytest

from src import models


@pytest.fixture()
def base_list() -> 'models.BaseString':
    return models.BaseString.new()


@pytest.mark.engine
def test_base_new(base_list):
    assert base_list.name == 'base'
    assert base_list.element == ''


@pytest.mark.engine
def test_base_imports():
    base = models.BaseString.imports(element='base:LongString')
    assert base.element == 'LongString'


@pytest.mark.engine
def test_base_export(base_list):
    base_list.element = 'NewElement'
    assert base_list.export() == 'base:NewElement'
