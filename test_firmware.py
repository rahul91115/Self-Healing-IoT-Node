import subprocess
import os

def run_test():
    print("🚀 Starting Automated Firmware Test...")
    
    # This automatically finds the .bin file regardless of the folder name
    firmware_path = ""
    for root, dirs, files in os.walk(".pio/build"):
        if "firmware.bin" in files:
            firmware_path = os.path.join(root, "firmware.bin")
            break

    if not firmware_path:
        print("❌ ERROR: Could not find firmware.bin. Did the build fail?")
        return False

    print(f"📦 Found firmware at: {firmware_path}")
    
    # Run Wokwi CLI
    cmd = f"wokwi-cli --timeout 15000 --bin {firmware_path} diagram.json"
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    # This is the "Self-Healing" check
    if "HEARTBEAT_HIGH" in result.stdout:
        print("✅ TEST PASSED: Heartbeat detected!")
        return True
    else:
        print("❌ TEST FAILED: Heartbeat not found.")
        print("Full Simulator Log Below:")
        print(result.stdout) # This will now show us EXACTLY what happened
        return False

if __name__ == "__main__":
    import sys
    sys.exit(0 if run_test() else 1)