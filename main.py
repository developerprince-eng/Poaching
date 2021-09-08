import pandas as pd
import numpy as np


def main():
    df = pd.read_excel("RhinoPoaching.xlsx", sheet_name='Sheet2',
                       header=1)  # can also index sheet by name or fetch all sheets
    x_list = df['X'].tolist()
    y_list = df['Y'].tolist()
    z_list = df['Z'].tolist()

    print("Country X :: ", format(x_list))
    print("Country Y :: ", format(y_list))
    print("Country Z :: ", format(z_list))

    np.array([x_list, y_list, z_list])


if __name__ == '__main__':
    main()
