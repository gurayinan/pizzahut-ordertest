from selenium.webdriver.common.by import By


class RegistrationLocators(object):
    LOGIN_LINK = (By.CLASS_NAME, "loginMember")
    NEW_MEMBERSHIP_BTN = (By.CLASS_NAME, "newLoginBtn")
    MEMBER_FORM_NAME = (By.ID, "ctl00_frmMain_txtYeniUyelikAdSoyad")
    MEMBER_FORM_MAIL = (By.ID, "ctl00_frmMain_txtYeniUyelikEmail")
    MEMBER_FORM_PHONE = (By.ID, "ctl00_frmMain_txtYeniUyelikTelefon")
    MEMBER_FORM_PASSWORD = (By.ID, "ctl00_frmMain_txtYeniUyelikSifre")
    MEMBER_FORM_CONTINUE = (By.ID, "ctl00_frmMain_lbfYeniUyelikSave")
    DIV_INFO_SAVED = (By.CLASS_NAME, "dvSuccess")
    GET_FROM_RESTAURANT = (By.ID, "ctl00_frmMain_lbfAccountGelAl")
    SELECT_CITY = (By.ID, "drpSHR_KOD")
    SELECT_REGION = (By.ID, "drpSRV_SEMT")


class SelectProductLocators(object):
    MENU_LIST = (By.CLASS_NAME, "menuLink")
    SELECT_PIZZA = (By.CSS_SELECTOR, "#prd130821 > div.listInner > div.addLink > a:nth-child(1)")
    CHANGE_INGREDIENTS = (By.CLASS_NAME, "malzemeDegisikligi")
    ADD_TOMATOES = (By.CSS_SELECTOR, 'a[data-id="25814"].addBtn')
    ADD_TO_CART = (By.CLASS_NAME, "addToCart")


class CartPageLocators(object):
    CASH_PAYMENT_TYPE = (By.ID, "rdOdmKod")
    CONFIRM_ORDER = (By.ID, "ctl00_u20_ascSepetSiparisOnay_btnSepetSiparisOnayla")
    PAYMENT_NOTE = (By.ID, "ctl00_u20_ascSepetSiparisOnay_txtSIP_ODEMENOTU")