echo off


copy ..\QtApp\passworddialog.ui  ..\customizeWindowUIfile\passworddialog.ui
pyuic5 -o ..\customizeWindowPyfile\ui2pyFile\ui_passworddialog.py  ..\customizeWindowUIfile\passworddialog.ui


rem pyrcc5 .\QtApp\res.qrc -o res_rc.py