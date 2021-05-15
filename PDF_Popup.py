import sys
from PyQt5.QtWidgets import QShortcut,QWidget,QApplication
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QKeySequence,QIcon
from ui_PDFWidget import Ui_PDFWidget

class PDF_Popup(QWidget):
    pdf_page_change = pyqtSignal(int)
    def __init__(self,parent = None):
        """
        :param parent: 父类，默认为None
        """
        super().__init__(parent)
        self.__ui = Ui_PDFWidget()
        self.__ui.setupUi(self)
        self.__actions()
        self.__max_page = 0 # self.pdf.pageCount - 1最大页数
        self.__current_page = 0
        self.setWindowTitle('书籍预览')
        self.setWindowIcon(QIcon(':/icons/icons/readingIcon.ico'))

    def set_max_page(self,max_page:int) -> None:
        """
        :param max_page: int,最大的页数
        :return: 无
        """
        self.__max_page = max_page

    def pdf_Label_height(self):
        """
        :param: 无
        :return: 无
        """
        return self.__ui.reading_area.height() # 返回书籍那里的height

    def __actions(self):
        """
        :param: 无
        :return: 无
        """
        # 这几个是用方向键来左右控制
        switch_left = QShortcut(QKeySequence(Qt.Key_Left),self)
        switch_right = QShortcut(QKeySequence(Qt.Key_Right),self)
        switch_left.activated.connect(self.__left)  # self.__left是自己的方法
        switch_right.activated.connect(self.__right)

    def __left(self):
        self.__switch_page(right = False)

    def __right(self):
        """
        :param: 无
        :return: 无
        """
        self.__switch_page(right = True)

    def __switch_page(self,right:bool) -> None:
        """
        :param right: bool,向左:False或向右:True
        :return: 无
        """
        if right and self.__current_page < self.__max_page: # 小于最后一页才加
            self.__current_page += 1
        elif not right and self.__current_page > 0:
            self.__current_page -= 1
        self.pdf_page_change.emit(self.__current_page)

    def set_currentPage(self,input_book_page):
        """
        :param input_book_page: PyQt5.QtGui.QPixmap,当前输入的页面
        :return: 无
        """
        self.__ui.reading_area.setPixmap(input_book_page)
        self.__ui.reading_area.setScaledContents(True)

def main():
    app = QApplication(sys.argv)
    form = PDF_Popup()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()