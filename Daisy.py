import os
import random
import sys
import sqlite3
import requests
from pprint import pprint
import time

def listToString(s, sep=' '):
    str1 = ""
    for ele in s:
        str1 += ele
        str1 += sep
    return str1

DB_PATH = "D://Desktop/Projects/How Can I Help You/todo.db"

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS todo (id INTEGER primary key, task text)')
    conn.commit()
    conn.close()

def add_todo(q):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todo (task) VALUES ("'+q+'")')
    conn.commit()
    conn.close()


def del_todo(q):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('delete from todo where id = ('+q+')')
    conn.commit()
    conn.close()

def show_todo():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    data=cursor.execute("select * from todo")
    print("\n************ Todo ************\n")
    for row in data:
        print(str(row[0]) + "\t" + row[1])
    print("\n")
    conn.commit()
    conn.close()
    return data

def create_gitRepo(repo_name):
    GITHUB_TOKEN = open("D:\\Desktop\\projects\\How Can I Help You\\token.gt", "r").read()
    API_URL = 'https://api.github.com'
    payload = '{"name": "'+repo_name+'"}'
    headers = {
        "Authorization" : "token " + GITHUB_TOKEN,
        "Accept": "application/vnd.github.v3+json"
    }
    r = requests.post(API_URL+"/user/repos",data=payload,headers=headers)
    pprint(r.json)
    repo_name = repo_name.replace(" ", "-")
    remote_repo = "https://github.com/rohitkrtiwari/"+repo_name+".git"
    return remote_repo

def create_project(project_name):
    os.chdir("D:\\Desktop\\projects")
    os.mkdir(project_name)
    os.chdir("D:\\Desktop\\projects\\"+project_name)
    os.system("git init")
    remote_repo = "https://github.com/rohitkrtiwari/Demo_Project-.git"
    # remote_repo = create_gitRepo(project_name)
    os.system("git remote add origin "+remote_repo)
    with open('readme.md', 'w') as fp:
        fp.write("# "+project_name)
    print(os.getcwd())
    os.system("git add .")
    os.system('git commit -m "Initial Commit"')
    
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
    "classroom" : "start chrome https://classroom.google.com/u/1/",
}

def main():
    cmd = sys.argv[1:]
    q = listToString(cmd)
    if ("open" in q):
        os.system(open_map[cmd[cmd.index("open")+1]])

    if("play song" in q):
        pickOne = my_songs_yt[random.randrange(0, len(my_songs_yt), 1)]
        link = "https://www.youtube.com/watch?v="+pickOne
        os.system("start chrome "+link)

    if("play local" in q):
        path = "C://Users//rohit//Music//"
        pickOne = os.listdir(path)[random.randrange(0, len(os.listdir(path)), 1)]
        os.startfile("C://Users//rohit//Music//"+pickOne)
        
    if("todo" in q):
        if(cmd[cmd.index("todo")-1] == "show"):
            show_todo()

        elif(cmd[cmd.index("todo")-1] == "add"):
            task = listToString(cmd[cmd.index("todo")+1:])
            add_todo(task)

        elif(cmd[cmd.index("todo")-1] == "delete"):
            id = cmd[cmd.index("todo")+1]
            del_todo(id)

    if("create project" in q):
        project_name = listToString(cmd[cmd.index("project")+1:])
        create_project(project_name)

    if (cmd[0] == "search"):
        query = listToString(cmd[1:], sep="%20")
        os.system("start chrome https://www.google.com/search?q="+query)
        
        

if __name__ == '__main__':
    main()