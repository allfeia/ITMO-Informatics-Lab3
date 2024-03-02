yaml = []
file = open('xml.input.xml')
strings = file.readlines()
for i in range(len(strings)):

    strings[i] = strings[i].replace('<', '')
    strings[i] = strings[i].replace('>', ': ')

    if '/' in strings[i]:
        strings[i] = strings[i][:strings[i].find('/')]
    if ': ' in strings[i]:
        strings[i] = strings[i][:strings[i].find(':')+2]+'"'+strings[i][strings[i].find(':')+2:]+'"'
    if '\n' in strings[i]:
        strings[i] = strings[i][:strings[i].find(': ')+1]

    yaml.append(strings[i])

print(*yaml, sep="\n")

















