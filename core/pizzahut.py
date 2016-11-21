# -*- coding: utf-8 -*-
from modules import *


class Core(object):

    def __init__(self):
        self.config_location = os.path.join(os.getcwd(), 'core', 'configuration.ini')
        self.data_config = {}
        self.retrieve_configuration()
        self.driver = None
        self.select_driver()
        self.wait = WebDriverWait(self.driver, 30)

    def retrieve_configuration(self):
        try:
            config = ConfigParser.ConfigParser()
            config.read(self.config_location)
            for section in config.sections():
                for option in config.options(section):
                    self.data_config[option] = config.get(section, option)
        except StandardError:
            raise

    def chrome_driver(self):
        try:
            if self.data_config is not None:
                self.driver = webdriver.Chrome(self.data_config.get('chrome_driver_location'))
                width = self.driver.execute_script("return window.screen.availWidth")
                height = self.driver.execute_script("return window.screen.availHeight")
                self.driver.set_window_position(0, 0)
                self.driver.set_window_size(width, height)
        except StandardError:
            raise

    def firefox_driver(self):
        try:
            if self.data_config is not None:
                self.driver = webdriver.Firefox(self.data_config.get('firefox_driver_location'))
                self.driver.maximize_window()
        except StandardError:
            raise

    def select_driver(self):
        try:
            desired_driver = self.data_config.get('desired_browser')
            if desired_driver == "chrome":
                self.chrome_driver()
            elif desired_driver == "firefox":
                self.firefox_driver()
            else:
                print "Selected driver is not available yet."
                exit()
        except StandardError:
            raise


class RegisterPage(Core):

    def register_new_user(self):
        try:
            if self.data_config is not None:
                self.wait.until(ec.element_to_be_clickable(RegistrationLocators.LOGIN_LINK)).click()
                self.wait.until(ec.element_to_be_clickable(RegistrationLocators.NEW_MEMBERSHIP_BTN)).click()
                self.wait.until(ec.element_to_be_clickable(RegistrationLocators.MEMBER_FORM_NAME)).\
                    send_keys(self.data_config.get('user_name'))
                curr_time = time.time()
                self.wait.until(ec.element_to_be_clickable(RegistrationLocators.MEMBER_FORM_MAIL)).\
                    send_keys(str(curr_time) + self.data_config.get('user_mail_prefix'))
                self.wait.until(ec.element_to_be_clickable(RegistrationLocators.MEMBER_FORM_PHONE)).\
                    send_keys(self.data_config.get('user_phone'))
                self.wait.until(ec.element_to_be_clickable(RegistrationLocators.MEMBER_FORM_PASSWORD)).\
                    send_keys(self.data_config.get('user_password'))
                self.driver.execute_script("$('#ctl00_frmMain_chkUYE_SOZLESME_FL').click()")
                self.wait.until(ec.element_to_be_clickable(RegistrationLocators.MEMBER_FORM_CONTINUE)).click()
                self.wait.until(ec.presence_of_element_located(RegistrationLocators.DIV_INFO_SAVED))
                self.wait.until(ec.element_to_be_clickable(RegistrationLocators.GET_FROM_RESTAURANT)).click()
                time.sleep(6)
                self.driver.switch_to.frame(self.driver.find_element_by_class_name('ifrGelAl'))
                time.sleep(6)
                city_select = Select(self.driver.find_element_by_id('drpSHR_KOD'))
                city_select.select_by_visible_text(self.data_config.get('city_selection'))
                time.sleep(3)
                region_select = Select(self.driver.find_element_by_id('drpSRV_SEMT'))
                region_select.select_by_visible_text(self.data_config.get('region_selection'))
                time.sleep(1)
                self.driver.execute_script("$('.divServisListe_DepoSec a')[0].click()")
                time.sleep(3)
                self.driver.switch_to.default_content()
                time.sleep(3)
        except StandardError:
            raise


class ProductSelectionPage(Core):

    def select_product(self):
        try:
            if self.data_config is not None:
                self.wait.until(ec.element_to_be_clickable(SelectProductLocators.MENU_LIST)).click()
                self.wait.until(ec.element_to_be_clickable(SelectProductLocators.SELECT_PIZZA)).click()
                #self.wait.until(ec.element_to_be_clickable(SelectProductLocators.CHANGE_INGREDIENTS)).click()
                time.sleep(6)
                self.driver.execute_script("test = $('.malzemeDegisikligi')[1];accordion.tabClicked(test)")
                time.sleep(3)
                self.driver.execute_script("$('a[data-id=\"25814\"].addBtn').click()")
                #self.wait.until(ec.element_to_be_clickable(SelectProductLocators.ADD_TOMATOES)).click()
                self.wait.until(ec.element_to_be_clickable(SelectProductLocators.ADD_TO_CART)).click()
        except StandardError:
            raise


class ProductPurchasePage(Core):

    def purchase_product(self):
        try:
            self.driver.get("https://www.pizzahut.com.tr/sepet/sepetim.aspx")
            self.driver.execute_script("window.scrollTo(0, 300)")
            time.sleep(2)
            self.driver.execute_script("$('#rdOdmKod').click()")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, 0)")
            self.wait.until(ec.element_to_be_clickable(CartPageLocators.PAYMENT_NOTE)).\
                send_keys('Test Purchase cancel it')
            self.wait.until(ec.element_to_be_clickable(CartPageLocators.CONFIRM_ORDER)).click()
        except StandardError:
            raise