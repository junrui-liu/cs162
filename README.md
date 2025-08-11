# Course Website for CS 162 - Programming Languages (Summer 2025)

## Pre-requisites

- `rust`
- [`mdbook`](https://rust-lang.github.io/mdBook/)
- [`mdbook-katex`](https://github.com/lzanini/mdbook-katex)

## Instructions

- To write or edit content, modify the files in the `src/` directory.
- To build, run `mdbook build`.
- To test, run `mdbook serve --open &`.
- To commit changes, first run `mdbook build` to ensure the book is up-to-date, then commit the changes in the `src/` directory, since the GitHub actions only serve the static files in the `book/` directory.