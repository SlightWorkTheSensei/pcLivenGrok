from flask import Flask, render_template, request
from pyngrok import ngrok
import qrcode
import os

app = Flask(__name__)

# Dictionary to manage multiple tunnels {port: tunnel_obj}
active_tunnels = {}

@app.route("/")
def index():
    return render_template("index.html", tunnels=active_tunnels)

@app.route("/start_tunnel", methods=["POST"])
def start_tunnel():
    # Get the port from the user input
    port = request.form.get("port")

    # Validate the port
    if not port.isdigit():
        return "Invalid port number. Please enter a valid number."

    port = int(port)

    # If tunnel for this port already exists, reuse it
    if port in active_tunnels:
        public_url = active_tunnels[port].public_url
    else:
        # Create a new ngrok tunnel
        tunnel = ngrok.connect(port)
        active_tunnels[port] = tunnel
        public_url = tunnel.public_url

        # Generate QR code for the new URL
        qr_image_path = os.path.join("static", f"qrcode_{port}.png")
        qr = qrcode.make(public_url)
        qr.save(qr_image_path)

    return render_template("index.html", tunnels=active_tunnels, qr_images=[f"qrcode_{p}.png" for p in active_tunnels])

@app.route("/stop_tunnel", methods=["POST"])
def stop_tunnel():
    port = request.form.get("port")

    if not port or not port.isdigit():
        return "Invalid port."

    port = int(port)

    if port in active_tunnels:
        ngrok.disconnect(active_tunnels[port].public_url)
        del active_tunnels[port]
        return render_template("index.html", message=f"Tunnel on port {port} stopped.", tunnels=active_tunnels)

    return render_template("index.html", message="No tunnel found on this port.", tunnels=active_tunnels)

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
