import psutil

def cpu_usage():
    return psutil.cpu_percent(interval= 1)

def ram_usage():
    ram = psutil.virtual_memory()
    available_memory = ram.available
    used_memory = ram.used
    return [available_memory, used_memory]

def bytes2gb(bytes):
    return round(bytes/1024/1024/1024, 1)