Our CNN network was written in Caffe and our submission contains, solver.prototxt, train_val.prototxt and deploy.prototxt

To train Wideception, please use the following command:
aprun build/tools/caffe train -solver path-to-solver.prototxt -gpu 0
To run from a snapshot:
aprun build/tools/caffe train -solver -snapshot path-to-the-snapshot-iteration.solverstate -gpu 0

To test Wideception, please use the following command:
aprun build/tools/caffe test -model path-to-train_val.prototxt
                          -weights path-to-weights-_iter_value.caffemodel -iterations value -gpu 0


Running Eigenfaces

Cite: We have sued the same code we submitted for assignment 3 for our project.
We have provided a3.cpp, Eigen.h, Makefile in our submission
make
./a3 train eigen
./a3 test eigen
