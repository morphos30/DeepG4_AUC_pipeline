from keras.utils import to_categorical
import numpy as np
def padding(mat, max_seq):
    # =============================================================================
    #     This function creates zero padding by conctinating it with a matrix of zeros
    #     Input: mat - the original one hot matrix, max_seq - the final width of the matrix
    #     Output: concate - the zerro padded matrix
    # =============================================================================
    length = max_seq - mat.shape[0]
    ze = np.zeros((length, mat.shape[1]), dtype='int')
    concate = np.concatenate((mat, ze), axis=0)
    return concate

def oneHot(string, max_seq=297):
  # =============================================================================
  #   This function creats one hot encoding to a given DNA string
  #     Input: string - the DNA string, max_seq - final length of the sequence
  #     Output: one_hot - the encoded matrix
  # =============================================================================
  trantab = str.maketrans('ACGT', '0123')
  string = string + 'ACGT'
  data = list(string.translate(trantab))
  mat = to_categorical(data)[0:-4]
  mat = padding(mat, max_seq).flatten()
  # mat = padding(mat, max_seq)
  return mat
