from PyQt5.QtCore import Qt
from random import shuffle, randint
from PyQt5.QtWidgets import ( QApplication, QButtonGroup, QGroupBox, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QHBoxLayout,  QRadioButton )
class Q():
    def __init__(self, quetion1, right_answer, wrong1,wrong2,wrong3):
        self.quetion1 = quetion1
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


quetion_list = []
quetion_list.append(Q('Сколько существует магических чисел?','8','4','0','1'))
quetion_list.append(Q('Сколько областей у Западной Cибири?','5','3','2','6'))
quetion_list.append(Q('Сколько?','0','2','3','4'))
quetion_list.append(Q('Сколько полос на флаге США? ','13','9','5','4'))
quetion_list.append(Q ('Сколько постоянных зубов у собаки?', '42' ,'50','34','29'))
quetion_list.append(Q('На каком языке больше всего слов?','Английский','Русский','Китайский','Японский'))
quetion_list.append(Q('Какая планета ближе всех расположена к Солнцу?','Меркурий','Нептун','Венера','Земля'))
quetion_list.append(Q('Изчего состоит Солнце','Из смеси газов','Раскалённый металл','Из чего-то другого','Лава'))
quetion_list.append(Q('К какой планете принадлежат спутники Оберон и Титания?','Уран','Земля','Нептун','Юпитер'))
quetion_list.append(Q('Какая из этих планет самая маленькая?','Меркурий','Земля','Венера','Нептун'))




app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(600,300)

quetion = QLabel('Какой национальности не существует')
vop1 = QRadioButton('Энцы')
vop2 = QRadioButton('Чулымцы')
vop3 = QRadioButton('Смурфы')
vop4 = QRadioButton('Алеуты')
knop = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')
la1 = QHBoxLayout()
la2 = QVBoxLayout()
la3 = QVBoxLayout()
la2.addWidget(vop1)
la2.addWidget(vop2)
la3.addWidget(vop3)
la3.addWidget(vop4)
la1.addLayout(la2)
la1.addLayout(la3)
RadioGroupBox.setLayout(la1)
la_1 = QHBoxLayout()
la_2 = QHBoxLayout()
la_3 = QHBoxLayout()
la_1.addWidget(quetion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
la_2.addWidget(RadioGroupBox)
la_3.addStretch(1)
la_3.addWidget(knop, stretch=2)
la_3.addStretch(1)

lc = QVBoxLayout()
lc.addLayout(la_1,stretch=2)
lc.addLayout(la_2, stretch=8)
lc.addStretch(1)
lc.addLayout(la_3, stretch=1)
lc.addStretch(1)
lc.setSpacing(5)




result = QGroupBox('Результат текста')
lresult = QLabel('Правильно/Неправильно')
lcorrect = QLabel('ответ будет тут!')

lres = QVBoxLayout()
lres.addWidget(lresult, alignment=(Qt.AlignLeft | Qt.AlignTop))
lres.addWidget(lcorrect, alignment=Qt.AlignHCenter, stretch=2)
result.setLayout(lres)
la_1.addWidget(quetion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))


la_2.addLayout(lres)

la_3.addStretch(1)
la_3.addWidget(knop,stretch=2)
la_3.addStretch(1)



RadioGroup = QButtonGroup()
RadioGroup.addButton(vop1)
RadioGroup.addButton(vop2)
RadioGroup.addButton(vop3)
RadioGroup.addButton(vop4)

def show_result():
    RadioGroupBox.hide()
    result.show()
    knop.setText('Следующий вопрос')




def show_quetion():
    RadioGroupBox.show()
    result.hide()
    knop.setText('Ответить')
    RadioGroup.setExclusive(False)
    vop1.setChecked(False)
    vop2.setChecked(False)
    vop3.setChecked(False)
    vop4.setChecked(False)
    RadioGroup.setExclusive(True)


answer = [vop1, vop2, vop3, vop4]
def ask(q: Q):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    quetion.setText(q.quetion1)
    lcorrect.setText(q.right_answer)
    show_quetion()
def show_correct(res):
    lcorrect.setText(res)
    show_result()
def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильно ответов: ', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')
            print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильно ответов: ', window.score)
            print('Рейтинг:', (window.score/window.total*100), '%')
def next_quetion():
    window.total += 1
    print('Статистика\n-Всего вопросов:', window.total, '/n-Правильных ответов:', window.score)
    'window.cur_quetion = window.cur_quetion + 1'
    cur_quetion = randint(0, len(quetion_list) - 1)
    q  = quetion_list[cur_quetion]
    '''if window.cur_quetion >= len(quetion_list):
        window.cur_quetion = 0
    q = quetion_list[window.cur_quetion]'''
    ask(q)

def click_ok():
    if knop.text() == 'Ответить':
        check_answer()
    else:
        next_quetion()


window.cur_quetion = -1
knop.clicked.connect(click_ok)
window.score = 0
window.total = 0
next_quetion()

next_quetion()

window.setLayout(lc)
window.show()
app.exec_()





