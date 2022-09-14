# MATLAB (engineering and science)
# scipy.io.loadmat() --> read .mat files
# scipy.io.savemat() --> write .mat files
import scipy.io

filename = './data/ja_mata2.mat'
mat = scipy.io.loadmat(filename)
print(type(mat))
print(type(mat['x']))
