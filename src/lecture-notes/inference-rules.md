# Russian Dolls 🪆

<iframe width="560" height="315" src="https://www.youtube.com/embed/eVBzfB5vHzs?si=2V82Q71sOsoq_scC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Motivate the need for precise definition of language semantics (use Yu's slides).

Crash course on inference rules:
- Google sheets as an analogy
- Example 0: minecraft recipes
- (membership) Example 1: is X a Russian doll?
- (membership for 2-place relation) Example 2: mystery relation: X <= Y?
- (determinization) Example 3: X tensor Y => Z
  - question: how to determinize examples 1 & 2?
- (operational semantics for pure expressions)

## Operational semantics for imperative languages

### All behaviors can be observed through `print`


CoinPython:
```
msg ::= "ok" | "oops"
p ::= pass
    | raise
    | print(msg)
    | if (*) {p} else {p}
    | p; p
    | while (*) {p}
```

Judgment:
```
p => s
```
means "execution of program `p` finishes without exception, and string `s` is printed to the console".

```
---------- R-Pass
pass => ""


----------------- R-Print
print(msg) => msg


(no rule for raise)


p1 => s1
p2 => s2
s3 = s1 + s2
------------ R-Seq
s1; s2 => s3


p1 => s1
--------------------------- R-If1
if (*) {p1} else {p2} => s1


s2 => s2
--------------------------- R-If2
if (*) {p1} else {p2} => s2


------------------- R-While
while (*) {p} => ""


p => s1
while (*) {p} => s2
s3 = s1 + s2
------------------- R-While
while (*) {p} => s3
```

- Is the relation deterministic?
- Are the rules *algorithmic*?