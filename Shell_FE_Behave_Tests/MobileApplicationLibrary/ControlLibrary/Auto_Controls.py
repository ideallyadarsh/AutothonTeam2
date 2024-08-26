from appium.webdriver.common.mobileby import MobileBy


class Auto_Controls:

    def __init__(self, driver):
        self.driver = driver

    view_tab = (MobileBy.ACCESSIBILITY_ID, "Views")
    control_tab = (MobileBy.ACCESSIBILITY_ID, "Controls")
    light_theme_tab = (MobileBy.ACCESSIBILITY_ID, "1. Light Theme")
    check_box = (MobileBy.ACCESSIBILITY_ID, "Checkbox 1")
    popup_btn = (MobileBy.ACCESSIBILITY_ID, "Make a Popup!")
    popup_menu = (MobileBy.ACCESSIBILITY_ID, "Popup Menu")
    text_swictcher = (MobileBy.ACCESSIBILITY_ID, "TextSwitcher")
    next_btn = (MobileBy.ACCESSIBILITY_ID, "Next")
    drag_and_drop = (MobileBy.ACCESSIBILITY_ID,"Drag and Drop")
    source_element = (MobileBy.ID,"io.appium.android.apis:id/drag_dot_1")
    target_element = (MobileBy.ID,"io.appium.android.apis:id/drag_dot_2")
    result_text = (MobileBy.ID,"io.appium.android.apis:id/drag_result_text")

    cancel = (MobileBy.ACCESSIBILITY_ID,"com.google.android.gms:id/cancel")
    username = (MobileBy.ACCESSIBILITY_ID,"Username, email or mobile number")
    username1 = (MobileBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.instagram.android:id/layout_container_main"]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText')
    password = (MobileBy.ACCESSIBILITY_ID,"Password")
    login = (MobileBy.XPATH,"//android.view.View[@content-desc='Log in']")
    new_post = (MobileBy.ACCESSIBILITY_ID,"Create")
    image_1 = (MobileBy.XPATH,'(//android.widget.GridView[@resource-id="com.instagram.android:id/media_picker_grid_view"]/android.view.ViewGroup)[1]')
    image_2 = (MobileBy.XPATH,'(//android.widget.GridView[@resource-id="com.instagram.android:id/media_picker_grid_view"]/android.view.ViewGroup)[2]')
    image_3 = (MobileBy.XPATH,'(//android.widget.GridView[@resource-id="com.instagram.android:id/media_picker_grid_view"]/android.view.ViewGroup)[3]')
    next = (MobileBy.ACCESSIBILITY_ID,"Next")
    caption = (MobileBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.instagram.android:id/caption_text_view"]')
    share = (MobileBy.XPATH,"//android.widget.Button[@text='Share']")

    def get_new_post(self):
        return self.driver.find_element(*Auto_Controls.new_post)
    def get_image_1(self):
        return self.driver.find_element(*Auto_Controls.image_1)
    def get_image_2(self):
        return self.driver.find_element(*Auto_Controls.image_2)
    def get_image_3(self):
        return self.driver.find_element(*Auto_Controls.image_3)
    def get_next(self):
        return self.driver.find_element(*Auto_Controls.next)
    def get_share(self):
        return self.driver.find_element(*Auto_Controls.share)
    def get_caption(self):
        return self.driver.find_element(*Auto_Controls.caption)
    
    def get_cancel(self):
        return self.driver.find_element(*Auto_Controls.cancel)
    def get_username(self):
        return self.driver.find_element(*Auto_Controls.username)
    def get_username1(self):
        return self.driver.find_element(*Auto_Controls.username1)
    def get_password(self):
        return self.driver.find_element(*Auto_Controls.password)
    def get_login(self):
        return self.driver.find_element(*Auto_Controls.login)


    def get_view_tab(self):
        return self.driver.find_element(*Auto_Controls.view_tab)

    def get_controls_view(self):
        return self.driver.find_element(*Auto_Controls.control_tab)

    def get_light_theme(self):
        return self.driver.find_element(*Auto_Controls.light_theme_tab)

    def get_checkbox(self):
        return self.driver.find_element(*Auto_Controls.check_box)

    def get_popup_menu(self):
        return self.driver.find_element(*Auto_Controls.popup_menu)

    def get_popup_btn(self):
        return self.driver.find_element(*Auto_Controls.popup_btn)

    def get_text_switcher(self):
        return self.driver.find_element(*Auto_Controls.text_swictcher)

    def get_next_btn(self):
        return self.driver.find_element(*Auto_Controls.next_btn)

    def get_drag_and_drop_tab(self):
        return self.driver.find_element(*Auto_Controls.drag_and_drop)

    def get_source_element(self):
        return self.driver.find_element(*Auto_Controls.source_element)

    def get_target_element(self):
        return self.driver.find_element(*Auto_Controls.target_element)

    def get_result_text(self):
        return self.driver.find_element(*Auto_Controls.result_text)

