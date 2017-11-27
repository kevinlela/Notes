import fnmatch
import os

matches = []
for root, dirnames, filenames in os.walk('../Algorithm/'):
    for filename in fnmatch.filter(filenames, '*.md'):
    	whole_name = os.path.join(root, filename)
        os.rename(whole_name, whole_name.replace(' ', '_'))

matches = []
for root, dirnames, filenames in os.walk('../Algorithm/'):
    for filename in fnmatch.filter(filenames, '*.md'):
        matches.append(os.path.join(root, filename))

print matches

catelog = open('../Algorithm/Catelog.md', 'w')
catelog_offline = open('../Algorithm/Catelog_offline.md', 'w')
print matches
algorithmDict = {};
allQ = [];

for m in matches:
	file_name = m[m.rfind('/') + 1:]
	folder_name = m[:m.rfind('/')]
	algorithm_name = folder_name[folder_name.rfind('/') + 1:]
	print file_name
	print folder_name
	allQ.append(file_name);
	if (algorithm_name in algorithmDict):
		algorithmDict[algorithm_name].append(file_name)
	else:
		algorithmDict[algorithm_name]=[file_name]
	
def sortQuestion(allQ):
	qnums = []
	alprob = []
	for f in allQ:
		try:
			qnums.append(int(f[0:f.find('_')]))
			alprob.append(f)
		except ValueError:
			continue
			# qnums.append(0)
	vs = [f for (q,f) in sorted(zip(qnums,alprob))]

	return vs;

git_path = 'https://github.com/kevinlela/Notes/tree/master/Algorithm/'
off_path = '../Algorithm/'
for k, v in algorithmDict.items():
	catelog.write("## " + k.replace("_", " ") + "\n\n")
	catelog_offline.write("## " + k.replace("_", " ") + "\n\n")
	vs = sortQuestion(v)
	for f in vs:
		f_s = f.replace('_', '\_')
		catelog.write('[' + f_s[:f.rfind('.')] + '](' + git_path + k + '/' + f_s + ')\n\n')
		catelog_offline.write('[' + f[:f.rfind('.')] + '](' + off_path + k + '/' + f + ')\n\n')


catelog.write("\n\n")
catelog.write("### All Questions\n\n")
allQ = sortQuestion(allQ)
num = 1
for f in allQ:
	f_s = f.replace('_', '\_')
	catelog.write(str(num) + '.' + '[' + f_s[:f.rfind('.')] + '](' + f_s + ')\n\n')
	print str(num) + '.' + '[' + f[:f.rfind('.')] + '](' + f + ')'
	num += 1
