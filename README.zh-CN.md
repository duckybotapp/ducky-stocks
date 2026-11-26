# 🦆 Ducky Stocks 美股小鸭子

[English](README.md)

查美股的高管交易、基金持仓和财经博主观点，用 Ducky 不用花钱。选一只股票，就能查到 SEC 申报原件，也能跳到博主视频里对应的那句话。

**[打开 Ducky 300 股票表](https://duckybot.app/zh/app/#/watchlist?scope=ducky&columns=all)** · **[拿英伟达试试](https://duckybot.app/zh/app/#/stock/NVDA)**

## 拿英伟达查三件事

| 想弄清什么 | 去哪儿看 |
| --- | --- |
| 基金上季度持有多少？ | Atreides Management 在 2026 年 11 月 16 日提交的 13F 披露的是 9 月 30 日的持仓。打开「基金持仓」，就能对照它前后两个季度持有的英伟达股数。[基金持仓](https://duckybot.app/zh/app/#/stock/NVDA?tab=funds) · [SEC 原始申报](https://www.sec.gov/Archives/edgar/data/1777813/000177781326000013/0001777813-26-000013-index.html) |
| 高管是哪天交易的？ | 英伟达高管 Timothy S. Teter 在 2026 年 11 月 23 日提交了 Form 4，里面有 11 月 19 日的交易。Ducky 在股价图上标出交易日，披露日可以回原件核对。[个股图表](https://duckybot.app/zh/app/#/stock/NVDA?tab=trail) · [Form 4 原件](https://www.sec.gov/Archives/edgar/data/1045810/000169684126000016/0001696841-26-000016-index.htm) |
| 博主当时怎么说的？ | 在「财经博主」里找到 Parkev Tatevosian 2026 年 11 月 25 日谈英伟达的记录，一点就从原视频第 23 秒开始播放。[博主观点](https://duckybot.app/zh/app/#/stock/NVDA?tab=creators) · [从 0:23 播放](https://www.youtube.com/watch?v=hOUk-GEHdM8&t=23s) |

OpenStock 能看九个市场，也能把行情终端装在自己的服务器上。它的英伟达公开页把图表和年报、季报放在一起。Ducky 的英伟达页还把高管交易、基金持仓和有出处的博主观点放在一起，方便你追查同一家公司的变化。[OpenStock 功能](https://openstock-ods.vercel.app/#inside) · [OpenStock 英伟达页](https://openstock-ods.vercel.app/s/NVDA)

## 哪些功能免费？

- **直接打开就能看。** 在 Ducky 300 里比较股票，也能点进个股预览。每个浏览器可预览 10 个不同的详情页。
- **免费注册就能保存。** 自选股、关注的财经博主、信号工坊里的提醒都跟着账号走，无需订阅或绑卡。
- **信号工坊也免费。** 比如选「日线 RSI 低于 30」，看看过去哪些股票符合，之后和同期 SPY 相比表现如何。历史结果是模拟值。想跟踪以后再出现的情况，可以单独开启提醒。[打开信号工坊](https://duckybot.app/zh/app/#/alerts) · [使用指南](https://duckybot.app/zh/signal-studio-guide/)

## 在电脑上查申报

用 Python 3 运行下面的示例，每次最多读三条公开记录，列出原始申报链接和本次查询的数据截止时间。这份公开披露档案延迟五天。

```sh
git clone https://github.com/duckybotapp/ducky-stocks.git
cd ducky-stocks
python3 examples/filings.py NVDA --kind insider
python3 examples/filings.py NVDA --kind 13f
```

把 `NVDA` 换成你关注的股票代码即可。示例只用 Python 标准库，联网就能运行，无需账号或 API 密钥。示例代码采用 MIT 许可证，研究服务由 Ducky 托管，原始资料按各来源的条款使用。[示例代码](examples/filings.py) · [许可证](LICENSE) · [Ducky 使用条款](https://duckybot.app/zh/terms/)

## 成为 Backer

如果小鸭子帮你省了翻申报、找视频的时间，可以请它喝杯咖啡，一次或每月都行。日常查资料、用信号工坊设提醒，免费账号就够了。[请小鸭子喝咖啡](https://buymeacoffee.com/duckybot)
