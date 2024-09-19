# Задание "Свой YouTube":
# Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.
#
# Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.
#
# Всего будет 3 класса: UrTube, Video, User.
#
# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.
#
# Подробное ТЗ:
#
# Каждый объект класса User должен обладать следующими атрибутами и методами:
#
#     Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
#
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
#
#     Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
#
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#
#      Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
#     Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
#     Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
#     Метод log_out для сброса текущего пользователя на None.
#     Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
#     Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
#     Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
#
# Для метода watch_video так же учитывайте следующие особенности:
#
#     Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
#     Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
#     Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
#     После воспроизведения нужно выводить: "Конец видео"
#
#
# Код для проверки:
# ur = UrTube()
# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
# # Добавление видео
# ur.add(v1, v2)
#
# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
#
# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
#
# Примечания:
#
#     Не забывайте для удобства использовать dunder(магические) методы: __str__, __repr__, __contains__, __eq__ и др. (повторить можно здесь)
#     Чтобы не запутаться рекомендуется после реализации каждого метода проверять как он работает, тестировать разные вариации.

import time


class UrTube:
    """

    """

    class User:
        """
        Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
        """        
        def __init__(self, nickname, password, age):
            self.nickname = nickname
            self.password = hash(password)
            self.age = age

        def __str__(self):
            return self.nickname

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    """
    Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users 
    с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. 
    Помните, что password передаётся в виде строки, а сравнивается по хэшу.
    """
    def log_in(self, nickname, password):
        for usr in self.users:
            if nickname == usr.nickname:
                if hash(password) == usr.password:
                    self.current_user = usr
                    return usr
                else:
                    return None
        return None

    """
    Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, 
    если пользователя не существует (с таким же nickname). Если существует, выводит на экран: 
    "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
    """
    def register(self, nickname, password, age):
        user_exist = False
        for usr in self.users:
            if nickname == usr.nickname:
                user_exist = True
                break

        if not user_exist:
            new_user = self.User(nickname, password, age)
            self.users.append(new_user)
            self.log_in(nickname, password)
        else:
            print(f"Пользователь {nickname} уже существует")

    """
    Метод log_out для сброса текущего пользователя на None.
    """
    def log_out(self):
        self.current_user = None

    """
    Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, 
    если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
    """
    def add(self, *args):
        count = 0
        for it in args:
            video_exist = False
            for it_video in self.videos:
                if it.title == it_video.title:
                    video_exist = True
                    break
            if not video_exist:
                self.videos.append(it)
                count += 1
        return count

    # in
    """
    Проверяет содержится ли название фильма title в списке фильмов self.videos
    (регистрозависимая проверка)
    """
    def __contains__(self, title):
        for it in self.videos:
            if title == it.title:
                return True
        return False

    """
    Возвращает найденный Объект Video из списка self.videos с названием title,
    если объект не найден возвращает None 
    """
    def find(self, title):
        for it in self.videos:
            if title == it.title:
                return it
        return None

    """
    Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, 
    содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' 
    (не учитывать регистр).
    """
    def get_videos(self, search_text):
        title_list = []

        for it_video in self.videos:
            if search_text in it_video:
                title_list.append(it_video.title)

        return title_list

    """
    Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), 
    то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. 
    После текущее время просмотра данного видео сбрасывается.
    """
    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        if title not in self.videos:
            return

        vd = self.find(title)

        if vd.adult_mode:
            if self.current_user.age < Video.age_restrict:
                print(f"Вам нет {Video.age_restrict} лет, пожалуйста покиньте страницу")
                return

        while vd.time_now < vd.duration:
            vd.time_now += 1
            print(f"{vd.time_now}", end=" ")
            time.sleep(1)
        print("Конец видео")
        vd.time_now = 0


class Video:
    """
    Атриубуты: title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)),
    adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """
    age_restrict = 18

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    """
    Функция __str__ в Python делает то же самое, но ее поведение всё же немного отличается. 
    Она предназначена для создания удобочитаемой версии, полезной для отслеживания или 
    отображения информации об объекте. А метод __repr__ предназначен для предоставления 
    «официального» текстового образа объекта, который можно использовать для воссоздания этого объекта.
    """
    def __str__(self):
        return self.title.lower()

    """
    Метод __repr__ в Python выдает текстовое или строковое представление сущности или объекта
    """
    def __repr__(self):
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"

    # in
    """
    Проверяет содержится ли строка text в заголовке title (регистронезависимая проверка)
    """
    def __contains__(self, text):
        return text.lower() in self.title.lower()

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title and self.duration == other.duration and self.adult_mode == other.adult_mode
        elif isinstance(other, str):
            return self.title == other


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
print("End")





