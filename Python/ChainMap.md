### Python ChainMap examples

<code>
k3@k3-Inspiron-123:~$ python3

Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux

Type "help", "copyright", "credits" or "license" for more information.

>>> from collections import ChainMap

>>> dict1 = {'one': 1, 'two': 2}

>>> dict2 = {'three': 3, 'four': 4}

>>> chain = ChainMap(dict1, dict2)

>>> chain

ChainMap({'two': 2, 'one': 1}, {'three': 3, 
'four': 4})

>>> chain['three']

3

>>> chain.items()

ItemsView(ChainMap({'two': 2, 'one': 1}, {'three': 
3, 'four': 4}))

>>> chain.values()

ValuesView(ChainMap({'two': 2, 'one': 1}, 
{'three': 3, 'four': 4}))

>>> sorted(chain.values())

[1, 2, 3, 4]

>>> sorted(chain.items())

[('four', 4), ('one', 1), ('three', 3), ('two', 2)]

>>> sorted(chain.keys())

['four', 'one', 'three', 'two']

>>> baseline = {'music': 'bach', 'art': 
'rembrandt'}

>>> adjustments = {'art': 'van gogh', 'opera': 
'carmen'}

>>> list(ChainMap(adjustments, baseline))

['music', 'art', 'opera']

>>> d = ChainMap(adjustments, baseline)

>>> d.items()

ItemsView(ChainMap({'art': 'van gogh', 'opera': 
'carmen'}, {'music': 'bach', 'art': 'rembrandt'}))

>>> d['art']

'van gogh'

>>> 

</code>

Reference : https://docs.python.org/3/library/collections.html#collections.ChainMap