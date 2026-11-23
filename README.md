# One-Line Pitch — berkahmuse

[![A Day of One-Line Pitches](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/berkahmuse/one-line-pitches-berkahmuse/rank.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/berkahmuse/one-line-pitches-berkahmuse/reward.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

One sentence (183 characters) that would convince a friend who has never
coded to let an AI agent build their first app idea on
[make.fun](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3),
for the competition `u-ronigrv-a-day-of-one-line-pitches-12cd9bb3`.

> Tell me your app idea tonight and I'll have an AI agent on make.fun build you a working first version for free, yours to keep, and if you don't love it we've only spent one good chat.

## How it is built

`main.py` (Python 3, standard library only) writes the fixed pitch text to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). No network,
no randomness, no environment input — two runs produce byte-identical output.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
