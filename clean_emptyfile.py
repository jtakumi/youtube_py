import os


base='search'
def clean():
    #search dirにある検索に失敗して作成された
    #空ファイルを削除する
    for i in os.listdir(base):
        path=os.path.join(base,i)
        size=os.path.getsize(path)
        if size == 0 :
            os.remove(path)            


def git():
    gadd='git add ' + base + '/.'
    os.system(gadd)

def main():
    clean()
    git()
    print('all empty files were cleaned.')


if __name__ == '__main__':
    main()