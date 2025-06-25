# 🔧 OPC UA Machine Simulator with Flask Monitoring

This project simulates multiple machines using OPC UA clients and exposes their status in a web dashboard using Flask. Each simulated machine sends temperature and pressure data to a secure OPC UA server. The server enforces certificate-based and user/password authentication.

## 📁 Project Structure

opcua/
├── opcua_server/
│ ├── server.py # Secure OPC UA server
│ └── certs/
│       ├── server.der # Server certificate (DER)
│       └── server.pem # Server private key
├── opcua_client/
│ └── client.py # OPC UA client simulator (create multiple clients)
│ └── certs/
│       ├── server.der # Server certificate (DER)
│       └── server.pem # Server private key
├── monitor_app/
│ └── app.py # Flask web app for monitoring machine data
├── config/
│ └── settings.py # Central config (cert paths, usernames, endpoints)
├── .gitignore
└── README.md


## 🚀 How to Run

### 1. Install dependencies
```bash
    pip install -r requirements.txt
```

### 2. Start the OPC UA Server
```bash
    python opcua_server/server.py
```

### 3. Run OPC UA Clients (in multiple terminals or threads)
```bash
    python opcua_client/client.py
```

### 4. Start the Flask Monitoring App
```bash
    python monitor_app/app.py
```
Open your browser to: http://localhost:5000

## 🔐 Security
- Certificates: The server uses X.509 certificates for authentication.

- User Auth: Clients must connect using valid username/password.

- Security Policy: Basic256_Sign is enforced.

- You can configure these in config/settings.py.

## ⚙️ Settings
All config paths, credentials, endpoints, and machine names are centralized in:
```bash
    config/settings.py
```
## ❗ .gitignore
Sensitive files like certs, logs, and virtual environments are excluded in .gitignore.
```bash
    env/
    *.pem
    *.der
    __pycache__/
    *.log
```


## 🙌 Credits
Built with:

- FreeOpcUa

- Flask

