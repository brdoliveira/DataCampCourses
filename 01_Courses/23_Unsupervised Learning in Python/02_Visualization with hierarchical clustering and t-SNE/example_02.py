"""
# Cluster labels in hirarchical clustering
# # Not only a visualization tool!
# # Cluster labels at any intermediate stage can be recovered
# # For use in e.g. cross-tabulations

# # Intermediate clusterings & height on dendogram
# # # E.g. at height 15:
# # # # Bulgaria, Cyprus, Greece are one cluster
# # # # Russia anf Moldova are another
# # # # Armenia in a cluster on its own

# # Dendograms show cluster distances
# # # Height on dendogram = distance between merging clusters
# # # E.g. clusters with only Cyprus and Greece had distance approx. 6
# # # This new clusters distance approx. 12 from cluster with only Bulgaria

# # Intermediate clustering & height on dendogram
# # # Height on dendogram specifies max. distance between merging clusters
# # # Don't merge clusters further apart than this (e.g. 15)

# # Distance between clusters
# # # Defined by a "linkage method"
# # # In "complete" linkage: distance between clusters is max. distance between their samples
# # # Specified via method parameter, e.g. linkage (samples,method="complete")
# # # Different linkage method, different hierarchical clustering!

# # Extracting cluster labels
# # # Use the fcluster() function
# # # Returns a NumPy array of cluster labels

# # Extracting cluster labels using fcluster
from scipy.cluster.hierarchy import linkage
mergings = linkage(samples,method='complete')

from scipy.cluster.hierarchy import fcluster
labels = fcluster(mergings,15,criterion='distance')
print(labels)

# # Aligning cluster labels with country names
# # # Given a list of string country_names:
import pandas as pd
pais = pd.DataFrame({'labels':labels, 'countries': country_names})
print(pairs.sort_values('labels'))

"""