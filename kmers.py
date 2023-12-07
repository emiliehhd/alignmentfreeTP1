import numpy as np

def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2
    str_val.reverse()
    return "".join(str_val)

def reverse_complement(mot_bit, k):
    """ Input : kmer read in the sequence. Compare the input kmer to its reverse complement and return the smallest one (alphabetically) """
    complement  = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    reverse     = ''
    mot         = kmer2str(mot_bit, k)
    for i in reversed(range(k)):
        reverse += complement[mot[i]]
    return min(mot, reverse)


def stream_kmers(text, k):
    """ To obtain kmers its integer representation(bit)"""
    encodage    = {'A': 0b00, 'C' : 0b01, 'T' : 0b10, 'G' : 0b11}
    mask        = (1<<(2*k))-1
    kmer        = 0
    kmer_final  = ''                                    # output kmer choosen between the kmer read and its reverse complement

    for i in (range(len(text)-k)):
        nucl = encodage[text[i]]
        kmer <<= 2
        kmer += nucl
        kmer &= mask
        if i >= k-1:            #on ignore les k-1 premieres itérations
            kmer_final = reverse_complement(kmer, k) #methode 1
            yield kmer_final



