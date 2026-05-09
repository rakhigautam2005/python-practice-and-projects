#wap to generate multiplication tables from 2 to 20 and write it to the  different files.Place these files in folder for 13-yera old.
def generateTable(n):
    table = ""#to make a string
    for i in range(1, 11):
        table += f"{n}x{i} = {n*i}\n"#added to fstring ti make a new  string 
        f.write(table)
    with open(f"tables/table_{n}.txt", "w")as f:#and then we will add it to   file by opening a folder
        for i in range(2, 21):
            generateTable(i)