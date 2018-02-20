from multilabel import multilabel_train_test_split
import pandas as pd
import numpy as np
import random
from warnings import warn

NUMERIC_COLUMNS = ['FTE', 'Total']
LABELS = ['Function',
          'Use',
          'Sharing',
          'Reporting',
          'Student_Type',
          'Position_Type',
          'Object_Type',
          'Pre_K',
          'Operating_Status']


def getTrainingData():
    filename = "TrainingData.csv"
    n = sum(1 for line in open(filename)) - 1  # number of records in file (excludes header)
    s = 24960  # desired sample size
    skip = sorted(random.sample(range(1, n + 1), n - s))  # the 0-indexed header will not be included in the skip list
    df = pd.read_csv(filename, skiprows=skip, index_col=0)

    df.drop(df[df['FTE'] > 1.04].index, inplace=True)
    return df

def multilabel_sample(y, size=1000, min_count=5, seed=None):
    """ Takes a matrix of binary labels `y` and returns
        the indices for a sample of size `size` if
        `size` > 1 or `size` * len(y) if size =< 1.
        The sample is guaranteed to have > `min_count` of
        each label.
    """
    try:
        if (np.unique(y).astype(int) != np.array([0, 1])).all():
            raise ValueError()
    except (TypeError, ValueError):
        raise ValueError('multilabel_sample only works with binary indicator matrices')

    print("min_count: {}".format(min_count))
    print("y:\n", y.sum(axis=0))
    if (y.sum(axis=0) < min_count).any():
        raise ValueError('Some classes do not have enough examples. Change min_count if necessary.')

    if size <= 1:
        size = np.floor(y.shape[0] * size)

    if y.shape[1] * min_count > size:
        msg = "Size less than number of columns * min_count, returning {} items instead of {}."
        warn(msg.format(y.shape[1] * min_count, size))
        size = y.shape[1] * min_count

    rng = np.random.RandomState(seed if seed is not None else np.random.randint(1))

    if isinstance(y, pd.DataFrame):
        choices = y.index
        y = y.values
    else:
        choices = np.arange(y.shape[0])

    sample_idxs = np.array([], dtype=choices.dtype)

    # first, guarantee > min_count of each label
    for j in range(y.shape[1]):
        label_choices = choices[y[:, j] == 1]
        label_idxs_sampled = rng.choice(label_choices, size=min_count, replace=False)
        sample_idxs = np.concatenate([label_idxs_sampled, sample_idxs])

    sample_idxs = np.unique(sample_idxs)

    # now that we have at least min_count of each, we can just random sample
    sample_count = int(size - sample_idxs.shape[0])

    # get sample_count indices from remaining choices
    remaining_choices = np.setdiff1d(choices, sample_idxs)
    remaining_sampled = rng.choice(remaining_choices,
                                   size=sample_count,
                                   replace=False)

    return np.concatenate([sample_idxs, remaining_sampled])


def multilabel_train_test_split(X, Y, size, min_count=5, seed=None):
    """ Takes a features matrix `X` and a label matrix `Y` and
        returns (X_train, X_test, Y_train, Y_test) where all
        classes in Y are represented at least `min_count` times.
    """
    index = Y.index if isinstance(Y, pd.DataFrame) else np.arange(Y.shape[0])

    test_set_idxs = multilabel_sample(Y, size=size, min_count=min_count, seed=seed)
    train_set_idxs = np.setdiff1d(index, test_set_idxs)

    test_set_mask = index.isin(test_set_idxs)
    train_set_mask = ~test_set_mask

    return (X[train_set_mask], X[test_set_mask], Y[train_set_mask], Y[test_set_mask])

df = getTrainingData()

# Create the DataFrame: numeric_data_only
numeric_data_only = df[NUMERIC_COLUMNS].fillna(-1000)

# Get labels and convert to dummy variables: label_dummies
label_dummies = pd.get_dummies(df[LABELS])

while (label_dummies.sum(axis=0) < 5).any():
    print("KO")
    sums = label_dummies.apply(sum)
    print(sums[sums < 5])

    df = getTrainingData()

    # Create the DataFrame: numeric_data_only
    numeric_data_only = df[NUMERIC_COLUMNS].fillna(-1000)

    # Get labels and convert to dummy variables: label_dummies
    label_dummies = pd.get_dummies(df[LABELS])

print("OK")
df.to_csv("TrainingDataSample.csv")
sums = label_dummies.apply(sum)
print(sums[sums < 5])
#print("numeric data only: \n", numeric_data_only.info())
#print("label dummies: \n", label_dummies.info())

# Create training and test sets
#X_train, X_test, y_train, y_test = multilabel_train_test_split(numeric_data_only,label_dummies,size=0.2,seed=123)


