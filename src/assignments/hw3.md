# HW3: User-Defined Types 🎨

stdlib:
- bool
- maybe
- nat
- list
- assoc list
  - hint at generics
- red-black tree
fun:
- coin python AST
- ast
- lazy queue

rec type (EC: DDoS)
pattern matching (EC: or-pattern)


### Problem 4 (✍️, 5 points)

**Definition:** The *language* of a CoinPython program $p$, denoted by $L(p)$, is the set of all strings $s$ such that `p => s`. That is, $L(p)$ is the mathematical set of all strings that an `AllOutputsInterpreter` can yield. For example, if $p$ is the program
```
if (*) { pass } else { print("okie"); print("dokie") }
```
then $L(p)$ is the set
```
{ "okiedokie", "" }
```

**Definition:** we say CoinPython programs $p_1$ and $p_2$ are *equivalent*, denoted by $p_1 == p_2$, if and only if the set $L(p_1)$ is equal to the set $L(p_2)$. 


Determine if the following equivalences $p_1 == p_2$ hold. If an equivalence holds, write "yes", and informally justify your answer in 1-2 sentences. If an equivalence does not hold, write "no", and give a counterexample (i.e., exhibit concrete programs $p_1$ and $p_2$ and a string $s$ such that $s \in L(p_1)$ but $s \notin L(p_2)$, or vice versa). Note that in the following, `p` and `q` can be arbitrary CoinPython programs.
1. `p; pass` == `p`
2. `raise; p` == `raise`
3. `p; q` == `q; p`
4. `if (*) { p } else { q }` == `if (*) { q } else { p }`
5. `if (*) { raise } else { p }` == `p`
6. `while (*) { p }` == `p`
7. `while (*) { while (*) { p } }` == `while (*) { p }`
8. `while (*) { pass }` == `pass`
9. 
      ```python
      p;
      while (*) { q; p }
      ```
      ==
      ```python
      while (*) { p; q };
      p
      ```
10.  
    ```python
    while (*) {
        if (*) { p }
        else { q }
    }
    ```
    ==
    ```python
    while (*) { p };
    while (*) {
        q;
        while (*) { p }
    }
    ```
11.  
       ```python
       while (*) { p } 
       ```
       
       ==
       
       ```python
       if (*) {
          p;
          while (*) { p }
       } else {
          pass
       }
       ```