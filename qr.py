import qrcode

# Website URL
url = "Your Link Here"

# Generate QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the QR code image
img.save("demo.png")

print("QR Code generated and saved as 'demo.png'")
