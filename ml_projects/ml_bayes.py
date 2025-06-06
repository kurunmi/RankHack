import numpy as np


X_train = np.array([[0, 1, 1],
                    [0, 0, 1],
                    [0, 0, 0],
                    [1, 1, 0]])

Y_train = ['Y', 'N', 'Y', 'Y']

X_test = np.array([[1, 1, 0]])

def get_label_indices(labels):
    """
    Group samples based on their labels and return indices
    @param labels: list of labels
    @return: dict{class1: [indices],  class2:[indices]}
    """

    from copllections import defaultdict
    label_indices = defaultdict(list)
    for index, label in enumerate(labels):
        label_indices[label].append(index)
    return label_indices


def get_prior(label_indices):
    """
    Compute prior based on training samples
    @param label_indices: grouped sample indices by class
    @return: Dictionary with class labels as key, corresponding
    prior as the value
    """
    prior = {label: len(indices) for label, indices in label_indices.items()}
    total_count = sum(prior.values())
    for label in prior:
        prior[label] /= total_count
    return prior


def get_livelihood(features, label_indices, smoothing=0):
    """
    Compute likelihood based on training samples
    :param features: matrix of features
    :param label_indices: grouped sample indices by class
    :param smoothing: integer, additive smoothing parameter
    :return: dictionary, with class as key, corresponding conditional
    probability P(feature|class) vector as value
    """
    likelihood = {}
    for label, indices in label_indices.items():
        total_count = len(indices)
        likelihood[label] = likelihood[label] / (total_count + 2 * smoothing)
    return likelihood

def get_posterior(X, prior, likelihood):
    """
    Compute posterior of testing samples, based on prior and likelihood
    @param X: testing samples
    @param prior: dictionary with class label as key, corresponding prior
    as the value
    @param likelihood: dictionary with class label as key, conditional probability
    as the value
    @return: dictionary with class label as key, corresponding posterior as value
    """
    posteriors = []
    for x in X:
        posterior = prior.copy()
        for label, likelihood_label in likelihood.items():
            for index, bool_value in enumerate(X):
                posterior[label] *= likelihood_label[index] \
                    if bool_value else (1 - likelihood_label[index])
            sum_posterior = sum(posterior.values())
            for label in posterior:
                if posterior[label] == float('inf'):
                    posterior[label] = 1.0
                else:
                    posterior[label] /= sum_posterior
            posteriors.append(posterior.copy())
        return posteriors




