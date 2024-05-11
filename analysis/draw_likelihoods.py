def draw_model_regions_iip(
        thres,
        pulse,
        regions_log,
        loc={
            'Shortest': [(30, 90), 90, 'x-large', 2],
            'Reversed': [(100, 100), 90, 'x-large', 0],
            'Hybrid': [(80, 20), 0, 'x-large', 1],
            'Avoidant': [(180, 110), 90, 'x-large', 3]
        },
        prefix="../figures",
        resolution=200):
    cs = [
        np.array([134, 197, 198]),
        np.array([253, 96, 78]),
        np.array([158, 171, 174]),
        np.array([202, 220, 111]),
    ]
    results = regions_log[(thres, pulse)]

    combined = np.zeros([resolution, resolution, 2], dtype=float)
    for i in range(resolution):
        for j in range(resolution):
            temp = results[i, j, :].copy()
            combined[i, j, 0] = np.argmax(temp)
            mtemp = np.max(temp)
            temp[int(combined[i, j, 0])] = 0.
            stemp = np.max(temp)
            combined[i, j, 1] = mtemp - stemp

    fig = plt.figure(figsize=[3.5, 3])
    ax = fig.subplots()
    c = ax.contourf(combined[:, :, 1].T,
                    levels=np.linspace(np.min(combined[:, :, 1]),
                                       np.max(combined[:, :, 1]), 400))

    borders = np.zeros([resolution, resolution, 4], dtype=float)
    for k in range(4):
        a = [0, 1, 2, 3]
        a.remove(k)
        borders[:, :, k] = results[:, :, k] - np.max(results[:, :, a], axis=2)
        ax.contour(borders[:, :, k].T,
                   levels=[0],
                   colors=['white', 'yellow', 'orange', 'red'][0:1])

    for key, val in loc.items():
        ax.text(*val[0],
                key,
                fontsize=val[2],
                rotation=val[1],
                c=cs[int(val[3])] / 255)

    ax.set_xticks([0, 99.5, 199])
    ax.set_xticklabels([0, "$exp(-\\alpha)$", 1])
    ax.set_yticks([0, 99.5, 199])
    ax.set_yticklabels([0, "$exp(-\\beta)$", 1],
                       rotation=90,
                       verticalalignment='center')
    fig.colorbar(c, ticks=np.linspace(0, 1, 10, endpoint=False))
    fig.tight_layout()
    fig.savefig(f"{prefix}/model_regions_{thres}_{pulse}.png", dpi=600)
