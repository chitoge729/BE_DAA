import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    char_freq = {}
    for char in data:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    heap = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(node, current_code, huffman_codes):
    if node is None:
        return

    if node.char:
        huffman_codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + '0', huffman_codes)
    build_huffman_codes(node.right, current_code + '1', huffman_codes)

def huffman_encoding(data):
    if len(data) == 0:
        return "", None

    root = build_huffman_tree(data)
    huffman_codes = {}
    build_huffman_codes(root, "", huffman_codes)

    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data

if __name__ == "__main__":
    user_input = input("Enter the data to be Huffman encoded: ")
    encoded_data = huffman_encoding(user_input)

    print(f"Original data: {user_input}")
    print(f"Encoded data: {encoded_data}")
