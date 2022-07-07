#ifndef WATERMARKDIALOG_H
#define WATERMARKDIALOG_H

#include <QDialog>

namespace Ui {
class WatermarkDialog;
}

class WatermarkDialog : public QDialog
{
    Q_OBJECT

public:
    explicit WatermarkDialog(QWidget *parent = nullptr);
    ~WatermarkDialog();

private slots:
    void on_colorComboBox_currentIndexChanged(const QString &arg1);

private:
    Ui::WatermarkDialog *ui;
};

#endif // WATERMARKDIALOG_H
