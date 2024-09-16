import qrcode

data = input("Enter the text or URL you want to encode in QR code: ")
file_name = input("Enter the file name for the QR code image: ")
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(file_name)
print(f"QR code image saved as {file_name}")
