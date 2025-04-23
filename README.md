# pcLivenGrok – Remote Tunnel Manager with QR Sharing

**pcLivenGrok** is a lightweight utility that lets you create up to **3 ngrok tunnels** from your local machine, perfect for testing or running Flask apps (or any local service) on the go. Each tunnel generates both a shareable link and a QR code that you can scan from your phone or any device — ideal for traders, developers, and mobile workflows.

## 🧠 Use Case

Running a Flask app on port `6969` but want to monitor it from your phone while at the gym?

**pcLivenGrok**:
- Spins up a public URL using ngrok
- Displays a scannable QR code for instant mobile access
- Works with up to **3 concurrent ports**

---

## 🔑 Prerequisites

You must have `ngrok` installed and authenticated:

1. [Download ngrok](https://ngrok.com/download) for your OS
2. Place `ngrok` in your system `PATH` or the project folder
3. Set your authentication token (from your ngrok dashboard):

```bash
ngrok config add-authtoken YOUR_NGROK_AUTH_TOKEN
