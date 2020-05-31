from sklearn.cluster import DBSCAN


def cluster(data, eps=12.5, min_samples=1):
    clusters = DBSCAN(eps=eps, min_samples=min_samples).fit(data)
    return clusters.labels_
