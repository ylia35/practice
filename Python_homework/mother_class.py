from copy import copy
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f'---Функция {func.__name__} выполнилась {wrapper.count} раз---')
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

class post:
    @counter
    def __init__(self, nikname, date, text):
        self.nikname = nikname
        self.date = date
        self.likes = 0
        self.text = text
        self.comments = []
    @counter
    def add_likes(self, how_much):
        try:
            how_much = int(how_much)
        except (ValueError, TypeError):
            self.likes = 'ERROR'
            print("Количество лайков указывается числом, а не буквами!!!")
        else:
            self.likes += how_much
    @counter
    def add_comment(self, comment_text):
        if 'сволоч' in comment_text.lower():
            pass
        else:
            self.comments.append(comment_text)
    @counter
    def get_all_comments(self):
        return self.comments
    @counter
    def __str__(self):
        return f'Nickname: {self.nikname}, date: {self.date}, text: {self.text} likes: {self.likes}, comments: {(self.comments[:3])}'
    def __copy__(self):
        new_obj = post(self.nikname, self.date, self.text)
        new_obj.text = "Закрыто для просмотра. Плати!"
        return  new_obj
pos = post('РИА Новости', '01.12.20022', 'Среди сотрудников ЗАЭС обнаружили наводчиков ВСУ')
new_obj = copy(pos)
