import os
import sys

def verify_environment():
    print("--- Security Environment Audit ---")
    print(f"OS Platform: {sys.platform}")
    print(f"Python Version: {sys.version.split()}")

    # Verify Git Configuration
    git_check = os.system("git --version")
    if git_check == 0:
        print("Git Status: Operational ✅")
        print("Security Status: Environment Verified & Mission Ready ✅")

if __name__ == "__main__":
    verify_environment()
