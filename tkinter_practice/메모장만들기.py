from tkinter import *
import tkinter.messagebox as msgbox


# 파일 이름 : mynote.txt / 파일 관련 함수
#######################################################
def open_file():
    try:
        my_file = open("mynote.txt", "r" ,encoding="utf8")
    except FileNotFoundError:
        msgbox.showerror("에러", "mynote.txt 파일이 존재하지 않습니다.\n \
        저장 후 실행해주세요.")
    else:
        sentences = my_file.read()
        txt.insert(END, sentences)
        my_file.close()

def store_file():
    my_file = open("mynote.txt", "w", encoding="utf8")
    sentences = txt.get("1.0", END)
    print(sentences)
    my_file.write(sentences)
    my_file.close()
#######################################################


root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+600+300")


# 스크롤바
#######################################################
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
#######################################################


# 텍스트 입력
#######################################################
txt = Text(root, width=640,height=480,yscrollcommand = scrollbar.set)
txt.pack()
scrollbar.config(command=txt.yview)
#######################################################


# 메뉴
#######################################################
menu = Menu(root)
# File 메뉴 / 열기,저장,끝내기
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command = open_file)
menu_file.add_command(label="저장", command = store_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command = root.quit)
menu.add_cascade(label="File", menu=menu_file)
# 편집 메뉴
menu.add_cascade(label="편집")
# 서식 메뉴
menu.add_cascade(label="서식")
# 보기 메뉴
menu.add_cascade(label="보기")
# 도움말 메뉴
menu.add_cascade(label="도움말")
#######################################################







root.config(menu=menu)
root.mainloop()
