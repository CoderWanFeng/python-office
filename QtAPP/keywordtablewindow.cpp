#include "keywordtablewindow.h"
#include "ui_keywordtablewindow.h"

keywordTableWindow::keywordTableWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::keywordTableWindow)
{
    ui->setupUi(this);
}

keywordTableWindow::~keywordTableWindow()
{
    delete ui;
}
