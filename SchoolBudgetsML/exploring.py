import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def fnInit():
    df = pd.read_csv('TrainingData.csv',index_col=0)
    # print(df.info())
    # print(df.describe())
    # print("traindata shape: {}".format(df.shape))

    df.drop(df[df['FTE'] > 1.04].index, inplace=True)
    return df

def fnEDA():
    df =  fnInit()
    print(df.info())

    # Print the summary statistics
    print(df.describe())

    # Import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt

    # Create the histogram
    plt.hist(df['FTE'].dropna())

    # Add title and labels
    plt.title('Distribution of %full-time \n employee works')
    plt.xlabel('% of full-time')
    plt.ylabel('num employees')

    # Display the histogram
    plt.show()


def fnUniques():
    df = fnInit()
    print("Uniques values of the Object_Type:\n")
    print(df['Object_Type'].unique)


def fnExploringDataTypes():
    df = fnInit()
    print(df.dtypes)
    print("----------------")
    print(df.dtypes.value_counts())
    print("----------------")

def fnLabelsAsVariables():
    LABELS = ['Function', 'Use', 'Sharing', 'Reporting', 'Student_Type', 'Position_Type', 'Object_Type', 'Pre_K', 'Operating_Status']

    df = fnInit()

    # Define the lambda function: categorize_label
    categorize_label = lambda x: x.astype('category')

    # Convert df[LABELS] to a categorical type
    df[LABELS] = df[LABELS].apply(categorize_label)

    # Print the converted dtypes
    print(df[LABELS].dtypes)

def fnCoutingUniqLabels():
    LABELS = ['Function', 'Use', 'Sharing', 'Reporting', 'Student_Type', 'Position_Type', 'Object_Type', 'Pre_K',
              'Operating_Status']

    df = fnInit()

    # Import matplotlib.pyplot
    import matplotlib.pyplot as plt
    plt.gcf().subplots_adjust(bottom=0.4)

    # Calculate number of unique values for each label: num_unique_labels
    num_unique_labels = df[LABELS].apply(pd.Series.nunique)

    # Plot number of unique values for each label
    num_unique_labels.plot(kind='bar')

    # Label the axes
    plt.xlabel('Labels')
    plt.ylabel('Number of unique values')

    # Display the plot
    plt.show()

def compute_log_loss(predicted, actual, eps=1e-14):
    predicted = np.clip(predicted, eps, 1 - eps)
    loss = -1 * np.mean( actual * np.log(predicted)
                         + (1 - actual)
                         * np.log(1 - predicted))
    return loss

def fnLoglossWithNumpy():
    correct_confident = np.array([ 0.95,  0.95,  0.95,  0.95,  0.95,  0.05,  0.05,  0.05,  0.05,  0.05])
    correct_not_confident = np.array([ 0.65,  0.65,  0.65,  0.65,  0.65,  0.35,  0.35,  0.35,  0.35,  0.35])
    wrong_not_confident = np.array([ 0.35,  0.35,  0.35,  0.35,  0.35,  0.65,  0.65,  0.65,  0.65,  0.65])
    wrong_confident = np.array([ 0.05,  0.05,  0.05,  0.05,  0.05,  0.95,  0.95,  0.95,  0.95,  0.95])
    actual_labels = np.array([ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.])

    # Compute and print log loss for 1st case
    correct_confident = compute_log_loss(correct_confident, actual_labels)
    print("Log loss, correct and confident: {}".format(correct_confident))

    # Compute log loss for 2nd case
    correct_not_confident = compute_log_loss(correct_not_confident, actual_labels)
    print("Log loss, correct and not confident: {}".format(correct_not_confident))

    # Compute and print log loss for 3rd case
    wrong_not_confident = compute_log_loss(wrong_not_confident, actual_labels)
    print("Log loss, wrong and not confident: {}".format(wrong_not_confident))

    # Compute and print log loss for 4th case
    wrong_confident = compute_log_loss(wrong_confident, actual_labels)
    print("Log loss, wrong and confident: {}".format(wrong_confident))

    # Compute and print log loss for actual labels
    actual_labels = compute_log_loss(actual_labels, actual_labels)
    print("Log loss, actual labels: {}".format(actual_labels))


fnLoglossWithNumpy()