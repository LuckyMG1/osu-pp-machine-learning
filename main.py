import random, numpy as np, csv

random.seed() # init rng
learning_rate = 0.15
# (max_combo, total_combo, n300, n100, n50, nX, acc, bpm, sr, length | awarded_pp)
# input layer: 10 nodes

# first layer: 2 nodes

# output layer: 1 node -> awarded pp

def init_weights(m1,n1,m2):
    w1 = np.random.normal(0, 0.4082, (m1,n1)) # 10,2
    w2 = np.random.normal(0, 0.8165, (n1,m2)) # 2,1
    return w1, w2

def init_bias(size_l1, size_l2):
    return np.full((size_l1, 1), 0, dtype=np.float64), np.full((size_l2,1), 0, dtype=np.float64)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_dx(x):
    return sigmoid(x)*(1 - sigmoid(x))

def train(inputs, label, w1, w2, b1, b2):
    inp_h1 = np.array([np.dot(inputs, w) for w in w1.T]) + b1.T
    act_inp_h1 = sigmoid(inp_h1)
    
    output = np.dot(act_inp_h1, w2) + b2.T
    
    error = 0.5*(label - output)*(label - output)
    out_minus_label = output - label # pre compute for efficiency

    # gradient in w1
    for i in range(10):
        for j in range(2):
            gradient = out_minus_label*w2[j]*sigmoid_dx(act_inp_h1[0,j])*inputs[i]
            w1[i,j] -= learning_rate * gradient.item()

    # gradient in bias1,2 &  w2
    for i in range(2):
        gradient = out_minus_label*w2[i]*sigmoid_dx(act_inp_h1[0,i])
        b1[i] -= learning_rate * gradient.item()
        gradient = out_minus_label*act_inp_h1[0,i]
        w2[i] -= learning_rate * gradient.item()

    # gradient in bias output
    b2  -= learning_rate * out_minus_label
    
    return output.item(), error.item()
    
if __name__ == "__main__":
    weights1, weights2 = init_weights(10,2,1)
    bias1, bias2 = init_bias(2,1)
    
    input_matrix = np.genfromtxt("plays_input2.csv", delimiter=',', skip_header=1)
    for iter, row in enumerate(input_matrix, start=1):
        output, error = train(row[0:10], row[10], weights1, weights2, bias1, bias2)
        if iter % 150 == 0 or iter == 1:
            print(f"Iteration: {iter}")
            print(f"Error: {error}")
            print(f"Predicted: {output}, Actual: {row[10]}")

    print("weights 1: ", weights1)
    print("weights 2: ", weights2)
    print("bias 1: ", bias1)
    print("bias 2: ", bias2)
