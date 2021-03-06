# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookDetailWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BookDetailWidget(object):
    def setupUi(self, BookDetailWidget):
        BookDetailWidget.setObjectName("BookDetailWidget")
        BookDetailWidget.resize(705, 986)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BookDetailWidget.sizePolicy().hasHeightForWidth())
        BookDetailWidget.setSizePolicy(sizePolicy)
        BookDetailWidget.setMinimumSize(QtCore.QSize(230, 480))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(BookDetailWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.book_cover = QtWidgets.QLabel(BookDetailWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_cover.sizePolicy().hasHeightForWidth())
        self.book_cover.setSizePolicy(sizePolicy)
        self.book_cover.setMinimumSize(QtCore.QSize(360, 480))
        self.book_cover.setMaximumSize(QtCore.QSize(360, 480))
        self.book_cover.setText("")
        self.book_cover.setObjectName("book_cover")
        self.horizontalLayout_2.addWidget(self.book_cover)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.book_info = QtWidgets.QTableWidget(BookDetailWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_info.sizePolicy().hasHeightForWidth())
        self.book_info.setSizePolicy(sizePolicy)
        self.book_info.setObjectName("book_info")
        self.book_info.setColumnCount(1)
        self.book_info.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.book_info.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.book_info.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.book_info.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.book_info.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.book_info.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.book_info.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.book_info.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.book_info.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.book_info.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.book_info.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.book_info.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.book_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.book_info.setItem(0, 0, item)
        self.horizontalLayout_2.addWidget(self.book_info)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.brief_intro = QtWidgets.QLabel(BookDetailWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.brief_intro.setFont(font)
        self.brief_intro.setFocusPolicy(QtCore.Qt.NoFocus)
        self.brief_intro.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.brief_intro.setAlignment(QtCore.Qt.AlignCenter)
        self.brief_intro.setObjectName("brief_intro")
        self.verticalLayout.addWidget(self.brief_intro)
        self.intro_content = QtWidgets.QTextEdit(BookDetailWidget)
        self.intro_content.setObjectName("intro_content")
        self.verticalLayout.addWidget(self.intro_content)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.book_borrow = QtWidgets.QPushButton(BookDetailWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.book_borrow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/????????????.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.book_borrow.setIcon(icon)
        self.book_borrow.setObjectName("book_borrow")
        self.horizontalLayout.addWidget(self.book_borrow)
        self.book_return = QtWidgets.QPushButton(BookDetailWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.book_return.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/????????????.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.book_return.setIcon(icon1)
        self.book_return.setObjectName("book_return")
        self.horizontalLayout.addWidget(self.book_return)
        self.PDF_preview = QtWidgets.QPushButton(BookDetailWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PDF_preview.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/????????????.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PDF_preview.setIcon(icon2)
        self.PDF_preview.setObjectName("PDF_preview")
        self.horizontalLayout.addWidget(self.PDF_preview)
        self.PDF_upload = QtWidgets.QPushButton(BookDetailWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PDF_upload.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/PDF??????.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PDF_upload.setIcon(icon3)
        self.PDF_upload.setObjectName("PDF_upload")
        self.horizontalLayout.addWidget(self.PDF_upload)
        self.PDF_delete = QtWidgets.QPushButton(BookDetailWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PDF_delete.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/PDF??????.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PDF_delete.setIcon(icon4)
        self.PDF_delete.setObjectName("PDF_delete")
        self.horizontalLayout.addWidget(self.PDF_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.label = QtWidgets.QLabel(BookDetailWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.BRLog_table = QtWidgets.QTableWidget(BookDetailWidget)
        self.BRLog_table.setObjectName("BRLog_table")
        self.BRLog_table.setColumnCount(9)
        self.BRLog_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("??????")
        font.setPointSize(12)
        item.setFont(font)
        self.BRLog_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("??????")
        font.setPointSize(12)
        item.setFont(font)
        self.BRLog_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("??????")
        font.setPointSize(12)
        item.setFont(font)
        self.BRLog_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("??????")
        font.setPointSize(12)
        item.setFont(font)
        self.BRLog_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("??????")
        font.setPointSize(12)
        item.setFont(font)
        self.BRLog_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("??????")
        font.setPointSize(12)
        item.setFont(font)
        self.BRLog_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("??????")
        font.setPointSize(12)
        item.setFont(font)
        self.BRLog_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("??????")
        font.setPointSize(12)
        item.setFont(font)
        self.BRLog_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("??????")
        font.setPointSize(12)
        item.setFont(font)
        self.BRLog_table.setHorizontalHeaderItem(8, item)
        self.verticalLayout_2.addWidget(self.BRLog_table)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(BookDetailWidget)
        QtCore.QMetaObject.connectSlotsByName(BookDetailWidget)

    def retranslateUi(self, BookDetailWidget):
        _translate = QtCore.QCoreApplication.translate
        BookDetailWidget.setWindowTitle(_translate("BookDetailWidget", "Form"))
        item = self.book_info.verticalHeaderItem(0)
        item.setText(_translate("BookDetailWidget", "ID"))
        item = self.book_info.verticalHeaderItem(1)
        item.setText(_translate("BookDetailWidget", "??????"))
        item = self.book_info.verticalHeaderItem(2)
        item.setText(_translate("BookDetailWidget", "ISBN"))
        item = self.book_info.verticalHeaderItem(3)
        item.setText(_translate("BookDetailWidget", "??????"))
        item = self.book_info.verticalHeaderItem(4)
        item.setText(_translate("BookDetailWidget", "??????"))
        item = self.book_info.verticalHeaderItem(5)
        item.setText(_translate("BookDetailWidget", "????????????"))
        item = self.book_info.verticalHeaderItem(6)
        item.setText(_translate("BookDetailWidget", "????????????"))
        item = self.book_info.verticalHeaderItem(7)
        item.setText(_translate("BookDetailWidget", "??????"))
        item = self.book_info.verticalHeaderItem(8)
        item.setText(_translate("BookDetailWidget", "??????"))
        item = self.book_info.verticalHeaderItem(9)
        item.setText(_translate("BookDetailWidget", "????????????"))
        item = self.book_info.verticalHeaderItem(10)
        item.setText(_translate("BookDetailWidget", "??????"))
        item = self.book_info.horizontalHeaderItem(0)
        item.setText(_translate("BookDetailWidget", "??????"))
        __sortingEnabled = self.book_info.isSortingEnabled()
        self.book_info.setSortingEnabled(False)
        self.book_info.setSortingEnabled(__sortingEnabled)
        self.brief_intro.setText(_translate("BookDetailWidget", "??????"))
        self.intro_content.setHtml(_translate("BookDetailWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">??????</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>"))
        self.book_borrow.setText(_translate("BookDetailWidget", "??????"))
        self.book_return.setText(_translate("BookDetailWidget", "??????"))
        self.PDF_preview.setText(_translate("BookDetailWidget", "PDF??????"))
        self.PDF_upload.setText(_translate("BookDetailWidget", "PDF??????"))
        self.PDF_delete.setText(_translate("BookDetailWidget", "PDF??????"))
        self.label.setText(_translate("BookDetailWidget", "????????????"))
        item = self.BRLog_table.horizontalHeaderItem(0)
        item.setText(_translate("BookDetailWidget", "??????ID"))
        item = self.BRLog_table.horizontalHeaderItem(1)
        item.setText(_translate("BookDetailWidget", "????????????"))
        item = self.BRLog_table.horizontalHeaderItem(2)
        item.setText(_translate("BookDetailWidget", "????????????"))
        item = self.BRLog_table.horizontalHeaderItem(3)
        item.setText(_translate("BookDetailWidget", "????????????"))
        item = self.BRLog_table.horizontalHeaderItem(4)
        item.setText(_translate("BookDetailWidget", "??????????????????"))
        item = self.BRLog_table.horizontalHeaderItem(5)
        item.setText(_translate("BookDetailWidget", "???????????????"))
        item = self.BRLog_table.horizontalHeaderItem(6)
        item.setText(_translate("BookDetailWidget", "????????????"))
        item = self.BRLog_table.horizontalHeaderItem(7)
        item.setText(_translate("BookDetailWidget", "????????????"))
        item = self.BRLog_table.horizontalHeaderItem(8)
        item.setText(_translate("BookDetailWidget", "??????????????????"))
import res_rc
