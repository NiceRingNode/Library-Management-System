from functools import wraps
from inspect import signature
from typing import NewType
from PyQt5.QtGui import QPixmap

self_type = NewType('self_type',None)
def typeassert(*type_args,**type_kwargs): # 检查参数正确性的装饰器，最外面套的这一层是用来指定类型的
        def decorate(func):
            sig = signature(func) # 返回函数func()的函数签名，函数签名：函数名、参数个数、参数类型、返回值
            bound_types = sig.bind_partial(*type_args,**type_kwargs).arguments  # arguments是个OrderedDict
            bound_types_without_self = {key:dict(bound_types)[key] for key in list(dict(bound_types).keys())[1:]}
            # 其实bind_partial是偏函数方法，就是固定原函数的某些参数
            @wraps(func) # 这个的作用是获取被装饰的函数的原始信息，保证不被覆盖
            def warpper(*args,**kwargs):
                bound_values = sig.bind(*args,**kwargs) # 这里处理的就是传入的参数的类型了
                bound_values_without_self = list(bound_values.arguments.items())[1:]
                for name,value in bound_values_without_self: # items()以列表返回可遍历的(键, 值) 元组数组
                    if name in bound_types_without_self:
                        # print(value,bound_types_without_self[name])
                        if not isinstance(value,bound_types_without_self[name]):
                            raise TypeError("arg {0}'s type is wrong,should be {1} type".format(name,bound_types[name]))
                return func(*args,**kwargs) # 因为这里是传入的参数，所以返回的就是func这个待传入参数的函数
            return warpper
        return decorate

class state_log:
    @typeassert(self_type,str,str,str,str,str,str)
    def __init__(self,readerID:str,borrowTime:str,borrowPlace:str,
        lending_period:str,retTime:str,retPlace:str) -> None:
        self.__readerID = readerID
        self.__borrowTime = borrowTime
        self.__borrowPlace = borrowPlace
        self.__lending_period = lending_period # 借阅时长
        self.__IsReturn = False
        self.__returnTime = retTime
        self.__returnPlace = retPlace
        self.__real_lendingperiod = '1'

    def get_readerID(self) -> str:
        return self.__readerID

    def get_borrowTime(self) -> str:
        return self.__borrowTime

    def get_borrowPlace(self) -> str:
        return self.__borrowPlace

    def get_lending_period(self) -> str:
        return self.__lending_period

    def get_IsReturn(self) -> bool:
        return self.__IsReturn

    def get_returnTime(self) -> str:
        return self.__returnTime

    def get_returnPlace(self) -> str:
        return self.__returnPlace

    def update_real_lendingperiod(self) -> str:
        return self.__real_lendingperiod

    @typeassert(self_type, str)
    def update_readerID(self, new_readerID: str):
        self.__readerID = new_readerID

    @typeassert(self_type,str)
    def update_borrowTime(self,new_borrowTime:str):
        self.__borrowTime = new_borrowTime

    @typeassert(self_type, str)
    def update_borrowPlace(self, new_borrowPlace: str):
        self.__borrowPlace = new_borrowPlace

    @typeassert(self_type, str)
    def update_lending_period(self, new_lending_period: str):
        self.__lending_period = new_lending_period

    def update_IsReturn(self):
        self.__IsReturn = bool(1 - self.__IsReturn) # 取反

    @typeassert(self_type, str)
    def update_returnTime(self, new_returnTime: str):
        self.__returnTime = new_returnTime

    @typeassert(self_type,str)
    def update_returnPlace(self,new_returnPlace:str):
        self.__returnPlace = new_returnPlace

    @typeassert(self_type, str)
    def update_real_lendingperiod(self, new_real_lendingperiod: str):
        self.__real_lendingperiod = new_real_lendingperiod

class book:
    global self_type
    # 带self的是实例变量，不在__init__的是类变量，私有性还是一样用下划线决定的，类变量就跟c++的静态变量差不多，所有实例都只有同一份
    # 实现：1.图书用一个类实现，图书的编号，ISBN，名字，作者，出版年月日，入库时间，类别，当前状态（库存or借出），借出的次数，借出的时间、地点，还回来的时间、地点（列表）
    @typeassert(self_type,str,str,str,str,str,str,str,str,str,str)
    def __init__(self,ID:str,name:str,ISBN:str,author:str,pageCnt:str,publishedDate:str,entryDate:str,price:str,catelog:str,balance = '1') -> None:
        self.__ID = ID # str
        self.__name = name  # str
        self.__ISBN = ISBN # str
        self.__author = author # str
        self.__pageCnt = pageCnt # str
        self.__publishedDate = publishedDate # str
        self.__entryDate = entryDate # str
        self.__price = price
        self.__catelog = catelog # 类别
        self.__state = '无借出' # str,1表示有借出
        self.__borrowCnt = '0' # str,借出的次数
        self.__balance = balance
        self.__BRLog = [] # 借出归还的日志，放在一起
        # self.update_borrowLog(state_log('1','2020-10-02','2020-10-03','10'))
        # self.update_returnLog(state_log('1','2020-10-02','2020-10-03','10'))
        self.__cover = QPixmap(':/images/images/no cover.jpg')
        self.__absolute_PDFAddr = ':/images/images/no cover.jpg'
        self.__introduction = '暂无'

    def get_ID(self) -> str:
        return self.__ID

    def get_name(self) -> str:
        return self.__name

    def get_ISBN(self) -> str:
        return self.__ISBN

    def get_author(self) -> str:
        return self.__author

    def get_pageCnt(self) -> str:
        return self.__pageCnt

    def get_publishedDate(self) -> str:
        return self.__publishedDate

    def get_entryDate(self) -> str:
        return self.__entryDate

    def get_price(self) -> str:
        return self.__price
    
    def get_catelog(self) -> str:
        return self.__catelog

    def get_state(self) -> str:
        return self.__state

    def get_borrowCnt(self) -> str:
        return self.__borrowCnt

    def get_balance(self) -> str:
        return self.__balance

    def get_BRLog(self) -> list:
        return self.__BRLog

    def get_cover(self) -> QPixmap:
        return self.__cover

    def get_absolute_PDFAddr(self) -> str:
        return self.__absolute_PDFAddr

    def get_introduction(self) -> str:
        return self.__introduction

    @typeassert(self_type,str)
    def update_ID(self,new_ID:str) -> None:
        self.__ID = new_ID

    @typeassert(self_type,str)
    def update_name(self,new_name:str) -> None:
        self.__name = new_name

    @typeassert(self_type,str)
    def update_ISBN(self,new_ISBN:str) -> None:
        self.__ISBN = new_ISBN

    @typeassert(self_type,str)
    def update_author(self,new_author:str) -> None:
        self.__author = new_author

    @typeassert(self_type,str)
    def update_pageCnt(self,pageCnt:str) -> None:
        self.__pageCnt = pageCnt

    @typeassert(self_type,str)
    def update_publishedDate(self,new_publishedDate:str) -> None:
        self.__publishedDate = new_publishedDate

    @typeassert(self_type,str)
    def update_entryDate(self,new_entryDate:str) -> None:
        self.__entryDate = new_entryDate

    @typeassert(self_type,str)
    def update_price(self,new_price:str) -> None:
        self.__price = new_price

    @typeassert(self_type,str)
    def update_catelog(self,new_catelog:str) -> None:
        self.__catelog = new_catelog
        
    @typeassert(self_type,str)
    def update_state(self,new_state:str) -> None:
        self.__state = new_state

    @typeassert(self_type,str)
    def update_borrowCnt(self,new_borrowCnt:str) -> None:
        self.__borrowCnt = new_borrowCnt

    def add_borrowCnt(self) -> None:
        self.__borrowCnt += 1

    @typeassert(self_type, str)
    def update_balance(self, new_balance: str) -> None:
        self.__balance = new_balance

    @typeassert(self_type,int,state_log)
    def update_BRLog(self,upd_index:int,new_state_log:state_log) -> None: # update是更新，先将最后一个pop出去再放一个完整的进来
        self.__BRLog.pop(upd_index)
        self.__BRLog.insert(upd_index,new_state_log)

    @typeassert(self_type, state_log)
    def add_BRLog(self, new_state_log: state_log) -> None:  # add是增加
        self.__BRLog.append(new_state_log)

    def find_BRLog(self,reader_ID):
        for cur_state_log in self.__BRLog:
            if reader_ID == cur_state_log.get_readerID():
                idx = self.__BRLog.index(cur_state_log)
                return (cur_state_log,idx)
        return None

    @typeassert(self_type, QPixmap)
    def update_cover(self, new_cover: QPixmap) -> None:
        self.__cover = new_cover

    @typeassert(self_type, str)
    def update_absolute_PDFAddr(self, new_addr: str) -> None:
        self.__absolute_PDFAddr = new_addr

    @typeassert(self_type, str)
    def update_introduction(self, new_intro: str) -> None:
        self.__introduction = new_intro