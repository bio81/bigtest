print ('Добро пожаловать!') # Приветсвуем Юзера
print ('Пожалуйста, пройдите наш непростой тест')
print ('-------------------')
print ('')
ball=0 # Создаем переменную в которой будем хранить количество правильных ответов
kol=0 # Создаем переменную в которой будем хранить количество вопросов
f=open('d:/YandexDisk/Documents/Python/10 Экзамен/q.txt','r', encoding='utf-8')
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
print ('Вы ответили правильно на ' + str(ball) + ' из ' + str(kol) + ' вопросов')
input ()
