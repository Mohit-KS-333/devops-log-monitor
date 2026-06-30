from collections import Counter

log_file = "logs/application.log"

keywords = ["ERROR", "FAILED", "EXCEPTION"]

total_logs = 0
error_logs = []
error_types = Counter()

with open(log_file, "r") as file:
    for line in file:
        total_logs += 1

        for keyword in keywords:
            if keyword in line:
                error_logs.append(line.strip())
                error_types[keyword] += 1

print("\n===== LOG ANALYSIS REPORT =====")
print(f"Total Logs: {total_logs}")
print(f"Total Errors: {len(error_logs)}")

print("\nError Summary:")
for error, count in error_types.items():
    print(f"{error}: {count}")

print("\nDetected Errors:")
for error in error_logs:
    print(error)
# Webhook Test