import telebot
from telebot import types
import psycopg2
from datetime import*



if datetime.date(datetime.today()).isocalendar()[1] %2 ==0:
    week = 'Нижняя'
else:
    week = 'Верхняя'


token = "***"

bot = telebot.TeleBot(token)

conn = psycopg2.connect(database="timetable_db",
                        user="***",
                        password="***",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница')
    keyboard.row('Расписание на эту неделю', 'Расписание на следующую неделю')
    keyboard.row('/help')
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУсИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Доброго времени суток, я - бот, который поможет Вам узнать Ваше расписание.\n '
                                      'Доступные команды:\n'
                                      '"День" - выведет расписание на введенный день недели\n'
                                      '"Расписание на эту/след. неделю" - выведет расписание на эту/след. неделю\n'
                                      '/week - покажет какая сейчас неделя(верхняя/нижняя)\n'
                                      '/mtuci - ссылка на официальный сайт МТУСИ')


@bot.message_handler(commands=['mtuci'])
def mtuci_message(message):
    bot.send_message(message.chat.id, 'Официальный сайт МТУСИ – https://mtuci.ru/')


@bot.message_handler(commands=['week'])
def mtuci_message(message):
    bot.send_message(message.chat.id, week)


@bot.message_handler(content_types=['text'])
def answer(message):
    subj_time = ['9:30-11:05', '11:20-12:55', '13:10-14:45', '15:25-17:00', '17:15-18:50']
    if week == 'Нижняя':
        if message.text.lower() == 'понедельник':
            cursor.execute("SELECT *FROM ttable.week_2 WHERE day='%s'" % message.text)
            result = list(cursor.fetchall())
            subj_today = []
            room_n = []
            teacher_t = []
            for string in result:
                for i in range(len(string)):
                    if i>1:
                        subj_today.append(string[i])
            cursor.execute("SELECT *FROM ttable.subject")
            room_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                room_n.append('')
                for string in room_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            room_n[i] = '('+string[column+1]+')'+' '+subj_time[i]
            cursor.execute("SELECT *FROM ttable.teacher")
            teacher_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                teacher_t.append('')
                for string in teacher_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            teacher_t[i] = string[column-1]

            bot.send_message(message.chat.id, result[0][1]+'\n'+'________'+"\n"
                             +'1. ' + subj_today[0]+room_n[0]+' '+teacher_t[0]+ '\n'
                             +'2. ' + subj_today[1]+room_n[1]+' '+teacher_t[1]+ '\n'
                             +'3. ' + subj_today[2]+room_n[2]+' '+teacher_t[2]+ '\n'
                             +'4. ' + subj_today[3]+room_n[3]+' '+teacher_t[3]+ '\n'
                             +'5. ' + subj_today[4]+room_n[4]+' '+teacher_t[4]+ '\n')
        elif message.text.lower() == 'вторник':
            cursor.execute("SELECT *FROM ttable.week_2 WHERE day='%s'" % message.text)
            result = list(cursor.fetchall())
            subj_today = []
            room_n = []
            teacher_t = []
            for string in result:
                for i in range(len(string)):
                    if i>1:
                        subj_today.append(string[i])
            cursor.execute("SELECT *FROM ttable.subject")
            room_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                room_n.append('')
                for string in room_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            room_n[i] = '('+string[column+1]+')'+' '+subj_time[i]
            cursor.execute("SELECT *FROM ttable.teacher")
            teacher_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                teacher_t.append('')
                for string in teacher_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            teacher_t[i] = string[column-1]

            bot.send_message(message.chat.id, result[0][1]+'\n'+'________'+"\n"
                             +'1. ' + subj_today[0]+room_n[0]+' '+teacher_t[0]+ '\n'
                             +'2. ' + subj_today[1]+room_n[1]+' '+teacher_t[1]+ '\n'
                             +'3. ' + subj_today[2]+room_n[2]+' '+teacher_t[2]+ '\n'
                             +'4. ' + subj_today[3]+room_n[3]+' '+teacher_t[3]+ '\n'
                             +'5. ' + subj_today[4]+room_n[4]+' '+teacher_t[4]+ '\n')
        elif message.text.lower() == 'среда':
            cursor.execute("SELECT *FROM ttable.week_2 WHERE day='%s'" % message.text)
            result = list(cursor.fetchall())
            subj_today = []
            room_n = []
            teacher_t = []
            for string in result:
                for i in range(len(string)):
                    if i>1:
                        subj_today.append(string[i])
            cursor.execute("SELECT *FROM ttable.subject")
            room_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                room_n.append('')
                for string in room_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            room_n[i] = '('+string[column+1]+')'+' '+subj_time[i]
            cursor.execute("SELECT *FROM ttable.teacher")
            teacher_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                teacher_t.append('')
                for string in teacher_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            teacher_t[i] = string[column-1]
            bot.send_message(message.chat.id, result[0][1]+'\n'+'________'+"\n"
                             +'1. ' + subj_today[0]+room_n[0]+' '+teacher_t[0]+ '\n'
                             +'2. ' + subj_today[1]+room_n[1]+' '+teacher_t[1]+ '\n'
                             +'3. ' + subj_today[2]+room_n[2]+' '+teacher_t[2]+ '\n'
                             +'4. ' + subj_today[3]+room_n[3]+' '+teacher_t[3]+ '\n'
                             +'5. ' + subj_today[4]+room_n[4]+' '+teacher_t[4]+ '\n')
        elif message.text.lower() == 'четверг':
            cursor.execute("SELECT *FROM ttable.week_2 WHERE day='%s'" % message.text)
            result = list(cursor.fetchall())
            subj_today = []
            room_n = []
            teacher_t = []
            for string in result:
                for i in range(len(string)):
                    if i>1:
                        subj_today.append(string[i])
            cursor.execute("SELECT *FROM ttable.subject")
            room_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                room_n.append('')
                for string in room_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            room_n[i] = '('+string[column+1]+')'+' '+subj_time[i]
            cursor.execute("SELECT *FROM ttable.teacher")
            teacher_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                teacher_t.append('')
                for string in teacher_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            teacher_t[i] = string[column-1]

            bot.send_message(message.chat.id, result[0][1]+'\n'+'________'+"\n"
                             +'1. ' + subj_today[0]+room_n[0]+' '+teacher_t[0]+ '\n'
                             +'2. ' + subj_today[1]+room_n[1]+' '+teacher_t[1]+ '\n'
                             +'3. ' + subj_today[2]+room_n[2]+' '+teacher_t[2]+ '\n'
                             +'4. ' + subj_today[3]+room_n[3]+' '+teacher_t[3]+ '\n'
                             +'5. ' + subj_today[4]+room_n[4]+' '+teacher_t[4]+ '\n')
        elif message.text.lower() == 'пятница':
            cursor.execute("SELECT *FROM ttable.week_2 WHERE day='%s'" % message.text)
            result = list(cursor.fetchall())
            subj_today = []
            room_n = []
            teacher_t = []
            for string in result:
                for i in range(len(string)):
                    if i>1:
                        subj_today.append(string[i])
            cursor.execute("SELECT *FROM ttable.subject")
            room_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                room_n.append('')
                for string in room_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            room_n[i] = '('+string[column+1]+')'+' '+subj_time[i]
            cursor.execute("SELECT *FROM ttable.teacher")
            teacher_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                teacher_t.append('')
                for string in teacher_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            teacher_t[i] = string[column-1]

            bot.send_message(message.chat.id, result[0][1]+'\n'+'________'+"\n"
                             +'1. ' + subj_today[0]+room_n[0]+' '+teacher_t[0]+ '\n'
                             +'2. ' + subj_today[1]+room_n[1]+' '+teacher_t[1]+ '\n'
                             +'3. ' + subj_today[2]+room_n[2]+' '+teacher_t[2]+ '\n'
                             +'4. ' + subj_today[3]+room_n[3]+' '+teacher_t[3]+ '\n'
                             +'5. ' + subj_today[4]+room_n[4]+' '+teacher_t[4]+ '\n')

        elif message.text.lower() == 'расписание на эту неделю':
            week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
            for i in range(len(week_days)):
                cursor.execute("SELECT *FROM ttable.week_2 WHERE day='%s'" % week_days[i])
                result = list(cursor.fetchall())
                subj_today = []
                room_n = []
                teacher_t = []
                for string in result:
                    for i in range(len(string)):
                        if i > 1:
                            subj_today.append(string[i])
                cursor.execute("SELECT *FROM ttable.subject")
                room_s = list(cursor.fetchall())
                for i in range(len(subj_today)):
                    room_n.append('')
                    for string in room_s:
                        for column in range(len(string)):
                            if subj_today[i] == string[column]:
                                room_n[i] = '(' + string[column + 1] + ')' + ' ' + subj_time[i]
                cursor.execute("SELECT *FROM ttable.teacher")
                teacher_s = list(cursor.fetchall())
                for i in range(len(subj_today)):
                    teacher_t.append('')
                    for string in teacher_s:
                        for column in range(len(string)):
                            if subj_today[i] == string[column]:
                                teacher_t[i] = string[column - 1]

                bot.send_message(message.chat.id, result[0][1] + '\n' + '________' + "\n"
                                 + '1. ' + subj_today[0] + room_n[0] + ' ' + teacher_t[0] + '\n'
                                 + '2. ' + subj_today[1] + room_n[1] + ' ' + teacher_t[1] + '\n'
                                 + '3. ' + subj_today[2] + room_n[2] + ' ' + teacher_t[2] + '\n'
                                 + '4. ' + subj_today[3] + room_n[3] + ' ' + teacher_t[3] + '\n'
                                 + '5. ' + subj_today[4] + room_n[4] + ' ' + teacher_t[4] + '\n')
        elif message.text.lower() == 'расписание на следующую неделю':
            week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
            for i in range(len(week_days)):
                cursor.execute("SELECT *FROM ttable.week_1 WHERE day='%s'" % week_days[i])
                result = list(cursor.fetchall())
                subj_today = []
                room_n = []
                teacher_t = []
                for string in result:
                    for i in range(len(string)):
                        if i > 1:
                            subj_today.append(string[i])
                cursor.execute("SELECT *FROM ttable.subject")
                room_s = list(cursor.fetchall())
                for i in range(len(subj_today)):
                    room_n.append('')
                    for string in room_s:
                        for column in range(len(string)):
                            if subj_today[i] == string[column]:
                                room_n[i] = '(' + string[column + 1] + ')' + ' ' + subj_time[i]
                cursor.execute("SELECT *FROM ttable.teacher")
                teacher_s = list(cursor.fetchall())
                for i in range(len(subj_today)):
                    teacher_t.append('')
                    for string in teacher_s:
                        for column in range(len(string)):
                            if subj_today[i] == string[column]:
                                teacher_t[i] = string[column - 1]

                bot.send_message(message.chat.id, result[0][1] + '\n' + '________' + "\n"
                                 + '1. ' + subj_today[0] + room_n[0] + ' ' + teacher_t[0] + '\n'
                                 + '2. ' + subj_today[1] + room_n[1] + ' ' + teacher_t[1] + '\n'
                                 + '3. ' + subj_today[2] + room_n[2] + ' ' + teacher_t[2] + '\n'
                                 + '4. ' + subj_today[3] + room_n[3] + ' ' + teacher_t[3] + '\n'
                                 + '5. ' + subj_today[4] + room_n[4] + ' ' + teacher_t[4] + '\n')
        else:
            bot.send_message(message.chat.id, 'Прошу прощения, я не понимаю чего Вы хотите.')


    elif week == 'Верхняя':
        if message.text.lower() == 'понедельник':
            cursor.execute("SELECT *FROM ttable.week_1 WHERE day='%s'" % message.text)
            result = list(cursor.fetchall())
            subj_today = []
            room_n = []
            teacher_t = []
            for string in result:
                for i in range(len(string)):
                    if i>1:
                        subj_today.append(string[i])
            cursor.execute("SELECT *FROM ttable.subject")
            room_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                room_n.append('')
                for string in room_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            room_n[i] = '('+string[column+1]+')'+' '+subj_time[i]
            cursor.execute("SELECT *FROM ttable.teacher")
            teacher_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                teacher_t.append('')
                for string in teacher_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            teacher_t[i] = string[column-1]

            bot.send_message(message.chat.id, result[0][1]+'\n'+'________'+"\n"
                             +'1. ' + subj_today[0]+room_n[0]+' '+teacher_t[0]+ '\n'
                             +'2. ' + subj_today[1]+room_n[1]+' '+teacher_t[1]+ '\n'
                             +'3. ' + subj_today[2]+room_n[2]+' '+teacher_t[2]+ '\n'
                             +'4. ' + subj_today[3]+room_n[3]+' '+teacher_t[3]+ '\n'
                             +'5. ' + subj_today[4]+room_n[4]+' '+teacher_t[4]+ '\n')
        elif message.text.lower() == 'вторник':
            cursor.execute("SELECT *FROM ttable.week_1 WHERE day='%s'" % message.text)
            result = list(cursor.fetchall())
            subj_today = []
            room_n = []
            teacher_t = []
            for string in result:
                for i in range(len(string)):
                    if i>1:
                        subj_today.append(string[i])
            cursor.execute("SELECT *FROM ttable.subject")
            room_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                room_n.append('')
                for string in room_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            room_n[i] = '('+string[column+1]+')'+' '+subj_time[i]
            cursor.execute("SELECT *FROM ttable.teacher")
            teacher_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                teacher_t.append('')
                for string in teacher_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            teacher_t[i] = string[column-1]

            bot.send_message(message.chat.id, result[0][1]+'\n'+'________'+"\n"
                             +'1. ' + subj_today[0]+room_n[0]+' '+teacher_t[0]+ '\n'
                             +'2. ' + subj_today[1]+room_n[1]+' '+teacher_t[1]+ '\n'
                             +'3. ' + subj_today[2]+room_n[2]+' '+teacher_t[2]+ '\n'
                             +'4. ' + subj_today[3]+room_n[3]+' '+teacher_t[3]+ '\n'
                             +'5. ' + subj_today[4]+room_n[4]+' '+teacher_t[4]+ '\n')
        elif message.text.lower() == 'среда':
            cursor.execute("SELECT *FROM ttable.week_1 WHERE day='%s'" % message.text)
            result = list(cursor.fetchall())
            subj_today = []
            room_n = []
            teacher_t = []
            for string in result:
                for i in range(len(string)):
                    if i>1:
                        subj_today.append(string[i])
            cursor.execute("SELECT *FROM ttable.subject")
            room_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                room_n.append('')
                for string in room_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            room_n[i] = '('+string[column+1]+')'+' '+subj_time[i]
            cursor.execute("SELECT *FROM ttable.teacher")
            teacher_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                teacher_t.append('')
                for string in teacher_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            teacher_t[i] = string[column-1]
            bot.send_message(message.chat.id, result[0][1]+'\n'+'________'+"\n"
                             +'1. ' + subj_today[0]+room_n[0]+' '+teacher_t[0]+ '\n'
                             +'2. ' + subj_today[1]+room_n[1]+' '+teacher_t[1]+ '\n'
                             +'3. ' + subj_today[2]+room_n[2]+' '+teacher_t[2]+ '\n'
                             +'4. ' + subj_today[3]+room_n[3]+' '+teacher_t[3]+ '\n'
                             +'5. ' + subj_today[4]+room_n[4]+' '+teacher_t[4]+ '\n')
        elif message.text.lower() == 'четверг':
            cursor.execute("SELECT *FROM ttable.week_1 WHERE day='%s'" % message.text)
            result = list(cursor.fetchall())
            subj_today = []
            room_n = []
            teacher_t = []
            for string in result:
                for i in range(len(string)):
                    if i>1:
                        subj_today.append(string[i])
            cursor.execute("SELECT *FROM ttable.subject")
            room_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                room_n.append('')
                for string in room_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            room_n[i] = '('+string[column+1]+')'+' '+subj_time[i]
            cursor.execute("SELECT *FROM ttable.teacher")
            teacher_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                teacher_t.append('')
                for string in teacher_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            teacher_t[i] = string[column-1]

            bot.send_message(message.chat.id, result[0][1]+'\n'+'________'+"\n"
                             +'1. ' + subj_today[0]+room_n[0]+' '+teacher_t[0]+ '\n'
                             +'2. ' + subj_today[1]+room_n[1]+' '+teacher_t[1]+ '\n'
                             +'3. ' + subj_today[2]+room_n[2]+' '+teacher_t[2]+ '\n'
                             +'4. ' + subj_today[3]+room_n[3]+' '+teacher_t[3]+ '\n'
                             +'5. ' + subj_today[4]+room_n[4]+' '+teacher_t[4]+ '\n')
        elif message.text.lower() == 'пятница':
            cursor.execute("SELECT *FROM ttable.week_1 WHERE day='%s'" % message.text)
            result = list(cursor.fetchall())
            subj_today = []
            room_n = []
            teacher_t = []
            for string in result:
                for i in range(len(string)):
                    if i>1:
                        subj_today.append(string[i])
            cursor.execute("SELECT *FROM ttable.subject")
            room_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                room_n.append('')
                for string in room_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            room_n[i] = '('+string[column+1]+')'+' '+subj_time[i]
            cursor.execute("SELECT *FROM ttable.teacher")
            teacher_s = list(cursor.fetchall())
            for i in range(len(subj_today)):
                teacher_t.append('')
                for string in teacher_s:
                    for column in range(len(string)):
                        if subj_today[i] == string[column]:
                            teacher_t[i] = string[column-1]

            bot.send_message(message.chat.id, result[0][1]+'\n'+'________'+"\n"
                             +'1. ' + subj_today[0]+room_n[0]+' '+teacher_t[0]+ '\n'
                             +'2. ' + subj_today[1]+room_n[1]+' '+teacher_t[1]+ '\n'
                             +'3. ' + subj_today[2]+room_n[2]+' '+teacher_t[2]+ '\n'
                             +'4. ' + subj_today[3]+room_n[3]+' '+teacher_t[3]+ '\n'
                             +'5. ' + subj_today[4]+room_n[4]+' '+teacher_t[4]+ '\n')

        elif message.text.lower() == 'расписание на эту неделю':
            week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
            for i in range(len(week_days)):
                cursor.execute("SELECT *FROM ttable.week_1 WHERE day='%s'" % week_days[i])
                result = list(cursor.fetchall())
                subj_today = []
                room_n = []
                teacher_t = []
                for string in result:
                    for i in range(len(string)):
                        if i > 1:
                            subj_today.append(string[i])
                cursor.execute("SELECT *FROM ttable.subject")
                room_s = list(cursor.fetchall())
                for i in range(len(subj_today)):
                    room_n.append('')
                    for string in room_s:
                        for column in range(len(string)):
                            if subj_today[i] == string[column]:
                                room_n[i] = '(' + string[column + 1] + ')' + ' ' + subj_time[i]
                cursor.execute("SELECT *FROM ttable.teacher")
                teacher_s = list(cursor.fetchall())
                for i in range(len(subj_today)):
                    teacher_t.append('')
                    for string in teacher_s:
                        for column in range(len(string)):
                            if subj_today[i] == string[column]:
                                teacher_t[i] = string[column - 1]

                bot.send_message(message.chat.id, result[0][1] + '\n' + '________' + "\n"
                                 + '1. ' + subj_today[0] + room_n[0] + ' ' + teacher_t[0] + '\n'
                                 + '2. ' + subj_today[1] + room_n[1] + ' ' + teacher_t[1] + '\n'
                                 + '3. ' + subj_today[2] + room_n[2] + ' ' + teacher_t[2] + '\n'
                                 + '4. ' + subj_today[3] + room_n[3] + ' ' + teacher_t[3] + '\n'
                                 + '5. ' + subj_today[4] + room_n[4] + ' ' + teacher_t[4] + '\n')
        elif message.text.lower() == 'расписание на следующую неделю':
            week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
            for i in range(len(week_days)):
                cursor.execute("SELECT *FROM ttable.week_2 WHERE day='%s'" % week_days[i])
                result = list(cursor.fetchall())
                subj_today = []
                room_n = []
                teacher_t = []
                for string in result:
                    for i in range(len(string)):
                        if i > 1:
                            subj_today.append(string[i])
                cursor.execute("SELECT *FROM ttable.subject")
                room_s = list(cursor.fetchall())
                for i in range(len(subj_today)):
                    room_n.append('')
                    for string in room_s:
                        for column in range(len(string)):
                            if subj_today[i] == string[column]:
                                room_n[i] = '(' + string[column + 1] + ')' + ' ' + subj_time[i]
                cursor.execute("SELECT *FROM ttable.teacher")
                teacher_s = list(cursor.fetchall())
                for i in range(len(subj_today)):
                    teacher_t.append('')
                    for string in teacher_s:
                        for column in range(len(string)):
                            if subj_today[i] == string[column]:
                                teacher_t[i] = string[column - 1]

                bot.send_message(message.chat.id, result[0][1] + '\n' + '________' + "\n"
                                 + '1. ' + subj_today[0] + room_n[0] + ' ' + teacher_t[0] + '\n'
                                 + '2. ' + subj_today[1] + room_n[1] + ' ' + teacher_t[1] + '\n'
                                 + '3. ' + subj_today[2] + room_n[2] + ' ' + teacher_t[2] + '\n'
                                 + '4. ' + subj_today[3] + room_n[3] + ' ' + teacher_t[3] + '\n'
                                 + '5. ' + subj_today[4] + room_n[4] + ' ' + teacher_t[4] + '\n')
        else:
            bot.send_message(message.chat.id, 'Прошу прощения, я не понимаю чего Вы хотите.')


if __name__ == '__main__':
    bot.infinity_polling()