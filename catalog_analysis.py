import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# Этап 1. Разминка: переменные, числа, math

""""Возвращает среднюю оценку по каталогу"""

def average_rating(movies:list) -> float:
    result = 0.0
    for i in movies:
        result +=  i["rating"]
    return round(result / len(movies), 1)

# print (average_rating(movies))

""""Возвращает кортеж"""

def catalog_age_stats(movies: list, current_year: int = 2026) -> tuple:
    min_year = max_year = movies[0]['year']
    average_year = 0
    
    for i in movies:
        average_year += i['year']
        if i['year'] < min_year:
            min_year = i['year']
        if i['year'] > max_year:
            max_year = i['year']
    return current_year-min_year, current_year-max_year, math.ceil(current_year - (average_year / len(movies)))

#print(catalog_age_stats(movies))

""""Переводит минуты в формат"""

def duration_in_hours(minutes: int) -> str:

    return f"{minutes // 60}ч {minutes % 60}м"

#print(duration_in_hours(movies[0]['duration_min']))

# Этап 2. Условия и match

"""Возвращает категорию"""

def rating_tier(rating:float) -> str:
    tier = ""
    if rating >= 9:
        tier = "шедевр"
    elif 7 <= rating <= 8.9:
        tier = "средне"
    else: 
        tier = "средне" if 5 <= rating <=6.9 else "слабо"

    return tier

#print(rating_tier(movies[3]["rating"]))


"""Возвращает метку в зависимости от выхода фильмa"""

def decade_label(year: int) -> str:

    match year:
        case _ if year >= 2020:
            return "новые"
        case _ if 2015 <= year < 2020:
            return "недавние"
        case _ if year < 2015:
            return "старые"
        case _:
            return ""

#print(decade_label(movies[0]['year']))

# Этап 3. Циклы

"""for i in movies:
    if "comedy" in i.get("genres"):
        continue
    else:
        print(i.get("title"))

i = 0
while i < len(movies) - 1:
    if movies[i].get('rating') >= 9.0:
        print(f"Фильм: {movies[i].get('title')}, рейтинг: {movies[i].get('rating')}")
        break
    else: 
        i += 1
else: 
    print("Шедевров не найдено")"""

"""Считает количество фильмов длиннее threshold"""

def count_long_movies(movie:list, threshold: int =120) -> int:
    count = 0
    for i in movie:
        if i['duration_min'] >= 120:
            count += 1
    return count

#print(count_long_movies(movies))

# Этап 4. Строки

""""Приводит строку к формату Title Case"""

def normalize_title(title: str) -> str:
    word = title.split()
    new_words = []
    for i in word:
        new_words.append(i[0].upper() + i[1:])
    return " ".join(new_words)

#print (normalize_title(movies[0]['title']))

"""Превращает нормализованное название в «слаг» вида"""

def make_slug(title: str) -> str:
    return title.lower().replace(" ", "-")

#print(make_slug(movies[0]['title']))

"""Возвращающает единую строку с описанием фильма"""

def format_report_line(movie: dict) -> str:
    return f'"{movie.get('title')}" ({movie.get('year')}) - {movie.get('rating')}/10, {duration_in_hours(movie.get("duration_min"))}, жанры: {", ".join(sorted(movie.get('genres')))}'

#print(format_report_line(movies[0]))

# Этап 5. Списки

""""Возращает список названий фильмов, отсортированных по убыванию рейтинга"""

def titles_sorted_by_rating(movies: list) -> list:
    movies_dict = {}
    for movie in movies:
        movies_dict[str(movie.get('title'))] = float(movie.get('rating'))

    movies_dict = dict(sorted(movies_dict.items(),key=lambda item: item[1], reverse=True))
    keys_list = list(movies_dict.keys()) 

    return keys_list

#print(titles_sorted_by_rating(movies))

""""Возращает список из n кортежей, (title, rating) - топ по рейтингу"""

def top_n_by_rating(movies: list, n: int =3) -> tuple:
    movies_dict = {}
    for movie in movies:
        movies_dict[str(movie.get('title'))] = float(movie.get('rating'))

    sorted_pairs = sorted(movies_dict.items(),key=lambda item: item[1], reverse=True)[:n]

    result = []
    for key, value in sorted_pairs:
        result.append((key, value))
    return result

#print(top_n_by_rating(movies))

# Этап 6. Словари

"""Возвращает словарь {жанр: количество фильмов}"""

def count_by_genre(movies: list):
    pass

""""Возвращает словарь {актер: [список названий фильмов]}"""

def actor_filmography(movies: list):
    actors = []
    result = {}

    for movie in movies:
        actors.extend(movies.get('actors'))

    actors = set(actors)

"""Генератора словаря для фильмов с рейтингом выше среднего"""

# Этап 7. Множества

def all_genres(movies: list) -> set:
    pass

def common_actors(movie1: dict, movie2: dict) -> set:
    pass

def genres_only_in_one(movies_a: dict, movies_b: dict) -> set:
    pass

#print(genres_only_in_one(movies[0], movies[3]))

# Этап 8. Итераторы и генераторы

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie.get('rating') >= min_rating:
            yield movie

for movie in iter_high_rated(movies):
    print(format_report_line(movie))

print(sum(m["duration_min"] for m in movies if m["rating"] > 7))

# Этап 9. Итоговый отчет

def build_report(movies):
    print("ОТЧеТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies, current_year=2026)[2]} лет \n")
    print("Топ-3 фильма:")

    for i in top_n_by_rating(movies):
        for movie in movies:
            if i[0] in movie.values():
                print("\t" + format_report_line(movie))

    print("Фильмов по жанрам:")