import sys
import csv
import sqlite3
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication
from PyQt5.QtGui import QPixmap, QFont, QIcon, QFontDatabase, QCursor, QCloseEvent
from PyQt5.QtCore import QSize, QTimer
from PyQt5.Qt import Qt
from random import choice
from datetime import datetime, timedelta
lse = list()  # list split elements
with open('Informations/informationshop.csv', encoding="utf8") as csvfile:  # открывается csv файл с информацией из магазина улучшений
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index > 0:
            lse.append(row)
all_artifacts = list()


con1 = sqlite3.connect('artifacts_and_information.sqlite')
cursor1 = con1.cursor()
resultat = cursor1.execute("""SELECT * FROM artifact""")  # открывается sqlite файл с информацией о всех артефактов
for i in resultat:
    all_artifacts.append([i[1], i[2], str(i[3] - 1)])
rarity = list()
con2 = sqlite3.connect('artifacts_and_information.sqlite')
cursor2 = con2.cursor()
resultat = cursor2.execute("""SELECT * FROM rarity""")  # открывается sqlite файл с информацией о редкости артефактов
for i in resultat:
    rarity.append([i[1]])


class GreenArtifact(QWidget):
    def __init__(self):
        super().__init__()
        # Тут задаются базовые настройки
        self.flag7 = False
        self.end = False
        self.file = open('Progress.txt', mode='rt').read()  # открывается файл, который хранит в себе все данные о игроке
        self.information = self.file.split('\n')
        if datetime.now().day == 31 and datetime.now().month == 10:  # в хеллоуин даётся скин
            dataday_hel = self.information[5].split(';')
            dataday_hel[2] = '1'
            dataday_hel = ';'.join(dataday_hel)
            self.information[5] = dataday_hel
        self.file = open('Progress.txt', mode='w')
        self.file.write('\n'.join(self.information))
        if self.information[3] == '0':
            self.information[3] = str(datetime.now() - timedelta(minutes=20))

        self.file2 = open('Shop.txt', mode='rt').read()  # открывается файл, который хранит в себе все данные о покупках
        self.forshop = self.file2.split('\n')
        self.file2 = open('Shop.txt', mode='w')
        self.file2.write('\n'.join(self.forshop))
        self.live = 0
        self.lila = int(self.information[2]) - int(self.forshop[0])
        self.accurat = int(self.forshop[1])
        self.flag4 = False
        self.initUI()  # тут и происходит вся магия. MAGIC!!!!!

    def logo(self):  # отображение логотипа в начале запуска игры
        if self.flag8:
            self.greenarifact.move(0, 0)
            self.flag8 = False
        else:
            self.greenarifact.move(1280, 720)
            self.logotip.move(120, 720)
            self.time4.stop()

    def dowload(self):  # окно загрузки
        if self.dq1 == 0:
            self.dow.move(0, 0)
        elif self.dq1 == 1:
            self.dow.setPixmap(QPixmap('dowload/d2.png'))
        elif self.dq1 == 2:
            self.dow.setPixmap(QPixmap('dowload/d3.png'))
        elif self.dq1 == 3:
            self.dow.setPixmap(QPixmap('dowload/d4.png'))
        elif self.dq1 == 4:
            self.dow.setPixmap(QPixmap('dowload/d1.png'))
            self.dq1 = -1
            self.time3.stop()
            self.dow.move(1280, 720)
        self.dq1 += 1

    def initUI(self):  # создание всех объектов в игре
        self.mahn = 0
        self.click = 0
        self.planet = ['land1.png']
        self.greening = [['green/c1.png', 'green/c2.png', 'green/c3.png', 'green/c4.png', 'green/c5.png', 'green/c6.png',
                          'green/c7.png', 'green/c8.png', 'green/c9.png', 'green/c10.png', 'green/c11.png']]
        self.setFixedSize(1280, 720)
        self.move(0, 30)
        self.setWindowTitle('Greenartifact')

        self.lbl = QLabel(self)
        self.lbl.resize(1280, 720)
        self.lbl.setPixmap(QPixmap("space(standart).png"))

        self.lbl2 = QLabel(self)
        self.lbl2.resize(1280, 720)
        self.lbl2.setPixmap(QPixmap('stars(test).png'))

        self.planets = QLabel(self)
        self.planets.resize(1280, 720)
        self.planets.setPixmap(QPixmap('planet(test).png'))

        for i in range(len(self.planet)):
            image = self.planet[i]
            self.planet[i] = QLabel(self)
            self.planet[i].resize(1280, 150)
            self.planet[i].setPixmap(QPixmap(image))
            self.planet[i].move(1280, 720)

        for i in range(len(self.greening)):
            for j in range(len(self.greening[i])):
                img = self.greening[i][j]
                self.greening[i][j] = QLabel(self)
                self.greening[i][j].resize(1280, 150)
                self.greening[i][j].setPixmap(QPixmap(img))
                self.greening[i][j].move(1280, 720)

        self.spaceship1 = QLabel(self)
        self.spaceship1.resize(1280, 720)
        self.spaceship1.setPixmap(QPixmap('Space_ship/spaceship_sost1.png'))

        self.spaceship_color = QLabel(self)
        self.spaceship_color.move(0, 0)
        self.spaceship_color.resize(1280, 720)
        self.spaceship_color.setPixmap(QPixmap(''))

        self.spaceship1piu = QLabel(self)
        self.spaceship1piu.resize(1280, 720)

        self.otch = QLabel(self)
        self.otch.move(1280, 720)
        self.otch.resize(150, 50)
        self.otch.setText(f'<font color="red">{self.click}/35')
        self.otch.setFont(QFont("progresspixel-bold", 20))

        self.lvl = QLabel(self)
        self.lvl.move(1280, 720)
        self.lvl.resize(150, 50)
        self.lvl.setText(f'Ур. <font color="red">{self.information[2]}')
        self.lvl.setFont(QFont("progresspixel-bold", 20))

        self.meteorses = ['meteor/meteor - 1.png', 'meteor/meteor - 2.png', 'meteor/meteor - 3.png',
                          'meteor/meteor - 4.png', 'meteor/meteor - 5.png', 'meteor/meteor - 6.png',
                          'meteor/meteor - 7.png', 'meteor/meteor - 8.png', 'meteor/meteor - 9.png',
                          'meteor/meteor - 10.png', 'meteor/meteor - 11.png', 'meteor/meteor - 12.png',
                          'meteor/meteor - 13.png', 'meteor/meteor - 14.png', 'meteor/meteor - 15.png',
                          'meteor/meteor - 16.png', 'meteor/meteor - 17.png', 'meteor/meteor - 18.png',
                          'meteor/meteor - 19.png', 'meteor/meteor - 20.png', 'meteor/meteor - 21.png',
                          'meteor/meteor - 22.png', 'meteor/meteor - 23.png', 'meteor/meteor - 24.png',
                          'meteor/meteor - 25.png', 'meteor/meteor - 26.png', 'meteor/meteor - 27.png']

        self.meteor1 = QPushButton(self)
        self.meteor1.resize(130, 130)
        self.meteor1.move(1280, 720)
        image = choice(self.meteorses)
        self.meteor1.setIcon(QIcon(image))
        self.meteor1.setIconSize(QSize(130, 130))
        self.meteor1.setStyleSheet("QPushButton{background: transparent;}")
        self.meteor1.clicked.connect(self.metor)

        self.meteor2 = QPushButton(self)
        self.meteor2.resize(130, 130)
        self.meteor2.move(1280, 720)
        image = choice(self.meteorses)
        self.meteor2.setIcon(QIcon(image))
        self.meteor2.setIconSize(QSize(130, 130))
        self.meteor2.setStyleSheet("QPushButton{background: transparent;}")
        self.meteor2.clicked.connect(self.metor)

        self.meteor3 = QPushButton(self)
        self.meteor3.resize(130, 130)
        self.meteor3.move(1280, 720)
        image = choice(self.meteorses)
        self.meteor3.setIcon(QIcon(image))
        self.meteor3.setIconSize(QSize(130, 130))
        self.meteor3.setStyleSheet("QPushButton{background: transparent;}")
        self.meteor3.clicked.connect(self.metor)

        self.pb = QPushButton(self)
        self.pb.resize(130, 50)
        self.pb.move(575, 650)
        self.pb.setIcon(QIcon('Button/start.png'))
        self.pb.setIconSize(QSize(130, 50))
        self.pb.setStyleSheet("QPushButton{background: transparent;}")
        self.pb.clicked.connect(self.button)

        self.give = QPushButton(self)
        self.give.resize(210, 50)
        self.give.setIcon(QIcon('Button/give.png'))
        self.give.setIconSize(QSize(210, 50))
        self.give.move(1280, 720)
        self.give.clicked.connect(self.restart)

        self.wat = ['Icon/water_0.png', 'Icon/water_1.png', 'Icon/water_2.png', 'Icon/water_3.png', 'Icon/water_4.png']

        self.wate = QLabel(self)
        self.wate.resize(50, 50)
        self.wate.move(1280, 720)

        self.watet = QLabel(self)
        self.watet.resize(50, 50)
        self.watet.move(1280, 720)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.water)

        self.back = QLabel(self)
        self.back.resize(1280, 720)
        self.back.setPixmap(QPixmap('back.png'))
        self.back.move(1280, 720)

        self.leav = QPushButton(self)
        self.leav.resize(185, 50)
        self.leav.setIcon(QIcon('Button/leave.png'))
        self.leav.setIconSize(QSize(185, 50))
        self.leav.move(1280, 720)
        self.leav.clicked.connect(self.restart)

        self.menu = QPushButton(self)
        self.menu.resize(50, 50)
        self.menu.setIcon(QIcon('Button/pause.png'))
        self.menu.setIconSize(QSize(50, 50))
        self.menu.move(1280, 720)
        self.menu.clicked.connect(self.pause)

        self.contin = QPushButton(self)
        self.contin.resize(265, 50)
        self.contin.setIcon(QIcon('Button/continue.png'))
        self.contin.setIconSize(QSize(265, 50))
        self.contin.move(1280, 720)
        self.contin.clicked.connect(self.pause)

        self.exit = QPushButton(self)
        self.exit.resize(50, 50)
        self.exit.setIcon(QIcon('Button/exit.png'))
        self.exit.setIconSize(QSize(50, 50))
        self.exit.move(10, 660)
        self.exit.clicked.connect(self.exitet)

        #  ---------------------------------------

        self.cristal = QLabel(self)
        self.cristal.resize(25, 25)
        self.cristal.setPixmap(QPixmap('Icon/mahn.png'))
        self.cristal.move(615, 10)

        self.cristal2 = QLabel(self)
        self.cristal2.resize(25, 25)
        self.cristal2.setPixmap(QPixmap('Icon/mahn.png'))
        self.cristal2.move(1280, 720)

        self.cristalt = QLabel(self)
        self.cristalt.move((615 - ((len(self.information[0]) + 1)) * 10), 8)
        self.cristalt.resize(100, 30)
        self.cristalt.setText(f'<font color="white">{self.information[0]}')
        self.cristalt.setFont(QFont("Tahoma", 15))

        self.money = QLabel(self)
        self.money.resize(25, 25)
        self.money.setPixmap(QPixmap('Icon/money.png'))
        self.money.move(715, 10)

        self.money2 = QLabel(self)
        self.money2.resize(25, 25)
        self.money2.setPixmap(QPixmap('Icon/money.png'))
        self.money2.move(1280, 720)

        self.moneyt = QLabel(self)
        self.moneyt.move((715 - ((len(self.information[1]) + 1)) * 10), 8)
        self.moneyt.resize(100, 30)
        self.moneyt.setText(f'<font color="white">{self.information[1]}')
        self.moneyt.setFont(QFont("Tahoma", 15))

        self.sost = QLabel(self)
        self.sost.move(1280, 720)
        self.sost.resize(len(str(self.mahn)) * 40, 60)
        self.sost.setText(f'<font color="white">{self.mahn}')
        self.sost.setFont(QFont("progresspixel-bold", 30))

        #  ---------------------------------------

        self.upgarde = QPushButton(self)
        self.upgarde.resize(50, 50)
        self.upgarde.setIcon(QIcon('Button/upgrade.png'))
        self.upgarde.setIconSize(QSize(50, 50))
        self.upgarde.move(5, 5)
        self.upgarde.clicked.connect(self.up_up)

        self.color_ship = QPushButton(self)
        self.color_ship.resize(50, 50)
        self.color_ship.setIcon(QIcon('Button/color_ship.png'))
        self.color_ship.setIconSize(QSize(50, 50))
        self.color_ship.move(5, 165)
        self.color_ship.clicked.connect(self.up_up)

        self.iven = QPushButton(self)
        self.iven.resize(50, 100)
        self.iven.setIcon(QIcon('Icon/inven.png'))
        self.iven.setIconSize(QSize(50, 100))
        self.iven.move(5, 60)
        self.iven.clicked.connect(self.up_up)

        self.tablo = QLabel(self)
        self.tablo.resize(1280, 720)
        self.tablo.setPixmap(QPixmap('Artifacts/tablo.png'))
        self.tablo.move(1280, 720)

        self.obmen = QPushButton(self)
        self.obmen.resize(210, 50)
        self.obmen.setIcon(QIcon('Button/obmen.png'))
        self.obmen.setIconSize(QSize(210, 50))
        self.obmen.move(1280, 720)
        self.obmen.clicked.connect(self.obmenik)

        self.select = QLabel(self)
        self.select.resize(60, 100)
        self.select.setPixmap(QPixmap('Icon/select.png'))
        self.select.move(1280, 0)

        self.up_space_ship = QPushButton(self)
        self.up_space_ship.resize(50, 90)
        self.up_space_ship.setIcon(QIcon('Icon/upgrade_space_ship.png'))
        self.up_space_ship.setIconSize(QSize(50, 90))
        self.up_space_ship.move(1280, 720)
        self.up_space_ship.clicked.connect(self.shop)
        self.up_space_shipt = QLabel(self)
        self.up_space_shipt.resize(100, 50)
        self.up_space_shipt.move(1280, 720)
        self.up_space_shipt.setText(f'<font color="white">{lse[1][2]}')
        self.up_space_shipt.setFont(QFont("progresspixel-bold", 12))

        self.up_coin = QPushButton(self)
        self.up_coin.resize(50, 90)
        self.up_coin.setIcon(QIcon('Icon/upgrade_coin.png'))
        self.up_coin.setIconSize(QSize(50, 90))
        self.up_coin.move(1280, 720)
        self.up_coin.clicked.connect(self.shop)
        self.up_coint = QLabel(self)
        self.up_coint.resize(100, 50)
        self.up_coint.move(1280, 720)
        self.up_coint.setText(f'<font color="white">{lse[2][2]}')
        self.up_coint.setFont(QFont("progresspixel-bold", 12))

        self.up_water = QPushButton(self)
        self.up_water.resize(50, 90)
        self.up_water.setIcon(QIcon('Icon/up_water.png'))
        self.up_water.setIconSize(QSize(50, 90))
        self.up_water.move(1280, 720)
        self.up_water.clicked.connect(self.shop)
        self.up_watert = QLabel(self)
        self.up_watert.resize(100, 50)
        self.up_watert.move(1280, 720)
        self.up_watert.setText(f'<font color="white">{lse[0][2]}')
        self.up_watert.setFont(QFont("progresspixel-bold", 12))

        self.plus1000 = QPushButton(self)
        self.plus1000.resize(50, 90)
        self.plus1000.setIcon(QIcon('Icon/plus1000'))
        self.plus1000.setIconSize(QSize(50, 90))
        self.plus1000.move(1280, 720)
        self.plus1000.clicked.connect(self.shop)
        self.plus1000t = QLabel(self)
        self.plus1000t.resize(100, 50)
        self.plus1000t.move(1280, 720)
        self.plus1000t.setText(f'<font color="white">{lse[3][2]}')
        self.plus1000t.setFont(QFont("progresspixel-bold", 12))

        #  ------------------------------------------

        self.esc = QPushButton(self)
        self.esc.resize(45, 45)
        self.esc.setIcon(QIcon('Button/esc.png'))
        self.esc.setIconSize(QSize(45, 45))
        self.esc.move(1280, 720)
        self.esc.clicked.connect(self.up_up)

        self.infa = QPushButton(self)
        self.infa.setFont(QFont("progresspixel-bold", 12))
        self.infa.setStyleSheet("""color: white;background-color: black;""")
        self.infa.setEnabled(False)
        self.infa.resize(400, 120)
        self.infa.move(1280, 720)
        self.img_artifacts = ['Artifacts/buljuga.png', 'Artifacts/flowerin.png', 'Artifacts/man.png',
                              'Artifacts/flower_shrakolik.png', 'Artifacts/flower_sun.png', 'Artifacts/oduwan.png',
                              'Artifacts/gold.png']
        self.select2 = QLabel(self)
        self.select2.resize(85, 85)
        self.select2.setPixmap(QPixmap('Icon/select2.png'))
        self.select2.move(1280, 0)

        for i in range(len(self.img_artifacts)):
            img = self.img_artifacts[i]
            self.img_artifacts[i] = QPushButton(self)
            self.img_artifacts[i].resize(75, 75)
            self.img_artifacts[i].setIcon(QIcon(img))
            self.img_artifacts[i].setIconSize(QSize(75, 75))
            self.img_artifacts[i].move(1280, 720)
            self.img_artifacts[i].clicked.connect(self.infa_for_artifact)

        self.colors = [['', ''], ['Space_ship/space_ship_white_color1.png', 'Space_ship/space_ship_white_color2.png'],
                       ['Space_ship/space_ship_red_color1.png', 'Space_ship/space_ship_red_color2.png']]

        self.colors_for_ship = ['Colors_ship/None.png', 'Colors_ship/White.png', 'Colors_ship/Red.png']
        for i in range(len(self.colors_for_ship)):
            img = self.colors_for_ship[i]
            self.colors_for_ship[i] = QPushButton(self)
            self.colors_for_ship[i].resize(75, 75)
            self.colors_for_ship[i].setIcon(QIcon(img))
            self.colors_for_ship[i].setIconSize(QSize(75, 75))
            self.colors_for_ship[i].move(1280, 720)
            self.colors_for_ship[i].clicked.connect(self.select_color)
            if self.information[5].split(';')[i] == '2':
                self.spaceship_color.setPixmap(QPixmap(self.colors[i][0]))

        self.you_winner = QLabel(self)
        self.you_winner.resize(1280, 50)
        self.you_winner.move(1280, 720)
        self.you_winner.setText('<font color="white">За попеду вы получаете один артефакт с этой планеты!')
        self.you_winner.setFont(QFont("progresspixel-bold", 20))

        self.dow = QLabel(self)
        self.dow.resize(1280, 720)
        self.dow.setPixmap(QPixmap('dowload/d1'))
        self.dow.move(1280, 720)
        self.dq1 = 0

        self.time2 = QTimer(self)
        self.time2.setInterval(100)
        self.time2.timeout.connect(self.anim2)

        self.time3 = QTimer(self)
        self.time3.setInterval(200)
        self.time3.timeout.connect(self.dowload)

        self.animation = QTimer(self)
        self.animation.setInterval(150)
        self.animation.timeout.connect(self.anim_live)

        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.start()
        self.time.timeout.connect(self.anim1)

        self.forgame = QTimer(self)
        self.forgame.setInterval(50)
        self.forgame.timeout.connect(self.game)

        self.flag = True
        self.flag2 = True
        self.flag3 = True
        self.flag5 = True

        self.logotip = QLabel(self)
        self.logotip.resize(1280, 720)
        self.logotip.setPixmap(QPixmap('logo.png'))
        self.greenarifact = QLabel(self)
        self.greenarifact.resize(1280, 720)
        self.greenarifact.setPixmap(QPixmap('greenartifactи.png'))
        self.greenarifact.move(1280, 720)
        self.flag8 = True
        self.time4 = QTimer(self)
        self.time4.setInterval(5000)
        self.time4.start()
        self.time4.timeout.connect(self.logo)
        self.mouseReleaseEvent = self.Cursor
        for j in range(len(self.colors_for_ship)):
            if self.information[5].split(';')[j] == '2':
                self.spaceship_color.setPixmap(QPixmap(self.colors[j][0]))

    def select_color(self):  # отвечает за покраску корабля
        self.select2.move(self.sender().x() - 5, self.sender().y() - 5)
        noting = list()
        for i in range(len(self.information[5].split(';'))):
            if (self.information[5].split(';'))[i] == '0':
                noting.append(int(i))
        users = list()
        for i in range(len(self.colors_for_ship)):
            if i not in noting:
                users.append(self.colors_for_ship[i])
        chislo = users.index(self.sender())
        ostatok = self.information[5].split(';')
        for i in range(len(users)):
            if i == chislo:
                ostatok[i] = str(2)
            else:
                ostatok[i] = str(1)
        ostatok = ';'.join(ostatok)
        self.information[5] = ostatok
        self.file = open('Progress.txt', mode='w')
        self.file.write('\n'.join(self.information))
        for j in range(len(self.colors_for_ship)):
            if self.information[5].split(';')[j] == '2':
                self.spaceship_color.setPixmap(QPixmap(self.colors[j][0]))

    def obmenik(self):  # отвечает за обмен легендарных вещей на пластинки
        self.addArtifact(self.img_artifacts[3], '-')
        self.information[1] = str(int(self.information[1]) + 1)
        self.moneyt.setText(f'<font color="white">{self.information[1]}')
        self.file = open('Progress.txt', mode='w')
        self.file.write('\n'.join(self.information))
        self.flag5 = True
        self.up_up()
        self.up_up()
        self.up_up(True)

    def infa_for_artifact(self):  # при нажатии на артефакт отображается о нём краткая информация
        kol = self.information[4].split(';')[self.img_artifacts.index(self.sender())]
        rar = rarity[int((all_artifacts[self.img_artifacts.index(self.sender())])[2])][0]
        ch = self.img_artifacts.index(self.sender())
        self.infa.setText(f'Редкость:{rar}\n-{all_artifacts[ch][0]}-\n{all_artifacts[ch][1]}\nу вас {kol} шт.')
        self.select2.move(self.sender().x() - 5, self.sender().y() - 5)
        self.obmen.move(1280, 720)
        if self.sender() == self.img_artifacts[3]:
            self.obmen.move(535, 650)

    def Cursor(self, event):  # даёт возможность нажимать на ПКМ и помогает не захломлять код
        if event == self.up_space_ship:
            self.infa.setText(f'Стоимость: {lse[1][2]} кристалов\n{lse[1][0]}\n{lse[1][1]}')
        elif event == self.up_coin:
            elemsplit = '\n'.join(lse[2][1].split('--'))
            self.infa.setText(f'Стоимость: {lse[2][2]} кристалов\n{lse[2][0]}\n{elemsplit}')
        elif event == self.up_water:
            self.infa.setText(f'Стоимость: {lse[0][2]} кристалов\n{lse[0][0]}\n{lse[0][1]}')
        elif event == self.plus1000:
            self.infa.setText(f'Стоимость: {lse[3][2]} пластинка\n{lse[3][0]}\n{lse[3][1]}')
        elif event.button() == Qt.RightButton and not self.flag5 and self.flag9:
            if event.x() in range(615, 666) and event.y() in range(315, 406):
                self.infa.setText(f'Стоимость: {lse[1][2]} кристалов\n{lse[1][0]}\n{lse[1][1]}')
                self.select.move(610, 310)
            if event.x() in range(685, 736) and event.y() in range(315, 406):
                self.select.move(680, 310)
                elemsplit = '\n'.join(lse[2][1].split('--'))
                self.infa.setText(f'Стоимость: {lse[2][2]} кристалов\n{lse[2][0]}\n{elemsplit}')
            if event.x() in range(545, 596) and event.y() in range(315, 406):
                self.select.move(540, 310)
                self.infa.setText(f'Стоимость: {lse[0][2]} кристалов\n{lse[0][0]}\n{lse[0][1]}')
            if event.x() in range(615, 666) and event.y() in range(465, 556):
                self.select.move(610, 460)
                self.infa.setText(f'Стоимость: {lse[3][2]} пластинка\n{lse[3][0]}\n{lse[3][1]}')

    def water(self):  # показывает состояние воды и можете ли вы отправиться на миссию
        if (datetime.now() - datetime.strptime(self.information[3], "%Y-%m-%d %H:%M:%S.%f")).seconds // 60 >= 0:
            self.wate.move(1225, 5)
            self.wate.setPixmap(QPixmap(self.wat[0]))
            self.flag6 = False
            self.flag7 = False
        if (datetime.now() - datetime.strptime(self.information[3], "%Y-%m-%d %H:%M:%S.%f")).seconds // 60 >= 5:
            self.wate.move(1225, 5)
            self.wate.setPixmap(QPixmap(self.wat[1]))
            self.flag6 = True
            self.flag7 = False
        if (datetime.now() - datetime.strptime(self.information[3], "%Y-%m-%d %H:%M:%S.%f")).seconds // 60 >= 10:
            self.wate.move(1225, 5)
            self.wate.setPixmap(QPixmap(self.wat[2]))
            self.flag6 = True
            self.flag7 = False
        if (datetime.now() - datetime.strptime(self.information[3], "%Y-%m-%d %H:%M:%S.%f")).seconds // 60 >= 15:
            self.wate.move(1225, 5)
            self.wate.setPixmap(QPixmap(self.wat[3]))
            self.flag6 = True
            self.flag7 = False
        if (datetime.now() - datetime.strptime(self.information[3], "%Y-%m-%d %H:%M:%S.%f")).seconds // 60 >= 20:
            self.wate.move(1225, 5)
            self.wate.setPixmap(QPixmap(self.wat[4]))
            self.file = open('Progress.txt', mode='w')
            self.information[3] = str(datetime.now() - timedelta(minutes=20))
            self.up_water.setIcon(QIcon('Icon/up_waterx.png'))
            self.file.write('\n'.join(self.information))
            self.flag6 = True
            self.flag7 = True
        minute = 19 - ((datetime.now() - datetime.strptime(self.information[3], "%Y-%m-%d %H:%M:%S.%f")).seconds // 60)
        if len(str(minute)) == 1:
            minute = '0' + str(minute)
        secunde = 60 - ((datetime.now() - datetime.strptime(self.information[3], "%Y-%m-%d %H:%M:%S.%f")).seconds % 60)
        if len(str(secunde)) == 1:
            secunde = '0' + str(secunde)
        if int(minute) == -1:
            minute = '00'
            secunde = '00'
        self.watet.setText(f'<font color="white">{minute}:<font color="white">{secunde}')
        self.watet.setFont(QFont("progresspixel-bold", 12))
        self.watet.move(1227, 45)

    def up_up(self, retur=False):  # своеобразное меню где можно пройти на следующие вкладки
        if self.flag5:
            if self.sender() == self.upgarde:
                self.flag9 = True
                self.infa.setText('Нажмите на ПКМ, для подробной\nинформации, ЛКМ для покупки!')
                if (int(self.information[2]) - int(self.forshop[0]) <= 1) or (int(self.information[0]) < int(lse[1][2])):
                    self.up_space_ship.setIcon(QIcon('Icon/upgrade_space_shipx.png'))
                if int(self.information[0]) < int(lse[2][2]):
                    self.up_coin.setIcon(QIcon('Icon/upgrade_coinx.png'))
                if int(self.information[0]) < int(lse[0][2]) or self.flag7:
                    self.up_water.setIcon(QIcon('Icon/up_waterx.png'))
                if int(self.information[1]) < int(lse[3][2]):
                    self.plus1000.setIcon(QIcon('Icon/plus1000x.png'))
                self.infa.move(440, 100)
                self.plus1000.move(615, 465)
                self.plus1000t.move(635, 425)
                self.up_coin.move(685, 315)
                self.up_coint.move(690, 275)
                self.up_space_shipt.move(625, 275)
                self.cristal2.move(628, 260)
                self.money2.move(628, 410)
                self.up_space_ship.move(615, 315)
                self.up_water.move(545, 315)
                self.up_watert.move(550, 275)
            elif self.sender() == self.iven or retur:
                self.infa.setText('Нажмите на иконку предмета, \nдля подробной информации!')
                self.infa.move(440, 100)
                self.tablo.move(0, 0)
                strochek = 1
                noting = list()
                for i in range(len(self.information[4].split(';'))):
                    if (self.information[4].split(';'))[i] == '0':
                        noting.append(int(i))
                allis = len(self.information[4].split(';')) - self.information[4].split(';').count('0')
                art = allis
                art2 = allis
                users = list()
                for i in range(len(self.img_artifacts)):
                    if i not in noting:
                        users.append(self.img_artifacts[i])
                while allis > 10:
                    strochek += 1
                    allis -= 10
                for i in range(strochek):
                    if i == strochek - 1:
                        for j in range(allis):
                            users[art - art2].move(205 + (j * 75) + j * 5, 295 + (i * 75) + i * 5)
                            art2 += 1
                    else:
                        for j in range(10):
                            users[art - art2].move(205 + (j * 75) + j * 5, 295 + (i * 75) + i * 5)
                            art2 += 1
            elif self.sender() == self.color_ship:
                self.infa.setText('Нажмите на иконку раскраски, \nчтобы применить!')
                self.infa.move(440, 100)
                self.tablo.move(0, 0)
                strochek = 1
                noting = list()
                selecting = 0
                for i in range(len(self.information[5].split(';'))):
                    if (self.information[5].split(';'))[i] == '0':
                        noting.append(int(i))
                    if (self.information[5].split(';'))[i] == '2':
                        selecting = int(i)
                allis = len(self.information[5].split(';')) - self.information[5].split(';').count('0')
                art = allis
                art2 = allis
                users = list()
                for i in range(len(self.colors_for_ship)):
                    if i not in noting:
                        users.append(self.colors_for_ship[i])
                while allis > 10:
                    strochek += 1
                    allis -= 10
                for i in range(strochek):
                    if i == strochek - 1:
                        for j in range(allis):
                            users[art - art2].move(205 + (j * 75) + j * 5, 295 + (i * 75) + i * 5)
                            art2 += 1
                    else:
                        for j in range(10):
                            users[art - art2].move(205 + (j * 75) + j * 5, 295 + (i * 75) + i * 5)
                            art2 += 1
                self.select2.move(users[selecting].x() - 5, users[selecting].y() - 5)
            self.color_ship.move(1280, 720)
            self.iven.move(1280, 720)
            self.upgarde.move(1280, 720)
            self.esc.move(5, 5)
            self.exit.move(1280, 720)
            self.back.move(0, 0)
            self.flag5 = False
        else:
            self.flag9 = False
            for i in range(len(self.img_artifacts)):
                self.img_artifacts[i].move(1280, 720)
            for i in range(len(self.colors_for_ship)):
                self.colors_for_ship[i].move(1280, 720)
            self.color_ship.move(5, 165)
            self.plus1000.move(1280, 720)
            self.plus1000t.move(1280, 720)
            self.obmen.move(1280, 720)
            self.select2.move(1280, 720)
            self.tablo.move(1280, 720)
            self.iven.move(5, 60)
            self.select.move(1280, 720)
            self.infa.move(1280, 720)

            self.up_water.move(1280, 720)
            self.up_watert.move(1280, 720)

            self.up_coin.move(1280, 720)
            self.up_coint.move(1280, 720)

            self.cristal2.move(1280, 720)
            self.money2.move(1280, 720)
            self.up_space_ship.setIcon(QIcon('Icon/upgrade_space_ship.png'))
            self.up_space_shipt.move(1280, 720)

            self.up_coin.setIcon(QIcon('Icon/upgrade_coin.png'))
            self.up_water.setIcon(QIcon('Icon/up_water.png'))
            self.plus1000.setIcon(QIcon('Icon/plus1000.png'))

            self.esc.move(1280, 720)
            self.flag5 = True
            self.exit.move(10, 660)
            self.back.move(1280, 720)
            self.upgarde.move(5, 5)
            self.up_space_ship.move(1280, 720)

    def shop(self):  # отвечает за покупку товара
        self.Cursor(self.sender())
        if self.sender() == self.up_space_ship:
            self.select.move(610, 310)
            if (int(self.information[2]) - int(self.forshop[0]) > 1) and (int(self.information[0]) >= int(lse[1][2])):
                self.information[0] = str(int(self.information[0]) - int(lse[1][2]))
                self.forshop[0] = str(int(self.forshop[0]) + 1)
                self.moneyt.setText(f'<font color="white">{self.information[1]}')
                self.cristalt.setText(f'<font color="white">{self.information[0]}')
                self.moneyt.move((715 - (len(self.information[1]) + 1) * 10), 8)
                self.cristalt.move((615 - (len(self.information[0]) + 1) * 10), 8)
                self.file = open('Progress.txt', mode='w')
                self.file.write('\n'.join(self.information))
                self.file2 = open('Shop.txt', mode='w')
                self.file2.write('\n'.join(self.forshop))
                self.lila = int(self.information[2]) - int(self.forshop[0])
        elif self.sender() == self.up_coin:
            self.select.move(680, 310)
            if int(self.information[0]) >= int(lse[2][2]):
                self.forshop[1] = str(int(self.forshop[1]) + 1)
                self.information[0] = str(int(self.information[0]) - int(lse[2][2]))
                self.moneyt.setText(f'<font color="white">{self.information[1]}')
                self.cristalt.setText(f'<font color="white">{self.information[0]}')
                self.moneyt.move((715 - (len(self.information[1]) + 1) * 10), 8)
                self.cristalt.move((615 - (len(self.information[0]) + 1) * 10), 8)
                self.file = open('Progress.txt', mode='w')
                self.file.write('\n'.join(self.information))
                self.file2 = open('Shop.txt', mode='w')
                self.file2.write('\n'.join(self.forshop))
                self.accurat = int(self.forshop[1])
        elif self.sender() == self.up_water:
            self.select.move(540, 310)
            if int(self.information[0]) >= int(lse[0][2]) and not self.flag7:
                self.information[0] = str(int(self.information[0]) - int(lse[0][2]))
                self.moneyt.setText(f'<font color="white">{self.information[1]}')
                self.cristalt.setText(f'<font color="white">{self.information[0]}')
                self.moneyt.move((715 - ((len(self.information[1]) + 1)) * 10), 8)
                self.cristalt.move((615 - ((len(self.information[0]) + 1)) * 10), 8)
                self.information[3] = str(datetime.now() - timedelta(minutes=20))
                self.file = open('Progress.txt', mode='w')
                self.file.write('\n'.join(self.information))
                self.flag7 = True
        elif self.sender() == self.plus1000:
            self.select.move(610, 460)
            if int(self.information[1]) >= int(lse[3][2]):
                self.information[1] = str(int(self.information[1]) - int(lse[3][2]))
                self.information[0] = str(int(self.information[0]) + 1000)
                self.moneyt.setText(f'<font color="white">{self.information[1]}')
                self.cristalt.setText(f'<font color="white">{self.information[0]}')
                self.moneyt.move((715 - ((len(self.information[1]) + 1)) * 10), 8)
                self.cristalt.move((615 - ((len(self.information[0]) + 1)) * 10), 8)
                self.file = open('Progress.txt', mode='w')
                self.file.write('\n'.join(self.information))
        if (int(self.information[2]) - int(self.forshop[0]) <= 1) or (int(self.information[0]) < int(lse[1][2])):
            self.up_space_ship.setIcon(QIcon('Icon/upgrade_space_shipx.png'))
        else:
            self.up_space_ship.setIcon(QIcon('Icon/upgrade_space_ship.png'))
        if int(self.information[0]) < int(lse[2][2]):
            self.up_coin.setIcon(QIcon('Icon/upgrade_coinx.png'))
        else:
            self.up_coin.setIcon(QIcon('Icon/upgrade_coin.png'))
        if int(self.information[0]) < int(lse[0][2]) or self.flag7:
            self.up_water.setIcon(QIcon('Icon/up_waterx.png'))
        else:
            self.up_water.setIcon(QIcon('Icon/up_water.png'))
        if int(self.information[1]) < int(lse[3][2]):
            self.plus1000.setIcon(QIcon('Icon/plus1000x.png'))

    def exitet(self):  # если пользователь решил выйти из игры
        if self.flag2:
            self.file = open('Progress.txt', mode='w')
            self.file.write('\n'.join(self.information))
            self.file2 = open('Shop.txt', mode='w')
            self.file2.write('\n'.join(self.forshop))
            sys.exit()

    def pause(self):  # ставит игру на паузу
        if self.flag3:
            self.contin.move(515, 300)
            self.menu.setIconSize(QSize(40, 40))
            self.back.move(0, 0)
            self.animation.stop()
            self.forgame.stop()
            self.flag3 = False
            self.leav.move(555, 360)
        else:
            self.contin.move(1280, 720)
            self.menu.setIconSize(QSize(50, 50))
            self.animation.start()
            self.forgame.start()
            self.back.move(1280, 720)
            self.flag3 = True
            self.leav.move(1280, 720)

    def anim1(self):  # отвечает за анимацию подёргивания планет и звёзд, ну и корабля
        if self.flag:
            self.planets.move(0, 10)
            if self.flag2:
                self.spaceship1.move(10, 0)
                self.spaceship_color.move(10, 0)
            self.flag = False
        else:
            self.planets.move(0, 0)
            if self.flag2:
                self.spaceship1.move(0, 0)
                self.spaceship_color.move(0, 0)
            self.flag = True

    def button(self):  # кнопка старта
        if self.flag2 and self.flag6:
            self.color_ship.move(1280, 720)
            self.flag7 = False
            self.file = open('Progress.txt', mode='w')
            self.information[3] = str(datetime.strptime(self.information[3], "%Y-%m-%d %H:%M:%S.%f") + timedelta(minutes=5))  # отнимается от воды 1 состояние
            self.file.write('\n'.join(self.information))
            self.upgarde.move(1280, 720)
            self.iven.move(1280, 720)
            self.exit.move(1280, 720)
            self.pb.setIconSize(QSize(120, 40))
            self.flag2 = False
            self.ch1 = 10
            self.ch2 = 1
            self.time2.start()

    def anim2(self):  # анимация полёта ракеты
        if self.spaceship1.x() <= 720:
            if self.ch2 == 1:
                self.spaceship1.setPixmap(QPixmap('Space_ship/spaceship_sost2.png'))
                self.spaceship1.move(self.ch1, 0)
                self.spaceship_color.move(self.ch1, 0)

            elif self.ch2 == 2:
                self.spaceship1.setPixmap(QPixmap('Space_ship/spaceship_sost3.png'))
                self.spaceship1.move(self.ch1, 0)
                self.spaceship_color.move(self.ch1, 0)

            elif self.ch2 == 3:
                self.spaceship1.setPixmap(QPixmap('Space_ship/spaceship_sost4.png'))
                self.spaceship1.move(self.ch1, 0)
                self.spaceship_color.move(self.ch1, 0)
                self.ch2 = 0
            self.ch1 += 20
            self.ch2 += 1
        else:
            self.ch1 = 10
            self.ch2 = 1
            self.time2.stop()
            self.time3.start()
            self.dowload()
            self.green()

    def restart(self):  # "если вы решили сдаться или вы прошли этот уровень"
        if self.end:
            self.addArtifact(self.winger, '+')
            self.you_winner.move(1280, 720)
            self.winger.move(1280, 720)
            self.information[2] = str(int(self.information[2]) + 1)
            self.information[0] = str(int(self.information[0]) + self.mahn)
            self.moneyt.setText(f'<font color="white">{self.information[1]}')
            self.cristalt.setText(f'<font color="white">{self.information[0]}')
            self.file = open('Progress.txt', mode='w')
            self.file.write('\n'.join(self.information))
        self.color_ship.move(5, 165)
        self.select2.move(1280, 720)
        self.upgarde.move(5, 5)
        self.iven.move(5, 60)
        self.money.move(715, 10)
        self.cristal.move(615, 10)
        self.moneyt.move((715 - ((len(self.information[1]) + 1)) * 10), 8)
        self.cristalt.move((615 - ((len(self.information[0]) + 1)) * 10), 8)
        self.end = False
        self.mahn = 0
        self.click = 0
        self.otch.setText(f'<font color="red">{self.click}/35')
        self.pause()

        self.fm1 = True
        self.fm2 = True
        self.fm3 = True
        self.flag4 = True
        self.game()  # запускается чтобы убрать все лишние метеориты с поля, задав перед этим нужные значения

        self.flag2 = True
        self.flag = True

        self.lila = int(self.information[2]) - int(self.forshop[0])  # обновление счётчика ударов о метеорит

        self.dowload()
        self.notkus()

    def notkus(self):  # убирает все лишние детали игры с поля
        for i in range(len(self.colors_for_ship)):
            if self.information[5].split(';')[i] == '2':
                self.spaceship_color.setPixmap(QPixmap(self.colors[i][0]))
        self.timer.start()
        self.animation.stop()
        self.live = 0
        self.lvl.move(1280, 720)
        self.sost.move(1280, 720)
        self.give.move(1280, 720)
        self.exit.move(10, 660)
        self.menu.move(1280, 720)
        self.lbl2.move(0, 0)
        self.pb.move(575, 650)
        self.planets.setPixmap(QPixmap('planet(test).png'))
        self.spaceship1.setPixmap(QPixmap('Space_ship/spaceship_sost1.png'))
        self.spaceship1.move(0, 0)
        self.spaceship_color.move(0, 0)
        self.plan1.move(10000, 400)
        self.time3.start()
        self.otch.move(1280, 720)
        for i in range(len(self.gren)):
            self.gren[i].move(1280, 720)

    def kus(self):  # добавляет детали игры на поле
        self.timer.stop()
        self.watet.move(1280, 720)
        self.wate.move(1280, 720)
        self.lvl.setText(f'Ур. <font color="red">{self.information[2]}')
        self.cristalt.move(1280, 720)
        self.cristal.move(1280, 720)
        self.money.move(1280, 720)
        self.moneyt.move(1280, 720)
        self.menu.move(10, 10)
        self.lbl2.move(1280, 720)
        self.pb.setIconSize(QSize(130, 50))
        self.pb.move(1280, 720)
        self.planets.setPixmap(QPixmap('stars(test).png'))
        self.spaceship1.setPixmap(QPixmap('Space_ship/spaceship_sost5.png'))
        self.spaceship1.move(0, 50)
        self.spaceship_color.move(0, 50)
        self.spaceship1piu.move(0, 50)
        self.plan1 = choice(self.planet)
        self.plan1.move(0, 570)
        self.gren = choice(self.greening)
        for i in range(len(self.gren)):
            self.gren[i].move(1280, 720)

    def green(self):  # запуск игры
        self.kus()
        self.meteor1.move(200 + choice(range(-100, 200)), -130 - choice(range(50, 200)))
        self.meteor2.move(550 + choice(range(-100, 200)), -130 - choice(range(50, 200)))
        self.meteor3.move(900 + choice(range(-100, 200)), -130 - choice(range(50, 200)))
        self.fm11 = 0
        self.fm22 = 0
        self.fm33 = 0
        self.kam = 5
        self.fm1 = True
        self.fm2 = True
        self.fm3 = True
        self.flag4 = False
        self.animation.start()
        self.forgame.start()

    def anim_live(self):  # анимация корабля на планете
        if self.live == 2:
            self.spaceship1.setPixmap(QPixmap('Space_ship/spaceship_sost5-2.png'))
        elif self.live == 4:
            self.spaceship1.setPixmap(QPixmap('Space_ship/spaceship_sost5-3.png'))
        elif self.live == 6:
            self.spaceship1.setPixmap(QPixmap('Space_ship/spaceship_sost5-4.png'))
        elif self.live == 8:
            self.spaceship1.setPixmap(QPixmap('Space_ship/spaceship_sost5.png'))
            self.live = -1
        self.live += 1

    def game(self):  # ту происходит сама игра
        for i in range(len(self.colors_for_ship)):
            if self.information[5].split(';')[i] == '2':  # создание наклейки корабля
                self.spaceship_color.setPixmap(QPixmap(self.colors[i][1]))
        # создание дополнительной информации о прохождении уровня и постоянное обновление
        self.forgame.setInterval(50)
        self.spaceship1piu.move(1280, 720)
        self.sost.move(640 - (len(str(self.mahn)) * 25 // 2), 10)
        self.sost.resize(len(str(self.mahn)) * 40, 60)
        self.sost.setText(f'<font color="white">{self.mahn}')
        self.otch.move(1150, 10)
        self.lvl.move(1160, 60)
        # перемещаются метеориты
        self.meteor1.move(self.meteor1.x(), self.meteor1.y() + self.kam)
        self.meteor2.move(self.meteor2.x(), self.meteor2.y() + self.kam)
        self.meteor3.move(self.meteor3.x(), self.meteor3.y() + self.kam)
        # проверка уничтоженности метеоритов
        if self.fm1:
            self.meteor1.setIcon(QIcon(choice(self.meteorses)))
            self.meteor1.setIconSize(QSize(130, 130))
            self.meteor1.move(200 + choice(range(-100, 200)), -130 - choice(range(300)))
            self.fm1 = False

        if self.fm2:
            self.meteor2.setIcon(QIcon(choice(self.meteorses)))
            self.meteor2.setIconSize(QSize(130, 130))
            self.meteor2.move(550 + choice(range(-100, 200)), -130 - choice(range(300)))
            self.fm2 = False

        if self.fm3:
            self.meteor3.setIcon(QIcon(choice(self.meteorses)))
            self.meteor3.setIconSize(QSize(130, 130))
            self.meteor3.move(900 + choice(range(-100, 200)), -130 - choice(range(300)))
            self.fm3 = False
        # создание новых метеоритов при уничтожении
        if (self.meteor1.y() >= 550 or self.fm11 >= self.lila) and not self.end:
            self.meteor1.setIcon(QIcon('meteor/boom.png'))
            self.forgame.setInterval(100)
            if self.fm11 >= self.lila:
                self.click += 1
                self.mahn += (20 + self.accurat)
            if self.mahn >= 10:
                self.mahn -= 10
            self.fm1 = True
            self.fm11 = 0
            self.otch.setText(f'<font color="red">{self.click}/35')
        if (self.meteor2.y() >= 550 or self.fm22 >= self.lila) and not self.end:
            self.meteor2.setIcon(QIcon('meteor/boom.png'))
            self.forgame.setInterval(100)
            if self.fm22 >= self.lila:
                self.click += 1
                self.mahn += (20 + self.accurat)
            if self.mahn >= 10:
                self.mahn -= 10
            self.fm2 = True
            self.fm22 = 0
            self.otch.setText(f'<font color="red">{self.click}/35')
        if (self.meteor3.y() >= 550 or self.fm33 >= self.lila) and not self.end:
            self.meteor3.setIcon(QIcon('meteor/boom.png'))
            self.forgame.setInterval(100)
            if self.fm33 >= self.lila:
                self.click += 1
                self.mahn += (20 + self.accurat)
            if self.mahn >= 10:
                self.mahn -= 10
            self.fm33 = 0
            self.fm3 = True
            self.otch.setText(f'<font color="red">{self.click}/35')
        # отвечает за правильную остановку игры
        if self.flag4:
            self.forgame.stop()
        else:
            self.greeng()

    def greeng(self):  # отвечает за изменение стадий озеленения планеты
        if self.click == 1:
            self.gren[0].move(0, 570)
        elif self.click == 2:
            self.gren[1].move(0, 570)
        elif self.click == 3:
            self.gren[2].move(0, 570)
        elif self.click == 5:
            self.gren[3].move(0, 570)
        elif self.click == 8:
            self.gren[4].move(0, 570)
        elif self.click == 13:
            self.gren[5].move(0, 570)
        elif self.click == 15:
            self.gren[6].move(0, 570)
        elif self.click == 18:
            self.gren[7].move(0, 570)
        elif self.click == 22:
            self.gren[8].move(0, 570)
        elif self.click == 33:
            self.gren[9].move(0, 570)
            self.gren[10].move(0, 420)
        elif self.click == 35:  # конец уровня
            self.end = True
            self.flag3 = False
            self.winger = choice(self.img_artifacts)
            self.you_winner.move(150, 50)
            self.menu.move(1280, 720)
            self.winger.move(605, 100)
            self.give.move(535, 640)
            self.fm1 = True
            self.fm2 = True
            self.fm3 = True
            self.flag4 = True

    def addArtifact(self, obj, m_p):  # добавление полученного артефакта в инвентарь
        dud = self.information[4].split(';')
        ch = self.img_artifacts.index(obj)
        if m_p == '+':
            dud[ch] = str(int(dud[ch]) + 1)
        elif m_p == '-':
            dud[ch] = str(int(dud[ch]) - 1)
        dud = ';'.join(dud)
        self.information[4] = dud
        self.file = open('Progress.txt', mode='w')
        self.file.write('\n'.join(self.information))

    def metor(self):  # отвечает за колличество кликов на метеорит и воспроизведение выстрела после нажатия
        if self.sender() == self.meteor1:
            self.meteor1.setIconSize(QSize(130 - self.fm11, 130 - self.fm11 * 2))
            self.fm11 += 1
        if self.sender() == self.meteor2:
            self.meteor2.setIconSize(QSize(130 - self.fm22, 130 - self.fm22 * 2))
            self.fm22 += 1
        if self.sender() == self.meteor3:
            self.meteor3.setIconSize(QSize(130 - self.fm33, 130 - self.fm33 * 2))
            self.fm33 += 1
        self.spaceship1piu.setPixmap(QPixmap(choice(['Space_ship/spaceship_sost5_piu1.png', 'Space_ship/spaceship_sost5_piu2.png'])))
        self.spaceship1piu.move(0, 50)

    def closeEvent(self, a0: QCloseEvent) -> None:  # если игра внезапно закрылась, то идёт сохранение всех данных.
        self.file = open('Progress.txt', mode='w')
        self.file.write('\n'.join(self.information))
        self.file2 = open('Shop.txt', mode='w')
        self.file2.write('\n'.join(self.forshop))


if __name__ == '__main__':  # запуск всего!
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('19363.ttf')
    ex = GreenArtifact()
    ex.show()
    sys.exit(app.exec())
