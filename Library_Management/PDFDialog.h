#ifndef PDFDIALOG_H
#define PDFDIALOG_H

#include <QDialog>

namespace Ui {
class PDFDialog;
}

class PDFDialog : public QDialog
{
    Q_OBJECT

public:
    explicit PDFDialog(QWidget *parent = nullptr);
    ~PDFDialog();

private slots:
    void on_pushButton_clicked();

    void on_btn_OK_clicked();

    void on_btn_Cancel_clicked();

private:
    Ui::PDFDialog *ui;
};

#endif // PDFDIALOG_H
