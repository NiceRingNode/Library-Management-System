#include "PDFWidget.h"
#include "ui_PDFWidget.h"

PDFWidget::PDFWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::PDFWidget)
{
    ui->setupUi(this);
}

PDFWidget::~PDFWidget()
{
    delete ui;
}
