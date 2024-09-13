
LISA road signs - v2 4 classes
==============================

This dataset was exported via roboflow.ai on November 29, 2021 at 12:14 AM GMT

It includes 11581 images.
Sign are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Fit (reflect edges))

The following augmentation was applied to create 2 versions of each source image:
* Random rotation of between -4 and +4 degrees
* Salt and pepper noise was applied to 1 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* Salt and pepper noise was applied to 1 percent of pixels


