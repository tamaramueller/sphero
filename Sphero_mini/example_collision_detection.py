import sphero_mini
import sys


def collision_callback():
    sphero.setLEDColor(red = 255, green = 0, blue = 0) # Turn LEDs red
    sphero.wait(2.0)
    sphero.setLEDColor(red = 0, green = 255, blue = 0) # Turn LEDs green


if len(sys.argv) < 2:
    print("Usage: 'python [this_file_name.py] [sphero MAC address]'")
    print("eg f2:54:32:9d:68:a4")
    print("On Linux, use 'sudo hcitool lescan' to find your Sphero Mini's MAC address")
    exit(1)

MAC = sys.argv[1] # Get MAC address from command line argument

# Connect:
sphero = sphero_mini.sphero_mini(MAC, verbosity = 1)

# battery voltage
sphero.getBatteryVoltage()
print(f"Bettery voltage: {sphero.v_batt}v")

# firmware version number
sphero.returnMainApplicationVersion()
print(f"Firmware version: {'.'.join(str(x) for x in sphero.firmware_version)}")

# Note: Collision detection is an experimental feature - sometimes crashes, with "unexpected response" from bluetooth module
sphero.configureCollisionDetection(callback=collision_callback) # Use default thresholds and pass function object as callback

sphero.setLEDColor(red = 0, green = 255, blue = 0) # Turn LEDs green
print('Waiting for collision')

while(1):
    sphero.wait(1)
