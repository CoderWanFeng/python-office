echo off


copy ..\QtApp\watermarkDialog.ui  ..\customizeWindowUIfile\watermarkDialog.ui
pyuic5 -o ..\customizeWindowPyfile\ui2pyFile\ui_watermarkDialog.py  ..\customizeWindowUIfile\watermarkDialog.ui