from initAdmin import *
from pickle import dump

import sys
app = QtWidgets.QApplication(sys.argv)
mainWindow = QtWidgets.QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(mainWindow)
mainWindow.show()

aaa = 'стартовые строки в стихе должны быть отмечанны знаком "*" отделённым пробелом.\n\nостальные строки (в начале каждой строки) должны  ' \
    'быть пронумерованны (и отделены пробелом). по следующей логике:\n\n' \
    '- не чётные - строки подсказки которые увидет пользователь. недопустимо повторение таких номеров.\n' \
    '- чётные - строки которые будут открываться после введения верного слова. при повторение\nтаких номеров строки откроются блоком,' \
    ' однако угадать будет нужно слово первой строки блока.'

bbb = ""

def prover(n, m):
    "проверка на цельность последовательности"
    global ohi
    n1 = n
    if ma_1 == 0 or ma_2 == 0:
        return 0
    while n != m:
        n = n1
        for i in d:
            try:
                if int(i[0]) == n:
                    n1 += 2
                    if n % 2 == 0:
                        break
            except:
                pass
        if n + 2 != n1:
            ohi += 1
            n1 = n + 2

def poisk_fa():
    'поиск файла'
    global d, ime
    try:
        d = []
        ime = ui.textEdit.toPlainText() + ".txt"
        with open(ime, "r") as fa:
            for line in fa:
                line = line.replace("\n", " ")
                a = line.strip().split(" ")
                d.append(a)
        return True

    except:

        bbb = "там нет стиха...  повторите."
        ui.label_2.setText(bbb)
        return False

def prov_na_ohi():
    'проверка последовательности и поиск прочих ошибок'
    global ma_1, ma_2, ohi
    ohi = 0
    for i in d:
        if i[0] != "*" and i[0] != "":
            try:
                de = int(i[0])
            except:

                ohi += 1
    ma_1 = [0]
    ma_2 = [0]
    for i in d:
        try:
            if int(i[0]) % 2 == 1:
                ma_1.append(int(i[0]))
            elif int(i[0]) % 2 == 0:
                ma_2.append(int(i[0]))
        except:
            pass
    ma_1 = max(ma_1)
    ma_2 = max(ma_2)
    if ma_1 + 1 != ma_2:
        ohi += 1
    prover(1, ma_1)
    prover(2, ma_2)
    if ohi != 0:
        global b
        bbb = "увы в тексте обраруженно " + str(ohi) + " шибок." \
                                                     "\nрекомендуется: удалить, исправить, и повторить."
        ui.label_2.setText(bbb)
    else:
        bbb = ""
        ui.label_2.setText(bbb)


def dobav_tex_inf():
    'запись тех. инфы в свиток'
    global d, im_sv
    d = ""
    with open(ime, "r") as fa:
        for line in fa:
            d += line

    im_sv = ui.textEdit_2.toPlainText()
    kod = ui.textEdit_3.toPlainText()
    kod_prob = "~~~"
    hoslo_ohi = 10000
    if ui.checkBox.isChecked():
        kod_prob = ui.textEdit_4.toPlainText()

        try:
            hoslo_ohi = int(ui.textEdit_5.toPlainText())

        except:
            b = "некорреттное значение предела ошибок"
            ui.label_2.setText(b)
            return False

    d = d + "sistem" + " " + str(kod) + " " + str(hoslo_ohi) + " " + str(kod_prob) + " " + str(0)
    return d

def kodir():
    a = ["*", "ф", "б", "!", "в", "г", "9", "а", "е", "2", "ё", "и", "6", "-", "о", "у", "д", "ж", "з", "й", "к", "л",
         "?", "7", "м", "3", "н", "п", "0", "х", "ч", "ц", "5", "ш", ":", "щ", " ", "8", "ы", "э", "Ш", "Щ", "ю",
         "я", "ь", "1", "ъ", ",", "р", "4", "с", ".", "т", "~", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
         "a", "s", "d", "f", "g", "h", "j", "Ь", "Э", "Ю", "Я", "k", "l", "z", "x", "c", "v", "b", "n", "m", "A",
         "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z", "\n", "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О",
         "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ъ", "Ы"]

    b = [str(i + 1).rjust(3, "3") if i % 3 == 0 else str(i + 11).rjust(3, "3") for i in range(len(a) * 2)]
    b = set(b)
    b = list(b)
    b.sort()

    c = [[a[i], b[i]] for i in range(len(a))]
    c = dict(c)

    d1 = ""
    for n in d:
        if n in c:
            d1 += c[n]

    with open(im_sv + ".bin", "wb") as fa:
        dump(d1, fa)

def sozd_svitok():
    "основная рабочая функция"
    if not(poisk_fa()):

        return False
    prov_na_ohi()

    if len(ui.textEdit_2.toPlainText()) == 0 or len(ui.textEdit_3.toPlainText()) == 0:
        b = "есть пустые поля."
        ui.label_2.setText(b)
        return False
    elif ui.checkBox.isChecked() and (len(ui.textEdit_4.toPlainText()) == 0 or len(ui.textEdit_5.toPlainText()) == 0 or
                                      not(ui.textEdit_5.toPlainText().isdigit())):
        b = "есть пустые поля, в области опасности."
        ui.label_2.setText(b)
        return False
    elif ui.checkBox.isChecked() == False and (len(ui.textEdit_4.toPlainText()) != 0 or len(ui.textEdit_5.toPlainText()) != 0):
        b = 'хм. возможно, забыта "галочка".'
        ui.label_2.setText(b)
        return False

    d = dobav_tex_inf()

    if d == False:

        return False
    else:
        kodir()
        if ohi == 0:
            bbb = '         ГОТОВО!'
            ui.label_2.setText(bbb)

ui.label.setText(aaa)
ui.label_2.setText(bbb)

ui.pushButton.clicked.connect(sozd_svitok)

sys.exit(app.exec_())