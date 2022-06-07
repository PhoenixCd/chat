#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding= 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convers(lines):
    new = []
    person = None  #預設為空值(null)
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: #如果person有值
            new.append(person + ': ' + line)
    return new 

def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convers(lines)
    write_file('output.txt',lines)

main() 