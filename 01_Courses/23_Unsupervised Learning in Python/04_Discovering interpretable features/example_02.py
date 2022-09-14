"""
# NMF learns interpretable parts

# # Example: NMF learns interpretable parts
# # # Word-frequency array articles (tf-idf)
# # # 20.000 scientific articles (rows)
# # # 800 worlds (columns)

# # Applying NMF to the articles
print(articles.shape)

from sklearn.decomposition import NMF
nmf = NMF(n_components=10) 
nmf.fit(articles)
print(nmf.components_.shape)

# # NMF Components
# # # For documents:
# # # # NMF components represent topics
# # # # NMF features combine topics into documents
# # # For images, NMF components are parts of images

# # Grayscale images
# # # "Grayscale" image = no colors, only shades of gray
# # # Measure pixel brightness
# # # Represent with value between 0 and 1 (0 is black)
# # # Convert to 2D array

# # Grayscale images as flat arrays
# # # Enumerate the entries
# # # Row-by-row
# # # From left to right, top of bottom

# # Encoding a collection of images
# # # Collection of image of the same size
# # # Encode as 2D array
# # # Each row corresponds to an image
# # # Each column corresponds to a pixel
# # # ...can apply NMF!

# # Visualizing samples
print(sample)

bitmap = sample.reshape((2,3))
print(bitmap)

from matplotlib.pyplot as plt
plt.imshow(bitmap,cmap='gray',interpolation='nearest')
plt.show()
"""