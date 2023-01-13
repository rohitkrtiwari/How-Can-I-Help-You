import os
import sys

def listToString(s, sep=' '):
    str1 = ""
    for ele in s:
        str1 += ele
        str1 += sep
    return str1

open_map = {
    "ds" : "explorer D:\\Desktop\\ICRB GATE CSE\\RBR\\Data Structures\\",
    "cd" : "explorer D:\\Desktop\\ICRB GATE CSE\\RBR\\DBMS CD TOC COA\\7.CD(10.10.23)-(2.99GB)",
    "dbms" : "explorer D:\\Desktop\\ICRB GATE CSE\\RBR\\DBMS CD TOC COA\\6.DBMS(38.19.06)-(9.13GB)",
    "toc" : "explorer D:\\Desktop\\ICRB GATE CSE\\RBR\\DBMS CD TOC COA\\8.TOC(126.07.04)-(5.72GB)",
    "coa" : "explorer D:\\Desktop\\ICRB GATE CSE\\RBR\\DBMS CD TOC COA\\9.COA(16.27.47)-(7.14GB)",
    "aptituide" : "explorer D:\\Desktop\\ICRB GATE CSE\\RBR\\Aptitiude",
    "daa" : "explorer D:\\Desktop\\ICRB GATE CSE\\RBR\\Algorithms",
    "dl" : "explorer D:\\Desktop\\ICRB GATE CSE\\RBR\\Digital Logic",
    "mathematics" : "explorer D:\\Desktop\\ICRB GATE CSE\\RBR\\Mathematics",
    "os" : "explorer D:\\Desktop\\ICRB GATE CSE\\RBR\\OS CN\\3.OS(35.15.48)-(8.99GB)",
    "cn" : "explorer D:\\Desktop\\ICRB GATE CSE\\RBR\\OS CN\\4.CN(45.12.45)-(14.8GB)",
    
    "youtube" : "start chrome https://www.youtube.com/",
    "linkedin" : "start chrome https://www.linkedin.com/feed/",
    "github" : "start chrome https://github.com/rohitkrtiwari/",
}

def main():
    cmd = sys.argv[1:]
    if (cmd[0] == "open"):
        os.system(open_map[cmd[1]])

    elif(cmd[0] == "play"):
        query = listToString(cmd[1:], sep="+")
        os.system("start chrome https://www.youtube.com/results?search_query="+query)
        
    elif (cmd[0] == "search"):
        query = listToString(cmd[1:], sep="%20")
        os.system("start chrome https://www.google.com/search?q="+query)
        
        

if __name__ == '__main__':
    main()