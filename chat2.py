#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding= 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convers(lines):
    person = None  #預設為空值(null)
    allen_word_cnt = 0
    allen_sticker_cnt = 0
    allen_image_cnt = 0
    viki_word_cnt = 0
    viki_sticker_cnt = 0
    viki_image_cnt = 0
    for line in lines:
        s = line.split(' ') #用split切割後變清單List
        time = s[0]
        name = s[1]
        if name == 'Allen':
           if s[2] == '貼圖':
               allen_sticker_cnt += 1
           elif s[2] == '圖片':
               allen_image_cnt += 1
           else:
               for m in s[2:]:
                    allen_word_cnt += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
               viki_sticker_cnt += 1
            elif s[2] == '圖片':
               viki_image_cnt += 1
            else: 
                for m in s[2:]:
                    viki_word_cnt += len(m)

    print('Allen說了', allen_word_cnt, '個字')
    print('Allen傳了', allen_sticker_cnt, '個貼圖')
    print('Allen傳了', allen_image_cnt, '張圖片')

    print('Viki說了', viki_word_cnt, '個字')
    print('Viki傳了', viki_sticker_cnt, '個貼圖')
    print('Viki傳了', viki_image_cnt, '張圖片')
    

def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convers(lines)
    # write_file('output.txt',lines)

main() 