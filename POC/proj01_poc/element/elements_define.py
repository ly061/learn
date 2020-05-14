from selenium.webdriver.common.by import By

class ElementsDefine(object):
    """
    Test Esacpe Element Define
    """

    def __init__(self):
        """
        init function
        """
        # homepage
        self.hompage_navigation = By.CLASS_NAME, "nae-nav-link"