# CS 162 - Programming Languages

<!-- > Everything here is work in progress, and is subject to change. -->

## Course description

Languages shape how we think.

This course will expand how you think about programming by showing *how languages are built*. We'll demystify so-called "paradigms" -- imperative, object-oriented, and functional -- by distilling them into their core building blocks. You'll come to see familiar languages in a new light, no longer bound to one "paradigm". You'll be able to see through surface-level syntax, and choose the right abstractions for the right problems.

More deeply, you'll learn powerful tools used by language designers and theorists to ensure the *correctness* of languages and programs written in them. In a world increasingly flooded with AI-generated slop, this course will sharpen your ability to separate signal from noise and build *provably unhackable* software, making you irreplaceable in the "AI future".

All this is grounded in hands-on projects. Throughout the session, you'll design and implement a simple but powerful language that unifies seemingly disjoint paradigms and previews next-generation language features.


## Learning outcomes
By the end of this course, you will be able to:
1. **Formalize** the syntax and semantics of programming languages from informal description.
2. **Visualize and reason about** languages and programs written in them using formal models.
3. **Implement** interpreters and type checkers from formal specifications.
4. **Analyze** widely held misconceptions about language features and "paradigms", and **desugar** surface-level features into their essential components.
5. **Apply** typed functional programming and computational effects to model and solve problems.
   <!-- 1. Model the data domain with algebraic data types.
   1. Carry out structural recursion (induction) to solve the problem over algebraically defined data.
   2. Identify recurring computational patterns in the solution, and abstract them into higher-order and/or polymorphic functions. -->

## Teaching team

Instructor:
- Junrui Liu
- Email: junrui@ucsb.edu
- Office hours: TBD

TA:
- Jiaming Shan
- Email: jiamingshan@ucsb.edu
- Office hours: TBD

Faculty mentor:
- Yu Feng
- Email: yufeng@cs.ucsb.edu

## Course communication

We will use Discord for most communication, including announcements and Q&A. The invitation link will be posted on Canvas. Sensitive information will be communicated via email (e.g., if you want to privately inquire about your grade).

## Schedule (tentative)


|       Date | Topic                                            | Out  | Due  |
| ---------: | ------------------------------------------------ | ---- | ---- |
| **Week 1** | **How to design a programming language?**        |      |      |
|      06/24 | Why study programming languages? + Python review | HW 1 |      |
|      06/25 | Syntax                                           |      |      |
|      06/26 | Inference rules                                  |      |      |
| **Week 2** | **What makes a programming language?**           |      |      |
|      07/01 | Semantics                                        | HW 2 |      |
|      07/02 | Names                                            |      | HW 1 |
|      07/03 | Types                                            |      |      |
| **Week 3** | **How to abstract *data*?**                      |      |      |
|      07/08 | Finite and recursive types                       | HW 3 |      |
|      07/09 | Pattern-matching                                 |      | HW 2 |
|      07/10 | *Quiz 1 (tentative)*                             |      |      |
| **Week 4** | **How to abstract *computation*?**               |      |      |
|      07/15 | Lambda calculus                                  | HW 4 |      |
|      07/16 | Polymorphism, type inference                     |      | HW 3 |
|      07/17 | Defunctionalization, continuation-passing        |      |      |
| **Week 5** | **How to change the world?**                     |      |      |
|      07/22 | Exceptions, abstract machines, effects           | HW 5 |      |
|      07/23 | Mutable states                                   |      | HW 4 |
|      07/24 | *Quiz 2 (tentative)*                             |      |      |
| **Week 6** | **What is the future of programming like?**      |      |      |
|      07/29 | TBD                                              |      |      |
|      07/30 | TBD                                              |      |      |
|      07/31 | TBD                                              |      |      |
|  **08/02** | **(End of summer session A)**                    |      | HW 5 |

<!-- |      07/29 | Curry-Howard correspondence                 |      |      |
|      07/30 | Codata, objects, subtyping, infinity        |      |      |
|      07/31 | It's lambda calculus all the way down!      |      |      | -->

## Textbooks and readings
The primary reference for this course is the lecture notes, which will be made available in the [Lecture Notes](./lecture-notes.md) section of this website. I will try to release the notes within 2-3 days after each lecture.

For additional reference, here're some of my personal favorite textbooks on programming languages, all of which are freely available online:
- [Types and Programming Languages](https://github.com/MPRI/M2-4-2/blob/master/Types%20and%20Programming%20Languages.pdf) by Benjamin C. Pierce
- [Practical Foundations for Programming Languages (2nd Ed)](https://web.archive.org/web/20221109205432/http://www.cs.cmu.edu/~rwh/pfpl/2nded.pdf) by Robert Harper
- [Programming Languages: Application and Interpretation (2nd Ed)](https://cs.brown.edu/courses/cs173/2012/book/) by Shriram Krishnamurthi
<!-- - Frank Pfenning's [lecture notes for 15-814](https://www.cs.cmu.edu/~fp/courses/15814-f21/schedule.html) at CMU -->

## Assessments and grading

Your grade will be determined by the following components:
- 5 homework assignments: 50%
  - includes a mix of written exercises and programming tasks
- 2 quizzes: 40%
  - held in class, no makeups except for formally documented emergencies
  - no quiz will be held during the last week of the session
- 2 reflections: 10%
  - more details in the [Reflections](#reflections) section below

We will using the following scale to determine your final letter grade. Note that:
- This is a tentative scale; the percentages may be *lowered* at the end of the session, but will not be raised, so you can always expect to get at least the letter grade corresponding to your percentage. 
- I have no incentive to enforce a normal, bell-shaped distribution of grades, so you can be assured that you will get the letter grade you deserve based on your *own* performance, not on how well your classmates do.

| Percentage | Letter Grade |
| ---------- | ------------ |
| 93% - 100% | A            |
| 90% - 92%  | A-           |
| 87% - 89%  | B+           |
| 83% - 86%  | B            |
| 80% - 82%  | B-           |
| 77% - 79%  | C+           |
| 73% - 76%  | C            |
| 70% - 72%  | C-           |
| 67% - 69%  | D+           |
| 63% - 66%  | D            |
| 60% - 62%  | D-           |
| 0% - 59%   | F            |

## Token system

You will receive tokens of my appreciation 💖 for giving me feedback on my teaching -- directly so by filling out surveys, or indirectly so by actively participating in class and coming to my office hours. You can redeem these tokens for *corrections on quizzes*. Each token allows you correct 1 point you lost on a quiz. There is no upper limit on the number of tokens you can earn. 

To redeem your tokens for quiz corrections, you will schedule an in-person meeting with me toward the end of the course, during which you will go over your original and corrected answers. More details will be provided later in the course.

Below is a tentative and non-exhaustive list of ways to earn tokens:
| Activity                                             | Tokens | Reset              |
| ---------------------------------------------------- | ------ | ------------------ |
| Filling out a survey                                 | 2 💖    | every survey       |
| Attending a lecture                                  | 1 💖    | every lecture      |
| Asking a question                                    | 1 💖    | every lecture half |
| Coming to Junrui's office hours                      | 2 💖    | every week         |
| Hidden events (explained when an event is triggered) | ??? 💖  | every event        |


## GenAI Policy
Unless otherwise specified, use of generative AI tools, including but not limited to chatbots (e.g., ChatGPT), coding assistants (e.g., Copilot), and coding agents (e.g., Cursor), is **not allowed** in this course.

Why?
- I want *you* to learn and think deeply about the materials.
   1. So that you become irreplaceable by AIs -- not training yet anthoer model for tech billionaires to replace the workers.
   2. The only way to gain muscle is to use that muscle. The only way to get good at an instrument is to practice. The only way to learn to speak a new language is to actually speak it. No learning occurs if the work doesn't happen *within you*.
- I respect your work, and I'd appreciate if you respect mine as well.
   1. I do not use AI to grade your work at all. If your work is AI generated, it's often easy to tell -- because a lot of the materials in this class are novel -- and I will be very sad to read something not from you. 
   2. I spent a lot of time designing and crafting this course. Although the materials may not be perfect, I'd greatly appreciate it if you respect my work by not feeding it as training data to some LLM. If something is not clear, please let me know, and I will do my best to make it better.
- Using those tools would be a [violation of UCSB's academic interity policy](https://studentconduct.sa.ucsb.edu/academic-integrity). I do not want to report anyone -- it will make everyone sad, not just me, but if that happens, I will have no choice but to follow the policy.
- On a more cheerful note, you won't ever need them, hopefully.
  1. You do not need to write any boilerplate code for this class. Every line of code you write matters, and is designed to check your understanding -- think of Gradescope autograder as a personalized TA vetted by me. The entirety of the interpreter + type checker you'll write for the entire class is fewer than 500 lines of code (at least in my own implementation). Spread over 5 assignments, that's about 100-200 LOC per week, which I hope is manageable.
  2. LLMs are ok with program syntax, and bad with program semantics, because they can't escape the Halting Problem! This course, however, is all about semantics and wreslting with the "undecidable". Even if you only use chatbots as "personalized tutors", they will likely give you non-sensical answers for questions related to language semantics (don't ask how I know this). So if you have questions, I'd highly encourage you to ask me, the TA, or your classmates instead. I and the TA will do our absolute best to help you understand everything taught in this class + get 100% on all assignments, if you're willing to put in the work. Come to office hours, ask questions in class and in Discord, and form study groups.
- Lastly, there is a reason, thousands of years after ancient Greece, the best way to teach and learn is still gathering in a room and talking to each other. LLMs are not a substitute for that. I'm here to learn from you as much as you are here to learn from me. I want to hear your thoughts, your questions, your ideas, and your struggles.

> **TL;DR.** I want you to learn and succeed. I'm here for exactly that and only that reason.


## Reflections

I will share a couple of Youtube videos each week on some aspect of programming languages -- either directly related to what we talked about that week, or some broader topic that might be interesting/important but unfortunately doesn't fit into the short time we have in class.

Out of 6 weeks, you pick 2 weeks to watch the videos and write a short (2-3 paragraphs) reflection on what you learned from the video, what surprised you, what you agreed/disagreed with, how does it change the way you think about programming languages, how does it relate to your own experience, etc.

Completion = full credit. No need to be a great writer. Just share your thoughts in a way that others can understand, be honest and be thoughtful. You're encouraged to share your reflections with the class and comment on other students' reflections, if you feel comfortable doing so.

Again, don't use LLMs. If you do, it'll defeat the purpose of reflections; I and other students will also waste time reading and commenting on some random string of emotionless symbols that doesn't come from *you*. If you're tempted to use LLMs, that likely means the week's topic doesn't interest you. In that case, you can skip it and do it in another week when the topic *does* genuinely interest you, since you only need to choose 2 weeks out of 6 anyway.




<!-- - 6 programming assignments, 50%
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
  - *turn in corrections for 50% credit back at the end of the session*
- "perspectives", 5%
  - LLM policy:
    - Do not use LLMs for these reflections. Think for yourself. -->




## Accessibility and accommodations
If you require any accommodations to fully participate in this course, please contact the [Disabled Students Program (DSP)](https://dsp.sa.ucsb.edu/). For exam accommodations, please submit requests at least 1 week before the quiz date, so that I can make the necessary arrangements.



<!-- 
## Pedagoy
- **Growth mindset**: ok to fail, but learn from it (that's why you'll get credit back if you turn in corrections). If you put in the work, you will get the grade you want.
- **Community, not competition** -> no curve to force a certain distribution of grades. Help each other out. Form study groups, come to office hours, ask lots of questions.
- Emphasize that **office hours are for everyone**, not just the struggling students. 
  - Extra credit or other incentives for attending office hours?
  - Feel free to come by and just chat about anything related to the course. There are absolutely no stupid questions. From my experience as a TA, I learn something new from every question asked and every student I talk to. Questions reveal not just gaps in understanding, but also gaps in my communication of the material, e.g., I was going too fast, or I was explaining something in a way that didn't make sense to the student. -->


<!-- 
## Difference with previous years

<details>
<summary>Click to expand</summary>

- Why not reuse existing materials?
  - I've TA'ed this course (which has recycled basically the same materials) for 4 years from 2022 to 2025. I have noticed that there remain a *lot* of things that could be improved to (1) make existing topics more accessible, (2) delete topics that are too theoretical and (3) reorient the course to be more relevant even after you graduate, no matter whether you become a programmer or a PL researcher. My overarching objective is to teach you the "PL way of thinking" that you still remember after 5 years.
  - Specially, I will try to teach the class in a way that I wish I had been taught when I first learned programming languages. I love PL deeply, and I want to share the beauty of the subject with you.
- The course is redesigned to be entirely **incremental**. The whole course culminates in your building a really powerful and elegant programming language step by step. Each lecture introduces a new feature into the language, and each assignment builds on the previous one. Previously, CS162 just gave you a fully complete language, and each assignment implements different aspects of the *full* language.
- Emphasis on the three roles of PL design process: motivating use case (client) -> relational design (designer) -> algorithmic implementation (implementer). Previously, CS162 just gave you a fully designed language and asked you to decipher a "god-given" design and write code to implement it. There weren't even use cases to motivate the design. This time, you will get a taste of all three roles of a language designer, and most importantly, you get to experiment with the design of the language yourself! How cool is that?
- Instead of a single final that's worth 50%, we have 3 quizzes spread out over the session (more immediate feedback), and you get 50% points back for corrections (it's ok to make mistakes; what matters is to learn from your own mistakes!).
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
</details> -->