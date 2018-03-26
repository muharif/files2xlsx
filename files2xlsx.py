import imp
if imp.util.find_spec("pandas") is None:
    raise ModuleNotFoundError('Please install pandas "pip install pandas" or "conda install pandas"')
if imp.util.find_spec("xlsxwriter") is None:
    raise ModuleNotFoundError('Please install xlsxwriter "pip install xlsxwriter" or "conda install xlsxwriter"')
import pandas as pd
import pandas as pd
import sys
import os
if os.path.isdir(sys.argv[1]):
    fn=os.listdir(sys.argv[1])
elif os.path.isfile(sys.argv[1]):
    fn=open(sys.argv[1],'r').readlines()
else:
    raise FileNotFoundError('File or folder %s not found' % sys.argv[1])
if sys.argv[2] == 'tab':
    sep='\t'
elif sys.argv[2] == 'csv':
    sep=','
else:
    raise ValueError('Unknown delimiter, select tab or csv')
if len(sys.argv) > 2:
    name=sys.argv[3]+'.xlsx'
else:
    name='combined.xlsx'
print(sys.argv)
df=[pd.read_csv(i.rstrip('\n').rstrip('\r'),sep=sep,index_col=0) for i in fn]
writer = pd.ExcelWriter(name, engine='xlsxwriter')
for i in range(len(df)):
    if len(fn[i]) > 31:
        sname=fn[i][0:31]
    else:
        sname=fn[i]
    df[i].to_excel(writer, sheet_name=sname)
writer.save()
