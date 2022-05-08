import pandas as pd
import matplotlib.pyplot as plt
# DRY (Don´t Repeat Yourself) and "Do One Thing"
# # Single Responsability

def load_data(path):
    """ Load a dataset.

    Args:
        path (str): The location of a CSV file.
    
    Return:
        tuple of ndarray: (features,labels)
    """

    data = pd.read_csv(path)
    Y = data['labels'].values
    X = data[col for col in data.columns 
            if col != 'labels'].values
    return X,Y

def plot_data(X):
    """ Plot the first tow principal components of a matrix.

    Args: 
        X (numpy.ndarray): The data to plot.
    """
    pca = PCA(n_components=2).fit_transform(X)
    plt.scatter(pca[:,0],pca[:,1])
