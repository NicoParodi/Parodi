a = ["Master", "Online"]
b = "Code"
a.insert(1, "Code")
print(a)

c = [1, 2, 3]
c = [4, 5, 6]
d = [1, 2, 3]
c.insert(0, d)
print(c)

Pep_Guardiola = ["Suarez", "Neymar", "Messi", "Xavi", "Iniesta", "Pique", "Ter Stegen", "Puyol", "Dani Alves", "Jordi Alba", "Sergio Busquet"]
Pep_Guardiola.sort()
print(Pep_Guardiola)

Pep_Guardiola = ["Suarez", "Neymar", "Messi", "Xavi", "Iniesta", "Pique", "Ter Stegen", "Puyol", "Dani Alves", "Jordi Alba", "Sergio Busquet"]
Pep_Guardiola.sort(reverse = True)
print(Pep_Guardiola)

Pep_Guardiola = ["Suarez", "Neymar", "Messi", "Javi", "Xavi", "Iniesta", "Pique", "Ter Stegen", "Puyol", "Dani Alves", "Jordi Alba", "Sergio Busquet"]
Pep_Guardiola.sort(reverse = True, key = len)
print(Pep_Guardiola)