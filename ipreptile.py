import requests
import csv
import time

# === Banner and Author Info ===
print(r"""
  ___ _____            _     _   _ _      
 |_ _|_   _|__ _ __ __| |___| | | (_) |_ ___
  | |  | |/ _ \ '__/ _` / __| |_| | | __/ _ \
  | |  | |  __/ | | (_| \__ \  _  | | ||  __/
 |___| |_|\___|_|  \__,_|___/_| |_|_|\__\___|

           IPReptile - IP Reputation Tracker
""")

print("Author    : Maveera")
print("Created   : May 22, 2025")
print("Maintainer: Mavizz")
print("\n🔗 Connect with me:")
print("Webpage   : https://maveera.rf.gd/")
print("Instagram : https://www.instagram.com/_.mavi._27_/")
print("LinkedIn  : https://www.linkedin.com/in/maveera/")
print("GitHub    : https://github.com/Maveera/")
print("\nProcessing...\n")

# === Configuration ===
API_KEY = "717fd96580d0966084dde4440a66c417b9fd82d6bd55195271e72f0fe4e0bd0c41453d7b3b6ce1b7"  # Replace with your AbuseIPDB API key
INPUT = "unique_ips.csv"
OUTPUT = "reputation_results.csv"
DAYS = 90  # Check reports in last 90 days
THRESHOLD = 0  # Print to console if score > this

headers = {
    "Key": API_KEY,
    "Accept": "application/json"
}

# === Process the IPs ===
with open(INPUT) as infile, open(OUTPUT, "w", newline="") as outfile:
    reader = csv.reader(infile)
    next(reader)  # Skip header
    writer = csv.writer(outfile)
    writer.writerow(["IP", "Score", "Reports", "LastReported", "Usage", "ISP", "Country"])

    for row in reader:
        ip = row[0]
        url = "https://api.abuseipdb.com/api/v2/check"
        params = {
            "ipAddress": ip,
            "maxAgeInDays": DAYS,
            "verbose": ""
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()

            result = response.json()
            if 'data' in result:
                data = result['data']
                score = data.get("abuseConfidenceScore", 0)
                writer.writerow([
                    data.get("ipAddress", ""),
                    score,
                    data.get("totalReports", ""),
                    data.get("lastReportedAt", ""),
                    data.get("usageType", ""),
                    data.get("isp", ""),
                    data.get("countryName", "")
                ])

                if score > THRESHOLD:
                    print(f"[ALERT] IP: {ip} | Score: {score} | Reports: {data.get('totalReports', '')} | LastReported: {data.get('lastReportedAt', '')}")
            else:
                print(f"No data found for IP: {ip}")
                writer.writerow([ip, "No data", "", "", "", "", ""])
        except requests.exceptions.HTTPError as e:
            print(f"[HTTP ERROR] IP {ip}: {e}")
            writer.writerow([ip, "HTTP error", "", "", "", "", ""])
        except Exception as e:
            print(f"[ERROR] IP {ip}: {e}")
            writer.writerow([ip, "Error", "", "", "", "", ""])

        time.sleep(1)  # Respect API rate limits

# === Completion Message ===
print("\n✅ Process Completed. Please find the file: reputation_results.csv")
