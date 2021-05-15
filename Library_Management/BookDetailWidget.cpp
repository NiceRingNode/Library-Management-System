#include "BookDetailWidget.h"
#include "ui_BookDetailWidget.h"

BookDetailWidget::BookDetailWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::BookDetailWidget)
{
    ui->setupUi(this);
}

BookDetailWidget::~BookDetailWidget()
{
    delete ui;
}


void BookDetailWidget::on_PDF_preview_clicked()
{

}


void BookDetailWidget::on_intro_content_textChanged()
{

}


void BookDetailWidget::on_book_borrow_clicked()
{

}

void BookDetailWidget::on_book_return_clicked()
{

}
