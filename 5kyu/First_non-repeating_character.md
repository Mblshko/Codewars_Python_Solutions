Write a function named `first_non_repeating_letter` that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input `'stress'`, the function should return `'t'`, since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input `'sTreSS'` should return `'T'`.

If a string contains all repeating characters, it should return an empty string (`""`) or `None` -- see sample tests.

---
### Solution

```python
def first_non_repeating_letter(string):
    string_lower = string.lower()
    res = ''
    for x in string:
        if string_lower.find(x.lower()) == string_lower.rfind(x.lower()):
            res += x
    if len(res) == 0:
        return ''
    else:
        return res[0]
   ```
   ---
   [See on CodeWars.com](https://www.codewars.com/kata/52bc74d4ac05d0945d00054e)
