import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch

np.random.seed(1)# random seed for consistency

mu_vec1 = np.array([0,0,0])
cov_mat1 = np.array([[1,0,0],[0,1,0],[0,0,1]])
class1_sample = np.random.multivariate_normal(mu_vec1, cov_mat1, 20).T
assert class1_sample.shape == (3,20), "The matrix has not the dimensions 3x20"

mu_vec2 = np.array([1,1,1])
cov_mat2 = np.array([[1,0,0],[0,1,0],[0,0,1]])
class2_sample = np.random.multivariate_normal(mu_vec2, cov_mat2, 20).T
assert class1_sample.shape == (3,20), "The matrix has not the dimensions 3x20"

##fig = plt.figure(figsize=(8,8))
##ax = fig.add_subplot(111, projection='3d')
##plt.rcParams['legend.fontsize'] = 10
##ax.plot(class1_sample[0,:], class1_sample[1,:], class1_sample[2,:],
##'o', markersize=8, color='blue', alpha=0.5, label='class1')
##ax.plot(class2_sample[0,:], class2_sample[1,:], class2_sample[2,:],
##'^', markersize=8, alpha=0.5, color='red', label='class2')
##plt.title('Samples for class 1 and class 2')
##ax.legend(loc='upper right')
##plt.show()

all_samples = np.concatenate((class1_sample, class2_sample), axis=1)
assert all_samples.shape == (3,40), "The matrix has not the dimensions 3x40"

mean_x = np.mean(all_samples[0,:])
mean_y = np.mean(all_samples[1,:])
mean_z = np.mean(all_samples[2,:])
mean_vector = np.array([[mean_x],[mean_y],[mean_z]])
#print('Mean Vector:\n', mean_vector)

scatter_matrix = np.zeros((3,3))
for i in range(all_samples.shape[1]):
    scatter_matrix += (all_samples[:,i].reshape(3,1) - mean_vector).dot((all_samples[:,i].reshape(3,1) - mean_vector).T)
#print('Scatter Matrix:\n', scatter_matrix)

# eigenvectors and eigenvalues for the from the scatter matrix
eig_val_sc, eig_vec_sc = np.linalg.eig(scatter_matrix)
for i in range(len(eig_val_sc)):
    eigvec_sc = eig_vec_sc[:,i].reshape(1,3).T
##    assert eigvec_sc.all() == eigvec_cov.all(), 'Eigenvectors are not identical'
##    print('Eigenvector {}: \n{}'.format(i+1, eigvec_sc))
##    print('Eigenvalue {} from scatter matrix: {}'.format(i+1, eig_val_sc[i]))
##    print('Eigenvalue {} from covariance matrix: {}'.format(i+1, eig_val_cov[i]))
##    print('Scaling factor: ', eig_val_sc[i]/eig_val_cov[i])
##    print(40 * '-')

eig_pairs = [(np.abs(eig_val_sc[i]), eig_vec_sc[:,i]) for i in range(len(eig_val_sc))]
eig_pairs.sort()
eig_pairs.reverse()
# Visually confirm that the list is correctly sorted by decreasing eigenvalues
##for i in eig_pairs:
##    print(i[0])

matrix_w = np.hstack((eig_pairs[0][1].reshape(3,1),eig_pairs[1][1].reshape(3,1)))
print('Matrix W:\n', matrix_w)

transformed = matrix_w.T.dot(all_samples)
##assert transformed.shape == (2,40), "The matrix is not 2x40 dimensional."
##plt.plot(transformed[0,0:20], transformed[1,0:20],'o', markersize=7, color='blue', alpha=0.5, label='class1')
##plt.plot(transformed[0,20:40], transformed[1,20:40],'^', markersize=7, color='red', alpha=0.5, label='class2')
##plt.xlim([-5,5])
##plt.ylim([-5,5])
##plt.xlabel('x_values')
##plt.ylabel('y_values')
##plt.legend()
##plt.title('Transformed samples with class labels')
##plt.show()
