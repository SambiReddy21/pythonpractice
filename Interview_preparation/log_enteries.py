log_entries = [
    "2025-04-03 12:34:56 ERROR Device failure detected server A",
    "2025-04-02 10:15:30 INFO System rebooted server B",
    "2025-04-03 14:22:10 ERROR Connection timeout host A",
    "2025-04-01 09:00:05 WARN High CPU usage server C"
]

target_date = "2025-04-03"

for log in log_entries:
    if log.startswith(target_date):
        print(log)