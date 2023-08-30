
class BasePage:
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def element_is_visible(self, locator, timeout=10):
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def open(self):
        self.browser.get(self.url)





