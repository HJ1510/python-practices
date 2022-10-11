#88.txt 내용 수정-수정할 내용 입력/ 수정 원치 않을시 c를 입력


# fr=open("./88.txt", "r", encoding="UTF-8")
# lines=fr.readlines()
# fr.close()

# fw=open("./88.txt","w", encoding="UTF-8")
# for line in lines:
#     update_text=input(f"전 문장 : {line.strip()}\n 바꿀 문장(취소는 c) :\t")
#     if update_text=="c":
#         fw.write(line.strip()) # \n 제거
#     else:
#         fw.write(update_text)
#     fw.write("\n")

# fw.close()



# fr=open("./88.txt","r", encoding="UTF-8")
# lines=fr.readlines()
# fr.close()

# fw=open("./88.txt","w", encoding="UTF-8")
# for line in lines:
#     updateTxt=input(f"전 문장 : {line}\n 바꿀 문장 (취소는 c) :\t")
#     if updateTxt=="c":
#         fw.write(line.strip())
#     else:
#         fw.write(updateTxt)
#     fw.write("\n")
# fw.close()