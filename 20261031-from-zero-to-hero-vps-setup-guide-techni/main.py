import psutil
def monitor_resource_usage():
  # Get current CPU and memory usage
  cpu_percent = psutil.cpu_percent()
  memory_percent = psutil.virtual_memory().percent
  print(f'CPU: {cpu_percent}%, Memory: {memory_percent}%')
monitor_resource_usage()
