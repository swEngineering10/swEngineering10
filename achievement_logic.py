from common_function import *


achievement_file = "achievements.txt"

# 업적 부분


def load_achievements(ob):
    try:
        with open(achievement_file, "r") as file:
            for line in file:
                achievement, count = line.split(":")
                ob.achievements.append(
                    {"name": achievement, "count": int(count)})
        print("업적 정보 로드 완료")
    except FileNotFoundError:
        print("업적 정보 파일이 존재하지 않습니다. 새로운 파일을 생성합니다.")


# 업적 정보 파일 저장


def save_achievements():
    with open(achievement_file, "w") as file:
        for achievement in achievement_file:
            file.write(f"{achievement['name']}:{achievement['count']}\n")
        print("업적 정보 저장 완료")

# 업적 파일 업데이트


def update_achievement(ob, achievement_name):
    for achievement in ob.achievements:
        if achievement["name"] == achievement_name:
            if achievement["count"] == 0:
                achievement["count"] = 1
                print(achievement_name, "업적 달성!")
                break
            if achievement["count"] != 0:
                break
