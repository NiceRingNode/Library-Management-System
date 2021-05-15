#ifndef TOURISTBORROWWIDGET_H
#define TOURISTBORROWWIDGET_H

#include <QWidget>

namespace Ui {
class TouristBorrowWidget;
}

class TouristBorrowWidget : public QWidget
{
    Q_OBJECT

public:
    explicit TouristBorrowWidget(QWidget *parent = nullptr);
    ~TouristBorrowWidget();

private:
    Ui::TouristBorrowWidget *ui;
};

#endif // TOURISTBORROWWIDGET_H
