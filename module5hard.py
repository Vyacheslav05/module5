import hashlib
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return int(hashlib.sha256(password.encode('utf-8')).hexdigest(), 16)


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

import time
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = User("", password, 0).hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return True
        return False

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return False
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)
        return True

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, video_name):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for video in self.videos:
            if video.title == video_name:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return

                while video.time_now < video.duration:
                    print(f' {video.time_now + 1}')
                    video.time_now += 1
                    time.sleep(0.5)  # пауза 0,5 сек между выводами

                print('Конец видео') # вот это в выводе на консоль тоже появится
                video.time_now = 0
                return

        print('Видео не найдено')

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
print(ur.current_user.nickname) # в задании было print(ur.current_user), я
# добавил nickname, чтобы вывелся urban_pythonist

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!') # вот это в выводе на консоль тоже появится,
# как "Видео не найдено"











