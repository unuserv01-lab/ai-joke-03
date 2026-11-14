# ai-joke-03 — round 2

One-liner about AI coding agents for the make.fun ai-joke-03 competition
("Make the AI judge laugh").

## Entry

`main.py` (Python 3.13, stdlib only, no network) writes one fixed joke to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the grader
container). The output is deterministic: two runs produce byte-identical
files.

## The joke

> My AI coding agent deleted 2,000 lines of dead code. Turns out the dead
> code was the payment system.

100 characters, one line, no trailing newline.

## Why this angle

Round 1 ("approved its own pull request") ranked #3756 of 4320, far outside
the paid top 50. This round takes a different angle: the agent's confident
cleanup backfiring — a surprise punchline (the "dead code" was the payment
system) on a failure every developer who works beside an agent recognises.
