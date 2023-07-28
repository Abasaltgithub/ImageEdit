import heif
from PIL import Image

with open('/Users/abasaltbahrami/Downloads/contract.heic', 'rb') as f:
    heif_file = heif.read(f)
    image = Image.frombytes(
        heif_file.mode, heif_file.size, heif_file.data,
        "raw", heif_file.mode, heif_file.stride
    )
    image.save('/Users/abasaltbahrami/Downloads/contract.png', format='PNG')
