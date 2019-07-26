import numpy
from preconvert import register


@register.converter(numpy.ndarray)
def numpy_listable(item):
    return item.tolist()


@register.converter(str, numpy.unicode_)
def numpy_stringable(item):
    return str(item)


@register.converter(numpy.bytes_)
def numpy_byte_decodeable(item):
    return item.decode()


@register.converter(numpy.bool_)
def numpy_boolable(item):
    return bool(item)


@register.converter(numpy.integer)
def numpy_integerable(item):
    return int(item)


@register.converter(float, numpy.floating)
def numpy_floatable(item):
    return float(item)
