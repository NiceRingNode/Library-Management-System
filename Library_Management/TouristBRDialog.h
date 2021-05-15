#ifndef TOURISTBRDIALOG_H
#define TOURISTBRDIALOG_H

#include <QDialog>

namespace Ui {
class TouristBRDialog;
}

class TouristBRDialog : public QDialog
{
    Q_OBJECT

public:
    explicit TouristBRDialog(QWidget *parent = nullptr);
    ~TouristBRDialog();

private slots:
    void on_OK_clicked();

    void on_Cancel_clicked();

    void on_tourist_info_cellActivated(int row, int column);

    void on_tourist_info_cellChanged(int row, int column);

private:
    Ui::TouristBRDialog *ui;
};

#endif // TOURISTBRDIALOG_H
