import re
import glob

all_files = glob.glob("/Users/bill/Documents/Corpus Files/British National Corpus/Spoken Text Only/*.txt")

for i in range(0,len(all_files)):
    current_file = all_files[i]
    open_file = open(current_file, "r+")
    content = open_file.read()
    #content = content.replace("</w>","")
    x = re.sub(r'^.*[<stext>|<stext \w*=\"\w*\">]', r'', content.rstrip())
    x = re.sub(r'<.*?>', r'', x.rstrip())
    print(x)
    writeFile = str(input("Do you want to write the file " + current_file + "(Y OR N)"))
    if writeFile == "y":
        with open(current_file, 'w') as file:
            file.write(x)
    elif writeFile == "n":
        pass
    i += 1
