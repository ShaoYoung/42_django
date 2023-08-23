from django.db import models
from random import randint


class Coin(models.Model):
    result = models.BooleanField()
    kick_time = models.DateTimeField(auto_now=True)

    @staticmethod
    def statistics(n: int):
        reshka = 0
        orel = 0
        for _ in range(n):
            coin = Coin(result=randint(0, 1))
            if coin.result:
                reshka += 1
            else:
                orel += 1
        result_dict = {
            'орёл': orel,
            'решка': reshka,
        }
        return result_dict


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Article(models.Model):
    head = models.CharField(max_length=200)
    content = models.TextField()
    public_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    public = models.BooleanField()


class Comment(models.Model):
    # у комментария один автор, но автор может писать комментарии к разным статьям (один ко многим)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # комментарий относится к одной статье (один к одному)
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    content = models.TextField()
    make_date = models.DateTimeField(auto_now=True)
    # дата изменения (при создании равна дате создания)
    modify_date = models.DateTimeField(auto_now=True)



