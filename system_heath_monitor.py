import psutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Thresholds
CPU_USAGE_THRESHOLD = 80  # in percent
MEMORY_USAGE_THRESHOLD = 80  # in percent
DISK_USAGE_THRESHOLD = 80  # in percent
PROCESS_COUNT_THRESHOLD = 300  # number of processes

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_USAGE_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
        print("[!] Sending Alert!!!")
    return cpu_usage

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_USAGE_THRESHOLD:
        logging.warning(f'High memory usage detected: {memory_usage}%')
        print("[!] Sending Alert!!!")
    return memory_usage

def check_disk_usage():
    disk_usage = psutil.disk_usage('/')
    disk_usage_percent = disk_usage.percent
    if disk_usage_percent > DISK_USAGE_THRESHOLD:
        logging.warning(f'High disk usage detected: {disk_usage_percent}%')
        print("[!] Sending Alert!!!")
    return disk_usage_percent

def check_process_count():
    process_count = len(psutil.pids())
    if process_count > PROCESS_COUNT_THRESHOLD:
        logging.warning(f'High number of processes detected: {process_count}')
        print("[!] Sending Alert!!!")
    return process_count

def main():
    logging.info('Starting system health monitoring')
    cpu_usage = check_cpu_usage()
    memory_usage = check_memory_usage()
    disk_usage = check_disk_usage()
    process_count = check_process_count()

    logging.info(f'CPU Usage: {cpu_usage}%')
    logging.info(f'Memory Usage: {memory_usage}%')
    logging.info(f'Disk Usage: {disk_usage}%')
    logging.info(f'Process Count: {process_count}')

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage}%")
    print(f"Process Count: {process_count}")

if __name__ == "__main__":
    print("\n")
    print("=====SYSTEM USEAGE===== \n")
    main()