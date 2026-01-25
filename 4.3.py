luku=input("Anna Luku: ")
if luku!='':
    lukuS=float(luku)
    vertausS=vertausP=lukuS
else:
    vertausS = vertausP="ei arvoa"
while luku !='':
    luku =input("Anna Luku: ")
    if (luku !=''):
        lukuS = float(luku)
        if(lukuS>vertausS):
            vertausS=lukuS
        if(lukuS<=vertausP):
            vertausP=lukuS
print(f"{vertausS} on suurin ja {vertausP} on pienin")