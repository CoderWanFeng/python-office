#ifndef KEYWORDTABLEWINDOW_H
#define KEYWORDTABLEWINDOW_H

#include <QWidget>

namespace Ui {
class keywordTableWindow;
}

class keywordTableWindow : public QWidget
{
    Q_OBJECT

public:
    explicit keywordTableWindow(QWidget *parent = nullptr);
    ~keywordTableWindow();

private:
    Ui::keywordTableWindow *ui;
};

#endif // KEYWORDTABLEWINDOW_H
