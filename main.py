from modules.scanner import run_scanner
from modules.bruteforce import run_ssh_bruteforce

def main():
    print("=== CODTECH PenTest Toolkit ===")
    print("1. Port Scanner")
    print("2. SSH Brute-Forcer")
    choice = input("\nSelect an option: ")

    if choice == '1':
        target = input("Enter target IP: ")
        ports = [21, 22, 80, 443, 3306] # Example common ports
        run_scanner(target, ports)
    elif choice == '2':
        target = input("Enter target IP: ")
        user = input("Enter username: ")
        wordlist = input("Enter path to wordlist.txt: ")
        run_ssh_bruteforce(target, user, wordlist)
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()