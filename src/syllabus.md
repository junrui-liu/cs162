# Syllabus

> Everything here is work in progress, and is subject to change.

## Instructor's & TA's info
  - Name
  - Email
  - Hobby
  - Office hours

## Communication
  - Slack

## Course overview
TBD

## Goals
TBD

  
## Struture
- 6 programming assignments, 50%
  - 5 required assignments, each one building on the previous one.
  - Since they are cumulative, I and the TA will do our absolute best to help you get 100% on all of them, if you're willing to put in the work. 
  - The 6th assignment is optional and replaces the one with the lowest score.
  - 5 tokens of "late days". you can use them all on one assignment or spread them out
  - after all 5 tokens used, no more late work accepted
  - LLM policy: TBD
    - Option 1: No LLMs whatsoever
    - Option 2:
      - No LLMs for the first 3 assignments. If you have questions, ask me, the TA, or your classmates. LLMs are known to hallucinate BS, which is antithetic to the goals of this course and especially problematic when you're trying to learn something *for the first time*. We want to teach you to think about programming very carefully, and write correct code!
      - LLMs allowed for the last 3 assignments (once you get a hang of things and can discern BS when you see one), but you should clearly document exactly what you used them for:
        - In file X, I used LLM to generate this line of code on line Y.
        - I asked LLM to explain code X or concept Y to me.
        - This also helps me gauge which concepts are still confusing to students.
- 3 quizzes, 45%
  - held in class, no makeups
  - closed book, closed notes, closed laptops, 15-30 minutes
  - *turn in corrections for 50% credit back at the end of the quarter*
- "perspectives", 5%
  - each week, I will share one or two Youtube videos on some aspect of programming languages -- either directly related to what we talked about that week, or some broader topic that might be interesting/important but unfortunately doesn't fit into the short time we have in class
  - Out of 6 weeks, you pick 3 weeks. For each week, write a short (2-3 paragraphs) reflection on what you learned from the video, what surprised you, what you agreed/disagreed with, how does it change the way you think about programming languages, etc. Share it with the class.
  - Completion = full credit. No need to be a great writer. Just share your thoughts in a way that we can understand, be honest and be thoughtful.
  - LLM policy:
    - Do not use LLMs for these reflections. Think for yourself.


## Tentaive Schedule and Topics


|   Date | Topic                                       | Out  | Due  |
| -----: | ------------------------------------------- | ---- | ---- |
| Week 1 | **How to design a programming language?**   |      |      |
|  06/24 | Why study programming languages?            |      |      |
|  06/25 | Python review                               |      |      |
|  06/26 | Inference rules                             | HW 1 |      |
| Week 2 | **What makes a programming language?**      |      |      |
|  07/01 | Semantics                                   |      |      |
|  07/02 | Names and bindings                          |      |      |
|  07/03 | Types                                       | HW 2 | HW 1 |
| Week 3 | **How to abstract *data*?**                 |      |      |
|  07/08 | Finite types (products)                     |      |      |
|  07/09 | Finite types (sums), bidirectional typing   |      |      |
|  07/10 | Recursive and generic types                 | HW 3 | HW 2 |
| Week 4 | **How to abstract *programs*?**             |      |      |
|  07/15 | Higher-order functions                      |      |      |
|  07/16 | Lambda calculus                             |      |      |
|  07/17 | Parametric polymorphism                     | HW 4 | HW 3 |
| Week 5 | **How to change the world?**                |      |      |
|  07/22 | Mutable states, garbage collection          |      |      |
|  07/23 | Exceptions, abstract machines               |      |      |
|  07/24 | Effect handlers                             | HW 5 | HW 4 |
| Week 6 | **What is the future of programming like?** |      |      |
|  07/29 | Curry-Howard correspondence                 |      |      |
|  07/30 | Codata, objects, infinity, and ducks        |      |      |
|  07/31 | It's lambda calculus all the way down!      |      |      |
|  08/02 | (End of summer session A)                   |      | HW 5 |


## Pedagoy
- **Growth mindset**: ok to fail, but learn from it (that's why you'll get credit back if you turn in corrections). If you put in the work, you will get the grade you want.
- **Community, not competition** -> no curve to force a certain distribution of grades. Help each other out. Form study groups, come to office hours, ask lots of questions.
- Emphasize that **office hours are for everyone**, not just the struggling students. 
  - Extra credit or other incentives for attending office hours?
  - Feel free to come by and just chat about anything related to the course. There are absolutely no stupid questions. From my experience as a TA, I learn something new from every question asked and every student I talk to. Questions reveal not just gaps in understanding, but also gaps in my communication of the material, e.g., I was going too fast, or I was explaining something in a way that didn't make sense to the student.

## Textbooks and other references (optional)
- [Programming Languages: Application and Interpretation (2nd Ed)](https://cs.brown.edu/courses/cs173/2012/book/) by Shriram Krishnamurthi
- [Types and Programming Languages](https://github.com/MPRI/M2-4-2/blob/master/Types%20and%20Programming%20Languages.pdf) by Benjamin C. Pierce
- Frank Pfenning's [lecture notes for 15-814](https://www.cs.cmu.edu/~fp/courses/15814-f21/schedule.html) at CMU
- [Practical Foundations for Programming Languages (2nd Ed)](https://web.archive.org/web/20221109205432/http://www.cs.cmu.edu/~rwh/pfpl/2nded.pdf) by Robert Harper


## Difference with previous years

<details>
<summary>Click to expand</summary>

- Why not reuse existing materials?
  - I've TA'ed this course (which has recycled basically the same materials) for 4 years from 2022 to 2025. I have noticed that there remain a *lot* of things that could be improved to (1) make existing topics more accessible, (2) delete topics that are too theoretical and (3) reorient the course to be more relevant even after you graduate, no matter whether you become a programmer or a PL researcher. My overarching objective is to teach you the "PL way of thinking" that you still remember after 5 years.
  - Specially, I will try to teach the class in a way that I wish I had been taught when I first learned programming languages. I love PL deeply, and I want to share the beauty of the subject with you.
- The course is redesigned to be entirely **incremental**. The whole course culminates in your building a really powerful and elegant programming language step by step. Each lecture introduces a new feature into the language, and each assignment builds on the previous one. Previously, CS162 just gave you a fully complete language, and each assignment implements different aspects of the *full* language.
- Emphasis on the three roles of PL design process: motivating use case (client) -> relational design (designer) -> algorithmic implementation (implementer). Previously, CS162 just gave you a fully designed language and asked you to decipher a "god-given" design and write code to implement it. There weren't even use cases to motivate the design. This time, you will get a taste of all three roles of a language designer, and most importantly, you get to experiment with the design of the language yourself! How cool is that?
- Instead of a single final that's worth 50%, we have 3 quizzes spread out over the quarter (more immediate feedback), and you get 50% points back for corrections (it's ok to make mistakes; what matters is to learn from your own mistakes!).
- Programming assignments now use Python instead of OCaml
  - As much I love OCaml (it's my favorite language & I use it on most programming projects), to be able to use it for CS162, we need to spend at least 1.5 weeks, and in the past students didn't get comfortable until several weeks in. Cramming it into a 6-week summer session course is just too much.
  - Hopefully, Python is easy enough to pick up (it's also used in CS8/9 and couple of other upper-div courses). Technically, Python will be a lot more "useful" once you get a real job.
  - But my secret agenda to convert all of you to functional programming aficionados is not dead yet. The object language is a functional language in disguise.
- We are now able to cover a lot more super cool topics (codata/objects, bidirectional typing, subtyping, type constructors, effects), since we completely removed the OCaml module (and moved the higher-order functions to the object language).
- Finer points:
  - Early introduction of typing.
  - Early introduction of procedures, and late introduction of lambda calculus.
    - Lambda calculus is a generalization of procedures anyway, so it's good to get lots of practice with procedures first.
  - Entirely skip capture-avoiding substitution. Variable captures had been a non-issue IMO (we didn't do dependent types so all programs are closed), and they felt like a topic forced onto the students which they were gonna forget immediately after the exam.
</details>