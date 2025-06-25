from opcua import Client

class OPCUAReader:
    def __init__(self, endpoint):
        self.client = Client(endpoint)

    def connect(self):
        self.client.connect()

    def disconnect(self):
        self.client.disconnect()

    def read_values(self, machine_list):
        data = {}
        root = self.client.get_root_node()
        for machine in machine_list:
            try:
                temp = root.get_child(["0:Objects", f"2:{machine}", "2:Temperature"]).get_value()
                press = root.get_child(["0:Objects", f"2:{machine}", "2:Pressure"]).get_value()
                data[machine] = {"temperature": temp, "pressure": press}
            except:
                data[machine] = {"temperature": "N/A", "pressure": "N/A"}
        return data
