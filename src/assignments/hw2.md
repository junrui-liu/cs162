# CS 162 - Homework 2

> Due: TBD

## Instructions
There are be 2 types of problems:
1. **Written problems** are marked with ✍️.
   - Must be done in **groups of either two or three**. Find a partner in the `#find-a-partner` Slack channel as soon as possible!
   - Each sub-problem will be graded out of 2 points: 2 for a fully solved problem with a correct (or almost correct) solution, 1 for a partially correct attempt with all work shown, and 0 for no attempt.
   - Once you're done, one member of your group should submit a PDF to Gradescope. The person who submits to Gradescope should also indicate who the other member(s) are.
2. **Coding problems** are marked with 🧑‍💻.
   - Must be done **individually**.
   - Coding problems are autograded on Gradescope. You will receive points for a sub-problem once you pass *all* pre-defined test cases. The autograder will show you which tests failed.
   - You can submit as many times as you want, but note that there will be a rate limit of 1 submission per hour for coding problems. This is to encourage you to test your code locally before submitting, and prevent abusing the autograder as a debugger.

- Problems (written or coding) marked with ⭐️ are extra credit problems. You can do them for fun and for extra credit, but they are completely optional.

- You're encouraged to talk about the problems with the instructor, the TA, and your classmates, but your group must write up your own solutions for the written problems, and you must individually write code for the coding problems.

- Note you won't be able to turn in corrections to homework problems, unlike quizzes.

- Use of generative AI tools and coding assistants is not allowed for this assignment. You will be able to use them for future assignments (maybe), but not for this one, since I really want to make sure you have the necessary understanding of the material and the ability to discern gold from trash, before you start enabling LLMs who will invariably spit out (mostly) trash to you on real problems.

- If you have any questions about the assignment, please come to the office hours, or post them in the `#hw2` Slack channel.

## (Coding) Problem 1
implement:
- type abbrev
- subst, procedures, let, prod, string
- env semantics

built-in:
- bool
- nat
- string

stdlib:
- rational




## (Written) Problem 2
First-order logic


## Problem 3

Recall the CoinPython language, and the `ProbabilisticInterpreter` that you wrote in Homework 1.

### Problem 3-A (✍️, 5 points)

Let's build a variation of `ProbabilisticInterpreter` -- which interpreted a CoinPython program using random coin flips and returns one possible output string -- by instead having the interpreter returning *all possible outputs* of a CoinPython program. In other words, the function should return a set of all strings `s` such that `p => s`. Note that the output string can be either empty (if the program can terminate without executing any `print` statements), or a concatenation of multiple messages, but nothing else.

To do so, first read about [generators in Python](https://realpython.com/python-iterators-iterables/#creating-generator-iterators), and implement such an interpreter using Python's `yield` statement:
```python
@dataclass
class AllOutputsInterpreter:

   def run(self, p: Program) -> Iterator[str]:
      match p:
         case Pass():
            return
         case Print(msg):
            yield msg
            return
         case Seq(p1, p2):
            # your code here
         case If(cond, p1, p2):
            # your code here
         case While(cond, body):
            # your code here
```
You should ensure that:
- The iterator is *fair*: every possible output string `s` should appear somewhere in the iteration in finite time.
- The iterator never yields the same string twice. For this, you can simply use a cache like Python's `set` to keep track of already yielded strings.

In your PDF, include the following:
1. The class definition of `AllOutputsInterpreter` that you wrote above.
2. The first 20 outputs of the interpreter on the following CoinPython program:
    ```python
    while (*) {
        if (*) { print("0") }
        else { print("1") }
    }
   ```
3. A brief discussion of how a `ProablisticInterpreter` could have be implemented in terms of an `AllOutputsInterpreter`.

<details>
<summary>Hint</summary>

The challenge is to ensure fairness:
- For `If`, you can take turns to alternate between two sub-generators.
- For `Seq`, you can use the following zig-zag pattern (aka [the Cantor pairing function](https://en.wikipedia.org/wiki/Pairing_function#Cantor_pairing_function)):

  ![Zig-zag pattern](https://upload.wikimedia.org/wikipedia/commons/c/c3/Cantor%27s_Pairing_Function.svg)

- For `While`, note that a `while` loop can always be "unrolled" into an `if` plus another `while`. For example, in Python:
   ```python
   while cond:
      body
   ```
   is equivalent to
   ```python
   if cond:
      body
      while cond:
         body
   ```

</details>
