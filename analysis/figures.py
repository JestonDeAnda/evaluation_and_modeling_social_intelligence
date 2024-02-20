import pickle
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm
import os
import torch




def generating_likelihood_sections_iip(gmap, routes,
                                       regions_log,
                                       params = [(0.3, 1), (0.99, 1), 
                                                 (0.3, 100), (0.99, 100)
                                                ],
                                       resolution = 200):
    
    for thres, pulse in params:
        results = np.zeros([resolution,resolution,4])
        # thres, pulse = 0.99, 1000

        for i, a in enumerate(np.linspace(0,1,resolution, endpoint=False) + 0.5/resolution):
            for j, b in enumerate(np.linspace(0,1,resolution, endpoint=False) + 0.5/resolution):
                # print(a, b)

                iip = S.IIP(torch.tensor([a,b, thres, pulse]), [1,2], routes, gmap)
                results[i,j,:] = iip.calculate(2,1).reshape(1,1,-1)

        fig, ax = plt.subplots(1,4)
        for i in range(4):
            ax[i].imshow(results[:,:100,i], vmin=0, vmax=1)

        regions_log[(thres, pulse)] = results.copy()
    return regions_log