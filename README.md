This code uses the psutil library to gather and print various system statistics, including CPU usage, virtual memory, network I/O, temperature, battery status, and disk usage

The psutil library (Python System and Process Utilities) is a cross-platform Python module used to retrieve information on system utilization (CPU, memory, disks, network, sensors, etc.) and running processes. It is widely used for system monitoring, profiling, and resource management in Python applications. Here’s a breakdown of its main features:

Key Functionalities of psutil:
CPU Information:
cpu_times(): Returns system CPU times as a named tuple (user time, system time, idle time, etc.).
cpu_percent(): Measures CPU usage as a percentage.
cpu_count(): Returns the number of logical or physical CPUs.
cpu_freq(): Fetches CPU frequency (MHz) for each core.

Memory Information:
virtual_memory(): Shows statistics on virtual memory (total, available, used, and free memory).
swap_memory(): Returns swap memory statistics.

Disk Information:
disk_partitions(): Lists disk partitions and their mount points.
disk_usage(): Displays total, used, and free disk space in bytes for a given disk partition.
disk_io_counters(): Provides statistics on read/write operations of physical disks.

Network Information:
net_io_counters(): Displays statistics on network I/O (bytes sent, received, packets sent, etc.).
net_connections(): Lists active network connections.
net_if_addrs(): Retrieves network interface addresses (IP, MAC, etc.).
net_if_stats(): Fetches network interface statistics like isup status and speed.

Sensors Information:
sensors_temperatures(): Returns temperatures of various system components (useful for monitoring hardware sensors).
sensors_fans(): Shows information about system fans.
sensors_battery(): Fetches the battery percentage, power plug status, and remaining time (on laptops).

Process Information:
Process(pid): Provides information on a specific process given its PID, including memory and CPU usage, open files, connections, and more.
process_iter(): Iterates over all running processes.

System-wide Information:
boot_time(): Returns the system boot time in seconds since the epoch.
users(): Returns information on currently logged-in users.
