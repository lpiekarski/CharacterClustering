from sklearn.cluster import OPTICS


def cluster(data):
    clusters = OPTICS(min_samples=2, xi=.001, min_cluster_size=.01).fit(data)
    return clusters.labels_
