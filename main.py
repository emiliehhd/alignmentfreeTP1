from loading import load_directory
from kmers import stream_kmers, kmer2str
import pandas as pd
import time

def jaccard(fileA, fileB, k):
    jacc        = 0
    dic_kmers   = {}
    inter       = 0
    union       = 0
    for seq_i in range(len(fileA)):
        for kmer in stream_kmers(fileA[seq_i], k):
            if kmer not in dic_kmers:
                dic_kmers[kmer] = 1
            else:
                dic_kmers[kmer] += 1
            union += 1

    for seq_j in range(len(fileB)):
        for kmer in stream_kmers(fileB[seq_j], k):
            if kmer in dic_kmers:
                inter               += 1
                dic_kmers[kmer]     -= 1
                if dic_kmers[kmer] == 0:
                    del dic_kmers[kmer]
            else:
                union +=1
    jacc = inter/union
    return jacc



if __name__ == "__main__":

    # Load all the files in a dictionary
    files       = load_directory("data")
    filenames   = list(files.keys())
    k           = 21
    df_jaccard  = pd.DataFrame(0, columns=filenames, index=filenames)


    # j = jaccard(files[filenames[0]], files[filenames[2]], k)  ##test
    # print(j)

    for i in range(len(files)):
        for j in range(i+1, len(files)):

            print("\nStart comparison : ", filenames[i], "and", filenames[j])
            start_time = time.time()

            dist_jaccard = jaccard(files[filenames[i]], files[filenames[j]], k)

            print(filenames[i], filenames[j], dist_jaccard)
            df_jaccard[filenames[i]][filenames[j]] = dist_jaccard

            end_time = time.time()
            print("Time taken to run the code:", end_time - start_time, "seconds")

    print(df_jaccard)
