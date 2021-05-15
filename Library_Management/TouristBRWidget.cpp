#include "TouristBORETWidget.h"
#include "ui_TouristBorrowWidget.h"

TouristBorrowWidget::TouristBorrowWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::TouristBorrowWidget)
{
    ui->setupUi(this);
}

TouristBorrowWidget::~TouristBorrowWidget()
{
    delete ui;
}
