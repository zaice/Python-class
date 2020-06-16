inputText = 'Если хочешь закончить, набери “выход”.\nА теперь, пожалуйста, укажи свой пол: '
gender = input(inputText)
while (gender != 'выход'):
   if (gender == 'мальчик' or gender == 'мужчина' or gender == 'юноша' or gender == 'муж' or gender == 'мужской' or gender == 'male' or gender == 'м' or gender == 'm'or gender == 'Мальчик' or gender == 'Мужчина' or gender == 'Юноша' or gender == 'Муж' or gender == 'Мужской' or gender == 'Male' or gender == 'М' or gender == 'M' or gender == 'МАЛЬЧИК' or gender == 'МУЖЧИНА' or gender == 'ЮНОША' or gender == 'МУЖ' or gender == 'МУЖСКОЙ' or gender == 'MALE'):
       print( 'Здорово, чувак!' )
   elif (gender == 'девочка' or gender == 'женщина' or gender == 'девушка' or gender == 'жен' or gender == 'женский' or gender == 'female' or gender == 'ж' or gender == 'f'or gender == 'Девочка' or gender == 'Женщина' or gender == 'Девушка' or gender == 'Жен' or gender == 'Женский' or gender == 'Female' or gender == 'Ж' or gender == 'F' or gender == 'ДЕВОЧКА' or gender == 'ЖЕНЩИНА' or gender == 'ДЕВУШКА' or gender == 'ЖЕН' or gender == 'ЖЕНСКИЙ' or gender == 'FEMALE'):
           print('Привет, милая!')
   else:
       print('Не знаю, что сказать...')
   gender = input(inputText)
print('Пока!')
