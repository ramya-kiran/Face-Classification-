all: CImg.h a3.cpp Classifier.h NearestNeighbor.h
	g++ -g a3.cpp -o a3 -lX11 -lpthread -I. -Isiftpp -O3 siftpp/sift.cpp -ggdb -std=c++11
clean:
	rm a3
