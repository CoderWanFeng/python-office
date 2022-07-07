#ifndef FILLKEYWORD_H
#define FILLKEYWORD_H

#include <QWidget>

namespace Ui {
class fillKeyword;
}

class fillKeyword : public QWidget
{
    Q_OBJECT

public:
    explicit fillKeyword(QWidget *parent = nullptr);
    ~fillKeyword();

private:
    Ui::fillKeyword *ui;
};

#endif // FILLKEYWORD_H
