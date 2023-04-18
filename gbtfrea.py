from PyQt5.QtWidgets import*

app = QApplication([])
okno = QWidget()

main = QHBoxLayout()
okno.setLayout(main)
sub = QVBoxLayout()
main.addLayout(sub)

lap = QLineEdit()
lik = QLineEdit()
kno = QPushButton('*')
nadp = QLabel('Здесь будет результат')
kno2 = QPushButton('+')
kno3 = QPushButton('-')
kno4 = QPushButton('/')
#kno5 = QPushButton('Результат')


sub.addWidget(lap)
sub.addWidget(lik)
sub.addWidget(kno)
sub.addWidget(kno2)
sub.addWidget(kno3)
sub.addWidget(kno4)
#sub.addWidget(kno5)

main.addWidget(nadp)

def result():
    a = lap.text()
    b = lik.text()
    try: 
        a = int(a)
        b = int(b)
        res = str(a * b)
        nadp.setText(res)
    except:
        okno2 = QMessageBox()
        okno2.setText('нужно ввести число')
        okno2.exec_()

kno.clicked.connect(result)

def result2():
    a = lap.text()
    b = lik.text()
    try: 
        a = int(a)
        b = int(b)
        res = str(a + b)
        nadp.setText(res)
    except:
        okno2 = QMessageBox()
        okno2.setText('нужно ввести число')
        okno2.exec_()

kno2.clicked.connect(result2)

def result3():
    a = lap.text()
    b = lik.text()
    try: 
        a = int(a)
        b = int(b)
        res = str(a - b)
        nadp.setText(res)
    except:
        okno2 = QMessageBox()
        okno2.setText('нужно ввести число')
        okno2.exec_()

kno3.clicked.connect(result3)

def result4():
    a = lap.text()
    b = lik.text()
    try: 
        a = int(a)
        b = int(b)
        res = str(a / b)
        nadp.setText(res)
    except:
        okno2 = QMessageBox()
        okno2.setText('нужно ввести число')
        okno2.exec_()

kno4.clicked.connect(result4)




okno.show()
app.exec_()
