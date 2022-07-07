#ifndef PASSWORDDIALOG_H
#define PASSWORDDIALOG_H

#include <QDialog>

namespace Ui {
class passwordDialog;
}

class passwordDialog : public QDialog
{
    Q_OBJECT

public:
    explicit passwordDialog(QWidget *parent = nullptr);
    ~passwordDialog();

private:
    Ui::passwordDialog *ui;
};

#endif // PASSWORDDIALOG_H
