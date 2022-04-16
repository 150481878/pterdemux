import os
import re

name_check_list = []

def cmd(directory):
    main_cmd = f'eac3to {directory} 1) 1:Chapters.txt 2:video.*'
    final_cmd = main_cmd 
    content_list =  getinfo(directory)
    for line in content_list:
        line = re.sub(' ', '', line.strip())
        if is10ch(line):
            if trackerLocation(line) == 2:
                lineName2 = line[3:]
                if renameCheck(lineName2) is False:  
                    if is24bits(line):
                        extracmd = f' {line}.flac -down16'
                        name_check_list.append(lineName2)
                        final_cmd += extracmd
                    else:
                        extracmd = f' {line}.flac'
                        name_check_list.append(lineName2)
                        final_cmd += extracmd
                else:  
                    if is24bits(line):
                        extracmd = f' {line}{name_check_list.count(lineName2) + 1}.flac -down16'
                        name_check_list.append(lineName2)
                        final_cmd += extracmd
                    else:
                        extracmd = f' {line}{name_check_list.count(lineName2) + 1}.flac'
                        name_check_list.append(f'{lineName2} {(name_check_list.count(lineName2) + 1)}')
                        final_cmd += extracmd
            elif trackerLocation(line) == 1:
                lineName1 = line[2:]
                if renameCheck(lineName1) is False:  
                    if is24bits(line):
                        extracmd = f' {line}.flac -down16'
                        name_check_list.append(lineName1)
                        final_cmd += extracmd
                    else:
                        extracmd = f' {line}.flac'
                        name_check_list.append(lineName1)
                        final_cmd += extracmd
                else:  
                    if is24bits(line):
                        extracmd = f' {line}{name_check_list.count(lineName1) + 1}.flac -down16'
                        name_check_list.append(lineName1)
                        final_cmd += extracmd
                    else:
                        extracmd = f' {line}{name_check_list.count(lineName1) + 1}.flac'
                        name_check_list.append(f'{lineName1} {(name_check_list.count(lineName1) + 1)}')
                        final_cmd += extracmd
        if is20ch(line):
            if trackerLocation(line) == 2:
                lineName2 = line[3:]
                if renameCheck(lineName2) is False:  
                    if is24bits(line):
                        extracmd = f' {line}.flac -down16'
                        name_check_list.append(lineName2)
                        final_cmd += extracmd
                    else:
                        extracmd = f' {line}.flac'
                        name_check_list.append(lineName2)
                        final_cmd += extracmd
                else:  
                    if is24bits(line):
                        extracmd =  f' {line}{name_check_list.count(lineName2) + 1}.flac -down16'
                        name_check_list.append(lineName2)
                        final_cmd += extracmd
                    else:
                        extracmd = f' {line}{name_check_list.count(lineName2) + 1}.flac'
                        name_check_list.append(f'{lineName2} {(name_check_list.count(lineName2) + 1)}')
                        final_cmd += extracmd
            elif trackerLocation(line) == 1:
                lineName1 = line[2:]
                if renameCheck(lineName1) is False:  
                    if is24bits(line):
                        extracmd = f' {line}.flac -down16'
                        name_check_list.append(lineName1)
                        final_cmd += extracmd
                    else:
                        extracmd = f' {line}.flac'
                        name_check_list.append(lineName1)
                        final_cmd += extracmd
                else:  
                    if is24bits(line):
                        extracmd = f' {line}{name_check_list.count(lineName1) + 1}.flac -down16'
                        name_check_list.append(lineName1)
                        final_cmd += extracmd
                    else:
                        extracmd = f' {line}{name_check_list.count(lineName1) + 1}.flac'
                        name_check_list.append(f'{lineName1} {(name_check_list.count(lineName1) + 1)}')
                        final_cmd += extracmd
        if is51ch(line):
            if trackerLocation(line) == 2:
                lineName2 = line[3:]
                if renameCheck(lineName2) is False:  
                    extracmd = f' {line}.ac3'
                    name_check_list.append(lineName2)
                    final_cmd += extracmd
                else:  
                    extracmd = f' {line}{name_check_list.count(lineName2) + 1}.ac3'
                    name_check_list.append(f'{lineName2} {(name_check_list.count(lineName2) + 1)}')
                    final_cmd += extracmd
            elif trackerLocation(line) == 1:
                lineName1 = line[2:]
                if renameCheck(lineName1) is False:  
                    extracmd = f' {line}.ac3'
                    name_check_list.append(lineName1)
                    final_cmd += extracmd
                else:  
                        extracmd = f' {line}{name_check_list.count(lineName1) + 1}.ac3'
                        name_check_list.append(f'{lineName1} {(name_check_list.count(lineName1) + 1)}')
                        final_cmd += extracmd
        if is71ch(line):
            if trackerLocation(line) == 2:
                lineName2 = line[3:]
                if renameCheck(lineName2) is False:  
                    extracmd = f' {line}.ac3'
                    name_check_list.append(lineName2)
                    final_cmd += extracmd
                else:  
                    extracmd = f' {line}{name_check_list.count(lineName2) + 1}.ac3'
                    name_check_list.append(f'{lineName2} {(name_check_list.count(lineName2) + 1)}')
                    final_cmd += extracmd
            elif trackerLocation(line) == 1:
                lineName1 = line[2:]
                if renameCheck(lineName1) is False:  
                    extracmd = f' {line}.ac3'
                    name_check_list.append(lineName1)
                    final_cmd += extracmd
                else:  
                    extracmd = f' {line}{name_check_list.count(lineName1) + 1}.ac3'
                    name_check_list.append(f'{lineName1} {(name_check_list.count(lineName1) + 1)}')
                    final_cmd += extracmd
        if isSub(line):
            if trackerLocation(line) == 2:
                lineName2 = line[3:]
                if renameCheck(lineName2) is False:  
                    extracmd = f' {line}.*'
                    name_check_list.append(lineName2)
                    final_cmd += extracmd
                else: 
                    extracmd = f' {line}{name_check_list.count(lineName2) + 1}.*'
                    name_check_list.append(f'{lineName2} {(name_check_list.count(lineName2) + 1)}')
                    final_cmd += extracmd
            elif trackerLocation(line) == 1:
                lineName1 = line[2:]
                if renameCheck(lineName1) is False:  
                    extracmd = f' {line}.*'
                    name_check_list.append(lineName1)
                    final_cmd += extracmd
                else: 
                    extracmd = f' {line}{name_check_list.count(lineName1) + 1}.*'
                    name_check_list.append(f'{lineName1} {(name_check_list.count(lineName1) + 1)}')
                    final_cmd += extracmd
    return final_cmd

def getinfo(directory):
    content_list = []  
    cmd = f'eac3to {directory} 1)'
    rlt = os.popen(cmd)
    content = rlt.read()
    for line in content.split('\n'):
        a=re.sub('[\x08]', '', line.strip())
        content_list.append(a)
    del content_list[0] 
    for line in content_list:
        if  line[0:1].isdigit() is False: 
            delindex = content_list.index(line)
            del content_list[delindex]
    return  content_list

def pterdemux(directory):
    final_cmd = cmd(directory)
    rlt = os.popen(final_cmd)
    content = rlt.read()
    return content

def is24bits(str):
    if '24bits' in str:
        return True
    else:
        return False

def is10ch(str):
    if '1.0ch' in str:
        return True
    else:
        return False

def is20ch(str):
    if '2.0ch' in str:
        return True
    else:
        return False

def is51ch(str):
    if '5.1ch' in str:
        return True
    else:
        return False

def is71ch(str):
    if '7.1ch' in str:
        return True
    else:
        return False

def renameCheck(str):
    if str not in name_check_list:
        return False 
    else:
        return True 


def isSub(line):
    if 'Subtitle' in line:
        return True 
    else:
        return False 

def trackerLocation(str):
    index = str.find(':')
    if index == 2: 
        return 2
    elif index == 1: 
        return 1

def main():
    print('\n','欢迎使用PTerdemux!','\n')
    directory = input('请将原盘目录文件夹拖进来，或者输入原盘目录：')
    print('程序运行中......')
    test = pterdemux(directory)
    print(test)
    print('程序运行结束，Have Fun!')

if __name__ == '__main__':
    main()


