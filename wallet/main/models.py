from django.db import models


class Users(models.Model):
    email = models.CharField('Электронная почта', max_length=255, null=False)
    code = models.CharField('Ключ подписи', max_length=255, null=False)
    progress = models.CharField('Прогресс', max_length=255, null=False)
    salt = models.CharField('Соль пароля', max_length=255, null=False)
    password = models.CharField('Пароль', max_length=255, null=False)
    lvl = models.CharField('Уровень', max_length=255, null=False)
    name = models.CharField('Имя', max_length=255, null=False)
    img = models.CharField('Фото', max_length=255, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Assets(models.Model):
    exp = models.CharField('Короткое название', max_length=255, null=False)
    state = models.CharField('Состояние', max_length=255, null=False)
    name = models.CharField('Название', max_length=255, null=False)
    mod = models.CharField('Изменение', max_length=255, null=False)
    img = models.CharField('Иконка', max_length=255, null=False)
    type = models.IntegerField('Тип изменения', null=False)
    user = models.IntegerField('Пользователь', null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актив'
        verbose_name_plural = 'Активы'


class Transactions(models.Model):
    coin = models.CharField('Валюта', max_length=255, null=False)
    sum = models.CharField('Сумма', max_length=255, null=False)
    date = models.CharField('Дата', max_length=255, null=False)
    sender = models.IntegerField('Отправитель', null=False)
    state = models.IntegerField('Состояние', null=False)
    user = models.IntegerField('Получатель', null=False)
    type = models.IntegerField('Тип', null=False)

    def __str__(self):
        return f"{self.sender} & {self.sum} {self.coin}"

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
