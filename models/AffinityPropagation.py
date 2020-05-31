from sklearn.cluster import AffinityPropagation


def cluster(data, damping=0.9, max_iter=200, convergence_iter=15):
    clusters = AffinityPropagation(damping=damping, max_iter=max_iter, convergence_iter=convergence_iter).fit(data)
    return clusters.labels_
