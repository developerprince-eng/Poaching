import pandas as pd
import numpy as np
def main():
    df = pd.read_excel('RhinoPoaching.xlsx', sheet_name='Sheet2', header=1)  # can also index sheet by name or fetch all sheets
    xlist = df['X'].tolist()
    ylist = df['Y'].tolist()
    zlist = df['Z'].tolist()

    print("Country X :: ",format(xlist))
    print("Country Y :: ",format(ylist))
    print("Country Z :: ",format(zlist))

    np.array([xlist, ylist, zlist])


if __name__ == '__main__':
    main()