# coding:utf-8
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPixmap, QPainter, QColor, QBrush, QPainterPath
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from qfluentwidgets import ScrollArea, isDarkTheme, FluentIcon
from ..common.config import cfg, HELP_URL, REPO_URL, EXAMPLE_URL, FEEDBACK_URL
from ..common.icon import Icon, FluentIconBase
from ..components.link_card import LinkCardView
from ..components.sample_card import SampleCardView
from ..common.style_sheet import StyleSheet


class BannerWidget(QWidget):
    """ Banner widget """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedHeight(336)
        self.vBoxLayout = QVBoxLayout(self)
        self.galleryLabel = QLabel('python-office', self)
        self.banner = QPixmap(':/gallery/images/header1.png')
        self.linkCardView = LinkCardView(self)

        self.galleryLabel.setObjectName('galleryLabel')

        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(0, 20, 0, 0)
        self.vBoxLayout.addWidget(self.galleryLabel)
        self.vBoxLayout.addWidget(self.linkCardView, 1, Qt.AlignBottom)
        self.vBoxLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.linkCardView.addCard(
            ':/gallery/images/logo.png',
            self.tr('官网'),
            self.tr('An overview of app development options and samples.'),
            HELP_URL
        )

        self.linkCardView.addCard(
            FluentIcon.GITHUB,
            self.tr('源代码'),
            self.tr(
                'The latest fluent design controls and styles for your applications.'),
            REPO_URL
        )

        self.linkCardView.addCard(
            FluentIcon.CODE,
            self.tr('案例'),
            self.tr(
                'Find samples that demonstrate specific tasks, features and APIs.'),
            EXAMPLE_URL
        )

        self.linkCardView.addCard(
            FluentIcon.FEEDBACK,
            self.tr('反馈'),
            self.tr('Help us improve PyQt-Fluent-Widgets by providing feedback.'),
            FEEDBACK_URL
        )

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHints(
            QPainter.SmoothPixmapTransform | QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        w, h = self.width(), 200
        path.addRoundedRect(QRectF(0, 0, w, h), 10, 10)
        path.addRect(QRectF(0, h-50, 50, 50))
        path.addRect(QRectF(w-50, 0, 50, 50))
        path.addRect(QRectF(w-50, h-50, 50, 50))
        path = path.simplified()

        # draw background color
        painter.fillPath(path, QColor(206, 216, 228))

        # draw banner image
        pixmap = self.banner.scaled(
            self.size(), transformMode=Qt.SmoothTransformation)
        path.addRect(QRectF(0, h, w, self.height() - h))
        painter.fillPath(path, QBrush(pixmap))


class HomeInterface(ScrollArea):
    """ Home interface """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.banner = BannerWidget(self)
        self.view = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.view)

        self.__initWidget()
        self.loadSamples()

    def __initWidget(self):
        self.view.setObjectName('view')
        StyleSheet.HOME_INTERFACE.apply(self)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 36)
        self.vBoxLayout.setSpacing(40)
        self.vBoxLayout.addWidget(self.banner)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

    def loadSamples(self):
        """ load samples """
        # basic input samples
        basicInputView = SampleCardView(
            self.tr("自动化办公 - 功能分类"), self.view)
        basicInputView.addSampleCard(
            icon=":/gallery/images/controls/Button.png",
            title="Button",
            content=self.tr(
                "A control that responds to user input and emit clicked signal."),
            routeKey="basicInputInterface",
            index=0
        )
        basicInputView.addSampleCard(
            icon=":/gallery/images/controls/Checkbox.png",
            title="CheckBox",
            content=self.tr("A control that a user can select or clear."),
            routeKey="basicInputInterface",
            index=4
        )
        basicInputView.addSampleCard(
            icon=":/gallery/images/controls/ComboBox.png",
            title="ComboBox",
            content=self.tr(
                "A drop-down list of items a user can select from."),
            routeKey="basicInputInterface",
            index=6
        )
        basicInputView.addSampleCard(
            icon=":/gallery/images/controls/RadioButton.png",
            title="RadioButton",
            content=self.tr(
                "A control that allows a user to select a single option from a group of options."),
            routeKey="basicInputInterface",
            index=7
        )
        basicInputView.addSampleCard(
            icon=":/gallery/images/controls/Slider.png",
            title="Slider",
            content=self.tr(
                "A control that lets the user select from a range of values by moving a Thumb control along a track."),
            routeKey="basicInputInterface",
            index=8
        )
        basicInputView.addSampleCard(
            icon=":/gallery/images/controls/ToggleSwitch.png",
            title="SwitchButton",
            content=self.tr(
                "A switch that can be toggled between 2 states."),
            routeKey="basicInputInterface",
            index=9
        )
        self.vBoxLayout.addWidget(basicInputView)

        # date time samples
        dateTimeView = SampleCardView(self.tr('Dialog samples'), self.view)
        dateTimeView.addSampleCard(
            icon=":/gallery/images/controls/DatePicker.png",
            title="DatePicker",
            content=self.tr("A control that lets a user pick a date value."),
            routeKey="dateTimeInterface",
            index=0
        )
        dateTimeView.addSampleCard(
            icon=":/gallery/images/controls/TimePicker.png",
            title="TimePicker",
            content=self.tr(
                "A configurable control that lets a user pick a time value."),
            routeKey="dateTimeInterface",
            index=2
        )
        self.vBoxLayout.addWidget(dateTimeView)

        # dialog samples
        dialogView = SampleCardView(self.tr('Dialog samples'), self.view)
        dialogView.addSampleCard(
            icon=":/gallery/images/controls/Flyout.png",
            title="Dialog",
            content=self.tr("A frameless message dialog."),
            routeKey="dialogInterface",
            index=0
        )
        dialogView.addSampleCard(
            icon=":/gallery/images/controls/ContentDialog.png",
            title="MessageBox",
            content=self.tr("A message dialog with mask."),
            routeKey="dialogInterface",
            index=1
        )
        dialogView.addSampleCard(
            icon=":/gallery/images/controls/ColorPicker.png",
            title="ColorDialog",
            content=self.tr("A dialog that allows user to select color."),
            routeKey="dialogInterface",
            index=2
        )
        self.vBoxLayout.addWidget(dialogView)

        # layout samples
        layoutView = SampleCardView(self.tr('Layout samples'), self.view)
        layoutView.addSampleCard(
            icon=":/gallery/images/controls/Grid.png",
            title="FlowLayout",
            content=self.tr(
                "A layout arranges components in a left-to-right flow, wrapping to the next row when the current row is full."),
            routeKey="layoutInterface",
            index=0
        )
        self.vBoxLayout.addWidget(layoutView)

        # material samples
        materialView = SampleCardView(self.tr('Material samples'), self.view)
        materialView.addSampleCard(
            icon=":/gallery/images/controls/Acrylic.png",
            title="AcrylicLabel",
            content=self.tr(
                "A translucent material recommended for panel background."),
            routeKey="materialInterface",
            index=0
        )
        self.vBoxLayout.addWidget(materialView)

        # menu samples
        menuView = SampleCardView(self.tr('Menu samples'), self.view)
        menuView.addSampleCard(
            icon=":/gallery/images/controls/MenuFlyout.png",
            title="RoundMenu",
            content=self.tr(
                "Shows a contextual list of simple commands or options."),
            routeKey="menuInterface",
            index=0
        )
        self.vBoxLayout.addWidget(menuView)

        # scroll samples
        scrollView = SampleCardView(self.tr('Scrolling samples'), self.view)
        scrollView.addSampleCard(
            icon=":/gallery/images/controls/ScrollViewer.png",
            title="ScrollArea",
            content=self.tr(
                "A container control that lets the user pan and zoom its content smoothly."),
            routeKey="scrollInterface",
            index=0
        )
        self.vBoxLayout.addWidget(scrollView)

        # state info samples
        stateInfoView = SampleCardView(self.tr('Scrolling samples'), self.view)
        stateInfoView.addSampleCard(
            icon=":/gallery/images/controls/ProgressRing.png",
            title="StateToolTip",
            content=self.tr(
                "Shows the apps progress on a task,or that the app is performing ongoing work that does block user interaction."),
            routeKey="statusInfoInterface",
            index=0
        )
        stateInfoView.addSampleCard(
            icon=":/gallery/images/controls/ToolTip.png",
            title="ToolTip",
            content=self.tr(
                "Displays information for an element in a pop-up window."),
            routeKey="statusInfoInterface",
            index=1
        )
        stateInfoView.addSampleCard(
            icon=":/gallery/images/controls/InfoBar.png",
            title="InfoBar",
            content=self.tr(
                "An inline message to display app-wide status change information."),
            routeKey="statusInfoInterface",
            index=3
        )
        self.vBoxLayout.addWidget(stateInfoView)

        # text samples
        textView = SampleCardView(self.tr('Text samples'), self.view)
        textView.addSampleCard(
            icon=":/gallery/images/controls/TextBox.png",
            title="LineEdit",
            content=self.tr("A single-line plain text field."),
            routeKey="textInterface",
            index=0
        )
        textView.addSampleCard(
            icon=":/gallery/images/controls/NumberBox.png",
            title="SpinBox",
            content=self.tr(
                "A text control used for numeric input and evaluation of algebraic equations."),
            routeKey="textInterface",
            index=1
        )
        textView.addSampleCard(
            icon=":/gallery/images/controls/RichEditBox.png",
            title="TextEdit",
            content=self.tr(
                "A rich text editing control that supports formatted text, hyperlinks, and other rich content."),
            routeKey="textInterface",
            index=6
        )
        self.vBoxLayout.addWidget(textView)

        # view samples
        collectionView = SampleCardView(self.tr('View samples'), self.view)
        collectionView.addSampleCard(
            icon=":/gallery/images/controls/TreeView.png",
            title="TreeView",
            content=self.tr(
                "The TreeView control is a hierarchical list pattern with expanding and collapsing nodes that contain nested items."),
            routeKey="viewInterface",
            index=0
        )
        self.vBoxLayout.addWidget(collectionView)
