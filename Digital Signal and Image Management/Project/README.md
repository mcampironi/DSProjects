# Digital Signal and Image Processing - Final Project

## Introduction
The main goal of this project is to retrieve the most similar clothes in our database based on an input picture given by an user. The idea was to use an R-CNN to identify the item of clothing in the picture, and then to use a trained CNN to extract the features and employ a K-D Tree to retrieve the top-5 most similar garments.

## R-CNN
We used the [matterport implementation](https://github.com/matterport/Mask_RCNN "Mask R-CNN") of Mask R-CNN on Python 3, Keras, and TensorFlow. It was trained on [DeepFashion2](https://github.com/switchablenorms/DeepFashion2 "DeepFashion2"), but we used the [following weights](https://drive.google.com/file/d/15ol8TU9pZHemhbpbW3MJxYa-1gheMDN3/view?usp=sharing "Weights") due to computational constraints.

## Technical implementation
More details can be found in our [presentation](https://github.com/matterport/Mask_RCNN "Presentation") (in Italian).
