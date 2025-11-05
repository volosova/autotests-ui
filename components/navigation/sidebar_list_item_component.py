from playwright.sync_api import Page, expect
from typing_extensions import Pattern

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.button import Button
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.icon = Icon(page, '{identifier}-drawer-list-item-icon', 'Icon')
        self.title = Text(page, '{identifier}-drawer-list-item-title-text', 'Title')
        self.button = Button(page, '{identifier}-drawer-list-item-button', 'Button')

    def check_visible(self, title: str, identifier: str):
        self.icon.check_visible(identifier=identifier)

        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(title, identifier=identifier)

        self.button.check_visible(identifier=identifier)

    def navigate(self, expected_url: Pattern):
        self.button.click()
        self.check_current_url(expected_url)