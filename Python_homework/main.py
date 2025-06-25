from mother_class import post
from child_class import spisok
from time import time
from copy import copy

pos = spisok('РИА Новости', '01.12.20022', 'Среди сотрудников ЗАЭС обнаружили наводчиков ВСУ')
s = str(input())
pos.add_comment(s)
pos.add_comment('Какая замечательная новость')

likes = input()
pos.add_likes(likes)

pos.get_all_comments()
print(pos)
new_obj = copy(pos)
print(' new ', new_obj)
