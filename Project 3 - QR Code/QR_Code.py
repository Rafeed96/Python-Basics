# install libraries
# function to collect text and perform conversion to QR code
# save the QR as an image
# run the function
# install packages


import qrcode


def generate_qecode(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,

    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")


generate_qecode("https://www.youtube.com")
