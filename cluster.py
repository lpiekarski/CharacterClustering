import sys
import os
from PIL import Image

output_filename = "output.txt"
output_html_filename = "output.html"


def generate_html(clusters):
    clusters_html = ""
    for cluster in clusters:
        for img_filename in cluster:
            clusters_html = clusters_html + '<img src="' + img_filename + '"></img>'
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
    print(sys.argv[0] + " [filename]")
    exit(1)

try:
    with open(sys.argv[1]) as input_file:
        image_files_to_cluster = input_file.read().splitlines()
        with open(output_html_filename, 'w') as output_html_file:
            clusters = [image_files_to_cluster, image_files_to_cluster]
            output_html_file.write(generate_html(clusters))
        for img_filename in image_files_to_cluster:
            img = Image.open(img_filename)


except FileNotFoundError:
    print('input file not found')
    exit(1)
