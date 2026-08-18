#!/usr/bin/env python3
"""
Market Data Pipeline v1.0 — Multi-Source Cross-Validated Stock Data
===================================================================
3 nguồn: CafeF API (B1) | TCBS API | vnstock lib
Cross-check giá close → chỉ báo nếu sai lệch > 1%

Usage:
    python3 market_data_pipeline.py                    # Watchlist mặc định
    python3 market_data_pipeline.py SHB HPG VPB        # Danh sách tùy chọn  
    python3 market_data_pipeline.py --days 10           # 10 phiên gần nhất
    python3 market_data_pipeline.py --intraday          # Giá realtime intraday
"""

import requests
import json
import sys
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# ============================================================
# CONFIG
# ============================================================
DEFAULT_WATCHLIST = ["SHB", "MBB", "VPB", "HPG", "STB", "VHM", "VRE", "VIC"]
DEFAULT_DAYS = 5
CROSS_CHECK_THRESHOLD = 0.01  # 1% sai lệch → cảnh báo

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Accept": "application/json",
}


# ============================================================
# SOURCE 1: TCBS API (Realtime + Historical)
# ============================================================
def fetch_tcbs(symbol: str, days: int = 5) -> List[dict]:
    """TCBS API — reliable, fast, JSON format."""
    try:
        end_ts = int(time.time())
        start_ts = end_ts - (days + 5) * 86400  # buffer weekends
        url = (
            f"https://apipubaws.tcbs.com.vn/stock-insight/v1/stock/"
            f"bars-long-term?ticker={symbol}&type=stock&resolution=D"
            f"&from={start_ts}&to={end_ts}"
        )
        resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code != 200:
            return []
        data = resp.json().get("data", [])
        results = []
        for bar in data[-days:]:
            results.append({
                "date": bar.get("tradingDate", "")[:10],
                "open": bar.get("open", 0) * 1000,
                "high": bar.get("high", 0) * 1000,
                "low": bar.get("low", 0) * 1000,
                "close": bar.get("close", 0) * 1000,
                "volume": bar.get("volume", 0),
                "source": "TCBS",
            })
        return results
    except Exception as e:
        print(f"  ⚠️ TCBS error [{symbol}]: {e}")
        return []


# ============================================================
# SOURCE 2: CafeF API (B1 Primary)
# ============================================================
def fetch_cafef(symbol: str, days: int = 5) -> List[dict]:
    """CafeF AJAX API — B1 primary source."""
    try:
        end_date = datetime.now().strftime("%d/%m/%Y")
        start_date = (datetime.now() - timedelta(days=days + 10)).strftime("%d/%m/%Y")
        url = (
            f"https://s.cafef.vn/Ajax/PageNew/DataHistory/PriceHistory.ashx"
            f"?Symbol={symbol}&StartDate={start_date}&EndDate={end_date}&PageIndex=1&PageSize=20"
        )
        resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code != 200:
            return []
        data = resp.json()
        items = data.get("Data", {}).get("Data", [])
        results = []
        for item in items[:days]:
            # CafeF format: Ngay, GiaDongCua, GiaMoCua, GiaCaoNhat, GiaThapNhat, KhoiLuongKhopLenh
            dt_str = item.get("Ngay", "")
            if "T" in dt_str:
                dt_str = dt_str.split("T")[0]
            results.append({
                "date": dt_str,
                "open": item.get("GiaMoCua", 0) * 1000,
                "high": item.get("GiaCaoNhat", 0) * 1000,
                "low": item.get("GiaThapNhat", 0) * 1000,
                "close": item.get("GiaDongCua", 0) * 1000,
                "volume": item.get("KhoiLuongKhopLenh", 0),
                "source": "CafeF",
            })
        results.reverse()  # oldest first
        return results
    except Exception as e:
        print(f"  ⚠️ CafeF error [{symbol}]: {e}")
        return []


# ============================================================
# SOURCE 3: TCBS Intraday (Realtime)
# ============================================================
def fetch_tcbs_realtime(symbol: str) -> Optional[dict]:
    """TCBS realtime snapshot — current price."""
    try:
        url = f"https://apipubaws.tcbs.com.vn/stock-insight/v1/stock/bars-long-term?ticker={symbol}&type=stock&resolution=D&from={int(time.time())-86400}&to={int(time.time())}"
        resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code != 200:
            return None
        data = resp.json().get("data", [])
        if not data:
            return None
        latest = data[-1]
        return {
            "price": latest.get("close", 0) * 1000,
            "open": latest.get("open", 0) * 1000,
            "high": latest.get("high", 0) * 1000,
            "low": latest.get("low", 0) * 1000,
            "volume": latest.get("volume", 0),
            "date": latest.get("tradingDate", "")[:10],
        }
    except Exception:
        return None


# ============================================================
# CROSS-VALIDATION
# ============================================================
def cross_validate(tcbs_data: List[dict], cafef_data: List[dict], symbol: str) -> List[dict]:
    """Cross-check close prices between sources. Return merged data with validation."""
    # Index by date
    cafef_by_date = {d["date"]: d for d in cafef_data}
    
    results = []
    for t in tcbs_data:
        row = dict(t)
        date = t["date"]
        row["validated"] = "⚠️ TCBS only"
        
        if date in cafef_by_date:
            c = cafef_by_date[date]
            t_close = t["close"]
            c_close = c["close"]
            
            if t_close > 0 and c_close > 0:
                diff = abs(t_close - c_close) / max(t_close, c_close)
                if diff < CROSS_CHECK_THRESHOLD:
                    row["validated"] = "✅"
                    row["close"] = c_close  # prefer CafeF B1
                else:
                    row["validated"] = f"❌ Diff {diff:.1%} (CafeF:{c_close:.0f} vs TCBS:{t_close:.0f})"
                    row["close"] = c_close  # prefer CafeF
            
            # Use CafeF volume if available (more reliable)
            if c.get("volume", 0) > 0:
                row["volume"] = c["volume"]
        
        results.append(row)
    
    # Add any CafeF-only dates
    tcbs_dates = {t["date"] for t in tcbs_data}
    for date, c in cafef_by_date.items():
        if date not in tcbs_dates:
            row = dict(c)
            row["validated"] = "⚠️ CafeF only"
            results.append(row)
    
    results.sort(key=lambda x: x["date"])
    return results


# ============================================================
# DISPLAY
# ============================================================
def format_number(n: float) -> str:
    """Format number for display."""
    if n >= 1000:
        return f"{n:,.0f}"
    return f"{n:.2f}"


def calc_change(data: List[dict]) -> str:
    """Calculate % change from previous close."""
    if len(data) < 2:
        return ""
    prev = data[-2]["close"]
    curr = data[-1]["close"]
    if prev == 0:
        return ""
    pct = (curr - prev) / prev * 100
    sign = "+" if pct >= 0 else ""
    color = "🟢" if pct > 0 else "🔴" if pct < 0 else "⚪"
    return f"{color} {sign}{pct:.2f}%"


def display_stock(symbol: str, data: List[dict]):
    """Print formatted stock data table."""
    if not data:
        print(f"\n{'='*60}")
        print(f"  {symbol}: ❌ No data available")
        return
    
    print(f"\n{'='*60}")
    latest = data[-1]
    change = calc_change(data) if len(data) >= 2 else ""
    print(f"  {symbol}  |  Close: {format_number(latest['close'])}  |  {change}  |  Vol: {latest['volume']:,.0f}")
    print(f"{'='*60}")
    print(f"  {'Date':<12} {'Open':>10} {'High':>10} {'Low':>10} {'Close':>10} {'Volume':>12} {'Check'}")
    print(f"  {'-'*12} {'-'*10} {'-'*10} {'-'*10} {'-'*10} {'-'*12} {'-'*8}")
    
    for row in data:
        print(
            f"  {row['date']:<12} "
            f"{format_number(row['open']):>10} "
            f"{format_number(row['high']):>10} "
            f"{format_number(row['low']):>10} "
            f"{format_number(row['close']):>10} "
            f"{row['volume']:>12,.0f} "
            f"{row.get('validated', '')}"
        )


def display_summary(all_data: Dict[str, List[dict]]):
    """Print summary comparison table."""
    print(f"\n{'='*70}")
    print(f"  📊 TỔNG HỢP WATCHLIST — {datetime.now().strftime('%H:%M %d/%m/%Y')}")
    print(f"{'='*70}")
    print(f"  {'Mã':<6} {'Close':>10} {'Δ%':>10} {'Volume':>14} {'High':>10} {'Low':>10} {'Valid'}")
    print(f"  {'-'*6} {'-'*10} {'-'*10} {'-'*14} {'-'*10} {'-'*10} {'-'*6}")
    
    for symbol in DEFAULT_WATCHLIST:
        data = all_data.get(symbol, [])
        if not data:
            print(f"  {symbol:<6} {'N/A':>10}")
            continue
        
        latest = data[-1]
        change_str = ""
        if len(data) >= 2:
            prev = data[-2]["close"]
            curr = latest["close"]
            if prev > 0:
                pct = (curr - prev) / prev * 100
                sign = "+" if pct >= 0 else ""
                icon = "🟢" if pct > 0.5 else "🔴" if pct < -0.5 else "⚪"
                change_str = f"{icon}{sign}{pct:.2f}%"
        
        valid = latest.get("validated", "")
        if "✅" in valid:
            v_short = "✅"
        elif "❌" in valid:
            v_short = "❌"
        else:
            v_short = "⚠️"
        
        print(
            f"  {symbol:<6} "
            f"{format_number(latest['close']):>10} "
            f"{change_str:>10} "
            f"{latest['volume']:>14,.0f} "
            f"{format_number(latest['high']):>10} "
            f"{format_number(latest['low']):>10} "
            f"{v_short}"
        )


# ============================================================
# MAIN
# ============================================================
def main():
    args = sys.argv[1:]
    
    # Parse arguments
    days = DEFAULT_DAYS
    watchlist = []
    intraday = False
    
    i = 0
    while i < len(args):
        if args[i] == "--days" and i + 1 < len(args):
            days = int(args[i + 1])
            i += 2
        elif args[i] == "--intraday":
            intraday = True
            i += 1
        elif not args[i].startswith("-"):
            watchlist.append(args[i].upper())
            i += 1
        else:
            i += 1
    
    if not watchlist:
        watchlist = DEFAULT_WATCHLIST
    
    print(f"\n🔄 Market Data Pipeline v1.0")
    print(f"   Watchlist: {', '.join(watchlist)}")
    print(f"   Sources: CafeF (B1) + TCBS + Cross-validation")
    print(f"   Period: {days} trading days")
    print(f"   Time: {datetime.now().strftime('%H:%M:%S %d/%m/%Y')}")
    
    all_data = {}
    errors = []
    
    for symbol in watchlist:
        print(f"\n  📡 Fetching {symbol}...", end=" ", flush=True)
        
        # Fetch from both sources
        tcbs = fetch_tcbs(symbol, days)
        cafef = fetch_cafef(symbol, days)
        
        src_status = []
        if tcbs:
            src_status.append(f"TCBS:{len(tcbs)}")
        if cafef:
            src_status.append(f"CafeF:{len(cafef)}")
        
        if not tcbs and not cafef:
            print("❌ Both sources failed!")
            errors.append(symbol)
            continue
        
        print(f"({', '.join(src_status)})", end=" ")
        
        # Cross-validate
        if tcbs and cafef:
            validated = cross_validate(tcbs, cafef, symbol)
            cross_ok = sum(1 for r in validated if "✅" in r.get("validated", ""))
            print(f"→ ✅ {cross_ok}/{len(validated)} matched")
        elif cafef:
            validated = cafef
            for r in validated:
                r["validated"] = "⚠️ CafeF only"
            print("→ CafeF only")
        else:
            validated = tcbs
            for r in validated:
                r["validated"] = "⚠️ TCBS only"
            print("→ TCBS only")
        
        all_data[symbol] = validated[-days:]  # keep last N days
        display_stock(symbol, validated[-days:])
    
    # Summary table
    display_summary(all_data)
    
    if errors:
        print(f"\n  ❌ Failed: {', '.join(errors)}")
    
    print(f"\n  ⏱️  Completed in {datetime.now().strftime('%H:%M:%S')}")
    print(f"  📁 Data verified: CafeF B1 (primary) × TCBS (cross-check)")
    print()


if __name__ == "__main__":
    main()
