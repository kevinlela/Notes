import fnmatch
import os

matches = []
for root, dirnames, filenames in os.walk('../Algorithm/'):
    for filename in fnmatch.filter(filenames, '*.md'):
        matches.append(os.path.join(root, filename))

print matches

catelog = open('../Algorithm/Catelog.md', 'w')
print matches
algorithmDict = {};
allQ = [];

for m in matches:
	file_name = m.split('/')[-1]
	folder_name = m.split('/')[-2]
	print file_name
	print folder_name
	allQ.append(file_name);
	if (folder_name in algorithmDict):
		algorithmDict[folder_name].append(file_name)
	else:
		algorithmDict[folder_name]=[file_name]
	
def sortQuestion(allQ):
	qnums = []
	for f in allQ:
		try:
			qnums.append(int(f[0:f.find('_')]))
		except ValueError:
			qnums.append(0)
	vs = [f for (q,f) in sorted(zip(qnums,allQ))]
	return vs;


for k, v in algorithmDict.items():
	catelog.write("##" + k.replace("_", " ") + "\n")
	vs = sortQuestion(v)
	for f in vs:
		catelog.write('[' + f + '](' + './' + k + '/' + f + ')\n')


catelog.write("\n\n")
catelog.write("### All Questions\n")
allQ = sortQuestion(allQ)
for f in allQ:
	catelog.write('[' + f + '](' + f + ')\n')
