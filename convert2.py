import sys

import pandas as pd
import pyarrow as pa

SPLIT_ROWS = 1000000

def main():
    schema = pa.Table.from_pandas(pd.read_csv('5000 Sales Records.csv',nrows=2)).schema 
    ### reads first two lines to define schema 

    with pa.OSFile('test.arrow', 'wb') as sink:
        with pa.RecordBatchFileWriter(sink, schema) as writer:            
            for split in pd.read_csv('5000 Sales Records.csv',chunksize=SPLIT_ROWS):
                table = pa.Table.from_pandas(split)
                writer.write_table(table)

            writer.close()

if __name__ == "__main__":
    main()  