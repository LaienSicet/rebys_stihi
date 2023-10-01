from pickle import dump, load
from intIgrok import *
import sys

QQQ = 0

def dekodir(d):
    'декодировка'
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
    c = [[b[i], a[i]] for i in range(len(a))]
    c = dict(c)
    d2 = ""
    for i, n in enumerate(d):
        d2 += n
        if (i+1) % 3 == 0:
            d2 += " "
    d = d2.split(" ")
    d1 = ""
    for n in d:
        if n in c:
            d1 += c[n]
    d1 = d1.split("\n")

    return d1

def kodir(d):
    'кодировка'
    d = "\n".join(d)
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

    return d1

def pri_stih(d, q=0, z=0):
    'подготовка стиха для вывова на экран'
    global stroka_p, otvet
    o = []
    d1 = ""
    for i, n in enumerate(d):
        n1 = n.split(" ")[0]
        if len(n) == 0:
            pass #d1 += "\n"
        elif i != len(d)-1 and n1 == "*":
            d1 += n[1::]
        elif i != len(d)-1 and n1 == str(q):
            d1 += n[1::] + " " * (25-len(n)) + "<-- !!!"
            stroka_p = n[1::]
            ui.label_4.setText(stroka_p)
        elif i != len(d)-1 and n1 == str(z):
            d1 += " " + "*" * 20 + " " * 5 + "<-- ???"
            if len(o) == 0:
                o.append(n[1::])
        elif i != len(d)-1:
            d1 += " " + "*" * 20
        d1 += "\n"
    if z != 0:
        try:
            o_1 = o[0].split(" ")
            otvet = hvost(o_1[len(o_1)-1])
        except:
            teh_i = "  проблемы со свитком."
            ui.label_2.setText(teh_i)
    return d1

def opr_q_z(d):
    'поиск с стихе тех. индексов и нахождение наименьшей пары'
    global q, z
    q_ = []
    z_ = []

    for i, n in enumerate(d):
        if len(n) == 0:
            pass
        elif n[0] == "*":
            pass
        elif n[0].isdigit():
            n1 = n.split(" ")
            n2 = int(n1[0])
            if n2 % 2 == 1:
                q_.append(n2)
            elif n2 % 2 == 0 and n2 != 0:
                z_.append(n2)
    if len(q_) == 0 and len(z_) == 0:

        gotovo()
        return True
    else:
        q = min(q_)
        z = min(z_)

def gotovo():
    "окончание"
    global QQQ
    QQQ = 1
    sistem = stih[len(stih) - 1].split(" ")

    if rip < int(sistem[2]) or sistem[3] == "~~~":
        AAA = "свиток расшифрован!!! код: " + sistem[1]
    else:
        AAA = "свиток расшифрован!!! код: " + sistem[3]

    teh_i = AAA
    ui.label_2.setText(teh_i)
    stih_1 = pri_stih(stih)
    ui.textBrowser.setText(stih_1)
    stroka_p = ""
    ui.label_4.setText(stroka_p)
    ui.textEdit_2.clear()

    if ui.checkBox.isChecked():
        stih_1 = kodir(stih)
        try:
            with open(i_fa, "wb") as fa:
                dump(stih_1, fa)
        except:
            teh_i = "  хм... проблемы с сохранением."
            ui.label_2.setText(teh_i)

def hvost(a):
    'отсев не_букв'
    b = ""
    for i in a:
        if i.isalpha():
            b += i
    return b

def open_fa():
    "КНОПКА. открытие файла"
    if QQQ == 1:
        return True
    teh_i = ""
    ui.label_2.setText(teh_i)
    global stih, rip, i_fa
    try:
        i_fa = ui.textEdit.toPlainText() + ".bin"
        with open(i_fa, "rb") as fa:
            stih_0 = load(fa)
        stih = dekodir(stih_0)
        s = []
        for i in stih:
            i1 = i.strip()
            s.append(i1)
        stih = s
        rip = int(stih[len(stih)-1].split(" ")[4])
        opr_q_z(stih)
        if QQQ==1:
            return True
        stih_1 = pri_stih(stih, q, z)
        ui.textBrowser.setText(stih_1)
        ui.textEdit.clear()

    except:
        ui.textBrowser.setText("")
        teh_i = "     проблемы со свитком."
        ui.label_2.setText(teh_i)

def proverit():
    "КНОПКА. проверка слова."
    if QQQ == 1:
        return True
    global rip
    teh_i = ""
    ui.label_2.setText(teh_i)
    if not(stih):
        teh_i = "       нет стиха."
        ui.label_2.setText(teh_i)
        return False
    if len(ui.textEdit_2.toPlainText()) == 0:
        teh_i = "    нет ответа. совсем нет..."
        ui.label_2.setText(teh_i)
        return False
    if ui.textEdit_2.toPlainText() == otvet:
        stih_cop = stih.copy()
        for i, n in enumerate(stih_cop):
            if len(n) != 0 and i != len(stih)-1 and n[0] != "*" and n[0] != "s":
                n_1 = int(n.split(" ")[0])
                if n_1 == q or n_1 == z:
                    zamena = n.split(" ")
                    zamena[0] = "*"
                    zamena = " ".join(zamena)
                    stih[i] = zamena

        opr_q_z(stih)

        if QQQ == 1:
            return True
        teh_i = " ВЕРНО!"
        ui.label_2.setText(teh_i)
        if q and z:
            stih_1 = pri_stih(stih, q, z)
        else:
            stih_1 = pri_stih(stih)
        ui.textBrowser.setText(stih_1)
        ui.textEdit_2.clear()
    else:
        rip += 1
        ui.textEdit_2.clear()
        teh_i = "   увы...   неверно."
        ui.label_2.setText(teh_i)

    if ui.checkBox.isChecked():
        stih_1 = kodir(stih)
        try:
            with open(i_fa, "wb") as fa:
                dump(stih_1, fa)
        except:
            teh_i = "  хм... проблемы с сохранением."
            ui.label_2.setText(teh_i)


app = QtWidgets.QApplication(sys.argv)
mainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()

stih = ""
ui.textBrowser.setText(stih)

teh_i = ""
ui.label_2.setText(teh_i)

stroka_p = ""
ui.label_4.setText(stroka_p)

ui.pushButton.clicked.connect(open_fa)
ui.pushButton_2.clicked.connect(proverit)

sys.exit(app.exec_())

