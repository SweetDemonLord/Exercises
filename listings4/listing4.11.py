age=dict([["Cat Matroskin",5],["Dog Bally",7],["Uncle Fedor",12]])
# Keys search
for s in age.keys():
    print(s+":", age[s])
# Enumeration of values
for v in age.values():
    print(v, end=" ")
print()
color=dict([[(255,0,0),"Red"],[(0,255,0),"Green"],[(0,0,255),"Blue"]])
# Accessing dictionary elements
color[(255,255,0)]="Yellow"
print("(255,0,0):", color[(255,0,0)])
print("(255,255,0):", color[(255,255,0)])
print("(0,255,0):", color.get((0,255,0)))
print("(0,0,255):", color.get((0,0,255), "White"))
print("(255,255,255):", color.get((255,255,255), "White"))
