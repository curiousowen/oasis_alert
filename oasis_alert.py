import ctypes
import time
import random
import string
import threading
import os
import socket


HKEY_CURRENT_USER = 0x80000001
KEY_WRITE = 0x20006


advapi32 = ctypes.windll.advapi32

def random_string(length):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Failed Login Attempts Simulation
def simulate_failed_logins():
    """Simulate failed login attempts."""
    while True:
        random_user = random_string(8)
        random_password = random_string(10)
        # This simulates failed login attempts by calling a fake function
        # Actual authentication attempts aren't made, but SOC tools often monitor account access logs
        print(f"Simulating failed login for user: {random_user}, password: {random_password}")
        time.sleep(random.uniform(0.5, 3))  # Random interval to simulate human behavior


def modify_files():
    """Simulate file modifications to trigger file integrity monitoring alerts."""
    while True:
        filename = f"C:\\temp\\important_file_{random_string(6)}.txt"
        with open(filename, "w") as f:
            f.write(random_string(100))
        print(f"Modified file: {filename}")
        time.sleep(random.uniform(0.1, 1))  # Small delays to avoid CPU overload


def simulate_port_scanning():
    """Simulate a network scan by attempting to connect to random ports."""
    while True:
        target_ip = "127.0.0.1"  # Scanning localhost to simulate activity
        target_port = random.randint(1, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        try:
            sock.connect((target_ip, target_port))
            print(f"Port {target_port} is open")
        except:
            pass  # Ignore closed ports
        finally:
            sock.close()
        time.sleep(random.uniform(0.05, 0.5))  # Speed can be adjusted


def simulate_command_execution():
    """Simulate the execution of system commands to trigger SOC alerts."""
    commands = ["whoami", "ipconfig", "netstat", "tasklist", "dir C:\\Windows\\System32"]
    while True:
        command = random.choice(commands)
        os.system(command)
        print(f"Executed command: {command}")
        time.sleep(random.uniform(1, 3))  # Random delay between commands


def modify_registry():
    """Simulate registry changes to trigger alerts for persistence mechanisms."""
    while True:
        hKey = ctypes.c_void_p()
        subkey = f"Software\\Simulated_{random_string(6)}"
        advapi32.RegCreateKeyExW(
            HKEY_CURRENT_USER, subkey, 0, None, 0, KEY_WRITE, None, ctypes.byref(hKey), None
        )
        advapi32.RegSetValueExW(hKey, "SimulatedValue", 0, 1, ctypes.c_wchar_p("RandomData"), 20)
        advapi32.RegCloseKey(hKey)
        print(f"Modified registry key: {subkey}")
        time.sleep(random.uniform(0.5, 2))  # Randomize frequency of registry changes


def oasis_alert():
    """Start all the alert fatigue simulations in separate threads."""
    threads = [
        threading.Thread(target=simulate_failed_logins),
        threading.Thread(target=modify_files),
        threading.Thread(target=simulate_port_scanning),
        threading.Thread(target=simulate_command_execution),
        threading.Thread(target=modify_registry)
    ]
    
   
    for thread in threads:
        thread.start()
    

    for thread in threads:
        thread.join()

if __name__ == "__main__":
  oasis_alert()
