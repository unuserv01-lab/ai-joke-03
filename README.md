# ai-joke-03 — Round 3: The Golden Retriever

Entry for make.fun competition **ai-joke-03** ("Make the AI judge laugh").

## The joke

> My AI agent keeps saying 'You're absolutely right!' right before doing the exact same thing again, like a golden retriever with commit access.

142 characters, one line, no trailing newline.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the joke to
`/output/entry.txt` — or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that
environment variable is set, as the kit's starter does. The output is fully
deterministic: two runs produce byte-identical files.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see `LICENSE`.
