print ('Добро пожаловать!') # Приветсвуем Юзера
print ('Пожалуйста, пройдите наш непростой тест')
print ('-------------------')
print ('')
ball=0 # Создаем переменную в которой будем хранить количество правильных ответов
kol=0 # Создаем переменную в которой будем хранить количество вопросов
f=open('d:/YandexDisk/Documents/Python/10Ekzamen/bigtest/q/thems.txt','r', encoding='utf-8')
tema1 = f.readline().strip()
tema2 = f.readline().strip()
tema3 = f.readline().strip()
f.close()
print ('Выберите тему на которую бы вы хотели пройти тест')
print (tema1)
print (tema2)
print (tema3)
usertema = int(input('Введите номер темы и нажмите ENTER: \n'))
if usertema == 1:
    f=open('d:/YandexDisk/Documents/Python/10Ekzamen/bigtest/q/q1.txt','r', encoding='utf-8')
    #открываем на чтение файл с вопросами
    while True:     #читаем файл построчно, пока есть вопросы:
        vopros=f.readline().strip() # Здесь вопрос
        if (not vopros):    # Если вопросов нет, то завершаем работу
            break
        otvet1=f.readline().strip() # Здесь 1 вариант ответа
        otvet2=f.readline().strip() # Здесь 2 вариант ответа
        otvet3=f.readline().strip() # Здесь 3 вариант ответа
        kod=f.readline().strip()    # Здесь указан номер правльного ответа
        print ('Вопрос ' +str(kol+1) + ': ' + str(vopros))
        print ('1.' + otvet1)
        print ('2.' + otvet2)
        print ('3.' + otvet3)
        k=str(input('Введите номер правильного ответа и нажмите ENTER: \n'))
        kol=kol+1
        if(k==kod):
            ball=ball+1
            print ('Вы ответили правильно!\n')
        else:
            print ('Вы ответили не правильно\n')
elif usertema == 2:
    f=open('d:/YandexDisk/Documents/Python/10Ekzamen/bigtest/q/q2.txt','r', encoding='utf-8')
    while True:     #читаем файл построчно, пока есть вопросы:
        vopros=f.readline().strip() # Здесь вопрос
        if (not vopros):    # Если вопросов нет, то завершаем работу
            break
        otvet1=f.readline().strip() # Здесь 1 вариант ответа
        otvet2=f.readline().strip() # Здесь 2 вариант ответа
        otvet3=f.readline().strip() # Здесь 3 вариант ответа
        kod=f.readline().strip()    # Здесь указан номер правльного ответа
        print ('Вопрос ' +str(kol+1) + ': ' + str(vopros))
        print ('1.' + otvet1)
        print ('2.' + otvet2)
        print ('3.' + otvet3)
        k=str(input('Введите номер правильного ответа и нажмите ENTER: \n'))
        kol=kol+1
        if(k==kod):
            ball=ball+1
            print ('Вы ответили правильно!\n')
        else:
            print ('Вы ответили не правильно\n')
else:
    f=open('d:/YandexDisk/Documents/Python/10Ekzamen/bigtest/q/q3.txt','r', encoding='utf-8')
    while True:     #читаем файл построчно, пока есть вопросы:
        vopros=f.readline().strip() # Здесь вопрос
        if (not vopros):    # Если вопросов нет, то завершаем работу
            break
        otvet1=f.readline().strip() # Здесь 1 вариант ответа
        otvet2=f.readline().strip() # Здесь 2 вариант ответа
        otvet3=f.readline().strip() # Здесь 3 вариант ответа
        kod=f.readline().strip()    # Здесь указан номер правльного ответа
        print ('Вопрос ' +str(kol+1) + ': ' + str(vopros))
        print ('1.' + otvet1)
        print ('2.' + otvet2)
        print ('3.' + otvet3)
        k=str(input('Введите номер правильного ответа и нажмите ENTER: \n'))
        kol=kol+1
        if(k==kod):
            ball=ball+1
            print ('Вы ответили правильно!\n')
        else:
            print ('Вы ответили не правильно\n')
f.close()
print ('Вы ответили правильно на ' + str(ball) + ' из ' + str(kol) + ' вопросов')
