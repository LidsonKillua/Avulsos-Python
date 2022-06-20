import os

pasta = r'C:\\ThotauED\\ImgRpt\\Produtos'
# pasta = r'C:\\Projetos\\Python\\Renomear'

for name in os.listdir(pasta):
    newname = ''
    name = pasta + '\\' + name

    if '.TXT' in name[-4:]:
        newname = name[:-4] + '.txt'
        newname += '.txt'

        os.rename(name, newname)

"""
for name in os.listdir(pasta):
    newname = ''
    name = pasta + '\\' + name

    if '.TXT' in name[-4:]:
        
        for i in range(len(name) - 4):
            newname += name[i]

        newname += '.txt'
        os.rename(name, newname)
"""
