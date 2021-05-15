#include "PDFDialog.h"
#include "ui_PDFDialog.h"

PDFDialog::PDFDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::PDFDialog)
{
    ui->setupUi(this);
}

PDFDialog::~PDFDialog()
{
    delete ui;
}

void PDFDialog::on_btn_OK_clicked()
{

}

void PDFDialog::on_btn_Cancel_clicked()
{

}
