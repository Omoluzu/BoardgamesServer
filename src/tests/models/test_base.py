from src import models


def test_base_new():
    base = models.BaseList.new()
    assert base.name == 'base'
    assert base.elements == []


def test_base_imports():
    base = models.BaseList.imports(elements='base:xrbg')
    assert base.elements == ['x', 'r', 'b', 'g']


def test_base_suffix_imports():
    class BaseTest(models.BaseList):
        suffix = True

    base = BaseTest.imports(elements='baseone:xrbg')
    assert base.name == 'baseone'
    assert base.elements == ['x', 'r', 'b', 'g']
    assert base.export() == 'baseone:xrbg'


def test_base_export():
    base = models.BaseList(elements=['x', 'r', 'b', 'g'])
    assert base.export() == 'base:xrbg'


def test_base_add_element():
    base = models.BaseList()
    base.element_add(element='t')
    assert base.elements == ['t']
    base.element_add(element='rb')
    assert base.elements == ['t', 'r', 'b']




