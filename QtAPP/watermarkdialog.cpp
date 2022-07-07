#include "watermarkdialog.h"
#include "ui_watermarkdialog.h"

WatermarkDialog::WatermarkDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::WatermarkDialog)
{
    ui->setupUi(this);
}

WatermarkDialog::~WatermarkDialog()
{
    delete ui;
}

void WatermarkDialog::on_colorComboBox_currentIndexChanged(const QString &arg1)
{

}
