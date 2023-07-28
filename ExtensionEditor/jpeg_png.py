from PIL import Image

# Open the JPEG image
with Image.open('/Users/abasaltbahrami/Downloads/contract.heic') as img:

    # Convert to PNG
    img.save('/Users/abasaltbahrami/Downloads/passport.png', 'png')
