from PyQt5.QtWidgets import QDialog,QMessageBox,QTableWidgetItem
from PyQt5.QtCore import pyqtSignal,pyqtSlot,QDate,Qt
from PyQt5.QtGui import QIcon,QFont
from ui_TouristBRDialog import Ui_TouristBRDialog

class TouristBR_Dialog(QDialog):
    tourist_info_borrow = pyqtSignal(list) # 非要作为一个类属性（静态属性）
    tourist_info_return = pyqtSignal(list)
    BRLog_table_update = pyqtSignal()
    def __init__(self,parent = None):
        """
        :param parent:父类，默认为None
        """
        super().__init__(parent)
        self.__ui = Ui_TouristBRDialog()
        self.__ui.setupUi(self)
        self.setWindowIcon(QIcon(':/icons/icons/borrow_return.ico'))

    def set_borrow_state_btn(self):
        """
        :param: 无
        :return: 无
        """
        self.__ui.borrow_choose.setEnabled(True)
        self.__ui.borrow_choose.setChecked(True)
        self.__ui.return_choose.setChecked(False)
        self.__ui.return_choose.setEnabled(False)

    def set_return_state_btn(self):
        """
        :param: 无
        :return: 无
        """
        self.__ui.borrow_choose.setChecked(False)
        self.__ui.borrow_choose.setEnabled(False)
        self.__ui.return_choose.setEnabled(True)
        self.__ui.return_choose.setChecked(True)

    def auto_setDate_whenBorrowReturn(self):
        """
        :param: 无
        :return: 无
        """
        cur_dateTime = QDate.currentDate()
        item = QTableWidgetItem(cur_dateTime.toString('yyyy-MM-dd'),1)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setFlags(Qt.ItemFlags(int('111101',2))) # 无法编辑
        self.__ui.tourist_info.setItem(1,0,item)

    def on_tourist_info_cellChanged(self,row,column):
        """
        :param row: int,当前行号
        :param column: int,当前列号
        :return: 无
        """
        item = self.__ui.tourist_info.item(row,column)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item.setFont(QFont('宋体',12))
        self.__ui.tourist_info.setItem(row,column,item)

    @pyqtSlot()
    def on_OK_clicked(self):
        """
        :param: 无
        :return: 无
        """
        borrow_judge = '1' if self.__ui.borrow_choose.isChecked() == True else '0'
        cur_col = 0
        cur_tourist_info = []
        cur_tourist_info.append(borrow_judge)  # 1是借书0是还书
        for i in range(4):  # ID不用传进来
            cur_item = self.__ui.tourist_info.item(i,cur_col)
            if cur_item == None:
                QMessageBox.critical(self, '信息错误', '表格不能有空')
                return  # 一定不能有空的
            text = cur_item.text()
            cur_tourist_info.append(text)
        # print(cur_tourist_info)
        if borrow_judge == '1':
            self.tourist_info_borrow.emit(cur_tourist_info)
        elif borrow_judge == '0':
            self.tourist_info_return.emit(cur_tourist_info)
        self.BRLog_table_update.emit()
        self.close()

    @pyqtSlot()
    def on_Cancel_clicked(self):
        """
        :param: 无
        :return: 无
        """
        self.close()
