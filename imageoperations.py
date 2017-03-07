from PIL import Image

def main():
    # Change the path in Line 6 to the path of the image you want to use as input 
    # for Windows users the path specify the path as "c:\\users\\alark1\\Pictures\\usfca.png"
    inputImage = Image.open('/Users/tjuntunen/desktop/project2/usfca.png')

    imageWidth, imageHeight = inputImage.size

	# Menu
    print("-----------------------------")
    print("Choose one of the following: ")
    print("1. Copy")
    print("2. Flip vertical")
    print("3. Flip horizontal")
    print("4. Lighten")
    print("5. Darken")
    print("6. Scroll horizontal")
    print("7. Scroll vertical")
    print("8. Grey scale")
    print("9. Rotate")
    print("10. Swap Corners")
    print("-----------------------------")

    userChoice = int(input("What do you want to do? (1-10): "))

    # Input validation
    while userChoice > 10 or userChoice < 1:
    	print("You must choose a number between 1 and 10")
    	userChoice = int(input("What do you want to do? (1-10): "))

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
    if userChoice == 6:
    	numpixels = int(input("Number of pixels to scroll horizontally: "))
    	scrollHorizontal(numpixels, inputImage, imageWidth, imageHeight)
    if userChoice == 7:
    	numpixels = int(input("Number of pixels to scroll vertically: "))
    	scrollVertical(numpixels, inputImage, imageWidth, imageHeight)
    if userChoice == 8:
    	makeGreyscale(inputImage, imageWidth, imageHeight)
    if userChoice == 9:
    	rotate(inputImage, imageWidth, imageHeight)
    if userChoice == 10:
        swapCorners(inputImage, imageWidth, imageHeight)

# Creates a copy of an image given the image variable, its width, and height
def copyImage(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((i, j), pixelColors)
    copyImageOutput.save("/Users/tjuntunen/desktop/project2/copy.png")
    print("Image copied")

def flipVertical(inputImage, imageWidth, imageHeight):
    flippedImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(imageWidth):
        for j in range(imageHeight):
            flippedHeight = imageHeight - j - 1
            pixelColors = inputImage.getpixel((i, j))
            flippedImageOutput.putpixel((i, flippedHeight), pixelColors)
    flippedImageOutput.save("/Users/tjuntunen/desktop/project2/verticalflip.png")
    print("Image flipped vertically")

def flipHorizontal(inputImage, imageWidth, imageHeight):
    flipHorizontalOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    for i in range(imageWidth):
        for j in range(imageHeight):
            flippedWidth = imageWidth - i - 1
            pixelColors = inputImage.getpixel((i, j))
            flipHorizontalOutput.putpixel((flippedWidth, j), pixelColors)
    flipHorizontalOutput.save("/Users/tjuntunen/desktop/project2/horizontalflip.png")
    print("Image flipped horizontally")

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
    print("Image lightened")

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
    print("Image darkened")

def scrollHorizontal(numpixels, inputImage, imageWidth, imageHeight):
	scrollHorizontalOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

	while numpixels > imageWidth:
		numpixels = numpixels // imageWidth

	for i in range(numpixels, imageWidth):
		for j in range(imageHeight):
			pixelColors = inputImage.getpixel((i, j))
			scrollHorizontalOutput.putpixel((i - numpixels, j), pixelColors)
	for i in range(numpixels):
		for j in range(imageHeight):
			pixelColors = inputImage.getpixel((i, j))
			scrollHorizontalOutput.putpixel((imageWidth - numpixels + i, j), pixelColors)
	scrollHorizontalOutput.save("/Users/tjuntunen/desktop/project2/scrollhorizontal.png")
	print("Image scrolled horizontally")

def scrollVertical(numpixels, inputImage, imageWidth, imageHeight):
	scrollVerticalOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

	while numpixels > imageHeight:
		numpixels = numpixels // imageHeight

	for i in range(imageWidth):
		for j in range(numpixels, imageHeight):
			pixelColors = inputImage.getpixel((i, j))
			scrollVerticalOutput.putpixel((i, j - numpixels), pixelColors)
	for i in range(imageWidth):
		for j in range(numpixels):
			pixelColors = inputImage.getpixel((i, j))
			scrollVerticalOutput.putpixel((i, imageHeight - numpixels + j), pixelColors)
	scrollVerticalOutput.save("/Users/tjuntunen/desktop/project2/scrollvertical.png")
	print("Image scrolled vertically")

def makeGreyscale(inputImage, imageWidth, imageHeight):
	makeGreyscaleOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

	for i in range(imageWidth):
		for j in range(imageHeight):
			pixelColors = inputImage.getpixel((i, j))
			oldRed = pixelColors[0]
			oldGreen = pixelColors[1]
			oldBlue = pixelColors[2]
			newRed = int(oldRed * 0.30)
			newGreen = int(oldGreen * 0.59)
			newBlue = int(oldBlue * 0.11)
			grey = newRed + newGreen + newBlue
			greyPixelColors = (grey, grey, grey)
			makeGreyscaleOutput.putpixel((i, j), greyPixelColors)
	makeGreyscaleOutput.save("/Users/tjuntunen/desktop/project2/greyscale.png")
	print("Image greyscaled")

def rotate(inputImage, imageWidth, imageHeight):
    rotateOutput = Image.new('RGB', (imageHeight, imageWidth), 'white')
    
    for i in range(imageWidth):
        newColumn = i
        for j in range(imageHeight):
            newRow = j
            flippedWidth = imageWidth - i - 1
            pixelColors = inputImage.getpixel((flippedWidth, j))
            rotateOutput.putpixel((newRow, newColumn), pixelColors)
    rotateOutput.save("/Users/tjuntunen/desktop/project2/rotate.png")
    print("Image rotated")

def swapCorners(inputImage, imageWidth, imageHeight):
    swapCornersOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    cornerWidth = imageWidth // 2
    cornerHeight = imageHeight // 2

    for i in range(imageWidth):
        for j in range(cornerHeight, imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            swapCornersOutput.putpixel((i, j - cornerHeight), pixelColors)
    for i in range(imageWidth):
        for j in range(cornerHeight):
            pixelColors = inputImage.getpixel((i, j))
            swapCornersOutput.putpixel((i, imageHeight - cornerHeight + j), pixelColors)
    swapCornersOutput.save("/Users/tjuntunen/desktop/project2/cornerswap.png")

    inputImage = Image.open("/Users/tjuntunen/desktop/project2/cornerswap.png")

    for i in range(cornerWidth, imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            swapCornersOutput.putpixel((i - cornerWidth, j), pixelColors)

    for i in range(cornerWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            swapCornersOutput.putpixel((imageWidth - cornerWidth + i, j), pixelColors)
    swapCornersOutput.save("/Users/tjuntunen/desktop/project2/cornerswap.png")
    print("Corners swapped")

main()
