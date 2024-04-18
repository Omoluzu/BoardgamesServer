from src import models


def test_base_new():
    base = models.BaseList.new()
    assert base.name == 'base'
    assert base.elements == []


def test_base_imports():
    base = models.BaseList.imports(elements='base:xrbg')
    assert base.elements == ['x', 'r', 'b', 'g']

    zero_base = models.BaseList.imports(elements='base:')
    assert zero_base.elements == []


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


def test_base_log_add_element():
    class New(models.BaseList):
        ...

    base = models.BaseList()
    assert not base.log.element_add

    base.element_add(element='bb')
    assert base.log.element_add == ['b', 'b']

    new = New()
    assert not new.log.element_add

    base.element_add(element='g')
    assert base.log.element_add == ['b', 'b', 'g']


def test_base_max_add_element():
    class BaseTest(models.BaseList):
        limit: int = 6

    base = BaseTest()
    base.element_add(element='rtyuiofghj')

    assert base.elements == ['r', 't', 'y', 'u', 'i', 'o']
    assert base.log.element_add == ['r', 't', 'y', 'u', 'i', 'o']
    assert base.log.element_extra == ['f', 'g', 'h', 'j']
    assert base.export() == 'base:rtyuio'

    base2 = BaseTest()
    base2.element_add(element='rtyu')
    base2.element_add(element='iof')

    assert base2.elements == ['r', 't', 'y', 'u', 'i', 'o']
    assert base2.export() == 'base:rtyuio'

