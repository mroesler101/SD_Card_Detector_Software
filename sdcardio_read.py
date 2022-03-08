import board
import busio
import sdcardio
import storage

spi = board.SPI()
cs = board.SDCARD_CS

sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

with open("/sd/test.txt", "r") as f:
    print("Printing lines in file:")
    line = f.readline()
    while line != '':
        print(line, end='')
        line = f.readline()
