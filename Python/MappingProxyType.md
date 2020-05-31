### Python MappingProxyType examples
<code>
k3@k3-Inspiron-123:~$ python3
Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux

Type "help", "copyright", "credits" or "license" for more information.

>>> from types import MappingProxyType

>>> read_only = MappingProxyType({'one': 1,'two':2})

>>> read_only['one']

1

>>> read_only['one']=10

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

TypeError: 'mappingproxy' object does not support 
item assignment

>>> read_only['three']=10

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

TypeError: 'mappingproxy' object does not support 
item assignment

>>> 

</code>

Reference : https://docs.python.org/3/library/types.html#types.MappingProxyType