#Univariate LSTM Models
# 1. Data Preparation
# 2. Vanilla LSTM
# 3. Stacked LSTM
# 4. Bidirectional LSTM
# 5. CNN LSTM
# 6. ConvLSTM

# univariate data preparation
from numpy import array

# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
    X, y = list(), list()
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the sequence
        if end_ix > len(sequence)-1:
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)

# define input sequence
raw_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# choose a number of time steps
n_steps = 3
# split into samples
X, y = split_sequence(raw_seq, n_steps)
# summarize the data
for i in range(len(X)):
    print(X[i], y[i])


# Vanilla LSTM
model = Sequential()
model.add(LSTM(50, activation = 'relu', input_shape = (n_steps, n_features)))
model.add(Dense(1))
model.compile(optimizer = 'adam', loss = 'mse')
