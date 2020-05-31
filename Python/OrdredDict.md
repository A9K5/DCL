### Python OrderedDict examples
<code>
k3@k3-Inspiron-123:~$ python3

Python 3.5.2 (default, Nov 12 2018, 13:43:14) 

[GCC 5.4.0 20160609] on linux

Type "help", "copyright", "credits" or "license" for more information.

>>> from collections import OrderedDict

>>> d = OrderedDict([ (one,1),(two,2), (three,3) ])

Traceback (most recent call last):File 
"<stdin>", line 1, in <module>

NameError: name 'one' is not defined

>>> d = OrderedDict([ ('one',1),('two',2), ('three',3) ])

>>> d

OrderedDict([('one', 1), ('two', 2), ('three', 3)])

>>> d['four'] = 4

>>> d

OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])

>>> d.keys()

odict_keys(['one', 'two', 'three', 'four'])

>>> d.popitem()

('four', 4)
>>> d.keys()

odict_keys(['one', 'two', 'three'])

>>> d.move_to_end('one')

>>> d

OrderedDict([('two', 2), ('three', 3), ('one', 1)])

>>> [d]

[OrderedDict([('two', 2), ('three', 3), ('one', 1)])]

>>> [i for i in d]

['two', 'three', 'one']

>>> [(i,j) for i,j in d.items()]

[('two', 2), ('three', 3), ('one', 1)]

>>> d.values()

odict_values([2, 3, 1])

>>> [d.values()]

[odict_values([2, 3, 1])]

>>> [j for i,j in d.items()]

[2, 3, 1]

</code>