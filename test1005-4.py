



# def solution(phone_number):
#     answer = ''
#     lenPhoneNumber=len(phone_number)
#     answer="*"*(lenPhoneNumber-4)
#     answer+=phone_number[-4:]
#     return answer

# print(solution("01033334444"))
# print(solution("027778888"))

#뒤 4자리만 빼고 다 *
#input 번호 받아서 010-0000-0000


# def solution(phone_number):
#     answer = ''
#     for i in range(0,len(phone_number)):
#         if i<len(phone_number)-4: #i=0, 0<11-4
#             if phone_number[i]=="-":
#                 answer+="-"
#             else:
#                 answer+="*"
#         else:
#             answer+=phone_number[i]
#     return answer
# phone_number=input("번호 000-0000-0000 ")
# print(solution(phone_number))
# print(solution("02-777-8888"))

