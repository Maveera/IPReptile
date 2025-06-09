# IPReptile

# 🛡️ IPReptile - IP Reputation Tracker

**IPReptile** is a passive IP reputation checker tool powered by [AbuseIPDB](https://www.abuseipdb.com/).  


Easily evaluate IPs against abuse score, last reported time, total abuse reports, and more.

---

## 🔧 Features

- Bulk IP abuse checking (CSV input/output)
- Realtime abuse score via AbuseIPDB API
- Prints IPs above defined abuse threshold
- Rate-limit safe with delay
- Clean, readable output CSV

---

## 📂 File Structure

- `ipreptile.py` – Main script
- `unique_ips.csv` – Input list of IPs (`IP Address` as header)
- `reputation_results.csv` – Output file with reputation data

---

## 🚀 How to Use

1. Replace the `API_KEY` inside `ipreptile.py` with your [AbuseIPDB](https://www.abuseipdb.com/account/api) key.
2. Prepare `unique_ips.csv`:

