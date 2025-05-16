class BrowserHistory:
    def __init__(self):
        self.back_stack = [] 
        self.forward_stack = []  
        self.current_page = None

    def visit(self, url):
        if self.current_page:
            self.back_stack.append(self.current_page)

        self.current_page = url
        self.forward_stack = []  

        return f"Visited: {url}"

    def back(self):
        if not self.back_stack:
            return "No back history"

        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()

        return f"Navigated back to: {self.current_page}"

    def forward(self):
        if not self.forward_stack:
            return "No forward history"

        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()

        return f"Navigated forward to: {self.current_page}"

    def get_current(self):
        if not self.current_page:
            return "No current page"

        return f"Current page: {self.current_page}"


def test_browser_history():
    print("Testing browser navigation:")
    browser = BrowserHistory()

    print(browser.get_current())

    print(browser.visit("https://www.example.com"))
    print(browser.visit("https://www.example.com/page1"))
    print(browser.visit("https://www.example.com/page2"))

    print(browser.get_current())
    print(browser.back())
    print(browser.back())
    print(browser.forward())

    print(browser.visit("https://www.example.com/page3"))
    print(browser.get_current())

    print(browser.forward())

    print(browser.back())
    print(browser.back())
    print(browser.back())  

    print("All browser history tests completed successfully!")


if __name__ == "__main__":
    test_browser_history()
