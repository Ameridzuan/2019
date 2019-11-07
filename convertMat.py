#From https://github.com/Ameridzuan

import scipy.io
import numpy as np

#csv file name
csvname = "your_csv_filename.csv"

#read and load the content into variable named "data"
data = scipy.io.loadmat("your_mathlab_filename.mat")

for header in data:
    #view all data in MATHLAB file
    #print(data)

    #view header available in MATHLAB file
    print(header)
    
    #exclude MATHLAB file header to be written in csv
    if "__" not in header:
        np.savetxt((csvname),data[header],delimiter=',', fmt='%s')
