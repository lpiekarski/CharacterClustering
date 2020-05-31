from sklearn.cluster import MeanShift, estimate_bandwidth


def cluster(data):
    bandwidth = estimate_bandwidth(data, quantile=0.5, n_samples=2)
    clusters = MeanShift(bandwidth=bandwidth, bin_seeding=True).fit(data)
    return clusters.labels_