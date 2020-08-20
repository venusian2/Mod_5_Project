import tensorflow as tf
import numpy as np
import os
import time
from tensorflow.keras.layers import Dense, Embedding, LSTM, GRU, Dropout
from tensorflow.keras import Sequential

#character index mappings that will be used for all models
char2idx = {'\t': 0, '\n': 1, ' ': 2, 'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9,
            'h': 10, 'i': 11, 'j': 12, 'k': 13, 'l': 14, 'm': 15, 'n': 16, 'o': 17, 'p': 18, 
            'q': 19, 'r': 20, 's': 21, 't': 22, 'u': 23, 'v': 24, 'w': 25, 'x': 26, 'y': 27, 'z': 28}

# charcaters present in all models
vocab = ['\t', '\n', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# numpy array of index to character mappings
idx2char = np.array(vocab)

# Length of the vocabulary
vocab_size = len(vocab)

# The embedding dimension
embedding_dim = 256

# Number of RNN units
rnn_units = 512

# builds models based on user input
def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim,
                              batch_input_shape=[batch_size, None]),
    tf.keras.layers.LSTM(rnn_units,
                         return_sequences=True,
                         stateful=True,
                         dropout = 0.15,
                         recurrent_dropout = 0.15),
    tf.keras.layers.LSTM(rnn_units, 
                         return_sequences=True,
                         stateful=True,
                         dropout = 0.15,
                         recurrent_dropout = 0.15),
    tf.keras.layers.Dense(vocab_size)
    ])
    return model


# creates pop model
def pop(start_string, temp):
    checkpoint_dir = 'models/pop/'
    model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)
    model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
    model.build(tf.TensorShape([1, None]))
    return generate_text(model, start_string, temp)

# creates rock model
def rock(start_string, temp):
    checkpoint_dir = 'models/rock/'
    model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)
    model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
    model.build(tf.TensorShape([1, None]))
    return generate_text(model, start_string, temp)

#creates rap model
def rap(start_string, temp):
    checkpoint_dir = 'models/rap/'
    model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)
    model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
    model.build(tf.TensorShape([1, None]))
    return generate_text(model, start_string, temp)

#creates country model
def country(start_string, temp):
    checkpoint_dir = 'models/country/'
    model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)
    model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
    model.build(tf.TensorShape([1, None]))
    return generate_text(model, start_string, temp)


#function to create lyrics
def generate_text(model, start_string, temp):
    # Evaluation step (generating text using the learned model)

    # Number of iterations for predictions
    num_generate = 2000

    # Converting our start string to numbers (vectorizing)
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    # Empty string to store our results
    text_generated = []

    # Low temperatures results in more predictable text.
    # Higher temperatures results in more surprising text.
    # user can chage this value
    temperature = temp

    # Here batch size == 1
    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        # remove the batch dimension
        predictions = tf.squeeze(predictions, 0)

        # using a categorical distribution to predict the character returned by the model
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

        # We pass the predicted character as the next input to the model
        # along with the previous hidden state
        input_eval = tf.expand_dims([predicted_id], 0)

        #stopping conditons for predictions
        # if characters generated is lesss than 1000, keep generating
        if i < 1000:
            text_generated.append(idx2char[predicted_id])
        # if characters are over 1000 set different stopping conditions
        elif i >= 1000:
            # if we generate a tab character we stop and return our song
            if idx2char[predicted_id] == '\t':
                return (start_string + ''.join(text_generated).replace('\n ', '\n').replace('\t ', '\n'))
            # if we generate 2 next line character in the pas three characters we stop
            elif ((text_generated[-1] and idx2char[predicted_id]) or (text_generated[-2] and idx2char[predicted_id])) == '\n':
                return (start_string + ''.join(text_generated).replace('\n ', '\n').replace('\t ', '\n'))
            # other wise we stop when we generate 2000 characters
            else:
                text_generated.append(idx2char[predicted_id])

    return (start_string + ''.join(text_generated).replace('\n ', '\n').replace('\t ', '\n'))