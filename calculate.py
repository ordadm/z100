from sto import makeroom, openfirstbox, opennextbox, wayprisoner, mission
import time
from tqdm import updt

start_time = time.time()

qtyprisoner: int = 100     # количество заключенных
qtymissions: int = 125  # количество экспериментов
qtychance: int = 50      # количество коробочек которые можно открыть
positiv = 0                 # количество успешных экспериментов

# отработка эксперимента несколько раз для статистики
def result():
    for stat in range(1, qtymissions+1):
    aroom = makeroom()
    updt(qtymissions, stat + .1,start_time,positiv)
#    print(f'миссия №, {stat}, стартовала')
#    print(aroom)
    if mission(aroom):
        positiv += 1
#       print(f'миссия№ {stat} успешна')
#    else:
#        print ('миссия №',stat,'провалена')

# Отображение результатов
# print(f'Количество заключенных {qtyprisoner}, количество попыток (открытие коробочек) {qtychance} \n'
#       f'Пройденых миссий {positiv} из {qtymissions}, что является {round(positiv/qtymissions*100,4)}%')
#
# print("--- %s seconds ---" % (time.time() - start_time))