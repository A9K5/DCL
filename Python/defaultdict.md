### Python defaultdict examples

<code>
k3@k3-Inspiron-123:~$ python3

Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> from collections import ordereddict

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ImportError: cannot import name 'ordereddict'

>>> from collections import defaultdict

>>> d = defaultdict(list)

>>> d

defaultdict(<class 'list'>, {})

>>> d['dogs'].append('rufus')

>>> d['dogs'].append('bruno')

>>> d['dogs']

['rufus', 'bruno']

>>> d['notexist']

[]

>>> type(d['notexist'])

<class 'list'>

>>> s = 'mississippi'

>>> d = defaultdict(int)

>>> for k in s:

...     d[k] += 1

... 

>>> d.items()

dict_items([('s', 4), ('m', 1), ('i', 4), ('p', 2)])

>>> sorted(d.items())

[('i', 4), ('m', 1), ('p', 2), ('s', 4)]

>>> d.values()

dict_values([4, 1, 4, 2])

>>> [d.values()]

[dict_values([4, 1, 4, 2])]

>>> sorted(d.values())

[1, 2, 4, 4]

>>> s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), 
('blue', 4)]

>>> d = defaultdict(set)

>>> for k,v in s: 

...     d[k].add(v)

... 

>>> d.items()

dict_items([('blue', {2, 4}), ('red', {1, 3})])

</code>
