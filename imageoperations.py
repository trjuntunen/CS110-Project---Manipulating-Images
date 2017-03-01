from PIL import Image

def main():
    # Change the path in Line 6 to the path of the image you want to use as input 
    # for Windows users the path specify the path as "c:\\users\\alark1\\Pictures\\usfca.png"
    inputImage = Image.open('/Users/tjuntunen/desktop/project2/usfca.png')
    imageWidth, imageHeight = inputImage.size
    if userChoice == 1:
    	copyImage(inputImage, imageWidth, imageHeight)
    if userChoice == 2:
    	flipVertical(inputImage, imageWidth, imageHeight)
    if userChoice == 3:
        flipHorizontal(inputImage, imageWidth, imageHeight)
    if userChoice == 4:
        amount = float(input("Enter a float point value between 0 and 1: "))
        lighten(amount, inputImage, imageWidth, imageHeight)
    if userChoice == 5:
        amount = float(input("Enter a float point value between 0 and 1: "))
        darken(amount, inputImage, imageWidth, imageHeight)

# Creates a copy of an image given the image variable, its width, and height
def copyImage(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((i, j), pixelColors)
    copyImageOutput.save("/Users/tjuntunen/desktop/project2/copy.png")
    print("Image copied successfully!")

# Flips the image vertically
def flipVertical(inputImage, imageWidth, imageHeight):
    flippedImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(imageWidth):
        for j in range(imageHeight):
            flippedHeight = imageHeight - j - 1
            pixelColors = inputImage.getpixel((i, j))
            flippedImageOutput.putpixel((i, flippedHeight), pixelColors)
    flippedImageOutput.save("/Users/tjuntunen/desktop/project2/verticalflip.png")
    print("Image flipped vertically successfully!")

def flipHorizontal(inputImage, imageWidth, imageHeight):
    flipHorizontalOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(imageWidth):
        for j in range(imageHeight):
            flippedWidth = imageWidth - i - 1
            pixelColors = inputImage.getpixel((i, j))
            flipHorizontalOutput.putpixel((flippedWidth, j), pixelColors)
    flipHorizontalOutput.save("/Users/tjuntunen/desktop/project2/horizontalflip.png")
    print("Image flipped horizontally successfully!")

def lighten(amount, inputImage, imageWidth, imageHeight):
    lightenOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            oldRed = pixelColors[0]
            oldGreen = pixelColors[1]
            oldBlue = pixelColors[2]
            newRed = int((((1 - amount) * oldRed) + (amount * 255)))
            newGreen = int((((1 - amount) * oldGreen) + (amount * 255)))
            newBlue = int((((1 - amount) * oldBlue) + (amount * 255)))
            lightenedPixelColors = (newRed, newGreen, newBlue)
            lightenOutput.putpixel((i, j), lightenedPixelColors)
    lightenOutput.save("/Users/tjuntunen/desktop/project2/lighter.png")
    print("Image lightened successfully!")

def darken(amount, inputImage, imageWidth, imageHeight):
    darkenOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            oldRed = pixelColors[0]
            oldGreen = pixelColors[1]
            oldBlue = pixelColors[2]
            newRed = int((1 - amount) * oldRed)
            newGreen = int((1 - amount) * oldGreen)
            newBlue = int((1 - amount) * oldBlue)
            darkenedPixelColors = (newRed, newGreen, newBlue)
            darkenOutput.putpixel((i, j), darkenedPixelColors)
    darkenOutput.save("/Users/tjuntunen/desktop/project2/darker.png")
    print("Image darkened successfully!")

# Menu
print("1. Copy")
print("2. Flip Vertical")
print("3. Flip Horizontal")
print("4. Lighten")
print("5. Darken")

# User choice
userChoice = int(input("What do you want to do? (1-5): "))

# Input validation
while userChoice > 5 or userChoice < 1:
	print("You must choose a number from 1-5.")
	userChoice = int(input("What do you want to do? (1-5): "))

main()