import psutil

# CPU Usage per core
cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
cpu_freq = psutil.cpu_freq(percpu=True)

print("CPU Usage per core:")
for i, (percent, freq) in enumerate(zip(cpu_percent, cpu_freq), start=1):
    print(f"Core {i}: {percent}% Frequency: {freq.current} MHz")

virtual_mem = psutil.virtual_memory()
swap = psutil.swap_memory()

print("\nVirtual Memory:")
print(f"Total: {virtual_mem.total / (1024 ** 3):.2f} GB")
print(f"Used: {virtual_mem.used / (1024 ** 3):.2f} GB")
print(f"Swap Total: {swap.total / (1024 ** 3):.2f} GB")
print(f"Swap Used: {swap.used / (1024 ** 3):.2f} GB")

print("\nNetwork Information:")
network = psutil.net_io_counters()
print(f"Bytes received: {network.bytes_recv}")
print(f"Bytes sent: {network.bytes_sent}")

try:
    temperatures = psutil.sensors_temperatures()
    if temperatures:
        print("\nTemperatures:")
        for name, entries in temperatures.items():
            for entry in entries:
                print(f"{name}: {entry.current}°C")
except Exception as e:
    print("\nTemperature information unavailable.")

# Battery information (if it's a laptop)
battery = psutil.sensors_battery()
if battery:
    plugged = "Plugged in" if battery.power_plugged else "Not Plugged"
    print(f"\nBattery Status: {plugged}, {battery.percent}%")
else:
    print("\nBattery information unavailable.")

disk = psutil.disk_usage('/')
print("\nDisk Information:")
print(f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB")
print(f"Used Disk Space: {disk.used / (1024 ** 3):.2f} GB")
print(f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")
