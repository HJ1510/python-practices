#제어문
a=2
b=5
if a>b:
    print(f"{a}는 {b}보다 크다")
    print(f"{a} 만세")
elif a<b:
    print(f"{a}는 {b}보다 작다")
    print(f"{b} 만세")
else: #위 조건이 다 아니면 마지막
    print("else")

x = {"company":"카카오"}
if x.get("company") == "카카오" or x.get("company") == "네이버": #if구문에선 and, or 사용가능
    print("대기업 직원이시네요")
else:
    print("중견기업 직원이시네요")

x = {"company":"비트"}
if x.get("company") == "카카오" or x.get("company") == "네이버":
    print("대기업 직원이시네요")
else:
    print("중견기업 직원이시네요")    


x = {"company":"카카오"}
if x.get("company") == "카카오" :
    print("카카오 직원이시네요")
elif x.get("company") == "네이버":
    print("네이버 직원이시네요")
else:
    print("중견기업 직원이시네요")
    
x = {"company":"카카오"}
match x.get("company"): #match에서는 and나 or등 사용할수 없음
    case "카카오" :
        print("카카오 직원이시네요")
    case "네이버" :
        print("네이버 직원이시네요")
    case _: # _ => 어떤것이든
        print("중견기업 직원이시네요")





x = {"company":"카카오", "isPartTime": False}
if x.get("company") == "카카오" :
    if x.get("isPartTime"):
        print("대기업 비정규직원") 
    else:
        print("대기업 정규직원")
elif x.get("company") == "네이버":
    print("네이버 직원이시네요")
else:
    print("중견기업 직원이시네요")




#Q. phone={"name":"갤럭시", "version":"플립"}
#phone이 애플이면 와우 / 갤럭시면 version을 보고 플립이면 접히네요 아니면 좋네요

phone={"name":"갤럭시", "version":"플립"}
if phone.get("name")=="갤럭시":
    if phone.get("version")=="플립":
        print("접히네요")
    else:
        print("좋네요")
elif phone.get("name")=="애플":
    print("와우")