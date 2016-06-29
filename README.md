# WVO

A Weight Value Object for Python with a focus on removing side-effects and mutation.

# Examples

First we need to import the module, then we can begin
`>>> import weight as w`

## Addition And Subtraction

```
>>> x = w.Weight(5, 'lb')
>>> y = w.Weight(56, 'kg')
>>>
>>> x + y
>>> weight.Weight object at 0x7f1519a8b358>
```
Every method in `Weight` brings back a new `Weight` object to reduce stateful problems.
To get a meaningful value...

```
>>> x = w.Weight(5, 'lb')
>>> y = w.Weight(56, 'kg')
>>>
>>> (x + y).value
>>> 128.45886682353142
>>>
>>> (y + x).value
>>> 58.26796185
```

Note above that the order of addition affects the way values are converted.
If you first add `'lb' + 'kg'` as we did in the first example, then the
resulting value will be in pounds(lb). However, if we reverse that,
and first add the 'kg', the value will be in kilograms(kg).

Subtraction behaves exactly the same

```
>>> x = w.Weight(5, 'lb')
>>> y = w.Weight(3, 'lb')
>>>
>>> (x - y).value
>>> 2
```

## Conversion

```
>>> x = w.Weight(5, 'lb')
>>> x.convert('kg').value
>>> 2.2679618500000003
```

# Installation and Tests

## Install

```
git clone https://github.com/joereynolds/wvo
```

## Test

To run the tests just do
`python3 test.py`
All tests should pass.

