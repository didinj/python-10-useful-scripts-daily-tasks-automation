import psutil
from datetime import datetime

def system_report():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = (
        f"System Report ({report_time})\n"
        f"CPU Usage: {cpu}%\n"
        f"Memory Usage: {memory}%\n"
        f"Disk Usage: {disk}%\n"
    )
    with open("system_report.txt", "a") as f:
        f.write(report + "\n")
    print("💻 System report generated successfully!")

# Example usage
# system_report()
