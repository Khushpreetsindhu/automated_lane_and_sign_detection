# automated_lane_and_sign_detection
This is a system for unmarked roads that detects lanes and their curves while simultaneously identifying oncoming traffic signs.
The lane detection part basically works in four steps:
1. Thresholding: .Color thresholding is done for unmarked roads
		 .BGR to HSV, to separeate road from surrounding
		 .This will convert image into a binary image(color of path will be white)
2. Warping: .lane edges can not be precisely located by the angled perspective
	   .bird's eye/top view
	   .For warping, we provide a set of points & their values will provide ROI
	   .Result would be an image which would be cropped w.r.t ROI & having a bird's eye view
3. Region of interest(ROI)
4. Pixel summation(Histogram):
     .To find the curve of the path
     .Histogram is used for graphically repersenting the color tone distribution of the image
	   .Using the thresholded image,histogram plots black(zero), white(non-zero)
     .Non-zero pixels represent lane geometry
			NOISE
			  .A certain threshold value,to determine if a particular column is a part of path or not
			  .Average value of histogram of the lower 1/4th part of image is considered as the base point(centre of the path)
				.Middle point=average value of histogram of complete image
				.CURVE VALUE = BASE POINT - MIDDLE POINT(for steering angle/radius of curvature)
For sign detection, images were flagged with the help of Yolov5 into three classification .i.e stop sign, red light and green light.
