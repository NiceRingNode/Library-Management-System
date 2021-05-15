#include "TouristBRDialog.h"
#include "ui_TouristBRDialog.h"

TouristBRDialog::TouristBRDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::TouristBRDialog)
{
    ui->setupUi(this);
}

TouristBRDialog::~TouristBRDialog()
{
    delete ui;
}

void TouristBRDialog::on_OK_clicked()
{

}

void TouristBRDialog::on_Cancel_clicked()
{

}

void TouristBRDialog::on_tourist_info_cellActivated(int row, int column)
{

}

void TouristBRDialog::on_tourist_info_cellChanged(int row, int column)
{

}
