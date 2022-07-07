#include "fillkeyword.h"
#include "ui_fillkeyword.h"

fillKeyword::fillKeyword(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::fillKeyword)
{
    ui->setupUi(this);
}

fillKeyword::~fillKeyword()
{
    delete ui;
}
