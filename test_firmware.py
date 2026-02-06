import subprocess
import os
import sys

def run_test():
    print("--- Starting Automated Firmware Test ---")
    
    firmware_path = ""
    for root, dirs, files in os.walk(".pio/build"):
        if "firmware.bin" in files:
            firmware_path = os.path.join(root, "firmware.bin")
            break

    if not firmware_path:
        print("ERROR: Could not find firmware.bin. Run 'pio run' first.")
        return False

    print(f"Found firmware at: {firmware_path}")
    
    # Run Wokwi CLI with a 15-second timeout
    cmd = f"wokwi-cli --timeout 15000 --bin {firmware_path} diagram.json"
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        print("--- SIMULATOR LOG START ---")
        print(result.stdout)
        print("--- SIMULATOR LOG END ---")

        if "HEARTBEAT_HIGH" in result.stdout:
            print("PASS: Heartbeat detected!")
            return True
        else:
            print("FAIL: Heartbeat not found in logs.")
            return False
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        return False

if __name__ == "__main__":
    sys.exit(0 if run_test() else 1)