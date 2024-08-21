import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.hashed_password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Users:
    def __init__(self, *args):
        self.users = [*args]

    def __contains__(self, item):
        if isinstance(item, tuple):
            return item in [(x.nickname, x.hashed_password) for x in self.users]
        elif isinstance(item, str):
            return item in [x.nickname for x in self.users]
        else:
            return False

    def __getitem__(self, item):
        users_list = [x for x in self.users if x.nickname == item]
        if len(users_list) > 0:
            return users_list[0]
        else:
            return None

    def __iadd__(self, other):
        self.users.append(other)
        return self


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        # self.users = []
        self.users = Users()
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        # ----- Code for: self.users = []
        # for user in self.users:
        #     if (user.nickname, user.hashed_password) == (nickname, hash(password)):
        #         self.current_user = user

        # ----- Code for: self.users = Users()
        if (nickname, hash(password)) in self.users:
            self.current_user = self.users[nickname]

    def register(self, nickname, password, age):
        # ----- Code for: self.users = []
        # if nickname in [u.nickname for u in self.users]:
        #     print(f"Пользователь {nickname} уже существует")
        # else:
        #     self.users.append(User(nickname, password, age))
        #     self.log_in(nickname, password)

        # ----- Code for: self.users = Users()
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users += User(nickname, password, age)
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(Video(video.title, video.duration, video.adult_mode))

    def get_videos(self, search_str):
        # ----- Variant 1
        # search_list = []
        # for video in self.videos:
        #     if search_str.lower() in video.title.lower():
        #         search_list.append(video.title)
        # return  search_list

        # ----- Variant 2
        return [s.title for s in filter(lambda s: search_str.lower() in s.title.lower(), self.videos)]

    def watch_video(self, video_title):
        if self.current_user is not None:
            for video in self.videos:
                if video.title == video_title:
                    if video.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        video_range = range(video.time_now + 1, video.duration + 1)
                        for video.time_now in video_range:
                            print(video.time_now, end=' ')
                            time.sleep(1)
                        print('Конец видео')
                        video.time_now = 0
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


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
