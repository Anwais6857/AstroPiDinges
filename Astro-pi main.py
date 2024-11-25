import cv2

image = cv2.imread("photo_0675.jpg")
cv2.imshow("Image", image)
colorThreshold = [37, 150, 190]
pixelsExceedingThreshold = 0

# Go over every pixel in the image and check if threshold is equal or greater than the pixel color
def filterPixels(rows, cols, pixelsExceed):
  for i in range(0,rows):
    for j in range(0,cols):
      color = image[i, j]
      if color[0] >= colorThreshold[0] and color[1] >= colorThreshold[1] and color[2] >= colorThreshold[2]:
        pixelsExceed += 1

def finalDecision(rows, cols):        
  #20% of pixels exceed threshold
  maxAllowedPixelsExceding= round(rows * cols * 0.2) 
  if maxAllowedPixelsExceding <= pixelsExceedingThreshold:
    print("Image contains too many clouds.")
    return 0
  else:
    print(f"Passed cloud test with {maxAllowedPixelsExceding} pixels exceeding the threshold.")
    return 1
  
print("Starting cloud test, this may take 10-15 seconds...")
filterPixels(image.shape[0], image.shape[1], pixelsExceedingThreshold)
finalDecision(image.shape[0], image.shape[1])




