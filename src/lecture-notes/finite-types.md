# Lecture 7: Multiply and Add ✖️➕


## Product types
- Procedures can only take one argument and return one value => motivate product types
- Binary => n-ary, or go directly to n-ary?
- Design choices:
  - elimination via indexing (`e.1`) or unpacking (`let (x, y) = e in ..`)?
    - [ ] indexing is what Python uses
    - [x] unpacking makes it easy to introduce syntactic sugar for procedures with multiple arguments
  - eager vs lazy introduction form?
    - Imagine we use lazy introduction form. What does this mean for elimination form? (Need to evaluate)
    - [x] Imagien we use eager introduction form. What does this mean for elimination form? (No need to evaluate)
  - Road not taken: lazy intro + elim via indexing (will take it soon)
- Special case: empty product
- Typing:
  - derive from big-step semantics
  - (exercise) small step

- Live-coding:
  - TBD

## Structs
- Generalize indexed product types to support indexing via arbitrary labels
- Lazy intro + elim via label indexing
  - Implications of this design choice will become clear when we talk about recursive types
- (In-class activity/HW) Design big-step, small-step, and typing

## Sum types
> might spill over to next lecture
- Motivate via error-handling. Examples:
  - Division by zero
  - Generalization of booleans
- Briefly discuss design choices, but we will only choose eager introduction form
- Do binary sum first, then HW generalizes to n-ary
  - Big-step
  - Give typing rules
  - Small-step (HW)


## Counting types
