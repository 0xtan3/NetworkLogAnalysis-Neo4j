import os
import pandas as pd
from falkordb import FalkorDB

db = FalkorDB(host='localhost', port=6379)

dataset_dir = './data'

def main(
    data = pd.read_csv(os.path.join(dataset_dir,'<file.csv>'))

    for 
)


if __name__ == "__main__":
    main()