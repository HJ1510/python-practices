#파일 입출력

#상대경로
# . 현재위치 c\test ==> .. c
# . 현재위치 c\test\test1 =test 폴더에서 12.py 파일 열고싶을때=> ..\12.py 
# . 현재위치 c\test\test1 =test2 폴더에서 34.py 파일 열고싶을때=> ..\test2\34.py 

#절대경로 c\test\test1\test.py

#프로젝트 있는 폴더 c:/test c:/project



# f=open("./test.txt", "w")
# f.write("hi\n")
# f.write("\n")
# f.write("\n")
# f.write("\tbye")
# f.close()

# f=open("./test1/test.txt", "w")
# f.write("hello")
# f.close()

# f=open("./test.txt",'r')
# lines=f.readlines() #전 라인을 read함
# for line in lines:
#     print(line)


# f=open("./test.py", "w")
# f.write('''f=open("./test1/test.txt", "w")
# f.write("hello")
# f.close()''')
# f.close()


# f=open("./test2/test.py", "w")
# f.write('''f=open("./test.txt",'r')
# lines=f.readlines() 
# for line in lines:
#     print(line)''')
# f.close()

# f=open("./free1004.py",'r')
# lines=f.readlines() 
# for line in lines:
#     print(line)
# f.close()



# f=open("./test.txt", "a")
# f.write("""
#     dhsdk""")
# f.close()


#내일 업데이트 class


#def open(filename, type):
    # filename이 있냐
    # if type=="w": 글 쓰기 모드 실행되는 순간 파일 안의 내용이 지워짐(실행 완료가 되어야 기존 내용이라도 나옴)
    # elif type=="r": 읽기 모드


# f=open("./124.txt", "w")
# f.write("""빅데이터
# 파이썬
# abc
# AI""")
# f.close()


# fr=open("./88.txt", "r", encoding="UTF-8")
# lines=fr.readlines()
# for line in lines:
#     print(line)
# fr.close()

# fw=open("./88.txt", "w", encoding="UTF-8")
# # print(lines)
# for line in lines:
#     line=line.strip() #\n 공백을 없애줌
#     # print(line)
#     if line=="한글":
#         fw.write("ML")
#     elif line=="쓰기":
#         fw.write("글쓰기")
#     else:
#         fw.write(f"{line}")
#     fw.write("\n")
# fw.close()
