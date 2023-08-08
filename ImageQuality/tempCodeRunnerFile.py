import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load images
image_paths = [
    '/Users/abasaltbahrami/My Drive/InCor - Brazil/CellMigration/CTR_0hr_1pm.png',
    '/Users/abasaltbahrami/My Drive/InCor - Brazil/CellMigration/CTR_5hr_6pm.png',
    '/Users/abasaltbahrami/My Drive/InCor - Brazil/CellMigration/B_0hr_1pm.png',
    '/Users/abasaltbahrami/My Drive/InCor - Brazil/CellMigration/B_5hr_6pm.png',
    '/Users/abasaltbahrami/My Drive/InCor - Brazil/CellMigration/Phone_5hr_6pm.png',
    '/Users/abasaltbahrami/My Drive/InCor - Brazil/CellMigration/Phone_5hr_6pm.png'
]

images = [mpimg.imread(image_path) for image_path in image_paths]

# Display images in a 2x2 grid without spaces and titles
plt.figure(figsize=(8, 8))  # Adjust the figure size as needed

for i, image in enumerate(images, 1):
    plt.subplot(3, 2, i)
    plt.imshow(image, cmap='gray')
    plt.axis('off')  # Turn off axis
    plt.subplots_adjust(wspace=0, hspace=0)  # Remove spaces

plt.show()
