from PyQt5.QtWidgets import QWidget,QLabel,QFileDialog,QTableWidgetItem,\
    QMessageBox,QAbstractItemView
from PyQt5.QtCore import Qt,pyqtSlot,QDir,pyqtSignal,QDate,QDateTime
from PyQt5.QtGui import QIcon,QPixmap,QImage
from ui_BookDetailWidget import Ui_BookDetailWidget
import fitz # pip install PyMuPDF
from PDF_Popup import PDF_Popup
from Linklist import CellType
from basic_logic import state_log
from enum import Enum
from TouristBR_Dialog import TouristBR_Dialog
import re

class ColNum(Enum):
    colID = 0
    colName = 1
    colISBN = 2
    colAuthor = 3
    colPageCnt = 4
    colPubDate = 5
    colEntDate = 6
    colPrice = 7
    colCatelog = 8
    colState = 9
    colBCnt = 10
    colBal = 11

class ColNum_BRLog(Enum):
    colReader_ID = 0
    colBT = 1
    colBP = 2
    colPeriod = 3
    colDue = 4
    colIsReturn = 5
    colRT = 6
    colRP = 7
    colRealPeriod = 8

class CellType_BRLog(Enum):
    ctReader_ID = 1000
    ctBT = 1001
    ctBP = 1002
    ctPeriod = 1003
    ctDue = 1004
    ctIsReturn = 1005
    ctRT = 1006
    ctRP = 1007
    ctRealPeriod = 1008

def render_PDF_cover(page_raw,size=(1, 1)): # page_raw是原来的那个封面，还没有生成QPixmap和QLabel
    """
    :param page_raw: fltz.Pixmap,pdf的每一页
    :param size: tuple(int,int),用于指定fitz.Matrix的大小
    :return: QPixmap,渲染后的图片
    """
    a,b = size
    zoom_matrix = fitz.Matrix(a,b)
    # 获取封面对应的fitz.Pixmap对象
    page_pixmap = page_raw.getPixmap(matrix=zoom_matrix, alpha=False) # alpha设置背景为白色
    img_format = QImage.Format_RGB888 # 是三个8
    page_img = QImage(page_pixmap.samples, page_pixmap.width, page_pixmap.height,
                      page_pixmap.stride, img_format)
    # 生成QPixmap对象
    pixmap = QPixmap()
    pixmap.convertFromImage(page_img)
    return pixmap

def generate_BRLog_items(each_log) -> list:
    """
    :param each_log:
    :return: list[PyQt5.QtWidgets.QTableWidgetItem],返回一个全是item的列表，用于设置到表格中
    """
    item_list = list()
    cur_reader_ID = each_log.get_readerID()
    item_reader_ID = QTableWidgetItem(cur_reader_ID if cur_reader_ID != ''
                                      else '无', CellType_BRLog.ctReader_ID.value)
    item_reader_ID.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    item_list.append(item_reader_ID)

    cur_borrowTime = each_log.get_borrowTime()
    item_borrowTime = QTableWidgetItem(cur_borrowTime if cur_borrowTime != ''
                                       else '无', CellType_BRLog.ctBT.value)
    item_borrowTime.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    item_list.append(item_borrowTime)

    cur_borrowPlace = each_log.get_borrowPlace()
    item_borrowPlace = QTableWidgetItem(cur_borrowPlace if cur_borrowPlace != ''
                                        else '无', CellType_BRLog.ctBP.value)
    item_borrowPlace.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    item_list.append(item_borrowPlace)

    cur_lending_period = int(''.join(re.findall(r'\d+', each_log.get_lending_period())))  # 90天 把天去掉
    item_lending_period = QTableWidgetItem(str(cur_lending_period) + '天', CellType_BRLog.ctPeriod.value)
    item_lending_period.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    item_list.append(item_lending_period)

    cur_dueDate = QDate.fromString(cur_borrowTime, 'yyyy-MM-dd').addDays(cur_lending_period).toString('yyyy-MM-dd')
    item_dueDate = QTableWidgetItem(cur_dueDate, CellType_BRLog.ctDue.value)
    item_dueDate.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    item_list.append(item_dueDate)

    cur_IsReturn = each_log.get_IsReturn()
    item_IsReturn = QTableWidgetItem('已归还', CellType_BRLog.ctIsReturn.value)
    if cur_IsReturn == False:
        item_IsReturn = QTableWidgetItem('未归还', CellType_BRLog.ctIsReturn.value)
    item_IsReturn.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    item_list.append(item_IsReturn)

    cur_returnTime = each_log.get_returnTime()
    item_returnTime = QTableWidgetItem(cur_returnTime if cur_returnTime != ''
                                       else '（未归还）', CellType_BRLog.ctRT.value)
    item_returnTime.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    item_list.append(item_returnTime)

    cur_returnPlace = each_log.get_returnPlace()
    item_returnPlace = QTableWidgetItem(cur_returnPlace if cur_returnPlace != ''
                                        else '（未归还）', CellType_BRLog.ctRP.value)
    item_returnPlace.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    item_list.append(item_returnPlace)

    cur_real_lendingPeriod = '（未归还）'
    if cur_borrowTime != '无' and cur_returnTime != '（未归还）':
        # 必须先转换为QDate
        cur_borrowTime += ' 00:00:00'
        cur_returnTime += ' 00:00:00'  # 必须要转为QDateTime
        cur_borrowDate = QDateTime.fromString(cur_borrowTime, 'yyyy-MM-dd hh:mm:ss')
        cur_returnDate = QDateTime.fromString(cur_returnTime, 'yyyy-MM-dd hh:mm:ss')
        seconds = cur_borrowDate.secsTo(cur_returnDate) / (24 * 3600)
        cur_real_lendingPeriod = str(int(seconds)) + '天'
    item_real_lendingPeriod = QTableWidgetItem(cur_real_lendingPeriod, CellType_BRLog.ctRealPeriod.value)
    item_real_lendingPeriod.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    item_list.append(item_real_lendingPeriod)
    return item_list

class Book_Detail(QWidget):
    BRLog_in_mainwindow = pyqtSignal()
    def __init__(self,cur_book,parent = None):
        """
        :param cur_book: node,当前的书籍节点
        :param parent: 父节点，默认为None
        """
        super().__init__(parent)
        self.__ui = Ui_BookDetailWidget()
        self.__ui.setupUi(self)
        self.__cur_book = cur_book
        self.__no_cover_addr = ':/images/images/no cover.jpg'
        self.setWindowIcon(QIcon(':/icons/icons/cat.ico'))
        self.__set_book_info()
        self.__set_BRLog()

    def __set_book_info(self):
        """
        :param: 无
        :return: 无
        """
        self.__ui.book_info.blockSignals(True)

        item_list = list()
        itemID = QTableWidgetItem(str(self.__cur_book.get_data().get_ID()),CellType.ctID.value)  # 第一个参数就是内容，ctID是指ID单元格
        itemID.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item_list.append(itemID)
        itemName = QTableWidgetItem(self.__cur_book.get_data().get_name(), CellType.ctName.value)
        itemName.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item_list.append(itemName)
        itemISBN = QTableWidgetItem(self.__cur_book.get_data().get_ISBN(), CellType.ctISBN.value)  # 第一个参数是内容，第二个参数是类型，类型可以自定义
        itemISBN.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item_list.append(itemISBN)
        itemAuthor = QTableWidgetItem(self.__cur_book.get_data().get_author(), CellType.ctAuthor.value)  # widgetItem全是str
        itemAuthor.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item_list.append(itemAuthor)
        itemPC = QTableWidgetItem(self.__cur_book.get_data().get_pageCnt(), CellType.ctPageCnt.value)
        itemPC.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item_list.append(itemPC)
        itemPD = QTableWidgetItem(self.__cur_book.get_data().get_publishedDate(), CellType.ctPubDate.value)
        itemPD.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item_list.append(itemPD)
        itemED = QTableWidgetItem(self.__cur_book.get_data().get_entryDate(), CellType.ctEntDate.value)
        itemED.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item_list.append(itemED)
        itemPrice = QTableWidgetItem(self.__cur_book.get_data().get_price(), CellType.ctPrice.value)
        itemPrice.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item_list.append(itemPrice)
        itemCatelog = QTableWidgetItem(self.__cur_book.get_data().get_catelog(), CellType.ctCatelog.value)
        itemCatelog.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item_list.append(itemCatelog)
        itemState = QTableWidgetItem(self.__cur_book.get_data().get_state(), CellType.ctState.value)
        itemState.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item_list.append(itemState)
        itemBC = QTableWidgetItem(self.__cur_book.get_data().get_borrowCnt(), CellType.ctBCnt.value)  # 这里要求是int
        itemBC.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item_list.append(itemBC)
        itemBA = QTableWidgetItem(self.__cur_book.get_data().get_balance(), CellType.ctBal.value)  # 这里要求是int
        itemBA.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        item_list.append(itemBA)
        for i in range(ColNum.colBal.value + 1):
            self.__ui.book_info.setItem(i,0,item_list[i])

        brief_intro = self.__cur_book.get_data().get_introduction()
        self.__ui.intro_content.setFontPointSize(18)
        self.__ui.intro_content.setPlainText(brief_intro)

        self.__cur_book.get_data().update_cover(QPixmap(self.__cur_book.get_data().get_absolute_PDFAddr()))
        # 没法，为了数据库
        self.__ui.book_cover.setPixmap(self.__cur_book.get_data().get_cover())
        self.__ui.book_cover.setScaledContents(True)
        self.__ui.book_info.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.__ui.BRLog_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.__ui.book_info.blockSignals(False)

    def __set_BRLog(self):
        """
        :param: 无
        :return: 无
        """
        all_rows = self.__ui.BRLog_table.rowCount()
        for i in range(all_rows):
            self.__ui.BRLog_table.removeRow(0) # 这个彻底删除行
            # 必须要删除0才行，因为删除后行号会调整，删除0行之后1行就变0行了，导致根本删除不了
        cur_BRLog_list = self.__cur_book.get_data().get_BRLog()
        if len(cur_BRLog_list) == 0:
            return
        for each_log in cur_BRLog_list:
            item_list = generate_BRLog_items(each_log)
            self.__set_BRLog_tableItem(item_list)
        self.BRLog_in_mainwindow.emit()

    def __set_BRLog_tableItem(self,item_list):
        """
        :param item_list: list(PyQt5.QtWidgets.QTableWidgetItem),将要设置在表格里的项
        :return: 无
        """
        row_no = self.__ui.BRLog_table.rowCount()
        self.__ui.BRLog_table.insertRow(row_no)
        for i in range(ColNum_BRLog.colRealPeriod.value + 1):
            self.__ui.BRLog_table.setItem(row_no,i,item_list[i])

    @pyqtSlot()
    def on_intro_content_textChanged(self):
        """
        :param: 无
        :return: 无
        """
        text = self.__ui.intro_content.toPlainText()
        self.__cur_book.get_data().update_introduction(text)
        if self.__ui.intro_content.document().isEmpty():
            self.__ui.intro_content.setFontPointSize(18)

    @pyqtSlot()
    def on_PDF_upload_clicked(self):
        """
        :param: 无
        :return: 无
        """
        cur_path = QDir.currentPath()
        title = '打开PDF文件'
        filt = 'PDF(*.pdf)'
        file_name, _ = QFileDialog.getOpenFileName(self,title,cur_path, filt)
        self.__cur_book.get_data().update_absolute_PDFAddr(file_name)
        self.__loadPDF(file_name) # 功能之一是设置封面

    def __loadPDF(self,file_name):
        """
        :param file_name: str,PDF文件名
        :return: 无
        """
        if file_name != '':
            pdf = fitz.open(file_name)
        else:
            return
        # 加载第一页（封面）
        first_page = pdf.loadPage(0) # 返回的是fltz.Pixmap
        cover = render_PDF_cover(first_page) # QPixmap
        width = self.__ui.book_cover.width()
        height = self.__ui.book_cover.height()
        pix_map = QPixmap(cover) # 不要self
        pix_map.scaled(width,height,Qt.IgnoreAspectRatio)
        self.__cur_book.get_data().update_cover(pix_map)
        self.__ui.book_cover.setPixmap(pix_map)
        self.__ui.book_cover.setScaledContents(True)

    @pyqtSlot()
    def on_PDF_preview_clicked(self):
        """
        :param: 无
        :return: 无
        """
        file_name = self.__cur_book.get_data().get_absolute_PDFAddr()
        if file_name != '' and file_name != self.__no_cover_addr:
            self.pdf = fitz.open(file_name)
        else:
            QMessageBox.critical(self,'错误','文件为空')
            return
        first_page = self.pdf.loadPage(0)  # 返回的是fltz.Pixmap
        cover = render_PDF_cover(first_page)
        self.pdf_widget = PDF_Popup(self)
        self.pdf_widget.pdf_page_change.connect(self.__update_pdf_page)
        self.pdf_widget.set_max_page(self.pdf.pageCount - 1)
        self.pdf_widget.setAttribute(Qt.WA_DeleteOnClose)  # 删除时窗口对象也删掉
        self.pdf_widget.setWindowFlag(Qt.Window, True)
        self.pdf_widget.setWindowFlag(Qt.WindowContextHelpButtonHint, False)  # 无帮助
        self.pdf_widget.set_currentPage(QPixmap(cover))
        self.pdf_widget.show()

    def __update_pdf_page(self,cur_page_num): # 这里是改变页面，不是改变页数
        """
        :param cur_page_num: int,当前的页面页数
        :return: 无
        """
        cur_page = self.pdf.loadPage(cur_page_num)
        cur_cover = render_PDF_cover(cur_page)
        self.pdf_widget.set_currentPage(QPixmap(cur_cover))
        return

    @pyqtSlot()
    def on_PDF_delete_clicked(self):
        """
        :param: 无
        :return: 无
        """
        self.__cur_book.get_data().update_absolute_PDFAddr(self.__no_cover_addr)
        self.__ui.book_cover.setPixmap(QPixmap(self.__cur_book.get_data().get_absolute_PDFAddr()))
        self.__ui.book_cover.setScaledContents(True)

    @pyqtSlot()
    def on_book_borrow_clicked(self):
        """
        :param: 无
        :return: 无
        """
        tourist_Dialog = TouristBR_Dialog(self)
        tourist_Dialog.tourist_info_borrow.connect(self.__addTouristInfo)
        tourist_Dialog.BRLog_table_update.connect(self.__set_BRLog)
        tourist_Dialog.set_borrow_state_btn()
        tourist_Dialog.auto_setDate_whenBorrowReturn()
        tourist_Dialog.setAttribute(Qt.WA_DeleteOnClose)  # 删除时窗口对象也删掉
        tourist_Dialog.setWindowTitle('游客登录状态 请输入信息')
        tourist_Dialog.setWindowFlag(Qt.Window, True)
        tourist_Dialog.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)  # 无最大最小化
        tourist_Dialog.setWindowFlag(Qt.WindowContextHelpButtonHint, False)  # 无帮助
        tourist_Dialog.show()

    def __addTouristInfo(self,cur_tourist_info):
        """
        :param cur_tourist_info: list[str],当前借书或还书输入的内容
        :return: 无
        """
        borrow_judge = cur_tourist_info[0]
        reader_ID = cur_tourist_info[1]
        time = cur_tourist_info[2]
        place = cur_tourist_info[3]
        period = cur_tourist_info[4] # 还书的话就是空的
        if borrow_judge == '1': # 此时是借书
            # 借书：读者ID，借书日期，借书地点，借书时长，是否归还（默参不传），剩下全是None
            cur_state_log = state_log(reader_ID, time, place, period, '', '')
            self.__cur_book.get_data().add_BRLog(cur_state_log)
        elif borrow_judge == '0': # 还书
            # 还书：读者ID，还书日期，还书地点
            cur_state_log = self.__cur_book.get_data().find_BRLog(reader_ID)
            try:
                if cur_state_log == None:
                    raise TypeError('current state log is None')
            except TypeError as t:
                QMessageBox.critical(self,'错误','该读者不存在或未借过此书')
                print('Error:',repr(t))
            else:
                cur_state_log, cur_idx = cur_state_log
                cur_state_log.update_IsReturn()
                cur_state_log.update_returnTime(time)
                cur_state_log.update_returnPlace(place)
                self.__cur_book.get_data().update_BRLog(cur_idx,cur_state_log)
                # 这个时候period没有 所以不用管

    @pyqtSlot()
    def on_book_return_clicked(self):
        """
        :param: 无
        :return: 无
        """
        tourist_Dialog = TouristBR_Dialog(self)
        tourist_Dialog.tourist_info_return.connect(self.__addTouristInfo)
        tourist_Dialog.BRLog_table_update.connect(self.__set_BRLog)
        tourist_Dialog.set_return_state_btn()
        tourist_Dialog.auto_setDate_whenBorrowReturn()
        tourist_Dialog.setWindowTitle('游客登录状态 请输入信息')
        tourist_Dialog.setWindowFlag(Qt.Window, True)
        tourist_Dialog.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)  # 无最大最小化
        tourist_Dialog.setWindowFlag(Qt.WindowContextHelpButtonHint, False)  # 无帮助
        tourist_Dialog.show()
