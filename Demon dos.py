import time
import os
import sys

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def slow_banner(text, delay=0.002, color=RED):
    """Print ASCII art banner with animation"""
    for line in text.splitlines():
        for char in line:
            sys.stdout.write(color + char + RESET)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    print()

def welcome_banner():
    banner_text = r"""
         ____                                
        |  _ \  ___  _ __ ___   ___  _ __  
        | | | |/ _ \| '_ ` _ \ / _ \| '_ \ 
        | |_| | (_) | | | | | | (_) | | | |
        |____/ \___/|_| |_| |_|\___/|_| |_|
                                            
             ██████╗ ███████╗███╗   ███╗ ██████╗ ███╗   ██╗
            ██╔═══██╗██╔════╝████╗ ████║██╔═══██╗████╗  ██║
            ██║   ██║█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
            ██║   ██║██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
            ╚██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
             ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                   AUTHOR LIKING
                  
                      D E M O N   D O S
    """
    print("=" * 60)
    slow_banner(banner_text, delay=0.003, color=RED)
    print("=" * 60)
    time.sleep(0.5)
    flashing_warning(">>> SYSTEM BOOTED IN DEMON DOS MODE <<<", 3)

def slow_print(text, delay=0.05, color=GREEN):
    """Prints text letter by letter"""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def flashing_warning(text, times=5):
    """Flashes a warning text"""
    for _ in range(times):
        sys.stdout.write(YELLOW + text + RESET + "\r")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(" " * len(text) + "\r")
        sys.stdout.flush()
        time.sleep(0.3)
    print()

def fake_scan():
    slow_print("Scanning system files...", 0.05)
    for i in range(1, 11):
        slow_print(f"Found suspicious file: virus{i}.exe", 0.04, YELLOW)
        time.sleep(0.4)
    flashing_warning("!!! SYSTEM INFECTED !!!")
    slow_print("Deleting infected files...", 0.05, RED)
    for i in range(1, 11):
        slow_print(f"Deleted: virus{i}.exe", 0.04, RED)
        time.sleep(0.3)
    slow_print("Scan complete. System secure.", 0.05)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    welcome_banner()
    slow_print("Demon DOS [Version 2.1]", 0.04)
    slow_print('''⚠️ WARNING ⚠️  
Unauthorized access detected!  
Your system is now under DEMON DOS surveillance.  
Any attempt to shut down will result in data corruption.  
Proceed at your own risk... AND TYPE HELP TO SHOW THE COMMANDS
''', 0.04, YELLOW)

    while True:
        cmd = input(GREEN + "C:\\> " + RESET).strip().lower()
        
        if cmd == "help":
            slow_print("Available commands: HELP, SCAN, ABOUT, ATTACK, CLS, EXIT, SIGNUP", 0.03)
        
        elif cmd == "scan":
            fake_scan()
        
        elif cmd == "cls":
            os.system("cls" if os.name == "nt" else "clear")
            welcome_banner()
        
        elif cmd == "exit":
            slow_print("Shutting down...", 0.05, YELLOW)
            break
        
        elif cmd == "about":
            slow_print('''================= ABOUT DEMON DOS =================

DEMON DOS v2.0  
Created by: Liking

This program is a simulation of old-school DOS systems,  
mixed with a hacker-style prank environment.  

⚡ Features:
- Realistic DOS-like commands (HELP, SCAN, CLS, EXIT)  
- Fake virus scanner with warnings & alerts  
- Flashing text effects for maximum impact  
- Creepy DEMON DOS banner for hacker vibes  

⚠ Disclaimer:
This is NOT a real virus.  
It is only for FUN, PRANKS, and LEARNING purposes.  

===================================================
''', 0.03, RED)
        
        elif cmd == "attack":
            while True:
                slow_print("⚠ ATTACK ALERT: Your phone is hacked your bank account is EMPTY! ⚠", 0.04, RED)
        
        elif cmd == "signup":
            a = input(YELLOW + "ENTER YOUR EMAIL ID: " + RESET,)
            b = input(GREEN + "ENTER YOUR PASSWORD: " + RESET,)
            slow_print("Signup successful! (But totally fake 😆)", 0.04, YELLOW)
        
        else:
            slow_print(f"'{cmd}' is not recognized as an internal or external command.", 0.03, RED)

if __name__ == "__main__":
    main()
