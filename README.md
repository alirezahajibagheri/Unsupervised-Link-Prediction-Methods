# unsupervised_link_predictions
This directory contains python implementation of standard well-known unsupervised link prediction methods such as Adamic/Adar, Common Neighbors, Jaccard Coefficient and Preferential Attachment.

Each method needs one input which is the graph (this version uses python igraph) and tehy return an array with size n*n as the output. Array[i][j] stands for the score assigned to pair (i,j) using each method.
