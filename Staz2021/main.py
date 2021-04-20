def add_to_list():
    file = open('vstup_data.txt', "r")
    sum = 0
    l = []
    for line in file:
        if line[-1] == '\n':
            l.append(line[:-1])
        else:
            l.append(line)
    file.close()
    return l

def count_lines():
    file = open('vstup_data.txt', "r")
    count = 0
    for line in file:
        if line != '\n':
            count += 1
    file.close()
    return count

def sum_of_object():
    count = count_lines()
    l = add_to_list()
    sum = 0
    help = 0
    check = int(((count - 1)/2)+1)
    for i in range(0, count):
        z = l[i].split(' ')
        y = 0
        leng = len(z)-1
        if i == 0:
            sum += int(z[0])
        if i > 0:
            if help + 1 > leng:
                help -= 1
            if z[help] > z[help + 1]:
                sum += int(z[help])
                y = 1
            if z[help] < z[help + 1] and y == 0:
                sum += int(z[help + 1])
                help += 1
            if i > check:
                if help == leng:
                    for j in range(i+1, count):
                        z = l[j].split(' ')
                        leng = len(z)-1
                        sum += int(z[leng])
                    return sum

print(sum_of_object())

