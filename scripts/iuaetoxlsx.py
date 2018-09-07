import pandas as pd
import numpy as np
import argparse
from openpyxl import load_workbook

parser = argparse.ArgumentParser()
parser.add_argument("xlsxtemplate", help="the template to use for the output xlsx")
parser.add_argument("iuaetsv", help="tsv document that containts the IUAE matrix")
parser.add_argument("iuaexlsx", help="xlsx file to store the IUAE matrix in")
args = parser.parse_args()

twb = load_workbook(args.xlsxtemplate)
tws = twb.active
iuae = pd.read_csv(args.iuaetsv, sep='\t')

fields = { 'Introducera':'C', 'Undervisa':'D', 'Använda':'E', 'Examinera':'F', 'Kommentar':'G' }

for f,c in fields.items():
	for i in range(28):
		if iuae[f].loc[i] is not np.nan:
			tws[f'{c}{i+7}'] = iuae[f].loc[i]

twb.save(args.iuaexlsx)