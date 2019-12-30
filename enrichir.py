import sys, re

corpus_medical = open(sys.argv[1], 'r', encoding="utf-8").readlines()
subst = open('./results/subst.dic', 'r', encoding="utf-16-le").readlines()
enrich = open("./results/subts_enrichi.dic", 'w', encoding="utf-16-le")

enrich.write('\ufeff')
enrich_list = []

for i in corpus_medical:
    token = re.search(r"^-? ?(\w+) :? ?(\d+|,)+ (mg|ml).+", i , re.I)
    if token:
        medecine = str(token.group(1)).lower()
        # some special cases that should not be included
        if not medecine.startswith("ø") and medecine != "témesta" and medecine != "intraveineuse" and medecine != "kardégic":
            subst.append(medecine + ",.N+subst\n")
            enrich_list.append(str(token.group(1)))
# Writing the subts_enrichi.dic File
count = 1
for i in enrich_list:
    enrich.write(i.lower() + "\n")
    # print(str(count) + " - " + i)
    count += 1
enrich.close()

# Building infos2.txt
infos2 = open('./results/infos2.txt', 'w')
enrich_list = list(dict.fromkeys(sorted(enrich_list)))
first_char = enrich_list[0][0]
count = 0
for i in enrich_list:
    if (i.startswith(first_char)):
        count += 1
    else:
        infos2.write("Number of medecines starting with letter '"+ first_char +"' : " + str(count) + "\n")
        first_char = i[0]
        count = 1
# Write the number with letter "Z"
infos2.write("Number of medecines starting with letter '"+ first_char +"' : " + str(count) + "\n")
infos2.write("\nTotal number of enriched medecines : " + str(len(enrich_list)))
infos2.close()

# Updating the subst.dic with all new changes
temp = open("./results/subst.dic","w",encoding="utf-16-le")
temp.write('\ufeff')

subst = list(dict.fromkeys(sorted(subst)))

temp.write(subst[-1])

for i in subst:
    if i[0] <= 'e':
        temp.write(i)

for i in subst:
    if i[0] == 'é':
        temp.write(i)

for i in subst:
    if i[0] > 'e' and i[0] <= 'z':
        temp.write(i)

temp.close()