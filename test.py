from zk import ZK
from datetime import datetime

# ✅ CONFIGURATION
DEVICE_IP = "192.168.1.102"  # Change this to your ESSL device IP
DEVICE_PORT = 4370           # Default port for ZKTeco

def test_connection():
    zk = ZK(DEVICE_IP, port=DEVICE_PORT, timeout=10)

    try:
        print(f"📡 Connecting to ESSL device at {DEVICE_IP}:{DEVICE_PORT}...")
        conn = zk.connect()
        print("✅ Connection successful.")

        conn.disable_device()
        print("⏳ Fetching attendance logs...")

        logs = conn.get_attendance()

        if not logs:
            print("🟡 No attendance logs found on the device.")
        else:
            print(f"📋 Found {len(logs)} log(s):\n")
            for log in logs:
                print(f"🕒 UID: {log.user_id} | Time: {log.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

        conn.enable_device()
        conn.disconnect()
        print("\n🔌 Disconnected from device safely.")

    except Exception as e:
        print(f"❌ ERROR: Could not connect or retrieve logs. Reason: {e}")

if __name__ == "__main__":
    test_connection()
