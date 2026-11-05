import os
import time
import random

# --- TERMINAL COLORS ---
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

def print_banner():
    os.system('clear')
    print(f"""{RED}
    ==================================================================
      ______  _____ __  __ ____  ______  _____  ______ 
     |__  __||  __ \\\\ \\/ /|  _ \\|  ____||  __ \\|____  |
        | |  | |__) |\\  / | |_) | |__   | |__) |   / / 
        | |  |  ___/  \\/  |  _ <|  __|  |  _  /   / /  
        | |  | |      | | | |_) | |____ | | \\ \\  / /   
        |_|  |_|      |_| |____/|______||_|  \\_\\/_/    
                                                       
           [ TINY & RAINY : THE DUAL SENTINELS (DEMO) ]
    ==================================================================
    {CYAN}"At your service, Master. Tiny watches the front. 
    Rainy guards the back. Hackers will be executed."{RESET}
    """)

def simulate_tiny():
    """Simulates Tiny blocking a brute-force attack"""
    fake_ip = f"{random.randint(11,200)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    print(f"\n{YELLOW}[TINY]{RESET} Front-door breach attempt detected from {fake_ip}!")
    time.sleep(1)
    print(f"{YELLOW}[TINY - FRONT DOOR]{RESET} Deflecting attack! IP {RED}{fake_ip}{RESET} has been ruthlessly executed and dropped.")

def simulate_rainy():
    """Simulates Rainy killing a backdoor process"""
    fake_port = random.choice(["4444", "1337", "4433", "9999"])
    fake_pid = random.randint(1000, 9999)
    print(f"\n{MAGENTA}[RAINY]{RESET} Back-door anomaly found! Unauthorized port {fake_port} is open.")
    time.sleep(1)
    print(f"{MAGENTA}[RAINY]{RESET} Target locked on Process ID: {RED}{fake_pid}{RESET}. Executing slaughter protocol...")
    time.sleep(0.5)
    print(f"{MAGENTA}[RAINY]{RESET} Process {fake_pid} eradicated. Back-door sealed. Area is secure.")

def main():
    print_banner()
    print(f"{GREEN}[SYSTEM] Tiny & Rainy are now actively patrolling your server... (SIMULATION MODE){RESET}\n")

    try:
        while True:
            # Randomly choose whether Tiny or Rainy finds an intruder
            event = random.choice(['tiny', 'rainy', 'clear', 'clear'])
            
            if event == 'tiny':
                simulate_tiny()
            elif event == 'rainy':
                simulate_rainy()
            else:
                print(f"{GREEN}[SYSTEM]{RESET} Area secure. No threats detected...")
            
            time.sleep(3) # Wait 3 seconds before next scan
    except KeyboardInterrupt:
        print(f"\n{CYAN}[SYSTEM]{RESET} Master has deactivated the Sentinels. Shutting down gracefully.")
        exit(0)

if __name__ == "__main__":
    main()