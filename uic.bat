echo off

copy .\Library_Management\MainWindow.ui MainWindow.ui
copy .\Library_Management\PDFWidget.ui PDFWidget.ui
copy .\Library_Management\PDFDialog.ui PDFDialog.ui
copy .\Library_Management\BookDetailWidget.ui BookDetailWidget.ui
copy .\Library_Management\TouristBRDialog.ui TouristBRDialog.ui

pyuic5 -o ui_MainWindow.py MainWindow.ui
pyuic5 -o ui_PDFWidget.py PDFWidget.ui
pyuic5 -o ui_PDFDialog.py PDFDialog.ui
pyuic5 -o ui_BookDetailWidget.py BookDetailWidget.ui
pyuic5 -o ui_TouristBRDialog.py TouristBRDialog.ui

pyrcc5 .\Library_Management\res.qrc -o res_rc.py