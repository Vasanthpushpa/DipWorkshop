

# Image Processing with OpenCV and Matplotlib

## Overview
This project demonstrates how to load two images, resize them, divide them into regions (quadrants), and swap specific regions between the two images using OpenCV. The result is displayed using `matplotlib`.

### Features:
- Load and resize images to 400x400 pixels.
- Divide each image into four equal regions (quadrants).
- Swap specific regions (R1 with R8, R2 with R7) between the images.
- Display the final images using `matplotlib`.

---

## Requirements

To run this project, you'll need the following libraries installed:

- OpenCV (`cv2`)
- Matplotlib

You can install them using `pip`:

```bash
pip install opencv-python matplotlib
```

---

## Files

- **`main.py`**: The main script that loads, resizes, splits, swaps, and displays the images.
- **`08.jpg`**: Sample image 1 (replace this with your own image).
- **`08a.jpg`**: Sample image 2 (replace this with your own image).

---

## How It Works

1. **Loading and Resizing**:
   The two images are loaded using OpenCV (`cv2.imread`) and resized to 400x400 pixels for consistency.
   
2. **Image Division**:
   Each image is divided into 4 quadrants:
   - Quadrants in image 1 are labeled as R1, R2, R3, R4.
   - Quadrants in image 2 are labeled as R5, R6, R7, R8.
   
3. **Region Swapping**:
   Specific quadrants are swapped:
   - R1 (top-left of image 1) is swapped with R8 (bottom-right of image 2).
   - R2 (top-right of image 1) is swapped with R7 (bottom-left of image 2).

4. **Displaying the Results**:
   The swapped images are displayed side by side using `matplotlib.pyplot`.

---

## Usage

1. Clone or download this repository.

2. Place your images in the project directory and ensure they are named `08.jpg` and `08a.jpg`, or modify the file paths in `main.py` to point to your images.

3. Run the script using Python:

```bash
python main.py
```

4. The swapped images will be displayed in a new window using `matplotlib`.

---

## Example

Below is an example of the final output after running the code:

- **Image 1**: Original image 1 with the top-left and top-right quadrants swapped with parts of image 2.
- **Image 2**: Original image 2 with the bottom-left and bottom-right quadrants swapped with parts of image 1.

---

## Code

```python
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
image2_resized[200:400, 200:400] = R3  # R3 is placed into image2's bottom-right

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
```


## Output:
![image](https://github.com/user-attachments/assets/9eb14a46-129b-4b39-b499-cb8ff414a184)

## Result
The program for Image Processing with OpenCV and Matplotlib exected successfully.

