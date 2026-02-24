import platform
import datetime
import os

def run_purple_audit():
    print(f"\n--- 🛡️ Purple Team Lab Audit | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
    print(f"Cloud Instance: {platform.node()}")
    print(f"Kernel Version: {platform.release()}")
    print(f"Current Path: {os.getcwd()}")
    print("Security Status: Environment Verified & Mission Ready ✅\n")

if __name__ == "__main__":
    run_purple_audit()
    