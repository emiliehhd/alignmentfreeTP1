import heapq
import math

def kmer2str(val, k):
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)


def stream_kmers(text, k):
    # Precompute the (k-1)-mer (and reverse)
    kmer = 0
    rkmer = 0
    for letter in text[:k-1]:
        # A = 00, C = 01, T = 10, G = 11
        # Forward kmer
        kmer <<= 2
        letter_value = (ord(letter) >> 1) & 0b11
        kmer += letter_value
        # Reverse kmer
        rkmer >>= 2
        rev_letter_value = (letter_value + 2) & 0b11
        rkmer += rev_letter_value << (2 * (k - 1))

    # Stream kmers
    mask = (1 << (2 * k)) - 1
    for letter in text[k-1:]:
        # Forward kmer
        kmer <<= 2
        letter_value = (ord(letter) >> 1) & 0b11
        kmer += letter_value
        kmer &= mask
        # Reverse kmer
        rkmer >>= 2
        rev_letter_value = (letter_value + 2) & 0b11
        rkmer += rev_letter_value << (2 * (k - 1))

        yield kmer, rkmer


def echantillonage(texts, k, s):
    """texts is a list that contains all the sequences of the genome
    s: le nombre de kmer dans l'echantillon"""
    sketch = [-math.inf] * s
    heapq.heapify(sketch)

    for seq in texts:                                   # to take in consideration every sequence of the file
        for kmer,rkmer in stream_kmers(seq, k):
            element =sketch[0]
            smallest_kmer = min(kmer, rkmer)            # choose the smallest kmer
            if -smallest_kmer > element:                # -kmer because element is negative
                heapq.heappop(sketch)                   # enlever plus petit
                heapq.heappush(sketch, -smallest_kmer)
    return sketch

