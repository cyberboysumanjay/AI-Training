# Neural Network
We divide our network in 3 parts
Input Layer
Hidden Layer
Output Layer

In forward pass we take all input x1,x2.. and connecting weights w1,w2.. randomly.
We get H1 and H2 according to random inputs what we have assumed in first forward pass.

We then put H1 and H2 as inputs in activation function (Sigmoid, ReNu, Leaky ReNu, Tanh)
The output we get by sending H1 as input is labelled as H1_out. (similarly H2,H3...)

We then compare Hout with original training data and find error[xSquare mean] (Very much error is likely)
Then we partially differentiate our error wrt to weights w1,w2... and minimize them so that error is reduced.
Use this w1=w1-a(d Error/d w1)  where a is alpha (Learning Rate)[Can be selected randomly]

After getting updated values of w1,w2 we then do back pass, ie. go back and put into the error equation and repeatedly
decrease error by doing many iterations(epochs).
