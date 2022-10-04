## Part B Analysis

Perform an analysis of the following recursive functions.

### function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0):       #1

		return 1            #0 if n>0
                            #1 if n=0

	elif (number == 1):     #1
		return value        #0 if n>1
                            #1 if n=1
	else:
		return value * function1(value, number-1)   # 3 + T(n-1) (return, *, -)
```
T(n) = 5 + T(n-1)

T(0) = 2

T(1) = 3

T(n-1) = 5 + T(n-2)

T(n-2) = 5 + T(n-3)

T(n-3) = 5 + T(n-4)

T(n) = 5(n-1)+3

T(n) = 5n - 2

Therefore, T(n) is O(n)

### function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python
# let T2(n) for recursive_function2
def recursive_function2(mystring,a, b):
	if(a >= b ):        #1
		return True     # 1, if b <= a
	else:
		if(mystring[a] != mystring[b]):     #2
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)        #3 + T(n-1) (return, +, -)

# Let T1(n) for function2
def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)             #2 (return, -)

```
T(0) = 2

T(1) = 6 + 2 = 8

T(n) = 6 + T(n-1)

T(n) = 6(n-1) + 2

T(n) = 6n - 4

Therefore, T(n) is O(n)


### function 3 (optional challenge):

Analyze the following function with respect to number

```python
def function3(value, number):
	if (number == 0):                       #1
		return 1                                #1, if num == 0
	elif (number == 1):                     #1
		return value                            #1, if num == 1
	else:
		half = number // 2                  #2
		result = function3(value, half)     # 1 + T(n-1)
		if (number % 2 == 0):               #2
			return result * result              #2, if num is even
		else:
			return value * result * result  #3, if num is not even (return, * , *)

```
T(n) = 1 + 1 + 2 + 1 + T(n-1) + 2 + 3

T(n) = 10 + T(n-1)

T(0) = 2

T(1) = 3

T(n) = 10 + 10 + 10 + T(n-3) ... + 3

T(n) = 10(n-1) + 3

T(n) = 10n - 7