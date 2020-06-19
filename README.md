# fsym
Simple tool to help me understand formal systems intuitively

# Example Usage

```bash
$ python
Python 3.7.3 (default, Dec 20 2019, 18:57:59) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from squares import *
>>> from fsym import NaiveAddTheorems
>>> sorted(T)
['N-']
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> sorted(T)
['--A--A--', '-A-A-', 'N-', 'N--']
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> sorted(T)
['----A--A-', '---A---A---', '--A--A--', '-A-A-', 'N-', 'N--', 'N---', 'S-', 'S----']
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> sorted(T)
['---------A---A-', '--------A----A---', '------A---A--', '-----A-----A-----', '----A----A----', '----A--A-', '---A---A---', '--A--A--', '-A-A-', 'N-', 'N--', 'N---', 'N----', 'N-----', 'S-', 'S----', 'S---------']
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> sorted(T)
['----------------A----A-', '---------------A-----A---', '------------A------A-----', '------------A----A--', '----------A-----A----', '---------A---A-', '--------A----A---', '-------A-------A-------', '------A------A------', '------A---A--', '-----A-----A-----', '----A----A----', '----A--A-', '---A---A---', '--A--A--', '-A-A-', 'N-', 'N--', 'N---', 'N----', 'N-----', 'N------', 'N-------', 'S-', 'S----', 'S---------', 'S----------------']
>>> len(sorted(T)[-1])-1
16
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> NaiveAddTheorems(R, T, AddTheorem)
>>> len(sorted(T)[-1])-1
25
```
