# K-Means (Clustering)
Unsupervised Data
Make clusters from data sets (Classes) by observing graph.
No. of classes = K

1: Randomly choose any 2 (A and B) points in the graph.
2: For 'i'th point in class find distance from point A and B.
    if distance of A is less for class 1 : assign A to class 1 else assign B to class 2.
3: Distance_A= Sum of all points of class 1 from A.
   Distance_B= Sum of all points of class 2 from B.
4: Mean_Distance_A= Distance_A / no. of points in class 1.
   Mean_Distance_B= Distance_B / no. of points in class 2.
5: Assign A=Mean_Distance_A and B= Mean_Distance_B
6: Repeat steps 2-5 and Point A,B will come closer and closer respectively towards their clusters.
   Value of A and B will not change when they reach a saturation value. (Centroid)

> NOTE: There is a possibility that points A and B are randomly located at a point such that their distance
      is equal from both clusters so the mean distance won't change and points won't converge to their
      respective clusters. So we run this algo 2 or 3 times and check loss in each case to figure out and
      fix any issue like this.

## How to find K?
K is found using elbow method.
In elbow method, a plot Loss V/S K is plotted.
On increasing value of K loss decreases rapidly. The point where rapid decrease in loss stops, is
declared as K and algo is applied using that value of K.

K-Means Clustering can be visualised from [here](https://www.naftaliharris.com/blog/visualizing-k-means-clustering/)

## Credits:
Datasets taken from [here](https://github.com/mubaris/friendly-fortnight/)
