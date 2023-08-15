# Install all the libraries needed
# Create a function that collects text and converts it to a qrcode
# Save the qrcode as an image
# run the function

import qrcode

def generate_QRCode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 14,
        border = 5,

    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="blue" , back_color="white")
    img.save("qrimg.png")

url = input(" Please enter your URL: ")
generate_QRCode (url)
