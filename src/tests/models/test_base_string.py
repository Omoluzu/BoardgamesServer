from src import models


def test_base_new():
    base = models.BaseString.new()
    assert base.name == 'base'
    assert base.element == ''


def test_base_imports():
    base = models.BaseString.imports(element='base:LongString')
    assert base.element == 'LongString'


def test_base_export():
    base = models.BaseString.new()
    base.element = 'NewElement'
    assert base.export() == 'base:NewElement'
