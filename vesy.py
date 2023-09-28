# This Python file uses the following encoding: utf-8
import datetime
import functools
import sys
import db
from PySide6.QtWidgets import QApplication, QWidget, QSizePolicy, QToolButton, QScrollArea, QScroller

from PySide6.QtMultimedia import QMediaPlayer, QMediaMetaData
from PySide6.QtCore import QUrl, QDate, QSize, QCoreApplication, Qt
from PySide6.QtGui import QRegularExpressionValidator, QDoubleValidator, QFont
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Vesy
from PySide6.QtMultimediaWidgets import QVideoWidget


# фото, видео
# тип грузов


import yaml


S = "АВЕКМНОРСТУХ"+"ABEKMHOPCTYX"
S += S.lower()

platetype = [
    f'[{S}]{{1}}\ ?[0-9]{{3}}\ ?[{S}]{{2}}\ ?[0-9]{{2,3}}',
    f'[{S}]{{2}}\ ?[0-9]{{3,4}}\ [0-9]{{2,3}}',
    f'[0-9]{{4}}\ ?[{S}]{{2}}\ ?[0-9]{{2,3}}',
]
platereg = "|".join(platetype)

platetranslate = str.maketrans(
    "ABEKMHOPCTYX" + "ABEKMHOPCTYX".lower(), "АВЕКМНОРСТУХ"*2)


class Vesy(QWidget):
    def on_meta_data_changed(self, *a, **kw):
        meta = self.player.metaData()
        if QMediaMetaData.Key.Resolution in meta.keys():
            size: QSize = meta.value(QMediaMetaData.Key.Resolution)
            scale = self.plaeyrs_zoom[self.current_player_index]
            size.scale(QSize(size.width()*scale, size.height()*scale),
                       Qt.AspectRatioMode.KeepAspectRatio)
            print(size)
            self.current_player_output.resize(size)

    def __init__(self, base: db.JournalModel, parent=None):
        super().__init__(parent)
        self.ui = Ui_Vesy()
        self.ui.setupUi(self)
        self.ui.line_plate.setValidator(QRegularExpressionValidator(platereg))
        dv = QDoubleValidator(
            0,
            999999,
            3
        )
        dv.setNotation(QDoubleValidator.Notation.StandardNotation)
        self.ui.line_weight.setValidator(dv)
        today = datetime.date.today()
        tomorow = datetime.date.today() + datetime.timedelta(days=1)
        self.ui.date_start.setDate(QDate(today.year, today.month, today.day))
        self.ui.date_start.setDate(
            QDate(tomorow.year, tomorow.month, tomorow.day)
        )
        self.players = []
        self.plaeyrs_zoom = []
        self.urls = []
        self.player = QMediaPlayer()

        # self.player.mediaStatusChanged.connect(self.on_media_status)
        self.player.metaDataChanged.connect(self.on_meta_data_changed)

        self.base = base

        cams = yaml.load(
            open("cameras.yml", 'r', encoding='utf-8'), Loader=yaml.Loader)
        self.current_player = None
        for cam in cams:
            self.urls.append(QUrl(cam['uri']))
            sa = QScrollArea(self.ui.viewtab)
            w = QVideoWidget(sa)
            w.setSizePolicy(QSizePolicy.Policy.Ignored,
                            QSizePolicy.Policy.Ignored)
            # w.setAspectRatioMode()

            sa.setWidget(w)
            # sa.setWidgetResizable(True)
            # sa.viewport().grabGesture(Qt.GestureType.TapAndHoldGesture, Qt.GestureFlag.DontStartGestureOnChildren)

            self.players.append(w)
            self.plaeyrs_zoom.append(0.5)
            self.ui.viewtab.addTab(sa, cam['label'])

        if self.players:
            self.swichplayer(0)
            self.ui.viewtab.setCurrentIndex(0)

        self.ui.viewtab.currentChanged.connect(self.swichplayer)
        self.ui.btn_write.clicked.connect(self.insert)

        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        font2 = QFont()
        font2.setPointSize(14)
        row = 0

        for load_type_row in yaml.load(open("load_types.yml", 'r', encoding='utf-8'), Loader=yaml.Loader):
            row += 1
            col = 0
            for load_type in load_type_row:
                col += 1
                btn_load = QToolButton(self.ui.grp_load)
                btn_load.setObjectName(f"btn_load_type_{load_type['id']}")

                sizePolicy4.setHeightForWidth(
                    btn_load.sizePolicy().hasHeightForWidth())
                btn_load.setSizePolicy(sizePolicy4)
                btn_load.setMinimumSize(QSize(60, 40))

                btn_load.setFont(font2)
                btn_load.setCheckable(True)
                btn_load.setAutoExclusive(True)
                btn_load.setAutoRaise(False)

                self.ui.grp_load_buttons.addWidget(btn_load, row, col, 1, 1)
                btn_load.setText(QCoreApplication.translate(
                    "Vesy", load_type['label'], None))

    def insert(self):
        plate = self.ui.line_plate.text().upper().translate(platetranslate)
        weight = self.ui.line_weight.text().replace(' ', '').replace(',', '.') or 0
        self.ui.line_weight.setText('')
        self.ui.line_plate.setText('')
        direction = ''
        if self.ui.radio_empty.isChecked():
            direction += 'Пустой'
            self.ui.radio_empty.setChecked(False)
        if self.ui.radio_income.isChecked():
            direction += 'Поступление'
            self.ui.radio_income.setChecked(False)
        if self.ui.radio_outcome.isChecked():
            direction += 'Отгрузка'
            self.ui.radio_outcome.setChecked(False)
        if self.ui.radio_nocross.isChecked():
            direction += 'Взвешивание'
            self.ui.radio_nocross.setChecked(False)

        load = None
        for (i) in self.ui.grp_load.children():
            if isinstance(i, QToolButton) and i.isChecked():
                load = i.text()
        print(plate, weight, direction, load)
        self.base.insert(plate, weight, direction, load, self.get_shot())

    def get_shot(self):
        pass

    def swichplayer(self, index):
        self.current_player_output = output = self.players[index]
        self.current_player_index = index
        self.player.stop()
        self.player.setVideoOutput(output)
        self.player.setSource(self.urls[index])
        self.player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    base = db.JournalModel(app)
    widget = Vesy(base)
    widget.ui.tableView.setModel(base)

    widget.show()
    sys.exit(app.exec())
