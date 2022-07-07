echo off


copy ..\QtApp\keywordtablewindow.ui  ..\customizeWindowUIfile\keywordtablewindow.ui
pyuic5 -o ..\customizeWindowPyfile\ui2pyFile\ui_keywordtablewindow.py  ..\customizeWindowUIfile\keywordtablewindow.ui