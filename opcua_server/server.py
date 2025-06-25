from opcua import Server, ua
import os
import config


MACHINE_LIST = config.MACHINE_LIST
def setup_server():
    opcserver = Server()

    # Endpoint URL
    opcserver.set_endpoint(config.SERVER_ENDPOINT)

    # Application and namespace
    opcserver.set_server_name(config.SERVER_NAME)
    uri = "http:arbi:machines"
    idx = opcserver.register_namespace(uri)

    # Load server cert/key
    opcserver.load_certificate(config.SERVER_CERT)
    opcserver.load_private_key(config.SERVER_KEY)

    # Security: allow only clients with trusted certs
    opcserver.set_security_policy([
        ua.SecurityPolicyType.Basic256_Sign
    ])
    opcserver.set_security_IDs(["Anonymous", "UserName"])
    
    # User auth (optional)
    def user_auth(username, password):
        return username == config.USERNAME and password == config.PASSWORD
    opcserver.user_manager.set_user_manager(user_auth)
    

    # Create machine nodes
    objects = opcserver.get_objects_node()

    for name in MACHINE_LIST:
        machine = objects.add_object(idx, name)
        temp = machine.add_variable(idx, "Temperature", 0.0)
        temp.set_writable()
        pressure = machine.add_variable(idx, "Pressure", 0.0)
        pressure.set_writable()

    return opcserver

if __name__ == "__main__":
    opcserver = setup_server()
    try:
        print("Starting OPC UA Server with security...")
        opcserver.start()
        input("Server is running. Press Enter to stop...\n")
    finally:
        print("Shutting down server.")
        opcserver.stop()
