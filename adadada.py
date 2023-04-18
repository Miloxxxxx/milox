from PyQt5.QtWidgets import*

app = QApplication([])
okno = QWidget()

main = QHBoxLayout()
okno.setLayout(main)
sub = QVBoxLayout()
main.addLayout(sub)

lap = QLineEdit()
kno = QPushButton('Резудьтат')
nadp = QLabel('Здесь будет результат')

sub.addWidget(lap)
sub.addWidget(kno)
main.addWidget(nadp)

def result():
    a = lap.text()
    try: 
        a = int(a)
        a += 2
        a = str(a)
        nadp.setText(a)
    except:
        okno2 = QMessageBox()
        okno2.setText('нужно ввести число')
        okno2.exec_()

kno.clicked.connect(result)




okno.show()
app.exec_()
