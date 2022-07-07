echo off


copy ..\QtApp\widget.ui  ..\customizeWindowUIfile\widget.ui
pyuic5 -o ..\customizeWindowPyfile\ui2pyFile\ui_Widget.py  ..\customizeWindowUIfile\widget.ui



