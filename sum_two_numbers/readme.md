# Two Sum #

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```


Ref:
- https://leetcode.com/problems/two-sum/#/description



function define:
```python
def two_sum(lst, sum)
```

input:
    > - lst: input list
    > - sum: expect sum

output:
    > return list of index tuple

example:
    > input list: [1, 2, 3, 4, 5]
    > input sum: 6
    > output return: [(0, 4), (1, 3)]
