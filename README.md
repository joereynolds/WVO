# WVO

A weight value object for Python with a focus on removing side-effects and mutation.

# Examples

```
>>> import weight as w
>>>
>>> x = w.Weight(5, 'lb')
>>> y = w.Weight(56, 'kg')
>>>
>>> x + y
>>> 128.45886682353142lb
>>>
>>> y + x
>>> 58.26796185kg
>>>
>>> x.convert('kg')
>>> 2.2679618500000003kg
```
