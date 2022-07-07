#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_chooseButtonWord2PDF_clicked()
{

}

void Widget::on_convertButtonWord2PDF_clicked()
{

}

void Widget::on_convertButtonPPT2PDF_clicked()
{

}

void Widget::on_chooseButtonPPT2PDF_clicked()
{

}

void Widget::on_chooseButtonImageExtract_clicked()
{

}

void Widget::on_ExtractButton_clicked()
{

}

void Widget::on_chooseButtonFileClassification_clicked()
{

}

void Widget::on_classificationButton_clicked()
{

}

void Widget::on_chooseDuplicateFileButton_clicked()
{

}

void Widget::on_duplicateFileButton_clicked()
{

}

void Widget::on_choosePathEncryption_clicked()
{

}

void Widget::on_encryptionButton_clicked()
{

}

void Widget::on_choosePathDecryption_clicked()
{

}

void Widget::on_DecryptionButton_clicked()
{

}

void Widget::on_chooseButtonKeywordReplace_clicked()
{

}

void Widget::on_adjustButtonKeyword_clicked()
{

}

void Widget::on_choosePathAddWatermarkButton_clicked()
{

}

void Widget::on_addWatermarkButton_clicked()
{

}
