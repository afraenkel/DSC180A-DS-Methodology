
import os
import pandas as pd
from joblib import dump
import time
from sklearn.linear_model import LogisticRegression

TRAINCOLS = [
    'Week', '1stD', 'PassY', 'RushY', 'Offense'
]

TAG = 'Unnamed: 5_level_1' # W or L


def data_loader(indir, traincols=TRAINCOLS, tag=TAG):

    df = pd.concat([pd.read_csv(os.path.join(indir, p)) for p in os.listdir(indir)])

    X = df[traincols]
    y = df[tag]

    return X, y


def train_model(X, y, outdir=None):

    lr = LogisticRegression()
    lr.fit(X, y)

    if outdir:
        t = int(time.time())
        dump(lr, os.path.join(outdir, 'lr-model-%d.joblib' % t))

    return lr


def driver(indir, outdir=None):

    if outdir and not os.path.exists(outdir):
        os.makedirs(outdir)

    X, y = data_loader(indir)
    train_model(X, y, outdir)
    return
