import adafruit_sdcard
import busio
import digitalio
import board
import storage

# Connect to the card and mount the filesystem.
spi = busio.SPI(board.SDCARD_SCLK, board.SDCARD_MOSI, board.SDCARD_MISO)
cs = digitalio.DigitalInOut(board.SDCARD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

with open("/sd/test.txt", "r") as f:
    print("Printing lines in file:")
    line = f.readline()
    while line != '':
        print(line, end='')
        line = f.readline()
