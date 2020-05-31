import sys
import os
import numpy as np
from image_transform import get_prepared_images_flat
#import tensorflow as tf

from models.hierarchy import cluster

output_filename = "output.txt"
output_html_filename = "output.html"
model_path = 'trained/cnn_128_3'
img_size = 64

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '_']


def find_letter(l):
    for i in range(len(letters)):
        if letters[i] == l:
            return i
    return len(letters)


def generate_html(clusters):
    clusters_html = ""
    for cluster in clusters:
        for img_filename in cluster:
            clusters_html = clusters_html + '<img src="' + img_filename + '"></img> &nbsp;'
        clusters_html = clusters_html + '<hr>'
    return """
    <html>
        <body>
        """ + clusters_html + """
        </body>
    </html>
    """


if len(sys.argv) != 2:
    print("Wrong usage. Try:")
    print(os.path.basename(sys.argv[0]) + " [filename]")
    exit(1)

try:
    with open(sys.argv[1]) as input_file:
        print('preprocessing images')
        image_files_to_cluster = input_file.readlines()
        image_data = get_prepared_images_flat(image_files_to_cluster, img_size)
        data = image_data
#        print('loading cnn')
#        model = tf.keras.models.load_model(model_path)
#        print('converting images to input vectors')
#        data = model(image_data)
#        for i in range(len(image_files_to_cluster)):
#            print(letters[np.argmax(data[i, :])])
        print('clustering')
        cluster_labels = cluster(data)
        max_c = max(cluster_labels)
        cluster_labels = [x if x != -1 else max_c + 1 for x in cluster_labels]

        print('saving output')
        clusters = [[] for _ in range(max(cluster_labels))]
#        preds = [[] for _ in range(max(cluster_labels))]
        if not clusters:
            clusters = [[]]
        clusters_output = [[] for _ in range(max(cluster_labels))]
        for i in range(len(cluster_labels)):
            clusters[cluster_labels[i] - 1 if cluster_labels[i] > 0 else 0].append(image_files_to_cluster[i])
            clusters_output[cluster_labels[i] - 1 if cluster_labels[i] > 0 else 0].append(os.path.basename(image_files_to_cluster[i].strip()))
#            preds[cluster_labels[i] - 1 if cluster_labels[i] > 0 else 0].append(letters[np.argmax(data[i, :])])
#        for pred in preds:
#            print(pred)
        with open(output_html_filename, 'w') as output_html_file:
            output_html_file.write(generate_html(clusters))
        with open(output_filename, 'w') as output_file:
            output_file.write("\n".join([" ".join(x) for x in clusters_output]))


except FileNotFoundError:
    print('input file not found')
    exit(1)
