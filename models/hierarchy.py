import scipy.cluster.hierarchy as hcluster


# no cnn:
#  threshold=9
# with cnn:
#  threshold=0.5
def cluster(data, threshold=9.5):
    clusters = hcluster.fclusterdata(data, threshold, criterion='distance')
    return clusters
