#ifndef BOOKDETAILWIDGET_H
#define BOOKDETAILWIDGET_H

#include <QWidget>

namespace Ui {
class BookDetailWidget;
}

class BookDetailWidget : public QWidget
{
    Q_OBJECT

public:
    explicit BookDetailWidget(QWidget *parent = nullptr);
    ~BookDetailWidget();

private slots:
    void on_pushButton_clicked();

    void on_preview_clicked();

    void on_PDF_preview_clicked();

    void on_borrow_clicked();

    void on_intro_content_textChanged();

    void on_retrun_clicked();

    void on_book_borrow_clicked();

    void on_book_return_clicked();

private:
    Ui::BookDetailWidget *ui;
};

#endif // BOOKDETAILWIDGET_H
