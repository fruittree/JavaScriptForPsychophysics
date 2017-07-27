from os import listdir
from os.path import isfile, join
import numpy
import cv2

# read in images from the folder
base_name = 'soap_map_b'
end_name = '_q4096.png'
mypath='png_cropped/'
outputpath = 'png_cropped_letter/'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
print(onlyfiles)
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):	
#for n in range(0, 1):	
	img = cv2.imread(join(mypath,onlyfiles[n]) )
	# extract a single letter
	crop_img = img[115:215, 80:187]
	#cv2.imshow("cropped", crop_img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	# save the images into a new folder with the same name. 
	new_name = onlyfiles[n]
	newfilename = str(outputpath) +new_name[:-4]+'_letter.png'
	cv2.imwrite(newfilename,crop_img)


	





