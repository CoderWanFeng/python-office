#include "passworddialog.h"
#include "ui_passworddialog.h"

passwordDialog::passwordDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::passwordDialog)
{
    ui->setupUi(this);
}

passwordDialog::~passwordDialog()
{
    delete ui;
}
