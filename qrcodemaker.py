#install all the libraries needed
#create a function tat collects the text and converts it to a Q code
#save qr code as an image
#run the function

#open a new terminal and type: pip install qcode Image

import qrcode 

def generate_qrcode(text):
  
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode, constants.ERROR_CORRECT_L,
        box-size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

url = input("Enter your url: ")
generate_qrcode("url")
