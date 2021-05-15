import sys
from typing import TypeVar,Generic,Type,NewType
from enum import Enum
from basic_logic import *

self_type = NewType('self_type',None)

class CellType(Enum): # 单元格类型
    ctID = 10000
    ctName = 10001
    ctISBN = 10002
    ctAuthor = 10003
    ctPageCnt = 10004
    ctPubDate = 10005
    ctEntDate = 10006
    ctPrice = 10007
    ctCatelog = 10008
    ctState = 10009
    ctBCnt = 100010
    ctBal = 100011
    ctBRLog = 100012

class node:
    @typeassert(self_type,book) # 规定是book_info类
    def __init__(self,input_data:book) -> None:
        self.data = input_data
        self.next = None
        self.pre = None

    def get_data(self) -> book:
        return self.data

    def get_pre(self):
        return self.pre

    def get_next(self):
        return self.next

book_node = NewType('book_node',node)

class linklist:
    def __init__(self):
        self.__dtype = node
        self.__head = None #  头结点是0啊
        self.__tail = self.__head
        self.__size = 0 # 头结点不算

    def linklist_init(self) -> book_node:
        return self.__head

    def head(self) -> book_node:
        return self.__head

    def tail(self) -> book_node:
        return self.__tail

    def size(self) -> int:
        return self.__size

    def add_size(self) -> None:
        self.__size += 1

    def sub_size(self) -> None:
        self.__size -= 1

    @typeassert(self_type,node)
    def insert(self,x) -> None: # 不会满，尾插法
        try:
            if self.__dtype != type(x):
                raise TypeError('Error:%s and %s is incompatible' % (type(self.__dtype),type(x)))
        except TypeError as t:
            print('Error:',repr(t))
            sys.exit()
        else:
            new_node = x
            self.add_size()
            if self.__head == None: # 在头结点后面插
                self.__head = new_node
                self.__tail = self.__head
                self.__head.pre = self.__tail
                self.__head.next = self.__tail
                self.__tail.pre = self.__head
                self.__tail.next = self.__head # 形成一个环
            else:
                self.__tail.next = new_node
                self.__tail.next.pre = self.__tail
                self.__tail = self.__tail.next
                self.__tail.next = self.__head
                self.__head.pre = self.__tail

    # 提供两个模式，通过pos来寻找和通过x来寻找然后删除
    # @typeassert(self_type,int)
    def erase_by_pos(self,pos) -> None: # 通过位置来删除
        try:
            if pos < 0 or pos > self.size() - 1: # 从0开始算
                raise IndexError('index(%d) is out of range' % pos)
        except IndexError as i:
            print('Error:',repr(i))
            sys.exit()
        print(pos)
        now = self.head()
        cnt = 0
        flag = True # 用来标识是否已经达到了尾节点，防止又从头结点循环回来
        while flag == True:
            if now == self.tail():
                flag = False
            if cnt == pos:
                if now == self.head(): # 如果是头结点
                    self.__head = now.next
                    if self.size() == 1: # 证明这是最后一个
                        self.__head = self.__tail = None
                        del now
                        break
                    self.__tail.next = self.__head
                    self.__head.pre = self.__tail
                elif now == self.tail(): # 如果是尾节点
                    self.__tail = now.pre
                    self.__tail.next = self.__head
                    self.__head.pre = self.__tail
                else: # 如果是中间节点
                    now.next.pre = now.pre
                    now.pre.next = now.next
                self.sub_size()
                del now
                break
            now = now.next
            cnt += 1
        if cnt > self.size():
            print("no this node")
            return

    @typeassert(self_type,node)
    def erase_by_x(self,x) -> None: # 通过数值来删除
        now = self.head()
        flag = True
        while flag == True:
            if now == self.tail():
                flag = False
            if now.data == x:
                if now == self.head(): # 如果是头结点
                    if self.size() == 1: # 证明这是最后一个
                        self.__head = self.__tail = None
                        del now
                        break
                    self.__head = now.next
                    self.__tail.next = self.__head
                    self.__head.pre = self.__tail
                elif now == self.tail(): # 如果是尾节点
                    self.__tail = now.pre
                    self.__tail.next = self.__head
                    self.__head.pre = self.__tail
                else: # 如果是中间节点
                    now.next.pre = now.pre
                    now.pre.next = now.next
                self.sub_size()
                del now
                break
            now = now.next
        if flag == False:
            print("no this node")
            return

    def traverse(self) -> None:
        now = self.head()
        flag = True
        while now != None and now.next != None and flag == True: # 第二次变成头结点的时候就停下来了
            # print("%d" % now.data,end = ' ')
            print(now.data.get_ID())
            now = now.next
            if now == self.head():
                flag = False
        print()

    # @typeassert(self_type,int)
    def search_by_pos(self,pos):
        try:
            if pos < 0 or pos > self.size() - 1:
                raise IndexError('index(%d) is out of range' % pos)
        except IndexError as i:
            print('Error:',repr(i))
            sys.exit()
        now = self.head()
        i = 0
        flag = True # 用来标识是否已经达到了尾节点，防止又从头结点循环回来
        while flag == True:
            if i == pos:
                return now
            i += 1
            if now == self.tail():
                flag = False
            now = now.next
        if flag == False:
            print("no this node")
            return

    @typeassert(self_type,node)
    def search_by_x(self,x):
        now = self.head()
        flag = True
        while flag == True:
            if now== self.tail(): # 防止达到尾节点
                flag = False
            if now.get_data() == x:
                return now
            now = now.next
        if flag == False:
            print("no this node")
            sys.exit()

    def modify(self,now,item_type,modify_content):
        if item_type == CellType.ctID.value:
            now.update_ID(modify_content)
        elif item_type == CellType.ctName.value:
            now.update_name(modify_content)
        elif item_type == CellType.ctISBN.value:
            now.update_ISBN(modify_content)
        elif item_type == CellType.ctAuthor.value:
            now.update_author(modify_content)
        elif item_type == CellType.ctPubDate.value:
            now.update_publishedDate(modify_content)
        elif item_type == CellType.ctEntDate.value:
            now.update_entryDate(modify_content)
        elif item_type == CellType.ctPrice.value:
            now.update_price(modify_content) # 艹 一开始忘了写这个
        elif item_type == CellType.ctCatelog.value:
            now.update_catelog(modify_content)
        elif item_type == CellType.ctState.value:
            now.update_state(modify_content)
        elif item_type == CellType.ctBCnt.value:
            now.update_borrowCnt(modify_content)
        elif item_type == CellType.ctBRLog.value:
            now.add_BRLog(modify_content)

    @typeassert(self_type,int)
    def modify_by_pos(self,pos,item_type,modify_content):
        try:
            if pos < 0 or pos > self.size() - 1:
                raise IndexError('index(%d) is out of range' % pos)
        except IndexError as i:
            print('Error:',repr(i))
            sys.exit()
        now = self.head()
        i = 0
        flag = True # 用来标识是否已经达到了尾节点，防止又从头结点循环回来
        while flag == True:
            if i == pos:
                self.modify(now.data,item_type,modify_content)
                return
            i += 1
            if now == self.tail():
                flag = False
            now = now.next
        self.traverse()
        if flag == False:
            print("no this node")
            return

def main():
    l = linklist()
    
if __name__ == '__main__':
    main()