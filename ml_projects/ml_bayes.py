import numpy as np
import pandas as pd

from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import matplotlib


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

    from collections import defaultdict
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


def get_likelihood(features, label_indices, smoothing=0):
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
        likelihood[label] =  features[indices, :].sum(axis=0) + smoothing
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
            for index, bool_value in enumerate(x):
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


def load_user_rating(df, n_users, n_movies):
    """
    Load ratings from a Pandas dataset
    @param df: Pandas dataset
    @param n_users: Unique users
    @param n_movies: Unique Movies
    @return: Dictionary containing
    """
    data = np.zeros([n_users, n_movies], dtype=np.intc)
    movie_id_mapping = {}
    for user_id, movie_id, rating in zip(df['user_id'], df['movie_id'], df['rating']):
        user_id = int(user_id) -1
        if movie_id not in movie_id_mapping:
            movie_id_mapping[movie_id] = len(movie_id_mapping)
        data[user_id, movie_id_mapping[movie_id]] = rating
    return data, movie_id_mapping


def load_user_rating_new(df, n1, n2, col1, col2, col3):
    """
    Load ratings from a pandas dataset
    :param df: pandas dataset
    :param n1: unique set 1
    :param n2: unique set 2
    :return: dictionary containing a matrix of n1 by n2
    """
    data = np.zeros([n1, n2], dtype=np.intc)
    data_map = {}
    for value1, value2, value3 in zip(df[col1], df[col2], df[col3]):
        value1 = int(value1)
        if value2 not in data_map:
            data_map[value2] = len(data_map)
        data[value1, data_map[value2]] = value3
    return data, data_map




if __name__ == '__main__':
    #label_indices = get_label_indices(Y_train)
    #print(label_indices)
    #prior = get_prior(label_indices)
    #print("Prior:", prior)
    #smoothing=1
    #likelihood = get_likelihood(X_train, label_indices, smoothing)
    #print("Likelihoood:", likelihood)
    #posterior = get_posterior(X_test, prior, likelihood)
    #print("Posterior:", posterior)
    #clf = BernoulliNB(alpha=1.0, fit_prior=True)
    #clf.fit(X_train, Y_train)
    #pred_prob = clf.predict_proba(X_test)
    #pred = clf.predict(X_test)
    #print('Scikit-learn probability:', pred_prob)
    #print('Scikit-learn prediction:', pred)
    data_path = '/home/bona/data/ml-1m/ratings.dat'
    df = pd.read_csv(data_path, header=None, sep='::', engine='python')
    df.columns = ['user_id', 'movie_id', 'rating', 'timestamp']
    #print(df)
    n_users = df['user_id'].nunique()
    n_movies = df['movie_id'].nunique()
    print(f"Users: {n_users}, movies: {n_movies}")
    data, movie_id_mapping = load_user_rating(df, n_users, n_movies)
    #print(movie_id_mapping)
    values, counts = np.unique(data, return_counts=True)
    #for value, count in zip(values, counts):
    #    print(f"Rating {value}: {count}")
    #print(df['movie_id'].value_counts())

    target_movie_id = 2858
    X_raw = np.delete(data, movie_id_mapping[target_movie_id], axis=1)
    Y_raw = data[:, movie_id_mapping[target_movie_id]]
    X = X_raw[Y_raw > 0]
    Y = Y_raw[Y_raw > 0]
    #print(f"X Shape {X.shape} Y shape {Y.shape}")
    recommend = 3
    Y[Y <= recommend] = 0
    Y[Y > recommend] = 1
    n_pos = (Y == 1).sum()
    n_neg = (Y == 0).sum()
    #print(f"{n_pos} positives and {n_neg} negatives")
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15, random_state=42)
    print(len(Y_train), len(Y_test), len(Y_test)/len(Y_train) * 100)
    clf = MultinomialNB(alpha=1.0, fit_prior=True)
    clf.fit(X_train, Y_train)
    prediction_prob = clf.predict_proba(X_test)
    #print(prediction_prob[0:10])
    prediction = clf.predict(X_test)
    print(prediction[0:10])
    accuracy = clf.score(X_test, Y_test)
    print('Accuracy is', accuracy)
    print(confusion_matrix(Y_test, prediction, labels=[0, 1]))
    print(precision_score(Y_test, prediction, pos_label=1))
    print(recall_score(Y_test, prediction, pos_label=1))
    print(f1_score(Y_test, prediction, pos_label=1))
    print(f1_score(Y_test, prediction, pos_label=0))
    print(classification_report(Y_test, prediction))
    pos_prob = prediction_prob[:, 1]
    thresholds = np.arange(0.0, 1.1, 0.05)
    true_pos, false_pos = [0] * len(thresholds), [0] * len(thresholds)
    for pred, y in zip(pos_prob, Y_test):
        for i, threshold in enumerate(thresholds):
            if pred >= threshold:
                if y == 1:
                    true_pos[i] += 1
                else:
                    false_pos[i] += 1
            else:
                break
    n_pos_test = (Y_test == 1).sum()
    n_neg_test = (Y_test == 0).sum()
    true_pos_rate = [tp / n_pos_test for tp in true_pos]
    false_pos_rate = [fp / n_neg_test for fp in false_pos]
    plt.figure()
    lw = 2
    plt.plot(false_pos_rate, true_pos_rate, color='darkorange', lw=lw)
    plt.plot([0.1], [0.1], color='navy', lw='lw', linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Charateristic')
    plt.legend(loc="lower right")
    plt.show()

