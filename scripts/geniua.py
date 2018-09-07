import pandas as pd
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("courselist", help="list of courses in tsv format")
args = parser.parse_args()

#columns = [ 'Namn', '1.1', '1.2', '1.3', '2.1', '2.2', '2.3', '2.4', '2.5', '3.1', '3.2', '3.3', 
	#		'4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6' ]


cldf = pd.read_csv(args.courselist, sep='\t')

#rs = []
#ci = []
#for i,r in cldf.iterrows():
#	ci.append(r['Kod'])
#	t = [r['Namn']]
#	for i in range(len(columns)-1):
#		t.append('')
#	rs.append(t)

iuadf = pd.DataFrame(index=cldf['Kod'].tolist())#, columns=columns)

for fn in glob.iglob('[1-9]*.tsv'):
	if '_' not in fn:
		continue

	cdf = pd.read_csv(fn, sep='\t', dtype={'CDIO':str})

	cc = fn.split('_')[0]

	for i,r in cdf[['CDIO', 'Introducera', 'Undervisa', 'Använda']].iterrows():
		if not '.' in r['CDIO']:
			continue
		iua=''
		iua += 'I' if r['Introducera'] == 'X' else '' 
		iua += 'U' if r['Undervisa'] == 'X' else '' 
		iua += 'A' if r['Använda'] == 'X' else ''

		iuadf.at[cc, r['CDIO']] = iua

iuadf.to_csv('IUA.tsv', index_label='Kod', sep='\t')