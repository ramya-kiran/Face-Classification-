import caffe
import argparse
import numpy as np

caffe.set_mode_gpu()
caffe.set_device(0)

parser = argparse.ArgumentParser()
parser.add_argument('source', nargs='+', help='list of image(s)')
parser.add_argument('model', help='model')
parser.add_argument('weights', help='pre-trained weights')
parser.add_argument('output', help='output')
args = parser.parse_args()

classifier = caffe.Classifier(args.model, args.weights)

inputs = [caffe.io.load_image(input) for input in args.source]

predictions = classifier.predict(inputs)

with open(args.output, 'w') as f:
    for file, prediction in zip(args.source, predictions):
        top_3_labels = np.argsort(prediction)[-1::-1][:3]
        top_3_confidence = prediction[top_3_labels]
        s = '{},{},{},{},{},{},{}\n'.format(file, top_3_labels[0], top_3_confidence[0], top_3_labels[1], top_3_confidence[1], top_3_labels[2], top_3_confidence[2])

        f.write(s)
