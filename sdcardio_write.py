import board
import busio
import sdcardio
import storage

spi = board.SPI()
cs = board.SDCARD_CS

sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

with open("/sd/test.txt", "w") as f:
    f.write("Hello world!\r\n")
