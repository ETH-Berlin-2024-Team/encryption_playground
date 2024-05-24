from PIL import Image
import stepic
import base64

# The message to encrypt
message = "Your secret message here."

# Base64 encode the message
encoded_message = base64.b64encode(message.encode())

# Open the image file
image = Image.open('image.png')

# Encode the base64 message into the image
encoded_image = stepic.encode(image, encoded_message)

# Save the new image with the embedded message
encoded_image.save('encoded_image.png')

# The recipient opens the image file
encoded_image = Image.open('encoded_image.png')

# Extract the base64 message from the image
extracted_message = stepic.decode(encoded_image)

# Base64 decode the extracted message
decoded_message = base64.b64decode(extracted_message).decode()

# Print the decoded message
print("Decrypted message:", decoded_message)
