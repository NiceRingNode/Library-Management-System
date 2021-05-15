#include "MainWindow.h"
#include "ui_MainWindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_book_add_clicked()
{

}

void MainWindow::on_book_delete_clicked()
{

}

void MainWindow::on_PDF_upload_clicked()
{

}

void MainWindow::on_start_search_clicked()
{

}

void MainWindow::on_book_form_add_currentCellChanged(int currentRow, int currentColumn, int previousRow, int previousColumn)
{

}

void MainWindow::on_book_form_add_cellChanged(int row, int column)
{

}



void MainWindow::on_book_form_add_cellDoubleClicked(int row, int column)
{

}

void MainWindow::on_book_form_add_cellEntered(int row, int column)
{

}


void MainWindow::on_book_class_2_itemClicked(QTreeWidgetItem *item, int column)
{

}

void MainWindow::on_book_class_2_itemChanged(QTreeWidgetItem *item, int column)
{

}

void MainWindow::on_txt_in_clicked()
{

}

void MainWindow::on_txt_out_clicked()
{

}

void MainWindow::on_Excel_in_clicked()
{

}

void MainWindow::on_Excel_out_clicked()
{

}

void MainWindow::on_EditISBN_editingFinished()
{

}

void MainWindow::on_EditName_editingFinished()
{

}

void MainWindow::on_EditAuthor_editingFinished()
{

}


void MainWindow::on_EditPrice2_editingFinished()
{

}


void MainWindow::on_EditPrice_editingFinished()
{

}


void MainWindow::on_PDF_table_cellClicked(int row, int column)
{

}

void MainWindow::on_PDF_delete_clicked()
{

}

void MainWindow::on_EditID_editingFinished()
{

}

void MainWindow::on_EditID_textEdited(const QString &arg1)
{

}

void MainWindow::on_EditID_cursorPositionChanged(int arg1, int arg2)
{

}

void MainWindow::on_book_form_search_cellClicked(int row, int column)
{

}


void MainWindow::on_db_save_clicked()
{

}
