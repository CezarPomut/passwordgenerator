list=["ana", "are", "mere"]

parole=open("parole.txt", "a")
for x in list:
    parole.write(f"{x}\n")

