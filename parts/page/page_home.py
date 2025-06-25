from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from siui.components import SiPixLabel
from siui.components.button import SiPushButtonRefactor, SiLongPressButtonRefactor
from siui.components.option_card import SiOptionCardLinear, SiOptionCardPlane
from siui.components.page import SiPage
from siui.components.slider import SiSliderH
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.components.widgets import (
    SiDenseHContainer,
    SiDenseVContainer,
    SiLabel,
    SiLineEdit,
    SiLongPressButton,
    SiPushButton,
    SiSimpleButton,
    SiSwitch,
)
from siui.core import GlobalFont, Si, SiColor, SiGlobal, SiQuickEffect, GlobalFontSize
from siui.gui import SiFont

from config import Settings as ST

from parts.components.themed_option_card import ThemedOptionCardPlane


class MCSHomepage(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 滚动区域
        self.scroll_container = SiTitledWidgetGroup(self)
        # 整个顶部
        self.head_area = SiLabel(self)
        self.head_area.setFixedHeight(550)
        # 创建背景底图和渐变
        self.background_image = SiPixLabel(self.head_area)
        self.background_image.setFixedSize(1366, 300)
        self.background_image.setBorderRadius(6)
        self.background_image.load(f"{ST.png_dir}" + "/homepage_background.png")

        self.background_fading_transition = SiLabel(self.head_area)
        self.background_fading_transition.setGeometry(0, 100, 0, 200)
        self.background_fading_transition.setStyleSheet(
            """
            background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 {}, stop:1 {})
            """.format(SiGlobal.siui.colors["INTERFACE_BG_B"],
                       SiColor.trans(SiGlobal.siui.colors["INTERFACE_BG_B"], 0))
        )
        # 创建背景底图和渐变
        self.title = SiLabel(self.head_area)
        self.title.setGeometry(64, 0, 500, 128)
        self.title.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.title.setText("Wedding Invitation")
        self.title.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        self.title.setFont(SiFont.tokenized(GlobalFont.XL_MEDIUM))

        self.subtitle = SiLabel(self.head_area)
        self.subtitle.setGeometry(64, 72, 500, 48)
        self.subtitle.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.subtitle.setText("THE_AUTHOR_IS_A_GOOD_LOOKING_PYQT5_PROJECT_BY_UF4")
        self.subtitle.setStyleSheet("color: {}".format(SiColor.trans(SiGlobal.siui.colors["TEXT_A"], 0.9)))
        self.subtitle.setFont(SiFont.tokenized(GlobalFont.S_MEDIUM))

        self.container_for_cards = SiDenseHContainer(self.head_area)
        self.container_for_cards.move(0, 170)
        self.container_for_cards.setFixedHeight(400)
        self.container_for_cards.setAlignment(Qt.AlignCenter)
        self.container_for_cards.setSpacing(32)
        # 添加卡片
        self.option_card_project = ThemedOptionCardPlane(self)
        self.option_card_project.setTitle("GitHub Repo")
        self.option_card_project.setFixedSize(218, 270)
        self.option_card_project.setThemeColor("#855198")
        self.option_card_project.setDescription(
            "connect to my project\r\n"
            "home page.you can click\r\n"
            "btu to project page")
        self.option_card_project.setURL("https://github.com/UF4OVER/auto_excal")

        self.option_card = ThemedOptionCardPlane(self)
        self.option_card.setTitle("Bilibili")
        self.option_card.setFixedSize(218, 270)
        self.option_card.setThemeColor("#FB7299")
        self.option_card.setDescription(
            "connect to my bilibili\r\n"
            "home page.you can click\r\n"
            "btu to my page .")  # noqa: E501
        self.option_card.setURL("https://space.bilibili.com/1000215778?spm_id_from=333.1007.0.0")

        self.option_card_demo = ThemedOptionCardPlane(self)
        self.option_card_demo.setTitle("My Home Page")
        self.option_card_demo.setFixedSize(218, 270)
        self.option_card_demo.setThemeColor("#58A6FF")
        self.option_card_demo.setDescription(
            "connect to my home \r\n"
            "page.you can click\r\n"
            "btu to my page .")  # noqa: E501
        self.option_card_demo.setURL("https://uf4.top")

        self.option_card_collaborator = ThemedOptionCardPlane(self)
        self.option_card_collaborator.setTitle("TreaYang-002")
        self.option_card_collaborator.setFixedSize(218, 270)
        self.option_card_collaborator.setThemeColor("#0366D6")
        self.option_card_collaborator.setDescription(
            "connect to collaborator\r\n"
            "home page.you can click\r\n"
            "btu to page .")  # noqa: E501
        self.option_card_collaborator.setURL("https://github.com/TreaYang-002")

        # 添加到水平容器

        self.container_for_cards.addPlaceholder(64)
        self.container_for_cards.addWidget(self.option_card_project)
        self.container_for_cards.addWidget(self.option_card)
        self.container_for_cards.addWidget(self.option_card_demo)
        self.container_for_cards.addWidget(self.option_card_collaborator)

        # 添加到滚动区域容器
        self.scroll_container.addWidget(self.head_area)

        self.body_area = SiLabel(self)
        self.body_area.setSiliconWidgetFlag(Si.EnableAnimationSignals)
        self.body_area.resized.connect(lambda _: self.scroll_container.adjustSize())

        # 下面的 titledWidgetGroups
        self.titled_widget_group = SiTitledWidgetGroup(self.body_area)
        self.titled_widget_group.setSiliconWidgetFlag(Si.EnableAnimationSignals)
        self.titled_widget_group.resized.connect(lambda size: self.body_area.setFixedHeight(size[1]))
        self.titled_widget_group.move(64, 0)

        with self.titled_widget_group as group:
            group.addTitle("启动服务器")
            start_tab = SiOptionCardLinear(self)
            start_tab.setTitle("Forge 47.4.0", "minecraft:1.20.1")
            start_tab.load(SiGlobal.siui.iconpack.get("ic_fluent_keyboard_layout_float_regular"))

            start_server_btu = SiLongPressButtonRefactor(self)
            start_server_btu.setText("启动服务器")

            open_left_layer_btu = SiPushButtonRefactor(self)
            open_left_layer_btu.setText("参数选择")
            open_left_layer_btu.clicked.connect(
                lambda: SiGlobal.siui.windows["MAIN_WINDOW"].layerLeftGlobalDrawer().showLayer())

            start_tab.addWidget(start_server_btu)
            start_tab.addWidget(open_left_layer_btu)

            group.addWidget(start_tab)

        self.titled_widget_group.addPlaceholder(64)

        # 添加到滚动区域容器
        self.body_area.setFixedHeight(self.titled_widget_group.height())
        self.scroll_container.addWidget(self.body_area)

        # 添加到页面
        self.setAttachment(self.scroll_container)
        self.scroll_container.adjustSize()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        w = event.size().width()
        self.body_area.setFixedWidth(w)
        self.background_image.setFixedWidth(w)
        self.titled_widget_group.setFixedWidth(min(w - 128, 900))
        self.background_fading_transition.setFixedWidth(w)
