# Lecture 8: Mutualism 🤝

- Typing for sums isn't algorithmic: when checking introduction form, needs the type to be an input
- Motivates a new form of typing judgment (type checking). Old judgment is synthesis.
- Question: how to turn typing rules into type checking or synthesis? ==> how does information flow?
- Observe:
  - sum types: injection checks, match synthesizes.
  - procedures: definition checks, application synthesizes.
- Generalize:
  - Product/struct types: packing checks, unpacking/projection synthesizes.
  - Variables synthesize
  - New rule: when checking and synthesis meets, we need to check type equality
- Exercise: add type annotation

