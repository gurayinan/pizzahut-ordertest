from core.pizzahut import *


class PizzaHutPurchaseTest(unittest.TestCase, RegisterPage, ProductSelectionPage, ProductPurchasePage):

    def setUp(self):
        RegisterPage.__init__(self)
        self.driver.get("http://www.pizzahut.com.tr")

    def test_main(self):
        self.register_new_user()
        self.select_product()
        self.purchase_product()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()