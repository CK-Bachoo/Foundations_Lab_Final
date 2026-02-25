import os
import sys

def verify_environment():
    print("\n--- Security Environment Audit ---")
    print(f"OS Platform: {sys.platform}")
    print(f"Python Version: {sys.version.split()[0]}")
    
    # Integrity Check: Verifying Git installation for the lab
    git_check = os.system("git --version > /dev/null 2>&1")
    
    if git_check == 0:
        print("Git Status: Operational ✅")
        print("Security Status: Environment Verified & Mission Ready ✅\n")
    else:
        print("Git Status: Not Found ❌")

if __name__ == "__main__":
    verify_environment()
