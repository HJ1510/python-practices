
import re


reg=re.compile("[0-9]{3}-[0-9]{3,4}-[0-9]{4}")
phone_number="010-2222-3333"
print(reg.match("phone_number"))