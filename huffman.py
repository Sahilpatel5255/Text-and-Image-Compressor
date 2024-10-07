import heapq
import os
from collections import defaultdict
import struct
import json

# Huffman Node class
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman tree
def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

# Function to generate Huffman codes
def generate_huffman_codes(node, prefix="", codebook={}):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_huffman_codes(node.left, prefix + "0", codebook)
        generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

# Function to compress text using Huffman coding
def compress(text):
    if not text:
        return "", {}

    huffman_tree = build_huffman_tree(text)
    huffman_codes = generate_huffman_codes(huffman_tree)

    compressed_text = ''.join(huffman_codes[char] for char in text)
    return compressed_text, huffman_codes

# Function to decompress text using Huffman codes
def decompress(compressed_text, huffman_codes):
    if not compressed_text or not huffman_codes:
        return ""

    reverse_codebook = {v: k for k, v in huffman_codes.items()}
    current_code = ""
    decompressed_text = []

    for bit in compressed_text:
        current_code += bit
        if current_code in reverse_codebook:
            decompressed_text.append(reverse_codebook[current_code])
            current_code = ""

    return ''.join(decompressed_text)

class huffman:
    def compress_file(self, input_file):
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Compress the text
        compressed_text, huffman_codes = compress(text)

        if not compressed_text:
            raise ValueError("Input file is empty or compression failed.")

        # Convert the compressed text into bytes
        padded_bits = (8 - len(compressed_text) % 8) % 8
        compressed_text += '0' * padded_bits

        byte_array = bytearray()
        for i in range(0, len(compressed_text), 8):
            byte_array.append(int(compressed_text[i:i + 8], 2))

        # Create the output file path
        output_file = input_file + '.huff'

        # Write the compressed data and codebook to the output file in binary format
        with open(output_file, 'wb') as file:
            # Write the length of padding
            file.write(struct.pack('B', padded_bits))

            # Write the codebook as a JSON string in binary format
            codebook_bytes = json.dumps(huffman_codes).encode('utf-8')
            file.write(struct.pack('I', len(codebook_bytes)))
            file.write(codebook_bytes)

            # Write the compressed data
            file.write(byte_array)

        return output_file

    def decompress_file(self, input_file):
        # Read the compressed file
        with open(input_file, 'rb') as file:
            # Read the length of padding
            padded_bits = struct.unpack('B', file.read(1))[0]

            # Read the length of the codebook and then the codebook itself
            codebook_length = struct.unpack('I', file.read(4))[0]
            codebook_bytes = file.read(codebook_length)
            huffman_codes = json.loads(codebook_bytes.decode('utf-8'))

            # Read the compressed text in binary format
            compressed_text_bits = ""
            byte = file.read(1)
            while byte:
                compressed_text_bits += f"{int.from_bytes(byte, 'big'):08b}"
                byte = file.read(1)

            # Remove the padding bits
            if padded_bits > 0:
                compressed_text_bits = compressed_text_bits[:-padded_bits]

        # Decompress the text
        decompressed_text = decompress(compressed_text_bits, huffman_codes)

        return decompressed_text

# Example usage
if __name__ == "__main__":
    huff = huffman()
    input_file = "example.txt"  # Replace with your input file path

    try:
        compressed_file = huff.compress_file(input_file)
        print(f"Compressed file saved at: {compressed_file}")

        decompressed_text = huff.decompress_file(compressed_file)
        output_file = input_file.replace('.txt', '_decompressed.txt')
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decompressed_text)
        print(f"Decompressed file saved at: {output_file}")

    except Exception as e:
        print(f"Error: {e}")
