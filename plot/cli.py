import argparse
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def main():
    parser = argparse.ArgumentParser( description="This plot csv" )
    parser.add_argument("path", type=str)
    parser.add_argument("-x", type=str)
    parser.add_argument("y", type=str)
    

    parser.add_argument("--xlim", type=str, default=None)
    parser.add_argument("--ylim", type=str, default=None)

    args = parser.parse_args()
    if args.xlim:
        xmin, xmax = tuple(args.xlim.split(":"))
        
    df = pd.read_csv(args.path)
    y = df[args.y]
    if args.x:
        x = df[args.x]
    else:
        x = None

    ##ig = plt.figure()
    fig = plt.figure(figsize=(8, 6))
    axes = plt.subplot()
    #axes.set_xlim(0,30)
    if args.xlim:
        xmin, xmax = tuple(map(int, args.xlim.split(":")))
        axes.set_xlim([xmin, xmax])
    if args.ylim:
        ymin, ymax = tuple(map(int, args.ylim.split(":")))
        axes.set_ylim([ymin, ymax])
    if x is not None:
        plt.plot(x.to_numpy(),y.to_numpy())
    else:
        plt.plot(y.to_numpy())
    plt.show()
    
    
if __name__ == "__main__":
    main()
