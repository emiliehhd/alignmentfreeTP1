from loading import load_directory
from kmers_tme2 import *
import time

def jaccard_graph(fileA, fileB, k, s):
    jacc        = 0
    dic_kmers   = {}
    inter       = 0
    union       = 0

    for kmer in echantillonage(fileA, k, s):
        if kmer not in dic_kmers:
            dic_kmers[kmer] = 1
        else:
            dic_kmers[kmer] += 1
        union += 1

    for kmer in echantillonage(fileB, k, s):
        if kmer in dic_kmers:
            inter += 1
            dic_kmers[kmer] -= 1
            if dic_kmers[kmer] == 0:
                del dic_kmers[kmer]
        else:
            union += 1

    jacc = inter/union
    return jacc


if __name__ == "__main__":
    # Load all the files in a dictionary
    files       = load_directory("data")
    filenames   = list(files.keys())
    k           = 21
    s           = 10000

    for i in range(len(files)):
       for j in range(i+1, len(files)):

            print("\nStart comparison : ", filenames[i], "and", filenames[j])
            start_time = time.time()
            dist_jaccard = jaccard_graph(files[filenames[i]], files[filenames[j]], k, s)

            print("jaccard dist : ", dist_jaccard)
            end_time = time.time()
            print("Time taken to run the code:", end_time - start_time, "seconds")

