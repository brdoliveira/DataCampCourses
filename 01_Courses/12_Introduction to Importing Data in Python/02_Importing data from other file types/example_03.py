# HDF5 --> Hierarchical Data Format version 5
# Standard for storing large quantities of numerical data
import h5py
filename = './data/L-L1_LOSC_4_V1-1126259446-32.hdf5'
data = h5py.File(filename,'r')
print(type(data))

for key in data.keys():
    print(key)

print(type(data['meta']))

for key in data['meta'].keys():
    print(key)

print(data['meta']['Description'].value, data['meta']['Detector'].value)