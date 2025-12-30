import asyncio
import json
import os
import websockets

HA_WS_URL = os.environ.get("HA_WS_URL", "ws://supervisor/core/websocket")
HA_TOKEN = os.environ.get("HA_TOKEN", "")

async def ha_ws_test():
    print("🔌 Connecting to Home Assistant WebSocket...")
    async with websockets.connect(HA_WS_URL) as ws:
        # Authenticate
        auth_msg = {
            "type": "auth",
            "access_token": HA_TOKEN
        }
        await ws.send(json.dumps(auth_msg))

        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            print("📨 HA:", data)

            if data.get("type") == "auth_ok":
                print("✅ Authenticated with Home Assistant WebSocket")
                break
            elif data.get("type") == "auth_invalid":
                print("❌ Authentication failed")
                return

asyncio.run(ha_ws_test())
