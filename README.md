# makefun-news-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/jawaddevisser-coder/makefun-news-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/jawaddevisser-coder/makefun-news-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Sum up the world's news of Thursday 19 November 2026 in one image: a front page with the ICJ ruling that Myanmar committed genocide against the Rohingya, the first Trump-Xi-Putin summit in Shenzhen, Ukraine's third strike on the Crimean Bridge, Israeli tanks pushing into Gaza, Anthropic's record IPO, GTA 6 releasing, and the EU's €45 billion loan proposal for Ukraine.

The image is drawn by `draw_news.py` (Python + Pillow, deterministic, no network) into `entry.png` (1024x1024, under 1 MiB). `main.ts` (Node 22, standard library only) copies it to the grader's output path.

## Run it

```sh
python3 draw_news.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
