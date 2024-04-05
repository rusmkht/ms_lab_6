import asyncio
from bleak import BleakScanner

async def discover_devices():
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Device: {device.name}\nAddress: {device.address}\nDetails: {device.metadata}\n")


if __name__ == '__main__':
    asyncio.run(discover_devices())
