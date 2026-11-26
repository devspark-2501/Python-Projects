import os
import qrcode

print('-----------------------------------------------')
print('         📱 Welcome to QR Code Generator!        ')
print('-----------------------------------------------')

data - input('Enter the data you want to encode in the QR code: ')
fileName = input('Enter the filename to save the QR code (without extension): ')

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

os.makedirs("generated_qr", exist_ok=True)

filepath = os.path.join("generated_qr", fileName + ".png")

img.save(filepath)

print("----------------------------------------")
print("QR Code generated successfully!")
print(f"Saved at: {filepath}")
print("----------------------------------------")
