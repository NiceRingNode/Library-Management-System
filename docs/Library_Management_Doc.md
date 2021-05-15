# Packages Needed

```python
PyQt5
openpyxl
fitz
PyMuPDF
pyinstaller
```

```shell
pip install --timeout=1000 -i https://pypi.tuna.tsinghua.edu.cn/simple pyqt5
pip install --timeout=1000 -i https://pypi.tuna.tsinghua.edu.cn/simple pyqt5-tools
pip install --timeout=1000 -i https://pypi.tuna.tsinghua.edu.cn/simple fitz
pip install --timeout=1000 -i https://pypi.tuna.tsinghua.edu.cn/simple PyMuPDF
pip install --timeout=1000 -i https://pypi.tuna.tsinghua.edu.cn/simple openpyxl
pip install --timeout=1000 -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
```

# Install

```shell
pyinstaller -F -w --i "D:\\Python Projects\\图书管理系统试验品\\Library_Management\\icons\\appIcon.ico" Library_MainWindow.py --noconsole
```

# Enumerations

```python
class ColNum(Enum)
```

功能：用以代指主窗口中表格中的不同行的行号

```python
class ColNum_BRLog(Enum)
```


功能：用以代指借阅归还记录（BRLog）表格中的不同行的行号

```python
class CellType(Enum)
```


功能：作为主窗口中的表格的QTableWidgetItem的类型

```python
class CellType_BRLog(Enum)
```

功能：作为借阅归还记录（BRLog）表格的QTableWidgetItem的类型

```python
class TreeItemType(Enum)
```

功能：作为类别树的子节点的类型



# Classes

## Library_Management

```python
class Library_Management(QMainWindow)
```

继承：PyQt5.QtWidgets.QMainWindow

功能：程序主界面

### Attributes

```python
self.__ui:class
```

功能：窗口的UI界面

```python
self.__book_list:list
```

功能：图书链表，用以储存所有图书

```python
self.__cate_dict:dict
```

功能：类别字典，用以储存所有图书的类别

```python
self.__picture_dict:dict
```

功能：图片字典，用以储存背景图片

```python
self.__search_place:dict
```

功能：每个键为图书的属性，对应的值为搜索输入框里的内容或0，用以判断某个键对应的输入框是否有输入

```python
self.__search_index:dict
```

功能：每个键为图书的属性，对应的值为属性在表格里的下标，方便搜索

```python
self.__timer:PyQt5.QtCore.QTimer
```

功能：定时器，在更换背景图片时计时

### Member Functions

#### __init__(self,parent = None)

```python
def __init__(self,parent = None)
    """
    :param parent: 父类，默认为None
    """
```

功能：初始化成员变量

#### __setUI(self)

```python
def __setUI(self)
    """
    :param: 无
    :return:无
    """
```

功能：初始化其他UI设置

#### __pictureDictGenerate(self)

```python
def __pictureDictGenerate(self)
    """
    :param: 无
    :return: 无
    """
```

功能：生成背景图片字典

#### paintEvent(self,event)

```python
def paintEvent(self,event)
    """
    :param event: PyQt5.QtCore.QEvent,标准绘画事件
    :return: 无
    """
```

功能：绘画事件调用，重绘背景图片

####  keyPressEvent(self,event)

```python
def keyPressEvent(self,event)
    """
    :param event: PyQt5.QtCore.QEvent,标准键盘事件
    :return: 无
    """
```

功能：键点击事件调用，在键盘上“Delete”键点击时执行图书删除操作

#### __createRow(self,row_no:int,flag:str,mode:str,*args)

```python
def __createRow(self,row_no:int,flag:str,mode:str,*args)
    """
    :param row_no: int,当前行号
    :param flag: str,创建行的两个表格位置，在book_form_add创建：'add',在book_form_search创建：'search'
    :param mode: str,创建行的两种模式，默认创建：'default',导入创建：'import'
    :param args: tuple,mode='import'时传入的不定长参数
    :return:无
    """
```

功能：创建默认的行或通过文件输入的内容创建表格中的行

#### __setAllItem(self,row_no:int,flag:str,itemID,itemISBN,itemName,itemAuthor,itemPC,itemPD,itemED,itemPrice,itemCatelog,itemState,itemBC,itemBA,itemBL,itemRL)

```python
    def __setAllItem(self,row_no:int,flag:str,item_list:list):
        """
        :param row_no: int,当前行号
        :param flag: str,创建行的两个表格位置，在book_form_add创建：'add',在book_form_search创建：'search'
        :param item_list: list[PyQt5.QtWidgets.QTableWidgetItem],将要设置在表格里的项组成的列表
        :return: 无
        """
```

功能：将不同的item设置到table上

#### __createRowByNode(self,row_no:int,book,flag:str)

```python
def __createRowByNode(self,row_no:int,book,flag:str)
    """
    :param row_no: int,当前行号
    :param book: node,传入的书籍节点
    :param flag: str,创建行的两个表格位置，在book_form_add创建：'add',在book_form_search创建：'search'
    :return: 无
    """
```

功能：通过图书列表的节点创建表格中的行

#### __addNewCatelog(self,cur_catelog,cur_row) -> None

```python
def __addNewCatelog(self,cur_catelog,cur_row) -> None
    """
    :param cur_catelog: str,当前书籍的类别
    :param cur_row: int,当前行号
    :return: 无
    """
```

功能：增加新的图书类别

#### __simultaneousItemChanged(self,row:int,col:int,new_content:str) -> None

```python
def __simultaneousItemChanged(self,row:int,col:int,new_content:str) -> None
    """
    :param row: int,当前行号
    :param col: int,当前列号
    :param new_content: str,用于更新的新内容
    :return: 无
    """
```

功能：在“图书录入导出”页面的表格的每一个小项改变时同时，也在“图书信息”页面内的表格的同样的位置改变相同的内容

#### on_book_add_clicked(self)

```python
def on_book_add_clicked(self)
    """
    :param: 无
    :return: 无
    """
```

功能：点击”添加“按钮进行书籍添加，此时为添加默认的行

#### on_book_delete_clicked(self)

```python
def on_book_delete_clicked(self)
    """
    :param: 无
    :return: 无
    """
```

功能：点击“删除”按钮进行书籍删除，如果有选中的行，就删除当前行；如果没有，则从最后一行开始删

#### __fixCatelogDict(self)

```python
def __fixCatelogDict(self)
    """
    :param: 无
    :return: 无
    """
```

功能：纠正出错的类别字典，在添加或删除书籍后类别可能会增加或减少

#### on_book_form_add_cellChanged(self,row:int,column:int)

```python
def on_book_form_add_cellChanged(self,row:int,column:int)
    """
    :param row: int,当前行号
    :param column: int,当前列号
    :return: 无
    """
```

功能：“图书录入导出”这个表格内的项改变时进行的一系列操作

#### __deleteOldCateloginDict(self,old_catelog:str,old_row:int) -> None

```python
def __deleteOldCateloginDict(self,old_catelog:str,old_row:int) -> None
    """
    :param old_catelog: str,旧的类别
    :param old_row: int,旧的行号
    :return: 无
    """
```

功能：删除旧的已经废除的图书类别

#### on_book_form_add_cellDoubleClicked(self,row:int,column:int) -> None

```python
def on_book_form_add_cellDoubleClicked(self,row:int,column:int) -> None
    """
    :param row: int,当前行号
    :param column: int,当前列号
    :return: 无
    """
```

功能：双击““图书信息”页面内的表格内的项时进行的一系列操作，此时一般为改变表格的项内容

#### on_book_class_2_itemClicked(self,item,column:int) -> None

```python
def on_book_class_2_itemClicked(self,item,column:int) -> None
    """
    :param item: PyQt5.QtWidgets.QTableWidgetItem,当前表格中选中的项
    :param column: int,当前列号
    :return: 无
    """
```

功能：单击“图书信息”页面内的树形表格内的项时进行的一系列操作

#### __set_main_BRLog_table(self)

```python
def __set_main_BRLog_table(self)
    """
    :param: 无
    :return: 无
    """
```

功能：设置主窗口的借阅/归还记录

#### on_book_form_search_cellClicked(self,row,column)

```python
def on_book_form_search_cellClicked(self,row,column)
    """
    :param row: int,当前行号
    :param column: int,当前列号
    :return: 无
    """
```

功能：单击“图书信息”页面内的表格内的项时进行的一系列操作

#### on_txt_in_clicked(self)

```python
def on_txt_in_clicked(self)
    """
    :param: 无
    :return: 无
    """
```

功能：单击“txt导入”按钮时执行的操作，打开.txt文件读入信息，并在表格中显示

#### __readTxt(self,file_name:str) -> bool

```python
def __readTxt(self,file_name:str) -> bool
    """
    :param file_name: str,txt文件名
    :return: bool,是否成功
    """
```

功能：配合on_txt_in_clicked()函数使用，打开.txt文件并进行编码和内容读入

#### __import2Table(self,line_str:str) -> None

```python
def __import2Table(self,line_str:str) -> None
    """
    :param line_str: str,从self.__readTxt()读入的单行文件str
    :return: 无
    """
```

功能：在txt文件打开后，将内容显示在表格上

#### on_txt_out_clicked(self)

```python
def on_txt_out_clicked(self)
    """
    :param: 无
    :return: 无
    """
```

功能：单击“txt导出”按钮时执行的操作，打开用户选择的.txt文件，将“图书录入导出”页面的表格的内容以txt的形式导出到文件里

#### __writeTxt(self,file_name)

```python
def __writeTxt(self,file_name)
    """
    :param file_name: str,txt文件名
    :return: 无
    """
```

功能：配合on_txt_out_clicked()函数使用，设定输出流

#### __exportTable(self,file_stream)

```python
def __exportTable(self,file_stream)
    """
    :param file_stream: PyQt5.QtCore.QTextStream,文件流
    :return: 无
    """
```

功能：在此函数内执行内容导出.txt文件

#### on_Excel_in_clicked(self)

```python
def on_Excel_in_clicked(self)
    """
    :param: 无
    :return: 无
    """
```

功能：单击“Excel导入”按钮时执行的操作，打开.xlsx文件读入信息，并在表格中显示

#### __readExcel(self,file_name:str)

```python
def __readExcel(self,file_name:str)
    """
    :param file_name: str,excel文件名，格式为.xlsx
    :return: 无
    """
```

功能：配合on_Excel_in_clicked()函数使用，打开.xlsx文件并进行编码和内容读入

#### on_Excel_out_clicked(self)

```python
def on_Excel_out_clicked(self)
    """
    :param: 无
    :return: 无
    """
```

功能：单击“Excel导出”按钮时执行的操作，打开用户选择的.xlsx文件，将“图书录入导出”页面的表格的内容以该形式导出到文件里

#### __writeExcel(self,file_name)

```python
def __writeExcel(self,file_name)
    """
    :param file_name: str,excel文件名，格式为.xlsx
    :return: 无
    """
```

功能：在此函数内执行内容导出到.xlsx文件

#### __connectDefaultDB(self)

```python
def __connectDefaultDB(self)
    """
    :param: 无
    :return: 无
    """
```

功能：如果不存在数据库，则创建并连接；存在则直接连接该数据库文件，连接后读出数据到表格里（功能未完善）

#### on_db_save_clicked(self)

```python
def on_db_save_clicked(self)
    """
    保存数据到数据库
    :param: 无
    :return: 无
```

功能：保存两个表（基础信息表和借还记录表）的数据到数据库

#### on_EditID_editingFinished(self)

#### on_EditName_editingFinished(self)

#### on_EditAuthor_editingFinished(self)

```python
def on_EditID_editingFinished(self)
    """
    :param: 无
    :return: 无
    """
def on_EditName_editingFinished(self)
    """
    :param: 无
    :return: 无
    """
def on_EditAuthor_editingFinished(self)
    """
    :param: 无
    :return: 无
    """
```

功能：这三个函数，分别对应在“”图书信息‘’页面的“书籍查询”模块中，在“ID”，“书名”，“ISBN”这三个对应的输入框输入完内容之后获取输入框里的内容放入self.__search_place字典中

#### search_output(self,index_text)

```python
def search_output(self,index_text)
    """
    :param index_text: int,需要找的节点的下标
    :return: 无
    """
```

功能：在搜索到符合条件的项后，在表格上显示该项

#### on_start_search_clicked(self)

```python
def on_start_search_clicked(self)
    """
    :param: 无
    :return: 无
    """
```

功能：点击“开始搜索”按钮后，对所有书籍进行搜索

#### book_list_traverse(self)

```python
def book_list_traverse(self)
    """
    :param: 无
    :return: 无
    """
```

功能：对书籍链表进行遍历



## Book_Detail

```python
class Book_Detail(QWidget)
```

继承：PyQt5.QtWidgets.QWidget

功能：书籍详细信息

### Attributes

TODO

### Member Functions

TODO



## TouristBR_Dialog

```python
class TouristBR_Dialog(QDialog)
```

继承：PyQt5.QtWidgets.QDialog

功能：游客借书还书时录入的信息

### Attributes

TODO

### Member Functions

TODO



## PDF_Popup

```python
class PDF_Popup(QWidget)
```

继承：PyQt5.QtWidgets.QWidget

功能：进行pdf预览时弹出的弹窗

### Attributes

TODO

### Member Functions

TODO



## node

```python
class node
```

功能：作为链表的节点

### Attributes

TODO

### Member Functions

TODO



## linklist

```python
class linklist
```

功能：链表，作为主数据结构

### Attributes

TODO

### Member Functions

TODO



## state_log

```python
class state_log
```

功能：书籍借阅/归还的信息，包括借阅时间、借阅地点等

### Attributes

TODO

### Member Functions

TODO



## book

```python
class book
```

功能：储存书籍的信息数据，放入node.data中，包括书名，ISBN等等

### Attributes

TODO

### Member Functions

TODO



# Functions

## render_PDF_cover(page_raw,size=(1, 1))

```python
def render_PDF_cover(page_raw,size=(1, 1))
    """
    :param page_raw: fltz.Pixmap,pdf的每一页
    :param size: tuple(int,int),用于指定fitz.Matrix的大小
    :return: QPixmap,渲染后的图片
    """
```

功能：渲染每一页pdf，使其从fltz.Pixmap转换为PyQt5.QtGui.QPixmap，用于后续pdf的显示

## generate_BRLog_items(each_log)

```python
def generate_BRLog_items(each_log) -> list:
    """
    :param each_log: 
    :return: list[PyQt5.QtWidgets.QTableWidgetItem],返回一个全是item的列表，用于设置到表格中
    """
```

功能：将每一个log的所有信息，如借书时间、地点等拆分并包装成QTableWidgetItem，并加入列表中，用于设置到相应的表格中

## typeassert(*type_args,**type_kwargs)

```python
def typeassert(*type_args,**type_kwargs)
```

功能：装饰器，用于进行类型判断