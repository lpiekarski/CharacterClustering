import scipy.cluster.hierarchy as hcluster


# no cnn:
#  threshold=12.5
# with cnn:
#  threshold=0.5
def cluster(data, threshold=9):
    clusters = hcluster.fclusterdata(data, threshold, criterion='distance')
    return clusters
