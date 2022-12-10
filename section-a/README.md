## Section A: Code Review (Python)

### Correctness

I'm not sure if you attempted to test or execute your solution, but when I tried I got the following error message:

```bash
🕙 2022-12-08 10:48:47  ❯ python anagram.py
  File "/Users/michaeljoseph/Source/hyperiondev-freelancer/anagram.py", line 3
    result = {}
               ^
IndentationError: unindent does not match any outer indentation level
```

Python is a whitespace sensitive language, so it's important to make sure that you [indent consistently] throughout your program.

I made the following change on L2 of your code:

```bash
🕙 2022-12-08 14:16:02  ❯ diff anagram.py corrected-anagram.py
2c2
<        def groupAnagrams(self, strs):
---
>    def groupAnagrams(self, strs):
```

Then the following error:

```bash
🕙 2022-12-08 13:40:52  ❯ python anagram.py
Traceback (most recent call last):
  File "/Users/michaeljoseph/Source/hyperiondev-freelancer/anagram.py", line 12, in <module>
    print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
  File "/Users/michaeljoseph/Source/hyperiondev-freelancer/anagram.py", line 5, in groupAnagrams
    x = "".join(sorted())
TypeError: sorted expected 1 argument, got 0
```

The error message is telling us that the <code>[sorted]</code> function takes one argument, but you didn't provide one in your code (on L5).

Let's presume that you intended to sort the current item `i`  of the list `strs` that you're iterating through:

```diff
🕙 2022-12-08 14:17:42  ✖  diff anagram.py corrected-anagram.py
2c2
<        def groupAnagrams(self, strs):
---
>    def groupAnagrams(self, strs):
5c5
<          x = "".join(sorted(i))
---
>          x = "".join(sorted())
```

Your program now successfully executes with the following output:

```bash
🕙 2022-12-08 14:21:33  ✖  python corrected-anagram.py
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

This is the expected output, so well done! 🎉🥳👍

The key takeaway should be that you should always execute your solution and try to make sense of the error messages that the interpreter is providing to help you.

### Documentation

Your solution is missing [comments or docstrings], which are useful ways of capturing your thinking and the purpose of your classes, functions and blocks  of code.

### Efficiency

Your implementation is reasonably efficient, since you're only looping through the input list once, which is good news for the [time complexity] of your function.

### Style

The accepted conventions for Python code formatting are documented in [PEP8], so please ensure that your Python solutions conform to these best practice.

## Section A: Code Review (Java)

I've only just read the requirement to have different language selections between Section A and C and since I'd prefer to problem solve in Python, here's a code review of the Java Task as well.

### Correctness

```
⚡20% 🕙 2022-12-08 15:02:54  ❯ javac recursion.java 
recursion.java:26: error: cannot find symbol
		return reverseString(myStr.substring(1)) + myStr.charAt(0);}
		      ^
  symbol:   method reverseString(String)
  location: class recursion
recursion.java:30: error: variable maxNumber is already defined in method <T>function(T)
		int maxNumber = 10; 
		   ^
  where T is a type-variable:
    T extends Object declared in method <T>function(T)
2 errors
```

L26: typo
L30: unused code, redefinition of input argument

```
1c1
< public class recursion {
---
> public class ReverseString {
26c26
< 		return reverseString(myStr.substring(1)) + myStr.charAt(0);}
---
> 		return reverse_string(myStr.substring(1)) + myStr.charAt(0);}
27a28
> 	/*
46a48
> 	*/
```

```
String to be passed in Recursive Function: mosewA si avaJ
String to be passed in Recursive Function: osewA si avaJ
String to be passed in Recursive Function: sewA si avaJ
String to be passed in Recursive Function: ewA si avaJ
String to be passed in Recursive Function: wA si avaJ
String to be passed in Recursive Function: A si avaJ
String to be passed in Recursive Function:  si avaJ
String to be passed in Recursive Function: si avaJ
String to be passed in Recursive Function: i avaJ
String to be passed in Recursive Function:  avaJ
String to be passed in Recursive Function: avaJ
String to be passed in Recursive Function: vaJ
String to be passed in Recursive Function: aJ
String to be passed in Recursive Function: J
String to be passed in Recursive Function: 
String in now Empty
The reversed string is: Java is Awesome
Fibonacci Series of 10 numbers:0 1 1 2 3 5 8 13 21 34 
```

### Documentation

### Efficiency

### Style



[indent consistently]: https://peps.python.org/pep-0008/#indentation
[sorted]: https://docs.python.org/3/library/functions.html#sorted
[comments or docstrings]: https://peps.python.org/pep-0008/#comments
[time complexity]: https://en.wikipedia.org/wiki/Time_complexity
[PEP8]: https://peps.python.org/pep-0008/