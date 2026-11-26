"""Show source links and dates for one stock from Ducky's public filings archive."""

import argparse
import json
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ARCHIVE = "https://api.duckybot.app/public/radar/archive.json"


def show_filing(row, kind):
    facts = (row.get("extra") or {}).get("facts") or {}
    if kind == "13f":
        fund = (row.get("filer") or {}).get("name") or row.get("reporter_name")
        print(f"\nFund: {fund or 'unavailable'}")
        print(f"  Quarter ended: {facts.get('report_period') or 'unavailable'}")
    else:
        owner = (row.get("reporter") or {}).get("name") or row.get("reporter_name")
        transactions = facts.get("transactions") or []
        dates = sorted({trade["date"] for trade in transactions if trade.get("date")})
        print(f"\nReporting owner: {owner or 'unavailable'}")
        print(f"  Transaction dates: {', '.join(dates) or 'unavailable'}")
        print(f"  SEC accepted: {facts.get('accepted_at') or 'unavailable'}")
    print(f"  Filing: {row.get('source_url') or 'link unavailable'}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ticker", help="Stock symbol, for example NVDA or BRK.B")
    parser.add_argument("--kind", choices=("insider", "13f"), default="insider")
    args = parser.parse_args()
    ticker = args.ticker.strip().upper()
    if not re.fullmatch(r"[A-Z][A-Z0-9.-]{0,9}", ticker):
        parser.error("Enter a stock symbol such as NVDA or BRK.B.")

    query = urlencode({"ticker": ticker, "kind": args.kind, "limit": 3})
    request = Request(f"{ARCHIVE}?{query}", headers={"Accept": "application/json"})
    try:
        with urlopen(request, timeout=20) as response:
            document = json.load(response)
    except HTTPError as error:
        raise SystemExit(f"Ducky could not serve the request (HTTP {error.code}).") from None
    except (URLError, OSError, ValueError) as error:
        raise SystemExit(f"Could not read the public archive: {error}") from None

    if not isinstance(document, dict) or not isinstance(document.get("items"), list):
        raise SystemExit("The public archive returned an unexpected response.")
    access = document.get("access") or {}
    print(f"{ticker} | {args.kind} | public disclosure archive")
    print(f"  Records available before: {access.get('available_before') or 'unavailable'}")
    if not document["items"]:
        print("No matching records in this public archive.")
    for row in document["items"]:
        show_filing(row, args.kind)


if __name__ == "__main__":
    main()
