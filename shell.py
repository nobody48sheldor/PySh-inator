import os
import sys
import time

commands_init = ["neofetch"]
symbole = "$"
run = True

path = ["home", "arnaud", "Desktop", "arnaud", "code", "python", "shell"]
PATH = ""

def run_once():
    for i in commands_init:
        os.system(i)

def main():
    while run:
        PATH = ""
        for i in path:
            PATH = PATH + "/" + i
        cmd = str(input("{} {} ".format(PATH, symbole)))
        verif = False

        for i in range(len(commands)):
            if cmd.startswith(commands[i]):
                exec(i, cmd, PATH)

def exec(n, cmd, PATH):
    if n == 0:
        print("goodbye")
        quit()
    if n == 1:
        os.system('clear')
    if n == 2:
        direct = False
        directory_ = os.listdir(PATH + "/")
        directory_.append("..")
        dir = cmd.split('cd ', 1)[-1]
        for i in directory_:
            if dir == i:
                direct = True
                if dir != "..":
                    path.append(dir)
                if dir == "..":
                    if len(path) != 0:
                        path.pop(len(path) - 1)
        if direct == False:
            print("direcotry does not exist. Do you want to see the direcotries available ? [y/N]")
            ans = input("     ? ")
            if ans == "Y":
                for i in directory_:
                    print("  - {}".format(i))
            if ans == "y":
                for i in directory_:
                    print("  - {}".format(i))
            if ans == "N":
                main()
            if ans == "n":
                main()
            else:
                main()
    if n == 3:
        directory = os.listdir(PATH + "/")
        for i in directory:
            print("  - {}".format(i))

    if n == 4:
        print(PATH)
    if n == 5:
        open(cmd.split('touch ', 1)[-1], "w")
    if n == 6:
        open(cmd.split('mk ', 1)[-1], "w")
    if n == 7:
        os.remove(cmd.split('rm ', 1)[-1])
    if n == 8:
        os.remove(cmd.split('d ', 1)[-1])
    if n == 9:
        with open(cmd.split('cat ', 1)[-1], "r") as file:
            for i in file.readlines():
                print(i)
    if n == 10:
        with open(cmd.split('p ', 1)[-1], "r") as file:
            for i in file.readlines():
                print(i)
    if n == 11:
        with open(cmd.split(' ', 3)[1], "w") as file:
            file.write(cmd.split('> ', 1)[-1])
    if n == 12:
        file_in = PATH + "/" + cmd.split(' ', 3)[1]
        file_out = PATH + "/" + cmd.split(' ', 3)[2]
        with open(file_in, "r") as filei:
            with open(file_out, "w+") as fileo:
                for i in filei.readlines():
                    fileo.write(i + "\n")
    if n == 13:
        os.mkdir(cmd.split(" ", 1)[-1])



commands = ["exit", "clear", "cd", "ls", "pwd", "touch", "mk", "rm", "d", "cat", "p", "w", "cp", "mkdir"]

run_once()
main()
