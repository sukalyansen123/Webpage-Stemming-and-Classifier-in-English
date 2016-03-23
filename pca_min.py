import numpy as np

all_samps = np.array([
       [ 1.62434536, -1.07296862,  1.74481176, 0.225],
       [-0.61175641,  0.86540763, -0.7612069 , 0.334],
       [-0.52817175, -2.3015387 ,  0.3190391 , 0.0112]
       ])
def pca(all_samples,k=2):
    n = all_samples.shape[0]
    mean = [[np.mean(all_samples[i,:])] for i in range(n)]
    mean_vector = np.array(mean)

    scatter_matrix = np.zeros((n,n))
    for i in range(all_samples.shape[1]):
        scatter_matrix += (all_samples[:,i].reshape(n,1) - mean_vector).dot((all_samples[:,i].reshape(n,1) - mean_vector).T)

    eig_val_sc, eig_vec_sc = np.linalg.eig(scatter_matrix)
    for i in range(len(eig_val_sc)):
        eigvec_sc = eig_vec_sc[:,i].reshape(1,n).T

    eig_pairs = [(np.abs(eig_val_sc[i]), eig_vec_sc[:,i]) for i in range(len(eig_val_sc))]
    for i in range(len(eig_pairs)):
        max = i
        for j in range(i+1,len(eig_pairs)):
            if(eig_pairs[j][0]>eig_pairs[max][0]):
                max = j
        temp = eig_pairs[i]
        eig_pairs[i] = eig_pairs[max]
        eig_pairs[max] = temp
##    print eig_pairs
##    input()
##    print eig_val_sc

    matrix_w = np.hstack([eig_pairs[i][1].reshape(n,1) for i in range(k)])
##    print('Matrix W:\n', matrix_w)

    transformed = matrix_w.T.dot(all_samples)
##    print('Transformed :\n', transformed)
    return matrix_w.transpose(),transformed.transpose()

##pca(all_samps)
