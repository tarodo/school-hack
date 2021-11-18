import random
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation


def fix_marks(schoolkid: Schoolkid):
    child_marks = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    for one_mark in child_marks:
        one_mark.points = 5
        one_mark.save()


def remove_chastisements(schoolkid: Schoolkid):
    all_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for one_chastisement in all_chastisements:
        one_chastisement.delete()


def create_commendation(child_name, subject_name):
    child = None
    try:
        child = Schoolkid.objects.filter(full_name__contains=child_name).get()
    except MultipleObjectsReturned:
        print('There are many children with this name')
        return None
    except ObjectDoesNotExist:
        print('There is no child with this name')
        return None
    child_lessons = Lesson.objects.filter(year_of_study=child.year_of_study, group_letter=child.group_letter,
                                          subject__title=subject_name, subject__year_of_study=child.year_of_study).all()
    commendations = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
                     'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
                     'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!',
                     'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!',
                     'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!',
                     'Здорово!', 'Это как раз то, что нужно!', 'Я тобой горжусь!',
                     'С каждым разом у тебя получается всё лучше!', 'Мы с тобой не зря поработали!',
                     'Я вижу, как ты стараешься!', 'Ты растешь над собой!', 'Ты многое сделал, я это вижу!',
                     'Теперь у тебя точно все получится!']
    one_lesson = random.choice(child_lessons)
    commendation_text = random.choice(commendations)
    commendation = Commendation.objects.create(text=commendation_text, created=one_lesson.date, schoolkid=child,
                                               subject=one_lesson.subject, teacher=one_lesson.teacher)
    commendation.save()
