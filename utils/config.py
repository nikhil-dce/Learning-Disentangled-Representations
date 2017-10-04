from .functional import *


class Config:
    def __init__(self, max_word_len, max_seq_len, word_vocab_size, char_vocab_size, learning_rate):

        self.learning_rate = learning_rate
        self.max_word_len = int(max_word_len)
        self.max_seq_len = int(max_seq_len) + 1  # go or eos token

        self.word_vocab_size = int(word_vocab_size)
        self.char_vocab_size = int(char_vocab_size)

        self.word_embed_size = 300
        self.char_embed_size = 15

        self.kernels = [(1, 25), (2, 50), (3, 75), (4, 100), (5, 125), (6, 150)]
        self.sum_depth = fold(lambda x, y: x + y, [depth for _, depth in self.kernels], 0)

        self.encoder_rnn_size = 600
        self.encoder_num_layers = 2

        self.latent_variable_size = 1100

        self.decoder_rnn_size = 600
        self.decoder_num_layers = 2


        # Sentiment Discriminator
        self.sentiment_kernel_size = [3,4,5]
        self.sentiment_kernel_num = 100
        self.sentiment_dropout = 0.3