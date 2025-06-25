from mother_class import post, counter

class spisok(post):
    @counter
    def __init__(self, nikname, date, text):
        super().__init__(nikname, date, text)
        self.list_ = ['твар', 'мраз', 'гнид']
        self.comments = []
    @counter
    def add_comment(self, comment_text):
        k = 0
        for j in range(len(self.list_)):
            if self.list_[j] in comment_text.lower():
                pass
            else:
                k += 1
        if k == len(self.list_):
            self.comments.append(comment_text)

    @counter
    def __str__(self):
        return super().__str__()

