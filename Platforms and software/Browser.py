import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window with tabs
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.tabs.currentChanged.connect(self.update_url_bar)

        # Set tabs as the central widget
        self.setCentralWidget(self.tabs)

        # Set window properties
        self.setWindowTitle("Hitarth's browser")
        self.setGeometry(200, 200, 1200, 800)

        # Navigation bar
        nav_bar = QToolBar()
        self.addToolBar(nav_bar)

        # Back button
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.navigate_back)
        nav_bar.addAction(back_btn)

        # Reload button
        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.reload_page)
        nav_bar.addAction(reload_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_bar.addWidget(self.url_bar)

        # New Tab button
        new_tab_btn = QAction("New Tab", self)
        new_tab_btn.triggered.connect(self.add_new_tab)
        nav_bar.addAction(new_tab_btn)

        # Add the initial tab
        self.add_new_tab(QUrl("https://www.google.com"))

    def add_new_tab(self, qurl=None, label="New Tab"):
        if qurl is None:
            qurl = QUrl("https://www.google.com")

        # Create a new QWebEngineView instance
        browser = QWebEngineView()
        browser.setUrl(qurl)

        # Add the new tab
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        # Update URL when it changes
        browser.urlChanged.connect(lambda q, browser=browser: self.update_url_bar(q, browser))
        browser.loadFinished.connect(lambda _, i=i, browser=browser: self.tabs.setTabText(i, browser.page().title()))

    def close_current_tab(self, i):
        if self.tabs.count() > 1:
            self.tabs.removeTab(i)

    def navigate_back(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.back()

    def reload_page(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.reload()

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.setUrl(QUrl(url))

    def update_url_bar(self, q, browser=None):
        if browser == self.tabs.currentWidget():
            self.url_bar.setText(q.toString())
            self.url_bar.setCursorPosition(0)


app = QApplication(sys.argv)
QApplication.setApplicationName("Simple Browser with Tabs")
window = Browser()
window.show()
sys.exit(app.exec_())
