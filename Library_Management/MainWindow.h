#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_book_add_clicked();

    void on_book_delete_clicked();

    void on_PDF_upload_clicked();

    void on_start_search_clicked();

    void on_book_form_add_currentCellChanged(int currentRow, int currentColumn, int previousRow, int previousColumn);

    void on_book_form_add_cellChanged(int row, int column);

    void on_book_form_add_itemChanged(QTableWidgetItem *item);

    void on_book_form_add_cellPressed(int row, int column);

    void on_book_form_add_cellDoubleClicked(int row, int column);

    void on_book_form_add_cellEntered(int row, int column);


    void on_book_class_2_itemClicked(QTreeWidgetItem *item, int column);

    void on_book_class_2_itemChanged(QTreeWidgetItem *item, int column);

    void on_txt_in_clicked();

    void on_txt_out_clicked();

    void on_Excel_in_clicked();

    void on_Excel_out_clicked();

    void on_EditNum_editingFinished();

    void on_EditISBN_editingFinished();

    void on_EditName_editingFinished();

    void on_EditAuthor_editingFinished();

    void on_EditPrice_editingFinished();

    void on_EditPrice2_editingFinished();

    void on_PDF_table_itemClicked(QTableWidgetItem *item);

    void on_book_form_add_itemClicked(QTableWidgetItem *item);

    void on_PDF_table_cellClicked(int row, int column);

    void on_PDF_delete_clicked();

    void on_EditID_editingFinished();

    void on_EditID_textEdited(const QString &arg1);

    void on_EditID_cursorPositionChanged(int arg1, int arg2);

    void on_book_form_search_cellClicked(int row, int column);

    void on_book_form_search_itemActivated(QTableWidgetItem *item);

    void on_pushButton_clicked();

    void on_db_save_clicked();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
