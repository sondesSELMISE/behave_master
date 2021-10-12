from selenium.webdriver import ActionChains

from Browser import Browser


objectToDrag="draggable"
objectToDrop="droppable"
x= 280
y = 16
class drag_drop(Browser):

    def drag(self):
        drag1 = self.driver.find_element_by_id(objectToDrag)
        drop1 = self.driver.find_element_by_id(objectToDrop)

        action = ActionChains(self.driver)
        action.drag_and_drop(drag1, drop1).perform()
    def message(self):

        msg = self.driver.find_element_by_id('droppable').text
        return (msg)

    def setup(self,link):
        self.driver.get(link)


    def slide(self):
        slider = self.driver.find_element_by_xpath("//body/form[@id='form1']/fieldset[@id='regform']/div[1]/div[5]/input[1]")
        ActionChains(self.driver).drag_and_drop_by_offset(slider, x, y).perform()

    def msg_slide (self):
        ms = self.driver.find_element_by_id("range").text
        return (ms)
