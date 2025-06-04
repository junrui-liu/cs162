# CS 162 - Homework 1

> Due: TBD

## Instructions
There are be 2 types of problems:
1. **Written problems** are marked with ✍️.
   - Must be done in **groups of either two or three**. Find a partner in the `#find-a-partner` Slack channel as soon as possible!
   - Unless specified otherwise, each sub-problem will be graded out of 2 points: 2 for a fully solved problem with a correct (or almost correct) solution, 1 for a partially correct attempt with all work shown, and 0 for no attempt.
   - Once you're done, one member of your group should submit a PDF to Gradescope. The person who submits to Gradescope should also indicate who the other member(s) are.
2. **Coding problems** are marked with 🧑‍💻.
   - Must be done **individually**.
   - Coding problems are autograded on Gradescope. Unless stated otherwise, you will receive points for a test suite once you pass *all* cases in the suite. The autograder will show you which tests failed.
   - You can submit as many times as you want, but note that there will be a rate limit of 1 submission per hour for coding problems. This is to encourage you to test your code locally before submitting, and prevent abusing the autograder as a debugger.


- Problems (written or coding) marked with ⭐️ are extra credit problems. You can do them for fun and for extra credit, but they are completely optional.

- You're encouraged to talk about the problems with the instructor, the TA, and your classmates, but your group must write up your own solutions for the written problems, and you must individually write code for the coding problems.

- Note you won't be able to turn in corrections to homework problems, unlike quizzes.

- Use of generative AI tools and coding assistants is not allowed for this assignment. You will be able to use them for future assignments (maybe), but not for this one, since I really want to make sure you have the necessary understanding of the material and the ability to discern gold from trash, before you start enabling LLMs who will invariably spit out (mostly) trash to you on real problems.

- If you have any questions about the assignment, please come to the office hours, or post them in the `#hw1` Slack channel.



## Problem 0 (✍️, 1 point)
Install Python 3.12 or later. In your PDF, attach a screenshot of the welcome message that you receive after running `python3`. For example, you should see something like this:
```bash
» python3
Python 3.9.12 (main, Jun  1 2022, 06:34:44)
[Clang 12.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
```
If you use VSCode, please also attach a screenshot of your VScode window that shows Copilot is disabled. There's a copilot icon in the bottom right corner that you can click to disable Copilot. Thank you so much.

Tips:
- If you're on Windows, we highly recommend you use the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) as the development environment.
- You're encouraged to use [Anaconda or Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) to manage your Python environment. Once you have Anaconda, `conda` will be available in your terminal. You can create a new environment with the command `conda create -n cs162 python=3.12`.
- To activate the environment, run `conda activate cs162`. Note that you need to run this command every time you open a new terminal window.
- All packages installed with `pip` for this class will stay in the `cs162` environment, so you don't have to worry about conflicts with your system Python installation.
- If you have trouble installing Python, please ask for help in the `#tech-support` channel on Slack.




## Problem 1

### Problem 1-A (🧑‍💻, 5 points)

Read about [structural pattern matching in Python](https://benhoyt.com/writings/python-pattern-matching/). Then, using (structural) pattern matching, define a recursive function `compress` that removes *consecutive* duplicate elements from a list:
```python
def compress(xs: list) -> list:
    match xs:
        # your code here
```
Again, if you routinely use Copilot or other coding assistants, I implore you to disable them at least for the first couple of assignments, so you won't:
- be accidentally spoiled with solutions,
- be robbed of a precious opportunity to think & learn for yourself -- opportunities like this are what make you irreplacable by AIs,
- violate the academic integrity policy (assignments have to be your own work!), or
- most importantly, make me sad, since I really want *you* to learn!

### Problem 1-B (🧑‍💻, 5 points)

Consider the language of arithmetic expressions, augmented with the only variable `x`, and a composition operator `|>`:
```
expr ::= number
       | expr + expr
       | expr - expr
       | expr * expr
       | expr |> expr
       | x
```
Intuitively, the only variable `x` stands for the "user input". The composition operator `|>` takes the value of the left-hand side expression, and feeds it into the "user input" of the right-hand side expression.

For example, the expression `1 + 2 * x |> x + 5` means:
- Ask the user for a number `n` for `x`. Let's say the user inputs `3`.
- Evaluate the left-hand side expression `1 + 2 * x` with `x = 3`, which evaluates to `1 + 2 * 3 = 7`.
- Feed the value `7` as input to the right-hand side expression `x + 5`, which evaluates to `7 + 5 = 12`.

The AST is defined in <this file: FIXME>. Your task is to implement the `eval` function that evaluates the input expression given an "user input" for `x`, using the following signature:
```python
def eval(x: int, expr: Expr) -> int:
    # your code here
```
You should use structural pattern matching to implement the function.


### Problem 1-C (🧑‍💻, 5 points)
Define a function `remove_compose` that takes an expression and returns a semantically equivalent expression that does not use the composition operator `|>`.
```python
def remove_compose(expr: Expr) -> Expr:
    # your code here
```

<details>
<summary>Hint</summary>

Define a helper function that *substitutes* `x` with another expression.
</details>


### Problem 1-D (🧑‍💻, 10 points)

Compilers routinely perform optimizations on programs to make them faster, smaller, etc. They do so before the program is run, so the optimizations need to be correct regardless of what the user inputs in the future.

Implement the `simplify` function that will optimize arithmetic expressions. In particular:

* Operations on constant expressions should be simplified, e.g. `1 + (1 * 3)` is simplified to `4`.
* Addition and multiplication identities should be simplified, e.g. `1 * (x + 0 + (5 * 0))` is simplified to `x`. Specifically, you need to handle addition by 0, multiplication by 0, and multiplication by 1.
* All other combinations of addition and multiplication should be left as-is. For example, you do not need to distribute multiplication (e.g., you should leave `2 * (x + 1)` as-is), nor do you need to combine multiple additions of a term into scaling the term by a constant (e.g., you should leave expressions such as `x + (2 * x)` as-is).
* All simplifications should be applied *as much as possible*.
* You may assume that all composition operators have already been removed from the expression.

<details>
<summary>Hint</summary>

Use simultaneous pattern matching and wildcard to make your code cleaner:
```python
match <x>, <y>:
    case <pattern1>, <pattern2>:
        # your code here
    case ...:
        # your code here
    case _:
        # _ is a wildcard that matches anything, so it's like a default "catch-all" case
        # this branch is executed only if none of the preceding patterns match
        
        # your code here
```
</details>
        

## Problem 2

In this problem, you will be a language designer, and design the syntax and semantics of propositional logic, which you first learned in [CS 40](https://sites.cs.ucsb.edu/~cappello/lectures/logic/1.1.pptx).

### Problem 2-A (✍️)

Formalize the abstract syntax of propositional logic propositions using context-free grammar. Your grammar should support `-` (unary negation), `/\` (binary conjunction), `\/` (binary or), `->` (binary implication), `<->` (iff), along with boolean constants ($\textsf{True}$ and $\textsf{False}$) and propositional variables.


### Problem 2-B (✍️)
Use Python's `dataclass` to represent the abstract syntax tree (AST) of propositions defined by your grammar. Name the abstract class `Prop`, and include the class definitions in your PDF:

```python
@dataclass
class Prop:
    pass

@dataclass
class Class1(Prop):
    # fields

@dataclass
class Class2(Prop):
    # fields

...
```

### Problem 2-C (✍️)
Pretend you’re the parser. For each of the following proposition, draw the corresponding AST. Then write down a Python object (of class `Prop`) that represents the same AST. The object should be constructed using a series of initialization for `Class1`, `Class2`, etc. that you defined in Problem 2-B.
- `A -> B -> C`
- `A \/ B \/ C`
- `A /\ B \/ C`
- `-A \/ -B <-> -(A /\ B)`

Use the following precedence and associativity rules to resolve any ambiguities:
- `-` has the highest precedence and is non-associative (since it's unary).
- `/\` has the second highest precedence and is left associative.
- `\/` has the third highest precedence and is left associative.
- `->` and `<->` have the lowest precedence and are right associative.

### Problem 2-D (✍️)
Define a Python function `pretty_print` that converts a proposition to a human-readable string. In the output string, use parentheses to clearly disambiguate nested operators. In the PDF, include the function definition, as well as the output of the function when given the Python AST objects that you wrote down for Problem 2-C.

```python
def pretty_print(prop: Prop) -> str:
    # your code here

# Example usage
print(pretty_print(...))
print(pretty_print(...))
print(pretty_print(...))
print(pretty_print(...))

# Output:
# Copy and paste stdout for the above print statements here
```


### Problem 2-E (✍️)
Define a Python function `size` that computes the number of nodes in a proposition AST. In the PDF, include the function definition, as well as the output of the function when given the Python AST objects that you wrote down for Problem 2-C.

```python
def size(prop: Prop) -> int:
    # your code here

# Example usage
print(size(...))
print(size(...))
print(size(...))
print(size(...))

# Output:
# Copy and paste stdout for the above print statements here
```

### Problem 2-F (✍️)
Formalize the meaning of logical formulas by inductively defining the judgment
$$
\alpha^+ \vdash P^+ \downarrow b^-
$$
where $P$ is a proposition, $b$ is a boolean value ($\textsf{True}$ or $\textsf{False}$), and $\alpha$ is an assignment of boolean values to propositional variables. Intuitively, this judgment means that under assignment $\alpha$, proposition $P$ evaluates to boolean value $b$. The assignment $\alpha$ and the proposition $P$ are annotated with a polarity of $+$ to indicate that they are "inputs", while the boolean value $b$ is annotated with a polarity of $-$ to indicate that it is the "output".

In designing your operational semantics:
- You should have at least one rule for each case in your abstract syntax.
- The meaning of each operator should be independent. That is, do not use a judgment involving `->` to define a judgment involving `<->`.
- The set of rules should be *algorithmic* -- at any point in a derivation, you should be able to apply at most one rule.
- The relation $\alpha^+ \vdash P^+ \downarrow b^-$ defined by your rules should be *deterministic* -- that is, for any assignment $\alpha$ and proposition $P$, there should be at most one boolean value $b$ such that $\alpha^+ \vdash P^+ \downarrow b^-$.
- There are several ways to handle variables in a proposition that are not defined by the assignment.
  - You can stipulate that there is *no applicable rule* if the variable is undefined.
  - You can explicitly return a special value (e.g., ☹️) to signal that the variable is undefined. So in judgment $\alpha \vdash P \downarrow b$, the value of $b$ can be $\textsf{True}$, $\textsf{False}$, or ☹️.

In addition, in your PDF, for each of the propositions in Problem 2-C, draw the derivation tree that shows $$\alpha \vdash P \downarrow \textsf{True}$$ for some assignment $\alpha$ of your choice. That is, pick an assignment $\alpha$ of the variables in $P$ that make $P$ evaluate to $\textsf{True}$, and draw the derivation trees where you apply your operational semantics rules.



## Problem 3

A programming language often provides *syntactic sugars* — nice-to-have features that allow programmers to write more concise code but are nevertheless expressible using (a combination of) more primitive features. 

A prototypical example is `for` loops, which is a syntactic sugar for `while` loops that increment a counter variable. For example, the following `for` loop:
```c
for (int i = 0; i < 10; i++) {
    printf("%d\n", i);
}
```
is a syntactic sugar for the following `while` loop:
```c
int i = 0;
while (i < 10) {
    printf("%d\n", i);
    i++;
}
```

Programmers -- well, human programmers at least -- love syntactic sugars, since they can write less code. Language implementers hate syntactic sugars, because they need to write *more* code to handle those sugars which are basically duplicates of the code for handling the primitives.

Luckily, a technique known as "desugaring" can make both the programmer and the language implementer happy, whereby a sugar is automatically translated into a combination of primitive features, before the primitive features are implemented. This way, the programmer can keep having their yummy sugar, but the implementer doesn't need to write any redundant code beyond the absolute necessary amount needed to handle the primitives.

We call an abstract syntax that has syntactic sugars the “surface syntax”, and an abstract syntax that doesn’t have them the “core syntax”.

For example, consider arithmetic expressions that we type into calculators. It’s convenient to type "-10" or "+123" using unary minus and plus, but they can be desugared into “0 - 10” and “123”. So the surface syntax of arithmetic expressions might look like this
```
expr ::= number
       | -expr
       | +expr
       | expr + expr
       | expr - expr
```
whereas the core syntax would look like this:
```
expr ::= number
       | expr + expr
       | expr - expr
```

The surface syntax has 5 cases, while the core syntax has only 3 cases. The translation from surface syntax to core syntax can be given by the following desugaring function:
```
desugar(number) = number
desugar(- expr) = 0 + desugar(expr)
desugar(+ expr) = desugar(expr)
desugar(expr + expr) = desugar(expr) + desugar(expr)
desugar(expr - expr) = desugar(expr) - desugar(expr)
```

An obvious but important property of desugaring is that it should not change the meaning (semantics) of the program.


### Problem 3-A (✍️)
The abstract syntax you designed for propositional logic in Problem 2 can be considered a surface syntax, since many operators can be expressed using a small set of primitives. Your task is to define a core syntax for propositional logic that has no more than 4 cases:
```
prop ::= T (true) | F (false)
       | x (variable)
       | <op> (operator)
```
where `<op>` is any operator of your choice. The operator doesn't have to be one that's already in the surface syntax -- you can come up with a brand new operator. The operator can be unary, binary, or ternary. As a (non-)example, here's a possible core syntax:
```
prop ::= T (true) | F (false)
       | x (variable)
       | prop /\ prop
```
although this is not a good choice, since `/\` doesn't have enough expressiveness to represent all propositions in the surface syntax.

Once you designed your operator, choose a sensible notation for it, and include the full grammar of the core syntax in your PDF. Then, intuitively describe the meaning of the operator using 1-2 sentences.


### Problem 3-B (✍️)
Formalize the operational semantics for your core syntax by formalizing the following judgment using inference rules:
$$
\alpha^+ \vdash P^+ \Downarrow b^-
$$
where, again, $b$ is a boolean value, $P$ is a proposition, and $\alpha$ is an assignment of boolean values to propositional variables. We use $\Downarrow$ instead of $\downarrow$ to distinguish the semantics of the core syntax ($\Downarrow$) from that of the surface syntax ($\downarrow$).

In designing your operational semantics:
- You should have at least one rule for each case in your core syntax.
- The meaning of each operator should be independent.
- Your rules should be algorithmic, and the resulting relation should be deterministic.

### Problem 3-C (✍️)
Use Python's `dataclass` to represent the abstract syntax tree (AST) of propositions defined by your core syntax. Name the abstract class `Core`, and include the class definitions in your PDF:

```python
@dataclass
class Core:
    pass

@dataclass
class Class1(Core):
    # fields

@dataclass
class Class2(Core):
    # fields
```

### Problem 3-D (✍️)

Define a Python function that translates the surface syntax into the core syntax.
```python
def desugar(p: Prop) -> Core:
    match prop:
        case <your code here>
```
The function should handle all ASTs in the surface syntax, and return an AST in the core syntax.

Include the function definition in your PDF, as well as the output of the function when given the Python AST objects that you wrote down for Problem 2-C.

```python
# Example usage
print(desugar(...))
print(desugar(...))
print(desugar(...))
print(desugar(...))
# Output:
# Copy and paste stdout for the above print statements here
```




### Problem 3-E (✍️)
Translate the semantic rules you just defined into a Python function `eval` that evaluates a proposition in the core syntax. The function should have the following signature:
```python
def eval(α: dict[str, bool], prop: Prop) -> Optional[bool]:
    match prop:
      # your code here
```
where $\alpha$ is a dictionary that maps propositional variables to boolean values, and `prop` is a proposition in the core syntax. The function should return the boolean value of the proposition under the assignment if all variables are defined in the assignment, or `None` if any variable is undefined.




### Problem 3-F (✍️, ⭐️extra credit⭐️, 2 points)
Prove by induction that the desugaring function you just defined preserves the meaning of the proposition. That is, for any proposition $P$ in the surface syntax, any assignment $\alpha$, and any value $b$, if

$$
\alpha \vdash P \downarrow b
$$
then
$$
\alpha \vdash \text{desugar}(P) \Downarrow b
$$

You can induct either on the size of the AST in surface syntax, or on the size of the derivation tree. If you need a refresher on induction, please feel free to come to office hours.


### Problem 3-G (✍️, ⭐️extra credit⭐️, 2 points)
Would you consider the composition operator `|>` from Problem 1-B to be a syntactic sugar, and the `remove_compose` function from Problem 1-C a "desugaring" function? Give a brief argument (1-2 sentences) to justify your answer. There are no right or wrong answers.


## Problem 4

Recall the CoinPython language:

```
p ::= pass
    | raise
    | print(msg)
    | if (*) {p} else {p}
    | p; p
    | while (*) {p}
msg ∈ M
```
where `M` is a finite set of strings, e.g., `M = {"ok", "oops"}`.
And recall the judgment:
```
p => s
```
which intuitively means "execution of program `p` terminates normally (without exception), and the content of the console is `s`". 

The AST for CoinPython programs is defined in <this file: FIXME>. 




### Problem 4-A (🧑‍💻, 5 points)

The most obvious way to determinize the relation `p => s` is to treat program `p` as input, and string `s` as output. In other words, we can write a CoinPython interpreter that executes a program `p` with some source of randomness, and collects the output `s` that is printed to the console.

In <this file: FIXME>, implement such an interpreter:
```python
@dataclass
class ProbablisticInterpreter:
    coin: Coin

    def run(self, p: Program) -> str:
        # your code here
```

In deciding the truth values of coin tosses (for `if (*)` and `while (*)`), the interpreter should use the `coin` object, which is an instance of the `Coin` class defined in <this file: FIXME>. The only method of `Coin` that you need to be aware of is `flip`, which returns either `True` or `False`:

```python
@dataclass
class Coin:
    def flip(self) -> bool:
        ...
```

For example, for the following CoinPython program:
```
if (*) { pass } else { print("okie"); print("dokie") }
```
the interpreter should return either the empty string `""` (if the first coin toss is heads) or the string `"okiedokie"` (if the first coin toss is tails).


### Problem 4-B (🧑‍💻, 5 points)

In programming language theory, an important problem is to predict the behavior of a program *before it is run*. Why? Because running a program can be costly in terms of time, money, and occasionally even human lives. For example, you don't want to find out that the aviation software on your flight that detects the speed of a plane has an overflow bug, and in particularly, you don't want to find out only after the plane has taken off, which will be too late.

Let's say the aviation software was written in Python, for some heinous reason (not that you should). Then, our CoinPython is a very useful model for the aviation software, as we have discussed in class: any interesting behavior of the aviation software can be modeled as a CoinPython program with appropriate print statements that log the behavior of interest.

With this in mind, let's determinize the relation `p => s` in a different way that allows us to predict whether a program `p` will print a string `s` *without* actually running the program (like using the interpreter that you wrote in Problem 4-A). In other words, this time, both program `p` and string `s` are inputs to the relation, and we want to write a function that returns `True` if and only if `p => s`, and `False` otherwise.

Your task is to implement the `predict` function that does just that:
```python
class Predictor:

    def predict(self, p: Program, s: str) -> bool:
        # your code here
```

For example, for the following CoinPython program:
```
if (*) { print("oops") } else { print("okie"); print("dokie") }
```
the predictor should return `True` for both `"oops"` and the string `"okiedokie"`, and `False` for any other string.


Your `predict` function should return a 100% correct answer if the program doesn't contain `while` (if it does contain `while`, just try your best). In particular, don't rely on the probablistic interpreter that you wrote in Problem 4-A: don't execute the program `p` at bunch of times, sample the outputs, and check if `s` is among the outputs. If you think doing this is fine, imagine that the pilot told you the aviation software is secured by the law of large numbers:
> Hey, I heard the programmer who wrote the aviation software tested it a million times on randomly generated inputs, and it never printed "oops". So I guess this plane is safe to fly!

Right?..

<details>
<summary>Hint</summary>
One of the tricky cases is sequencing, where you need to "guess" how to split the input string into two substrings. Since you need to be 100% correct, you have to try all possible guesses.
</details>





