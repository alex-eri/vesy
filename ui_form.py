# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateTimeEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QTabWidget,
    QTableView, QToolButton, QVBoxLayout, QWidget)

class Ui_Vesy(object):
    def setupUi(self, Vesy):
        if not Vesy.objectName():
            Vesy.setObjectName(u"Vesy")
        Vesy.resize(785, 641)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Vesy.sizePolicy().hasHeightForWidth())
        Vesy.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Vesy)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 9, -1)
        self.splitter = QSplitter(Vesy)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFrameShape(QFrame.NoFrame)
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.leftlayout = QVBoxLayout(self.layoutWidget1)
        self.leftlayout.setObjectName(u"leftlayout")
        self.leftlayout.setContentsMargins(0, 0, 0, 0)
        self.dateselectlayout = QHBoxLayout()
        self.dateselectlayout.setObjectName(u"dateselectlayout")
        self.date_start = QDateTimeEdit(self.layoutWidget1)
        self.date_start.setObjectName(u"date_start")
        self.date_start.setMinimumSize(QSize(120, 0))
        self.date_start.setFocusPolicy(Qt.ClickFocus)
        self.date_start.setCalendarPopup(True)

        self.dateselectlayout.addWidget(self.date_start)

        self.date_end = QDateTimeEdit(self.layoutWidget1)
        self.date_end.setObjectName(u"date_end")
        self.date_end.setMinimumSize(QSize(120, 0))
        self.date_end.setFocusPolicy(Qt.ClickFocus)
        self.date_end.setCalendarPopup(True)

        self.dateselectlayout.addWidget(self.date_end)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dateselectlayout.addItem(self.horizontalSpacer)

        self.btn_load_nums = QToolButton(self.layoutWidget1)
        self.btn_load_nums.setObjectName(u"btn_load_nums")

        self.dateselectlayout.addWidget(self.btn_load_nums)

        self.btn_upload = QToolButton(self.layoutWidget1)
        self.btn_upload.setObjectName(u"btn_upload")
        self.btn_upload.setFocusPolicy(Qt.ClickFocus)

        self.dateselectlayout.addWidget(self.btn_upload)


        self.leftlayout.addLayout(self.dateselectlayout)

        self.tableView = QTableView(self.layoutWidget1)
        self.tableView.setObjectName(u"tableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy1)
        self.tableView.setFocusPolicy(Qt.ClickFocus)
        self.tableView.setFrameShape(QFrame.Box)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setAlternatingRowColors(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setDefaultSectionSize(120)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)

        self.leftlayout.addWidget(self.tableView)

        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.rightlayout = QVBoxLayout(self.layoutWidget2)
        self.rightlayout.setObjectName(u"rightlayout")
        self.rightlayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.rightlayout.setContentsMargins(0, 0, 0, 0)
        self.viewtab = QTabWidget(self.layoutWidget2)
        self.viewtab.setObjectName(u"viewtab")
        self.viewtab.setMinimumSize(QSize(320, 240))

        self.rightlayout.addWidget(self.viewtab)

        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")

        self.rightlayout.addWidget(self.label_2)

        self.line_plate = QLineEdit(self.layoutWidget2)
        self.line_plate.setObjectName(u"line_plate")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_plate.sizePolicy().hasHeightForWidth())
        self.line_plate.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(24)
        self.line_plate.setFont(font)
        self.line_plate.setAlignment(Qt.AlignCenter)

        self.rightlayout.addWidget(self.line_plate)

        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.rightlayout.addWidget(self.label)

        self.line_weight = QLineEdit(self.layoutWidget2)
        self.line_weight.setObjectName(u"line_weight")
        sizePolicy2.setHeightForWidth(self.line_weight.sizePolicy().hasHeightForWidth())
        self.line_weight.setSizePolicy(sizePolicy2)
        self.line_weight.setFont(font)
        self.line_weight.setStyleSheet(u"padding-right:1em")
        self.line_weight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.rightlayout.addWidget(self.line_weight)

        self.grp_direction = QGroupBox(self.layoutWidget2)
        self.grp_direction.setObjectName(u"grp_direction")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.grp_direction.sizePolicy().hasHeightForWidth())
        self.grp_direction.setSizePolicy(sizePolicy3)
        self.grp_direction.setFlat(False)
        self.horizontalLayout = QHBoxLayout(self.grp_direction)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radio_empty = QToolButton(self.grp_direction)
        self.radio_empty.setObjectName(u"radio_empty")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.radio_empty.sizePolicy().hasHeightForWidth())
        self.radio_empty.setSizePolicy(sizePolicy4)
        self.radio_empty.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(12)
        self.radio_empty.setFont(font1)
        self.radio_empty.setCheckable(True)
        self.radio_empty.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.radio_empty)

        self.radio_income = QToolButton(self.grp_direction)
        self.radio_income.setObjectName(u"radio_income")
        sizePolicy4.setHeightForWidth(self.radio_income.sizePolicy().hasHeightForWidth())
        self.radio_income.setSizePolicy(sizePolicy4)
        self.radio_income.setMinimumSize(QSize(0, 40))
        self.radio_income.setFont(font1)
        self.radio_income.setCheckable(True)
        self.radio_income.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.radio_income)

        self.radio_outcome = QToolButton(self.grp_direction)
        self.radio_outcome.setObjectName(u"radio_outcome")
        sizePolicy4.setHeightForWidth(self.radio_outcome.sizePolicy().hasHeightForWidth())
        self.radio_outcome.setSizePolicy(sizePolicy4)
        self.radio_outcome.setMinimumSize(QSize(0, 40))
        self.radio_outcome.setFont(font1)
        self.radio_outcome.setCheckable(True)
        self.radio_outcome.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.radio_outcome)

        self.radio_nocross = QToolButton(self.grp_direction)
        self.radio_nocross.setObjectName(u"radio_nocross")
        sizePolicy4.setHeightForWidth(self.radio_nocross.sizePolicy().hasHeightForWidth())
        self.radio_nocross.setSizePolicy(sizePolicy4)
        self.radio_nocross.setMinimumSize(QSize(0, 40))
        self.radio_nocross.setFont(font1)
        self.radio_nocross.setCheckable(True)
        self.radio_nocross.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.radio_nocross)


        self.rightlayout.addWidget(self.grp_direction)

        self.grp_load = QGroupBox(self.layoutWidget2)
        self.grp_load.setObjectName(u"grp_load")
        sizePolicy3.setHeightForWidth(self.grp_load.sizePolicy().hasHeightForWidth())
        self.grp_load.setSizePolicy(sizePolicy3)
        self.grp_load.setMinimumSize(QSize(0, 0))
        self.grp_load.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.grp_load)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.grp_load_buttons = QGridLayout()
        self.grp_load_buttons.setObjectName(u"grp_load_buttons")

        self.verticalLayout.addLayout(self.grp_load_buttons)

        self.line_another_load_type = QLineEdit(self.grp_load)
        self.line_another_load_type.setObjectName(u"line_another_load_type")

        self.verticalLayout.addWidget(self.line_another_load_type)


        self.rightlayout.addWidget(self.grp_load)

        self.btn_write = QPushButton(self.layoutWidget2)
        self.btn_write.setObjectName(u"btn_write")
        self.btn_write.setFont(font)

        self.rightlayout.addWidget(self.btn_write)

        self.grp_semafor = QGroupBox(self.layoutWidget2)
        self.grp_semafor.setObjectName(u"grp_semafor")
        sizePolicy3.setHeightForWidth(self.grp_semafor.sizePolicy().hasHeightForWidth())
        self.grp_semafor.setSizePolicy(sizePolicy3)
        self.grp_semafor.setCursor(QCursor(Qt.ArrowCursor))
        self.grp_semafor.setFlat(False)
        self.grp_semafor.setCheckable(False)
        self.horizontalLayout_2 = QHBoxLayout(self.grp_semafor)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_from_outside = QToolButton(self.grp_semafor)
        self.btn_from_outside.setObjectName(u"btn_from_outside")
        sizePolicy4.setHeightForWidth(self.btn_from_outside.sizePolicy().hasHeightForWidth())
        self.btn_from_outside.setSizePolicy(sizePolicy4)
        self.btn_from_outside.setMinimumSize(QSize(0, 30))
        self.btn_from_outside.setFont(font1)
        self.btn_from_outside.setAutoFillBackground(True)
        self.btn_from_outside.setStyleSheet(u"::checked{\n"
"background:rgb(0, 170, 0)\n"
"}")
        self.btn_from_outside.setCheckable(True)
        self.btn_from_outside.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btn_from_outside)

        self.btn_to_outside = QToolButton(self.grp_semafor)
        self.btn_to_outside.setObjectName(u"btn_to_outside")
        sizePolicy4.setHeightForWidth(self.btn_to_outside.sizePolicy().hasHeightForWidth())
        self.btn_to_outside.setSizePolicy(sizePolicy4)
        self.btn_to_outside.setMinimumSize(QSize(0, 30))
        self.btn_to_outside.setFont(font1)
        self.btn_to_outside.setStyleSheet(u"::checked{\n"
"background:rgb(0, 170, 0)\n"
"}")
        self.btn_to_outside.setCheckable(True)
        self.btn_to_outside.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btn_to_outside)

        self.btn_to_inside = QToolButton(self.grp_semafor)
        self.btn_to_inside.setObjectName(u"btn_to_inside")
        sizePolicy4.setHeightForWidth(self.btn_to_inside.sizePolicy().hasHeightForWidth())
        self.btn_to_inside.setSizePolicy(sizePolicy4)
        self.btn_to_inside.setMinimumSize(QSize(0, 30))
        self.btn_to_inside.setFont(font1)
        self.btn_to_inside.setStyleSheet(u"::checked{\n"
"background:rgb(0, 170, 0)\n"
"}")
        self.btn_to_inside.setCheckable(True)
        self.btn_to_inside.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btn_to_inside)

        self.btn_from_inside = QToolButton(self.grp_semafor)
        self.btn_from_inside.setObjectName(u"btn_from_inside")
        sizePolicy4.setHeightForWidth(self.btn_from_inside.sizePolicy().hasHeightForWidth())
        self.btn_from_inside.setSizePolicy(sizePolicy4)
        self.btn_from_inside.setMinimumSize(QSize(0, 30))
        self.btn_from_inside.setFont(font1)
        self.btn_from_inside.setStyleSheet(u"::checked{\n"
"background:rgb(0, 170, 0)\n"
"}")
        self.btn_from_inside.setCheckable(True)
        self.btn_from_inside.setChecked(False)
        self.btn_from_inside.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btn_from_inside)


        self.rightlayout.addWidget(self.grp_semafor)

        self.splitter.addWidget(self.layoutWidget2)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(Vesy)

        self.btn_write.setDefault(True)


        QMetaObject.connectSlotsByName(Vesy)
    # setupUi

    def retranslateUi(self, Vesy):
        Vesy.setWindowTitle(QCoreApplication.translate("Vesy", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0432\u0435\u0441\u043e\u0432\u043e\u0439", None))
        self.date_start.setDisplayFormat(QCoreApplication.translate("Vesy", u"yyyy-MM-dd HH:mm", None))
        self.date_end.setDisplayFormat(QCoreApplication.translate("Vesy", u"yyyy-MM-dd HH:mm", None))
        self.btn_load_nums.setText(QCoreApplication.translate("Vesy", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043d\u043e\u043c\u0435\u0440\u0430", None))
        self.btn_upload.setText(QCoreApplication.translate("Vesy", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Vesy", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.line_plate.setText("")
        self.line_plate.setPlaceholderText(QCoreApplication.translate("Vesy", u"A 000 AA 37", None))
        self.label.setText(QCoreApplication.translate("Vesy", u"\u0412\u0435\u0441", None))
        self.line_weight.setPlaceholderText(QCoreApplication.translate("Vesy", u"0000", None))
        self.grp_direction.setTitle(QCoreApplication.translate("Vesy", u"\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.radio_empty.setText(QCoreApplication.translate("Vesy", u"\u041f\u0443\u0441\u0442\u043e\u0439", None))
#if QT_CONFIG(shortcut)
        self.radio_empty.setShortcut(QCoreApplication.translate("Vesy", u"U", None))
#endif // QT_CONFIG(shortcut)
        self.radio_income.setText(QCoreApplication.translate("Vesy", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
#if QT_CONFIG(shortcut)
        self.radio_income.setShortcut(QCoreApplication.translate("Vesy", u"I", None))
#endif // QT_CONFIG(shortcut)
        self.radio_outcome.setText(QCoreApplication.translate("Vesy", u"\u041e\u0442\u0433\u0440\u0443\u0437\u043a\u0430", None))
#if QT_CONFIG(shortcut)
        self.radio_outcome.setShortcut(QCoreApplication.translate("Vesy", u"O", None))
#endif // QT_CONFIG(shortcut)
        self.radio_nocross.setText(QCoreApplication.translate("Vesy", u"\u0412\u0437\u0432\u0435\u0448\u0438\u0432\u0430\u043d\u0438\u0435", None))
#if QT_CONFIG(shortcut)
        self.radio_nocross.setShortcut(QCoreApplication.translate("Vesy", u"P", None))
#endif // QT_CONFIG(shortcut)
        self.grp_load.setTitle(QCoreApplication.translate("Vesy", u"\u0413\u0440\u0443\u0437", None))
        self.line_another_load_type.setPlaceholderText(QCoreApplication.translate("Vesy", u"\u0414\u0440\u0443\u0433\u043e\u0439 \u0442\u0438\u043f \u0433\u0440\u0443\u0437\u0430", None))
        self.btn_write.setText(QCoreApplication.translate("Vesy", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.btn_write.setShortcut(QCoreApplication.translate("Vesy", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.grp_semafor.setTitle(QCoreApplication.translate("Vesy", u"\u0421\u0432\u0435\u0442\u043e\u0444\u043e\u0440", None))
        self.btn_from_outside.setText(QCoreApplication.translate("Vesy", u"\u0441 \u0443\u043b\u0438\u0446\u044b", None))
#if QT_CONFIG(shortcut)
        self.btn_from_outside.setShortcut(QCoreApplication.translate("Vesy", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.btn_to_outside.setText(QCoreApplication.translate("Vesy", u"\u043d\u0430 \u0443\u043b\u0438\u0446\u0443", None))
#if QT_CONFIG(shortcut)
        self.btn_to_outside.setShortcut(QCoreApplication.translate("Vesy", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.btn_to_inside.setText(QCoreApplication.translate("Vesy", u"\u0432\u043e \u0434\u0432\u043e\u0440", None))
#if QT_CONFIG(shortcut)
        self.btn_to_inside.setShortcut(QCoreApplication.translate("Vesy", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.btn_from_inside.setText(QCoreApplication.translate("Vesy", u"\u0441\u043e \u0434\u0432\u043e\u0440\u0430", None))
#if QT_CONFIG(shortcut)
        self.btn_from_inside.setShortcut(QCoreApplication.translate("Vesy", u"R", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

