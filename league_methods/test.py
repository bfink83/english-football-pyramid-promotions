import pandas as pd
import dataframe_image as dfi
 
df = pd.DataFrame({'A': [5,6,7,8],
                   'B':['A','B','C','D']})
 
dfi.export(df, './TEST.png')