#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_chooseButtonWord2PDF_clicked();

    void on_convertButtonWord2PDF_clicked();

    void on_convertButtonPPT2PDF_clicked();

    void on_chooseButtonPPT2PDF_clicked();

    void on_chooseButtonImageExtract_clicked();

    void on_ExtractButton_clicked();

    void on_chooseButtonFileClassification_clicked();

    void on_classificationButton_clicked();

    void on_chooseDuplicateFileButton_clicked();

    void on_duplicateFileButton_clicked();

    void on_choosePathEncryption_clicked();

    void on_encryptionButton_clicked();

    void on_choosePathDecryption_clicked();

    void on_DecryptionButton_clicked();

    void on_chooseButtonKeywordReplace_clicked();

    void on_adjustButtonKeyword_clicked();

    void on_choosePathAddWatermarkButton_clicked();

    void on_addWatermarkButton_clicked();

private:
    Ui::Widget *ui;
};

#endif // WIDGET_H
