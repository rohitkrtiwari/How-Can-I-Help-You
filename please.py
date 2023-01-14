import os
import random
import sys

def listToString(s, sep=' '):
    str1 = ""
    for ele in s:
        str1 += ele
        str1 += sep
    return str1

my_songs_yt = [
    "erWlHBJLA20",
    "9emx__jxcTE",
    "1ap_cUpy4_M",
    "SAcpESN_Fk4",
    "cAAD8boQp_o",
    "Tn3fQz9kZzc",
    "MhXCj8E9CZU",
    "IlcL1KheS18",
    "Tn3fQz9kZzc",
    "kTJmO0gLPGY",
    "VuG7ge_8I2Y",
    "GsxB2fpCUZU",
    "ou9yRKdLoNE",
    "eBdR7Zi8u8w",
    "AZmAgoir1Tc",
    "mNRiMe1V8ps",
    "Hx1vffjeH_Q",
    "Is-X3M7MHuU",
    "DiJzNNewpXA",
    "gxoOxYvryp0",
    "1zl-PcP-xPg",
    "TYetCN6v8jg",
    "HmwXnw68Eeo",
    "47noolJchOY",
    "dpF_8qlrdxs"
]

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
    "projects" : "explorer D:\\Desktop\\projects",
    
    "youtube" : "start chrome https://www.youtube.com/",
    "linkedin" : "start chrome https://www.linkedin.com/feed/",
    "github" : "start chrome https://github.com/rohitkrtiwari/",
}

def main():
    cmd = sys.argv[1:]
    q = listToString(cmd)
    if ("open" in q):
        os.system(open_map[cmd[cmd.index("open")+1]])

    if("play song on youtube" in q):
        pickOne = my_songs_yt[random.randrange(0, len(my_songs_yt), 1)]
        link = "https://www.youtube.com/watch?v="+pickOne
        os.system("start chrome "+link)

    if("play local song" in q):
        path = "C://Users//rohit//Music//"
        pickOne = os.listdir(path)[random.randrange(0, len(os.listdir(path)), 1)]
        os.startfile("C://Users//rohit//Music//"+pickOne)
        
    if (cmd[0] == "search"):
        query = listToString(cmd[1:], sep="%20")
        os.system("start chrome https://www.google.com/search?q="+query)
        
        

if __name__ == '__main__':
    main()