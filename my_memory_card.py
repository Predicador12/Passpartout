from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('¿Que pelicula gano los Oscars en 2022?', 'Todo a la vez en todas partes', 'Oppenheimer', 'El Pacto', 'Creed III'))
questions_list.append(Question('¿Que pelicula tardo mas en salir en cines?', 'Los Simpsons:La Pelicula', 'Super Mario Bros: La palicula', 'Minecraft', 'Avatar 2'))
questions_list.append(Question('¿Que pais es el mas pobre de Africa?', 'Níger', 'Sur-Africa', 'Chad', 'Uganda'))
questions_list.append(Question('¿Que videojuego es el MENOS popular?', 'Hitman 2', 'Lies of P', 'Dragon Ball Budokai Tenkaichi 3', 'Fortnite'))
questions_list.append(Question('¿Que pelicula salio antes?', 'La escena del jardín de Roundhay', 'Superman: La Pelicula', 'Titanic', 'Pintura secandose'))
questions_list.append(Question('¿Que Evento tuvo mas impacto en el mundo?', 'Revolucion Industrial', 'Evento final Capitulo 2 Remix', 'WWII', 'Descubrimiento de America'))
questions_list.append(Question('¿Cuántos animales metió Moisés en el arca?', 'Ninguno. El del arca fue Noé', '7', 'Tipos diferentes', 'Todos los del mundo'))
questions_list.append(Question('¿Qué pasó ayer en París de 6pm a 7pm?', '1 Hora', 'Nada', 'Invasion de Napoleon', 'Muerte de 100 personas'))
questions_list.append(Question('¿Qué es blanco, negro y rojo por todas partes?', 'Periodico', 'Libro', 'Una Persona', 'La Torre Eiffel'))
questions_list.append(Question('¿Cuantos orificios tiene un Pantalon?', '3', '1', '4', '9'))
questions_list.append(Question('¿En qué país se encuentra Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch?', 'Gales', 'Escocia', 'Irlanda', '¡NO EXISTE!'))
questions_list.append(Question('√Onion', 'Shallot', 'Carrot', '28', 'π'))
shuffle(questions_list)
#llista de preguntes
app = QApplication([])
btn_OK = QPushButton('Responder') 
lb_Question = QLabel('¡La pregunta más difícil del mundo!')


RadioGroupBox = QGroupBox("Opciones de respuesta") 
rbtn_1 = QRadioButton('Opción 1')
rbtn_2 = QRadioButton('Opción 2')
rbtn_3 = QRadioButton('Opción 3')
rbtn_4 = QRadioButton('Opción 4')


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 


RadioGroupBox.setLayout(layout_ans1) 


AnsGroupBox = QGroupBox("Resultado de prueba")
lb_Result = QLabel('¿Es correcto o no?')
lb_Correct = QLabel('¡Aquí estará la respuesta!')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


def show_result():
    ''' mostrar panel de respuesta '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Siguiente pregunta')


def show_question():
    ''' mostrar panel de pregunta '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Responder')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    ''' la función escribe el valor de la pregunta y responde en los widgets correspondientes mientras distribuye las opciones de respuesta de forma aleatoria'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 


def show_correct(res):
    ''' mostrar resultado - coloca el texto escrito en “resultado” y muestra el panel correspondiente '''
    lb_Result.setText(res)
    show_result()


def check_answer():
    ''' si se seleccionó una opción de respuesta, revisa y muestra el panel de respuesta '''
    if answers[0].isChecked():
        show_correct('¡Correcto!')
        window.right += 1
        window.Preguntas += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('¡Incorrecto!')
            window.right -= 1
            window.Preguntas +=1
#funció next question
def next_question():
    shuffle(questions_list)
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
        shuffle(questions_list)
    q = questions_list[window.cur_question]
    ask(q)
    print('Puntuacion Total:', window.right)
    print('Preguntas Respuestas:', window.Preguntas)
def click_OK():
    if btn_OK.text() == 'Responder':
        check_answer()
    else:
        next_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Tarjeta de memoria')
window.cur_question = -1
window.total = 0
window.right = 0
window.Preguntas = 0
btn_OK.clicked.connect(click_OK)#canviar
#next question
window.resize(400, 300)
window.show()
app.exec()