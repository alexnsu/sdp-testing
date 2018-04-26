import logging

import pandas as pd

def get_df(dataset, version):
    df = pd.read_csv('datasets/{}/{}.csv'.format(dataset, version), delimiter=',')
    df = df.filter(items=['name.1', 'bug'])
    df = df.loc[df['bug'] >= 1]

    return df['name.1'].tolist()

def check_dupes(train, test):
    counter = 0
    for f in train:
        if any(f in s for s in test):
            counter += 1

    return counter

def main():
    datasets = ['camel', 'jedit', 'lucene', 'poi', 'synapse', 'xalan', 'xerces']
    for ds in datasets:
        logging.info("Analysing dataset:\t{}".format(ds))
        train = get_df(ds, 'train')
        test = get_df(ds, 'test')

        n_dupes = check_dupes(train, test)
        n_test = len(test)

        print("Checking dataset:\t\t\t\t\t{}".format(ds))
        print("Overlapping buggy files between training and test set:\t{}".format(n_dupes))
        print("Number of buggy files in test set:\t\t\t{}".format(n_test))
        print("Ratio:\t\t\t\t\t\t\t{0:.2f}".format(n_dupes/n_test))
        print()

if __name__ == '__main__':
    logging.basicConfig(filename='logs.log',level=logging.DEBUG, format='%(asctime)s %(message)s', filemode='w')
    try:
        main()
    except Exception as e:
        logging.exception("Main crashed. Error:\n%s", e)

