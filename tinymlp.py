# tinymlp.py
import math, random

class TinyMLP:
    def __init__(self, input_size=10, hidden_size=5, output_size=1):
        # random weights
        self.w1 = [[random.uniform(-1, 1) for _ in range(input_size)] for _ in range(hidden_size)]
        self.b1 = [random.uniform(-1, 1) for _ in range(hidden_size)]
        self.w2 = [random.uniform(-1, 1) for _ in range(hidden_size)]
        self.b2 = random.uniform(-1, 1)

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def forward(self, inputs):
        hidden = []
        for i, w_row in enumerate(self.w1):
            h = sum([x * w for x, w in zip(inputs, w_row)]) + self.b1[i]
            hidden.append(self.sigmoid(h))
        out = sum([hidden[i] * self.w2[i] for i in range(len(hidden))]) + self.b2
        return self.sigmoid(out)

# helpers
def encodeText(text, max_length=10):
    array = [ord(c) % 10 for c in text[:max_length]]
    while len(array) < max_length:
        array.append(0)
    return array

def runMLP(text):
    mlp = TinyMLP()
    encoded = encodeText(text=text)
    result = mlp.forward(encoded)
    print(f"[TinyMLP output] {result:.3f}")
