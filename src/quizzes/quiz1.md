

## Problem
For each of the following methods of defining language semantics, give one reason why it can be problematic:
1. Define the semantics of a language feature by explaining the feature using natural language and concrete examples
2. Define the semantics of a language feature by implementing the feature in a compiler or an interpreter
3. Define the semantics of a language feature by consulting ChatGPT


## Problem
Consider the language of arithmetic expressions on natural numbers:
```
expr ::= N
       | expr + expr
       | expr - expr
       | expr * expr
value ::= zero | succ(value)
```

Let us augment the language with a new kind of expression:
```
expr ::= ...
       | expr ⊔ expr
```

Intuitively, `e1 ⊔ e2` is the expression that evaluates to the maximum of `e1` and `e2`. Augment the operational semantics of the language by defining rules for evaluating `e1 ⊔ e2`. You should ensure that
1. your rules are algorithmic: at any point in time, at most one rule is applicable to evaluating `e1 ⊔ e2` 
2. the evaluation relation `e => v` remains deterministic in `e`: for any expression `e`, there is at most one value `v` such that `e => v`


## Problem
Consider the language of arithmetic expressions on natural numbers augmented with the max operator:
```
expr ::= zero | succ(expr)
       | expr + expr
       | expr - expr
       | expr * expr
       | expr ⊔ expr
```
Let us define a new kind of values, called *approximate values*:
```
approximate_value ::= zero | nonzero | idk
```

Using inference rules, define a new evaluation relation:
```
expr =>> approximate_value
```
which intuitively means "expression `e` evaluates to an approximate value `v`":
- The approximate value `zero` means the expression definitely evaluates to zero
- The approximate value `nonzero` means the expression definitely evaluates to a non-zero natural number.
- The approximate value `idk` means the expression may evaluate to either zero or a non-zero natural number.

You should ensure that
1. your rules are algorithmic
2. the evaluation relation `e =>> v` is deterministic in `e`.

The following rules are provided for you:
```
----------------- Zero
zero =>> zero

----------------- Succ
succ(v) =>> nonzero
```

Your task is to define the rules for the remaining cases. Choose the most precise approximate value that is still a valid over-approximation.

## Problem

> This problem assesses:
> formalize semantics of a language using inference rules
> give examples of rules that are (non-)algorithmic
> give examples of relations that are (non-)deterministic

Recall the CoinPython language:

```
p ::= pass
    | raise
    | print(msg)
    | if (*) {p} else {p}
    | p; p
    | while (*) {p}
msg ::= "ok" | "oops"
```
and the judgment:
```
p => s
```
which intuitively means "execution of program `p` terminates normally (without exception), and the content of the console is `s`". 


Define the following (unary) relation using inference rules:
```
sneaky(p)
```
which means "program `p` *may* terminate normally without printing anything to the console". Note "may" means "probablistically possible", i.e., there exists a (possibly empty) sequence of coin tosses that leads to the program terminating normally without printing anything to the console. For example, the program
```
if (*) { pass } else { raise }
```
is sneaky, because if the first coin toss is heads, the `if` branch is executed, and the program terminates normally without printing anything to the console. However, the program
```
if (*) { print("ok") } else { raise }
```
is not sneaky, because if the first coin toss lands heads, then "ok" is printed to the console, and if the first coin toss lands tails, the program raises an exception.


## Problem
Desugar n-ary sequence and choice (switch) into CoinPython, and vice versa.


## Problem
Consider the abstract syntax of arithmetic expressions with *integer* constants, addition, subtraction, multiplication, sequence summation and sequence multiplication:

$$
\begin{align}
e  ::&=  N &\text{integer constant} \\
     &\mid x  &\text{variable} \\
     &\mid e + e &\text{addition}\\
     &\mid e \times e &\text{multiplication} \\
     &\mid sum(e_1, e_2, x.\, e_3) &\text{sequence sum} \\
     &\mid prod(e_1, e_2, x.\, e_3) &\text{sequence product}\\
\end{align}
$$
where
$sum(e_1, e_2, x.\, e_3)$ represents sequence summation of the form
$$
\sum_{x=e_1}^{e_2} e_3
$$
and $prod(e_1, e_2, x.\, e_3)$ represents sequence multiplication of the form
$$
\prod_{x=e_1}^{e_2} e_3
$$ 

As an example, the expression
$$
\sum_{i=1}^{100} \left(i + \sum_{j=1}^{i} \prod_{k=1}^{i+j} (i * j + k)\right)
$$
is a valid expression in this language.

Draw the abstract binding tree (ABT) for the above expression.

## Problem

Recall that the `Binder` class is defined as follows:
```python
@dataclass
class Binder[T]:
    var: str
    scope: T
```


Finish the representation of ABTs for this language by declaring fields for the `SequenceSum` and `SequenceProd` classes:


```python
@dataclass
class Expr:
    pass

@dataclass
class Constant(Expr):
    value: int

@dataclass
class Var(Expr):
    name: str

@dataclass
class Add(Expr):
    left: Expr
    right: Expr

@dataclass
class Mul(Expr):
    left: Expr
    right: Expr

@dataclass
class SequenceSum(Expr):
    # your code here

@dataclass
class SequenceProd(Expr):
    # your code here
```

## Problem
Finish the implementation of the `subst` function that substitutes a variable `x` with another expression `e` in `s`. Note that `s` can be either an `Expr`, or a `Binder`.
```python
def subst(x: str, e: Expr, s):
    match s:
        case Constant():
            return s
        case Add(left, right):
            return Add(subst(x, e, left), subst(x, e, right))
        case Mul(left, right):
            return Mul(subst(x, e, left), subst(x, e, right))
        case SequenceSum(binder, body):
            # your code here
        case SequenceProd(binder, body):
            # your code here
        case Var(name):
            # your code here
        case Binder(var, scope):
            # your code here
        case _:
            raise ValueError("Unknown expression/binder type")
```

## Problem

Using the `subst` function, finish the implementation of the `eval` that evaluates an expression. You may assume that the original input expression is closed, i.e., it does not contain any free variables.
```python
def eval(e: Expr) -> int:
    match e:
        case Constant(value):
            return value
        case Add(left, right):
            return eval(left) + eval(right)
        case Mul(left, right):
            return eval(left) * eval(right)
        case SequenceSum(binder, body):
            # your code here
        case SequenceProd(binder, body):
            # your code here
        case Var(name):
            # your code here
        case _:
            raise ValueError("Unknown expression type")
```

## Problem

Finish the implementation of the `eval_env` function that uses an environment instead of substitution to evaluate an expression. The environment is a mapping from variable names to expressions. You may assume that the original input expression is closed, i.e., it does not contain any free variables, and the original input environment is empty.
```python
def eval_env(env: dict[str, Expr], e: Expr) -> int:
    match e:
        case Constant(value):
            return value
        case Add(left, right):
            return eval_env(env, left) + eval_env(env, right)
        case Mul(left, right):
            return eval_env(env, left) * eval_env(env, right)
        case SequenceSum(binder, body):
            # your code here
        case SequenceProd(binder, body):
            # your code here
        case Var(name):
            # your code here
        case _:
            raise ValueError("Unknown expression type")
```

## Problem
Consider the following property about X expressions:
TBD

Show that this property is undecidable by reducing it to the halting problem.


## Problem

Language with
- unit
- pairs with fst and snd
```
const ::= true | false | 0 | 1 | 2 | ...
expr ::= const | expr + expr | (expr, expr) | expr.0 | expr.1
value ::= const | (v0, v1)
type ::= Nat | Bool | t0 * t1
```

We provide abstract syntax.
You define operational semantics and typing rules.
State (but don't prove) inversion lemmas, and prove type soundness.


## Problem

Consider the full X language whose n-ary tuples are replaced with n-ary tuples (n >= 0) with runtime indexing. That is, the indices no longer have to be constants, and can be expressions that evaluate to natural numbers.

```
const ::= true | false | 0 | 1 | 2 | ...
expr ::= const | expr + expr | (expr0, .., exprn-1) | expr.expr
value ::= const | (v0, .., vn-1)
```
We provide operational semantics.

Can you design a type system for this language, such that expressions like
- `let x = 2 in (1+2, 1 > 2).(2-1)` is well-typed and has type `Bool.
- type checking is decidable

If so, define the typing rules, and draw the derivation tree that shows `let x = 2 in (1+2, 1 > 2).(2-1)` has type `Bool`.

If not, explain why it is impossible to design such a type system.

