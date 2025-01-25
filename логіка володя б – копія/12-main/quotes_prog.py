with open("quotes.txt", "r",encoding="utf-8") as file:
    for line in file:
        print(line)

a = input(" хто написав")
with open("quotes.txt","a") as file:
    file.write("\n "+a+" \n")

while 1:
    b =input ("чи хочуш додати").lower()
    if b == "ні":
        print("ви вибрали відмову")
        break
    else:
        q = input("цитата:")
        with open("quotes.txt","a") as file:
            file.write("\n "+q+" \n")
        a = input("хто написав")
        with open("quotes.txt","a") as file:
            file.write("\n "+q+" \n")

        a = input("чи хочеш додати ").lower()
