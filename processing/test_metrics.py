from functools import total_ordering
from nis import cat
import os
import quality_metrics as qm
import matlab.engine

folder = "psnr33.5"
valueList = []
totalVal = 0.0

for img in os.listdir(folder):
    orig_img = os.path.splitext(img)[0]
    orig_img = os.path.splitext(orig_img)[0]
    orig_img += ".ppm"
    print(orig_img)
    try:
        currVal = qm.psnr(folder+"/"+img, "input/"+orig_img)
        
        if(currVal < 10000): #manchmal kommt inf daher
            valueList.append(currVal)
            totalVal += currVal
    except matlab.engine.MatlabExecutionError:
        print("error with: "+img)

print(valueList)

print(totalVal/len(valueList))