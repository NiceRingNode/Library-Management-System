#ifndef PDFWIDGET_H
#define PDFWIDGET_H

#include <QWidget>

namespace Ui {
class PDFWidget;
}

class PDFWidget : public QWidget
{
    Q_OBJECT

public:
    explicit PDFWidget(QWidget *parent = nullptr);
    ~PDFWidget();

private:
    Ui::PDFWidget *ui;
};

#endif // PDFWIDGET_H
