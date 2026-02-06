import subprocess
import time

def run_test():
    print("🚀 Starting Automated Firmware Test...")
    
    # This command runs Wokwi for 10 seconds and saves output to 'log.txt'
    # The --timeout tells it when to stop automatically
    cmd = "wokwi-cli --timeout 10000 --bin .pio/build/az-delivery-devkit-v4/firmware.bin diagram.json"
    
    try:
        # Run the simulation and capture what it prints
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout
        
        # The "Healing" Logic: Check if our heartbeats exist
        if "HEARTBEAT_HIGH" in output and "HEARTBEAT_LOW" in output:
            print("✅ TEST PASSED: Heartbeat detected!")
            return True
        else:
            print("❌ TEST FAILED: Heartbeat missing or system crashed.")
            print("Log Snippet:", output[:200]) # Show the first bit of the error
            return False
            
    except Exception as e:
        print(f"❗ Error running test: {e}")
        return False

if __name__ == "__main__":
    if run_test():
        exit(0) # Success signal to GitHub
    else:
        exit(1) # Failure signal to GitHub