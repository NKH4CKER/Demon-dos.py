import time
import os
import sys

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def fake_scan():
    slow_print("Scanning system files...", 0.05)
    time.sleep(1)
    slow_print("C:\\> Checking boot sector... OK")
    time.sleep(0.5)
    slow_print("C:\\> Checking Windows directory... INFECTED!")
    time.sleep(0.5)
    slow_print("C:\\> Removing files...")
    for i in range(1, 11):
        slow_print(f"Deleting file {i}/10", 0.05)
        time.sleep(0.3)
    slow_print("System cleaning complete!")
    time.sleep(0.5)
    slow_print("WARNING: System unstable! 😈")

def main():
    os.system("clear" if os.name == "posix" else "cls")
    slow_print("Microsoft Windows [Version 10.0.19045.3324]")
    slow_print("(c) Microsoft Corporation. All rights reserved.\n")

    while True:
        cmd = input("C:\\> ").strip().lower()
        
        if cmd == "help":
            print("Commands: help, scan, cls, about, exit")
        elif cmd == "scan":
            fake_scan()
        elif cmd == "cls":
            os.system("clear" if os.name == "posix" else "cls")
        elif cmd == "about":
            print("Fake DOS Virus Simulator v1.0 - Safe for fun!")
        elif cmd in ("exit", "quit", "q"):
            slow_print("Shutting down...", 0.05)
            time.sleep(1)
            sys.exit()
        else:
            print(f"'{cmd}' is not recognized as an internal or external command.")

if __name__ == "__main__":
    main()
