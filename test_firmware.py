import subprocess
import sys

def run_test():
    print("--- Starting Automated Firmware Test ---")
    
    # The '.' tells wokwi-cli to look at wokwi.toml for the path
    cmd = "wokwi-cli --timeout 15000 ."
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')
        output = result.stdout + result.stderr
        
        print("\n--- SIMULATOR OUTPUT ---")
        print(output if output.strip() else "No output received.")
        print("--- END OF OUTPUT ---\n")

        if "HEARTBEAT_HIGH" in output:
            print("PASS: Heartbeat detected!")
            return True
        else:
            print("FAIL: Heartbeat not found.")
            return False
    except Exception as e:
        print(f"PYTHON ERROR: {e}")
        return False

if __name__ == "__main__":
    sys.exit(0 if run_test() else 1)