from collections import Counter
import os

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

# -------------------------
# Generate HTML Report
# -------------------------

os.makedirs("reports", exist_ok=True)

html = f"""
<!DOCTYPE html>
<html>
<head>
<title>DevOps Log Report</title>

<style>
body {{
    font-family: Arial;
    background: #f4f4f4;
    padding: 40px;
}}

.container {{
    background: white;
    padding: 30px;
    border-radius: 10px;
}}

h1 {{
    color: #2c3e50;
}}

table {{
    border-collapse: collapse;
    width: 50%;
}}

th, td {{
    border: 1px solid black;
    padding: 10px;
}}

th {{
    background: #3498db;
    color: white;
}}
</style>

</head>

<body>

<div class="container">

<h1>DevOps Log Analysis Report</h1>

<h2>Summary</h2>

<p><b>Total Logs:</b> {total_logs}</p>
<p><b>Total Errors:</b> {len(error_logs)}</p>

<h2>Error Summary</h2>

<table>
<tr>
<th>Error Type</th>
<th>Count</th>
</tr>
"""

for error, count in error_types.items():
    html += f"<tr><td>{error}</td><td>{count}</td></tr>"

html += """
</table>

<h2>Detected Errors</h2>
<ul>
"""

for err in error_logs:
    html += f"<li>{err}</li>"

html += """
</ul>

</div>

</body>
</html>
"""

with open("reports/report.html", "w") as file:
    file.write(html)

print("\nHTML report generated successfully!")