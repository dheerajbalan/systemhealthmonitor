
System Health Monitor

System Health Monitor is a Python tool that checks the health of your system by monitoring CPU usage, memory usage, disk usage, and the number of running processes. It logs this information and sends alerts if any of the usage metrics exceed predefined thresholds.
Features

 Monitors CPU usage, memory usage, disk usage, and process count.
 Logs information with timestamps.
 Sends alerts when usage metrics exceed the specified thresholds.

Requirements

    Python 3.6+
    psutil library

Installation

    Clone the repository:

    bash

	git clone https://github.com/yourusername/SystemHealthMonitor.git
	cd SystemHealthMonitor

Create a virtual environment and activate it:

bash

	python3 -m venv env
	source env/bin/activate  # On Windows use `env\Scripts\activate`

Install the required dependencies:

bash

    	pip install psutil

Usage

To run the System Health Monitor tool, use the following command:

bash

	python system_health_monitor.py

Thresholds

You can modify the threshold values in the script to customize the alert levels:

CPU_USAGE_THRESHOLD: CPU usage percentage threshold (default: 80%)
MEMORY_USAGE_THRESHOLD: Memory usage percentage threshold (default: 80%)
DISK_USAGE_THRESHOLD: Disk usage percentage threshold (default: 80%)
PROCESS_COUNT_THRESHOLD: Number of processes threshold (default: 300)

Example

Sample output when running the tool:

yaml

=====SYSTEM USAGE=====

CPU Usage: 75.5%
Memory Usage: 60.2%
Disk Usage: 70.3%
Process Count: 150

If any usage exceeds the threshold, you will see an alert message:

css

[!] Sending Alert!!!

Log File

The tool logs all the information in a file named system_health.log in the following format:

yaml

2023-07-21 10:00:00 Starting system health monitoring
2023-07-21 10:00:01 CPU Usage: 75.5%
2023-07-21 10:00:01 Memory Usage: 60.2%
2023-07-21 10:00:01 Disk Usage: 70.3%
2023-07-21 10:00:01 Process Count: 150

Contact

For any inquiries or issues, please contact dheerajbalan7@gmail.com.
