# fsys
Simple tool to help me understand formal systems intuitively

# Example Usage

```bash
$ python
Python 3.7.3 (default, Dec 20 2019, 18:57:59) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from squares import *
>>> from fsym import NaiveAddTheorems
>>> T
['N-']
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> T
['N-', 'N--', '-A-A-', '--A--A--', '----A--A-', 'S-', 'S----']
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> T
['N-', 'N--', '-A-A-', '--A--A--', '----A--A-', 'S-', 'S----', 'N---', '---A---A---', '------A---A--']
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> T
['N-', 'N--', '-A-A-', '--A--A--', '----A--A-', 'S-', 'S----', 'N---', '---A---A---', '------A---A--', 'N----', '----A----A----', '---------A---A-', '--------A----A---', 'S---------']
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> T
['N-', 'N--', '-A-A-', '--A--A--', '----A--A-', 'S-', 'S----', 'N---', '---A---A---', '------A---A--', 'N----', '----A----A----', '---------A---A-', '--------A----A---', 'S---------', 'N-----', '-----A-----A-----', '------------A----A--', '----------A-----A----']
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> T
['N-', 'N--', '-A-A-', '--A--A--', '----A--A-', 'S-', 'S----', 'N---', '---A---A---', '------A---A--', 'N----', '----A----A----', '---------A---A-', '--------A----A---', 'S---------', 'N-----', '-----A-----A-----', '------------A----A--', '----------A-----A----', 'N------', '------A------A------', '----------------A----A-', '---------------A-----A---', '------------A------A-----', 'S----------------']
>>> len(T[-1])-1
16
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> len(T[-1])-1
25
```
