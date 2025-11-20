import qrcode

url = input("Enter the URL to generate QR code: ")
filename = input("filename you want to save it as")
if not filename.endswith(".png"):
    filename += ".png"
img = qrcode.make(url)
img.save(filename)