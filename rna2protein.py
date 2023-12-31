#   this is horrible, should've used a dict but i got the if statements to work so oh well
#   paste rna string into "rnastring.txt", translated protein string is written to "proteinstring.txt"

def main():
    f = open("rnastring.txt", "r")
    w = open("proteinstring.txt", "w")

    w.write('')

    w.close()

    w = open("proteinstring.txt", "a")


    s = f.read()
    
    rna = []
    mRNA = []

    for i in range(len(s)):
        rna.append(s[i])

    x = 0

    # checks all 64 base combos
    # why did i make so many if statements
    # this is horrendous
    for i in range(len(rna)):
        if x != len(rna):
            if rna[x] == 'U':
                if rna[x+1] == 'U':
                    if rna[x+2] == 'U':
                        w.write('F')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('F')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('L')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('L')
                        x += 3
                        continue
                elif rna[x+1] == 'C':
                    if rna[x+2] == 'U':
                        w.write('S')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('S')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('S')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('S')
                        x += 3
                        continue
                elif rna[x+1] == 'A':
                    if rna[x+2] == 'U':
                        w.write('Y')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('Y')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        break
                    elif rna[x+2] == 'G':
                        break
                elif rna[x+1] == 'G':
                    if rna[x+2] == 'U':
                        w.write('C')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('C')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        break
                    elif rna[x+2] == 'G':
                        w.write('W')
                        x += 3
                        continue
            elif rna[x] == 'C':
                if rna[x+1] == 'U':
                    if rna[x+2] == 'U':
                        w.write('L')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('L')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('L')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('L')
                        x += 3
                        continue
                elif rna[x+1] == 'C':
                    if rna[x+2] == 'U':
                        w.write('P')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('P')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('P')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('P')
                        x += 3
                        continue
                elif rna[x+1] == 'A':
                    if rna[x+2] == 'U':
                        w.write('H')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('H')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('Q')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('Q')
                        x += 3
                        continue
                elif rna[x+1] == 'G':
                    if rna[x+2] == 'U':
                        w.write('R')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('R')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('R')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('R')
                        x += 3
                        continue
            elif rna[x] == 'A':
                if rna[x+1] == 'U':
                    if rna[x+2] == 'U':
                        w.write('I')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('I')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('I')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('M')
                        x += 3
                        continue
                elif rna[x+1] == 'C':
                    if rna[x+2] == 'U':
                        w.write('T')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('T')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('T')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('T')
                        x += 3
                        continue
                elif rna[x+1] == 'A':
                    if rna[x+2] == 'U':
                        w.write('N')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('N')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('K')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('K')
                        x += 3
                        continue
                elif rna[x+1] == 'G':
                    if rna[x+2] == 'U':
                        w.write('S')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('S')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('R')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('R')
                        x += 3
                        continue
            elif rna[x] == 'G':
                if rna[x+1] == 'U':
                    if rna[x+2] == 'U':
                        w.write('V')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('V')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('V')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('V')
                        x += 3
                        continue
                elif rna[x+1] == 'C':
                    if rna[x+2] == 'U':
                        w.write('A')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('A')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('A')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('A')
                        x += 3
                        continue
                elif rna[x+1] == 'A':
                    if rna[x+2] == 'U':
                        w.write('D')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('D')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('E')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('E')
                        x += 3
                        continue
                elif rna[x+1] == 'G':
                    if rna[x+2] == 'U':
                        w.write('G')
                        x += 3
                        continue
                    elif rna[x+2] == 'C':
                        w.write('G')
                        x += 3
                        continue
                    elif rna[x+2] == 'A':
                        w.write('G')
                        x += 3
                        continue
                    elif rna[x+2] == 'G':
                        w.write('G')
                        x += 3
                        continue
    f.close()
    w.close()
    
main()