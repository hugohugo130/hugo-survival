from github import Github as g
from os.path import exists
from os import makedirs as md
result = None

for c in ["module","lang"]:
    if not exists(c):
        md(c)

link = "hugohugo130/hugosurvival"
filename = ["game.py","d_live.py","play_xiaozi_live.py","module\\check_all_requirements.py","module\\check_file_update.py","module\\getxiaozilivelink.py","lang\\tc.py","lang\\sc.py","req.req","plrnamechanger.py"]
for curfilename in filename:
    if "\\" not in curfilename:
        curfilename_ = curfilename
    else:
        curfilename_ = curfilename.split("\\")[-1]
    print(f"正在檢查{curfilename_}...")
    git = g("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")
    repo = git.get_repo(link)
    content = repo.get_contents(curfilename if "\\" not in curfilename else curfilename.split("\\")[-1])
    latestfile = content.decoded_content
    if not exists(curfilename):
        result = 2
    else:
        with open(curfilename,"rb") as gamefile:
            gamefilec = gamefile.read()
        if gamefilec != latestfile:
            result = 1
        else:
            result = 0
    
    if result == 1 or result == 2:
        if result == 1:
            print(f"檢測到更新!正在更新{curfilename_}...")
        else:
            print(f"正在從github獲取{curfilename_}")
        with open(curfilename,"wb") as gamefile:
            gamefile.write(latestfile)
    else:
        print(f"目前你的{curfilename_}是最新的,沒有更新!")

input("執行完畢")
