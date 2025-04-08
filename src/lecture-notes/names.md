# Lecture 5: Names 🏷️

- Use second-class procedures to motivate names and bindings
- Introduce local variables
  - https://github.com/fredfeng/CS162/blob/winter-2024/sections/sec03/README.md
- Represent generic binder interface in Python
- Binder operations as visitor pattern or match?
- Operational semantics for `let` and procedures.
  - Design choices:
    - Eager vs lazy?  
      - Do variables stand for values or (unevaluated) code?
      - Efficiency considerations: eager = more efficient if shared, lazy = more efficient if not used, same if used exactly once
    - Scoping for procedures
      - Mutually recursive?
    - Variable scoping in procedures: 
      - Start with clean environment when evaluating a procedure?