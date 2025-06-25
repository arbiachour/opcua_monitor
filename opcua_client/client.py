from opcua import Client, ua
import random
import time


class SimulatedMachineClient:
    def __init__(self, endpoint, cert_path, key_path, machine_name):
        self.endpoint = endpoint
        self.machine_name = machine_name
        self.cert_path = cert_path
        self.key_path = key_path
        self.client = Client(endpoint)
        self.client.set_security_string(
            f"Basic256Sha256,SignAndEncrypt,{cert_path},{key_path}"
        )
        self.client.set_user("machine")  # or whatever user you define
        self.client.set_password("machinepass")

    def connect(self):
        self.client.connect()
        print(f"[{self.machine_name}] Connected to server.")
        self.root = self.client.get_root_node()
        self.temp_node = self.root.get_child(["0:Objects", f"2:{self.machine_name}", "2:Temperature"])
        self.press_node = self.root.get_child(["0:Objects", f"2:{self.machine_name}", "2:Pressure"])

    def simulate_data(self):
        while True:
            temp = round(random.uniform(20.0, 80.0), 2)
            press = round(random.uniform(1.0, 5.0), 2)
            print(f"[{self.machine_name}] Temp: {temp} °C | Pressure: {press} bar")
            self.temp_node.set_value(ua.Variant(temp, ua.VariantType.Float))
            self.press_node.set_value(ua.Variant(press, ua.VariantType.Float))
            time.sleep(2)

    def run(self):
        try:
            self.connect()
            self.simulate_data()
        except Exception as e:
            print(f"[{self.machine_name}] Error: {e}")
        finally:
            self.client.disconnect()
