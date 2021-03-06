import random
from datacenter.models import (
    Schoolkid,
    Mark,
    Chastisement,
    Lesson,
    Commendation,
    Subject,
)


def fix_marks(schoolkid: Schoolkid):
    child_marks = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    for one_mark in child_marks:
        one_mark.points = 5
        one_mark.save()
    print("Success! You are an excellent student!")


def remove_chastisements(schoolkid: Schoolkid):
    all_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for one_chastisement in all_chastisements:
        one_chastisement.delete()
    print("Success! You are a student w/o problems!")


def create_commendation(child_name, subject_name):
    child = None
    try:
        child = Schoolkid.objects.filter(full_name__contains=child_name).get()
    except Schoolkid.MultipleObjectsReturned:
        print("There are many children with this name")
        return None
    except Schoolkid.DoesNotExist:
        print("There is no child with this name")
        return None
    try:
        lesson_subject = Subject.objects.filter(
            year_of_study=child.year_of_study, title=subject_name
        ).get()
    except Subject.DoesNotExist:
        print("There is no subject with this name")
        return None
    try:
        one_lesson = (
            Lesson.objects.filter(
                year_of_study=child.year_of_study,
                group_letter=child.group_letter,
                subject=lesson_subject,
            )
            .order_by("?")
            .first()
        )
    except Lesson.DoesNotExist:
        print("There is no lesson for commendation")
        return None
    commendations = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!",
    ]
    commendation_text = random.choice(commendations)
    commendation = Commendation.objects.create(
        text=commendation_text,
        created=one_lesson.date,
        schoolkid=child,
        subject=one_lesson.subject,
        teacher=one_lesson.teacher,
    )
    commendation.save()
    print(
        f"'{commendation.schoolkid}' received commendation "
        f"'{commendation.text}' for the "
        f"{commendation.subject} on {commendation.created}"
    )
