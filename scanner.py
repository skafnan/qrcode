import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
qr= pyqrcode.create("https://www.youtube.com/results?search_query=mr+beast")
qr.png("mycode.png", scale=8)