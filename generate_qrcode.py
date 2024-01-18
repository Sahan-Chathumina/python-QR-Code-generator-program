import qrcode

# Take user input for Name, Business name, Email, Contact number, and Website or Social Media link
name = input("Enter Name: ")
business_name = input("Enter Business Name: ")
email = input("Enter Email: ")
contact_number = input("Enter Contact Number: ")
website_or_social_media = input("Enter Website or Social Media Link: ")

# Combine user inputs into a single string (you can customize the format as needed)
data = f"Name: {name}\nBusiness Name: {business_name}\nEmail: {email}\nContact Number: {contact_number}\nWebsite or Social Media: {website_or_social_media}"

# Create QR code instance with a smaller box size
qr = qrcode.QRCode(
    version=15,  # Version of the QR code (adjust as needed)
    box_size=5,  # Smaller box size
    border=5  # Thickness of the border
)

# Add user input data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Specify the file name to save the QR code image
file_name = "my_qrcode.png"

# Save the QR code image to a file
img.save(file_name)

print(f"QR code saved to {file_name}")
