# Digital Signal and Image Processing - Assignments

### Assignment 1
 Implement the  **Zero-crossing rate (ZCR)**  feature to describe a single-channel audio signal, starting from the commands shown in the excercises.  Verify the effect of using ZCR in combination with other features available in the published notebook. Using libraries such as Librosa is  **not**  allowed, as they offer pre-made functions to compute ZCR. It is, instead, possible to use numpy for the basic operations (shift, sign, etc.)
### Assignment 2
Experiment with the **compression of a color image** by blurring the chroma channels of the YCbCr representation.
### Assignment 3
Implement a script for  **image stitching**  of two images. It is  **not**  allowed to use cv.createStitcher() or other complete functions for image stitching. You should, however, use pre-made functions for the computation of the Homography and for image warping.
### Assignment 4
Implement a  **neural network**  to classify the MNIST and CIFAR10 datasets, following the guidelines shown in the notebook. Adhere to the following architecture:

-   Explicit input layer
-   Convolution (2D) with 32 3×3 filters
-   ReLU
-   Max pooling (2D) with a 2×2 filter
-   Flattening
-   Fully-connected mapping to 128 dimensions
-   ReLU
-   Fully-connected mapping to the final problem size
### Assignment 5
Implement a classification script based on the  **fine tuning of a neural network**  for the 101 object classes dataset. Verify the impact over the model performance given by:  
1.  A different architecture (i.e.  **no mobile net)**
2.  **Data augmentation**  operations
