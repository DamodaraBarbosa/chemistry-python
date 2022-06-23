import pubchempy as pcp

results = pcp.get_compounds('FeSO4', 'smiles')
# nome = pcp.Compound.from_cid(f'{c}')
print(results)
# for i in results:
#     i = composto
# print(composto)
# # for i in composto:
#     print(i)
# for i, l in enumerate(results):
#     for i, l in enumerate(results[i]):
#         if i.isnumeric() == True:
#             print(l)
c1 = pcp.Compound.from_cid(24393)
# c2 = pcp.Compound.from_cid(5460455)
# c3 = pcp.Compound.from_cid(6973630)

print(c1.iupac_name)
# print(c2.iupac_name)
# print(c3.iupac_name)

# print(nome)