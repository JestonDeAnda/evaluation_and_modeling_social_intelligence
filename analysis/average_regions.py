"""
Generate regional figures for multiple examples.
"""
import json
import pickle
import numpy as np
import multiprocessing as mp
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm
import os
import torch
import signal_model_torch as S
from regression import parse_json_prompt, construct_board, calculate

if __name__ == '__main__':
    prefix = "../data/regions/"
    files = list(os.walk(prefix))[0][2]
    print(files)
    with open(prefix + fname, "rb") as fp:
        data = pickle.load(fp)

    print(data)
