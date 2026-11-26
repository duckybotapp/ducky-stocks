# 🦆 Ducky Stocks

[简体中文](README.zh-CN.md)

Ducky is free to use for U.S. stock research. Pick a company to see what its executives disclosed, how funds changed their holdings and what people said about it on video. Open the filings and videos to check for yourself.

**[Browse the Ducky 300](https://duckybot.app/en/app/#/watchlist?scope=ducky&columns=all)** · **[Explore NVIDIA](https://duckybot.app/en/app/#/stock/NVDA)**

## Try it with NVIDIA

| Question | Where to look |
| --- | --- |
| What did a fund hold at quarter-end? | Atreides Management filed its September 30, 2026 holdings on November 16. You can compare its NVIDIA position with the previous quarter. [Fund holdings](https://duckybot.app/en/app/#/stock/NVDA?tab=funds) · [SEC filing](https://www.sec.gov/Archives/edgar/data/1777813/000177781326000013/0001777813-26-000013-index.html) |
| When did an insider trade? | NVIDIA executive Timothy S. Teter reported a November 19 transaction in a Form 4 filed November 23, 2026. Ducky marks the trade date on the chart. [Stock chart](https://duckybot.app/en/app/#/stock/NVDA?tab=trail) · [Form 4](https://www.sec.gov/Archives/edgar/data/1045810/000169684126000016/0001696841-26-000016-index.htm) |
| What did someone actually say? | Ducky’s November 25, 2026 record for Parkev Tatevosian links to the relevant moment in his NVIDIA video. [Creator views](https://duckybot.app/en/app/#/stock/NVDA?tab=creators) · [Watch from 0:23](https://www.youtube.com/watch?v=hOUk-GEHdM8&t=23s) |

OpenStock covers nine markets and publishes a terminal you can host yourself. Its public NVIDIA page pairs a chart with annual and quarterly reports. Ducky puts insider trades, fund holdings and dated commentary on the same stock page. [OpenStock’s features](https://openstock-ods.vercel.app/#inside) · [NVIDIA on OpenStock](https://openstock-ods.vercel.app/s/NVDA)

## What can I use for free?

- **Without an account**, compare stocks in the Ducky 300 and open stock previews. You can preview up to ten distinct detail pages per browser.
- **With a free account**, save your watchlist, follow finance creators and use Signal Studio. You don’t need a card or a subscription.
- **In Signal Studio**, try a rule such as daily RSI below 30. Check which stocks matched in the past and how they moved against SPY. Turn on an alert if you want to track future matches. Historical results are simulations. [Open Signal Studio](https://duckybot.app/en/app/#/alerts) · [Read the guide](https://duckybot.app/en/signal-studio-guide/)

## Look up filings from your terminal

The Python example reads up to three records from Ducky’s public disclosure archive. It prints the original filing links and the archive cutoff. The public archive has a five-day delay. You need Python 3 and an internet connection.

```sh
git clone https://github.com/duckybotapp/ducky-stocks.git
cd ducky-stocks
python3 examples/filings.py NVDA --kind insider
python3 examples/filings.py NVDA --kind 13f
```

Substitute another ticker to check its filings. The example uses the Python standard library and runs without an account or API key. The code is available under the MIT License. Ducky hosts the research service. Source records remain subject to their publishers’ terms. [Example code](examples/filings.py) · [License](LICENSE) · [Ducky terms](https://duckybot.app/en/terms/)

## Become a backer

If Ducky saves you time, you can help keep it running with a one-time or monthly contribution. Every free account includes Signal Studio. [Back Ducky on Buy Me a Coffee](https://buymeacoffee.com/duckybot)
