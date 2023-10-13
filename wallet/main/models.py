from django.db import models


class Coin(models.Model):
    name = models.CharField('Название', max_length=255, unique=True),
    img = models.CharField('Иконка', max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюта'


class Users(models.Model):
    email = models.CharField('Электронная почта', max_length=255, unique=True)
    code = models.CharField('Ключ подписи', max_length=255, unique=True)
    progress = models.CharField('Прогресс', max_length=255, default='0')
    salt = models.CharField('Соль пароля', max_length=255)
    password = models.CharField('Пароль', max_length=255)
    ip = models.CharField('IP адрес', max_length=255, blank=True)
    session = models.CharField('Токен сессии', max_length=255, blank=True)
    lvl = models.CharField('Уровень', max_length=255, default='1')
    name = models.CharField('Имя', max_length=255, unique=True)
    img = models.CharField('Фото', max_length=255, default='placeholder.png')
    date = models.DateTimeField('Дата', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date']
        indexes = [
            models.Index(fields=['-date'])
        ]


class Assets(models.Model):
    class Status(models.IntegerChoices):
        UNKNOWN = 0, 'Не изменилось'
        DOWN = 1, 'Упало'
        UP = 2, 'Поднялось'

    exp = models.CharField('Короткое название', max_length=255)
    state = models.CharField('Состояние', max_length=255)
    name = models.CharField('Название', max_length=255)
    mod = models.CharField('Изменение', max_length=255)
    img = models.CharField('Иконка', max_length=255)
    type = models.IntegerField('Тип изменения', choices=Status.choices, default=Status.UNKNOWN)
    user = models.IntegerField('Пользователь')
    date = models.DateTimeField('Дата', auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актив'
        verbose_name_plural = 'Активы'
        ordering = ['-date']
        indexes = [
            models.Index(fields=['-date'])
        ]


class TransactionsAccessManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Transactions.Status.ACCESS)


class TransactionsCanceledManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Transactions.Status.CANCELED)


class Transactions(models.Model):
    class Status(models.IntegerChoices):
        CANCELED = 0, 'Отменена'
        PROGRESS = 2, 'В процессе'
        ACCESS = 1, 'Прошла'

    coin = models.CharField('Валюта', max_length=255)
    sum = models.CharField('Сумма', max_length=255)
    sender = models.IntegerField('Отправитель')
    state = models.IntegerField('Состояние')
    user = models.IntegerField('Получатель')
    type = models.IntegerField('Тип')
    status = models.IntegerField('Статус', choices=Status.choices, default=Status.PROGRESS)
    date = models.DateTimeField('Дата', auto_now_add=True)

    objects = models.Manager()
    access = TransactionsAccessManager()
    canceled = TransactionsCanceledManager()

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ['-date']
        indexes = [
            models.Index(fields=['-date'])
        ]
