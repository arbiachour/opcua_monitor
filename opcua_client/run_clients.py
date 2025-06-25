from client import SimulatedMachineClient
import threading
import config

def launch_client(machine_name):
    client = SimulatedMachineClient(
        endpoint=config.SERVER_ENDPOINT,
        cert_path=config.CLIENT_CERT,
        key_path=config.SERVER_KEY,
        machine_name=machine_name
    )
    client.run()

if __name__ == "__main__":
    machines =config.MACHINE_LIST
    for m in machines:
        t = threading.Thread(target=launch_client, args=(m,))
        t.start()
