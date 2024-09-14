import cv2
import matplotlib.pyplot as plt

# Load the images
image1 = cv2.imread('08.jpg')
image2 = cv2.imread('08a.jpg')

# Resize the images to (400, 400)
image1_resized = cv2.resize(image1, (400, 400))
image2_resized = cv2.resize(image2, (400, 400))

# Split the images into 4 regions
R1 = image1_resized[0:200, 0:200]
R2 = image1_resized[0:200, 200:400]
R3 = image1_resized[200:400, 0:200]
R4 = image1_resized[200:400, 200:400]

R5 = image2_resized[0:200, 0:200]
R6 = image2_resized[0:200, 200:400]
R7 = image2_resized[200:400, 0:200]
R8 = image2_resized[200:400, 200:400]

# Swap regions
image1_resized[0:200, 0:200] = R8  # R1 <-> R8
image1_resized[0:200, 200:400] = R7  # R2 <-> R7
image2_resized[200:400, 200:400] = R3  # Swapping more regions as needed

# Display the resized images using matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image1_resized, cv2.COLOR_BGR2RGB))
plt.title('Image 1 with Swapped Regions')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(image2_resized, cv2.COLOR_BGR2RGB))
plt.title('Image 2 with Swapped Regions')
plt.axis('off')

plt.show()
