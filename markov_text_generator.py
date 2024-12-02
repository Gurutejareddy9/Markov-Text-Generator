import random
import re

class MarkovTextGenerator:
    def __init__(self, source_text, chain_length=2):
        self.source_text = source_text
        self.chain_length = chain_length
        self.markov_chain = self._build_markov_chain()

    def _build_markov_chain(self):
        chain = {}
        for i in range(len(self.source_text) - self.chain_length):
            key = self.source_text[i:i + self.chain_length]
            value = self.source_text[i + self.chain_length]
            if key in chain:
                chain[key].append(value)
            else:
                chain[key] = [value]
        return chain

    def generate_text(self, length=100):
        if not self.markov_chain:
            return "Insufficient source text to generate new text."
        
        key = random.choice(list(self.markov_chain.keys()))
        generated_text = list(key)
        
        for _ in range(length - self.chain_length):
            if key in self.markov_chain:
                next_char = random.choice(self.markov_chain[key])
                generated_text.append(next_char)
                key = key[1:] + next_char
            else:
                break
        
        return ''.join(generated_text)

def main():
    source_text = input("Enter/Paste the source text: ")
    generator = MarkovTextGenerator(source_text, chain_length=3)
    print("Generated Text:")
    print(generator.generate_text(length=200))

if __name__ == "__main__":
    main()
