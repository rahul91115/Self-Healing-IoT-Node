import subprocess
import os
import sys
import time

def run_test():
    print("--- Starting Automated Firmware Test ---")
    
    # 1. Get the Absolute Path (Fixes Windows/Linux slash issues)
    firmware_path = ""
    for root, dirs, files in os.walk(".pio/build"):
        if "firmware.bin" in files:
            firmware_path = os.path.abspath(os.path.join(root, "firmware.bin"))
            break

    if not firmware_path:
        print("ERROR: Could not find firmware.bin. Did you run 'pio run'?")
        return False

    print(f"Targeting: {firmware_path}")
    
    # 2. Command - Added --serial-log to ensure output is captured
    cmd = "wokwi-cli --timeout 15000 ."
    
    try:
        # We use shell=True and combine stdout/stderr for maximum visibility
        process = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True, 
            encoding='utf-8'
        )
        
        output = process.stdout + process.stderr
        
        print("\n--- SIMULATOR OUTPUT ---")
        print(output if output.strip() else "[No output received from Wokwi CLI]")
        print("--- END OF OUTPUT ---\n")

        # 3. Check for our "Self-Healing" markers
        if "HEARTBEAT_HIGH" in output:
            print("PASS: Heartbeat detected!")
            return True
        else:
            print("FAIL: Heartbeat not found.")
            return False
            
    except Exception as e:
        print(f"PYTHON SCRIPT ERROR: {e}")
        return False

if __name__ == "__main__":
    sys.exit(0 if run_test() else 1)