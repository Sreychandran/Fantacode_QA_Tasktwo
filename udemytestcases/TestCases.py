import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


options = uc.ChromeOptions()
options.headless = False
options.add_argument("--disabled-gpu")
driver = uc.Chrome(options=options)
actions = ActionChains(driver)
driver.implicitly_wait(10)


class TestCases:
    def test_case_one(self):
        driver.get("https://www.google.com/")
        actualUrl = driver.current_url
        expectedUrl = "https://www.google.com/"
        assert actualUrl == expectedUrl

    def test_case_two(self):
        driver.find_element(By.ID, "APjFqb").send_keys("Test Automation Learning")
        actions.send_keys(Keys.ENTER).perform()
        actualValue = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").get_attribute("value")
        expectedValue = "Test Automation Learning"
        assert actualValue == expectedValue

    def test_case_three(self):
        udemyUrl = driver.find_element(By.XPATH,
                                       "//a[@href='https://www.udemy.com/topic/automation-testing/']//div["
                                       "@class='notranslate HGLrXd NJjxre iUh30 ojE3Fb']//div[@class='q0vns']//div["
                                       "@class='CA5RN']//div[@class='byrV5b']//cite[@role='text']")
        udemyUrl.click()
        actualUrl = driver.current_url
        expectedUrl = "https://www.udemy.com/topic/automation-testing/"
        assert actualUrl == expectedUrl

    def test_case_four(self):
        udemySearchBox = driver.find_element(By.NAME, "q")
        udemySearchBox.send_keys("BDD with cucumber")
        udemySearchBtn = driver.find_element(By.XPATH, "//button[@type='submit']")
        udemySearchBtn.click()
        actualLabel = driver.find_element(By.XPATH, "//span[normalize-space()='Udemy Business']").text
        expectedLabel = "Udemy Business"
        assert actualLabel == expectedLabel

    def test_case_five(self):
        sortBox = driver.find_element(By.XPATH, "//div[@class='ud-select-container ud-select-container-large']")
        sortBox.click()
        sortValues = driver.find_element(By.NAME, "sort")
        rating = Select(sortValues)
        rating.select_by_visible_text("Highest Rated")
        sortText = sortBox.text
        expectedText = "Most Relevant\nMost Reviewed\nHighest Rated\nNewest"
        assert sortText == expectedText

    def test_case_six(self):
        time.sleep(5)
        course = driver.find_element(By.XPATH, "//a[contains(text(),'Cucumber 7.0 BDD for')]")
        course.click()

    def test_case_seven(self):
        courseTitle = driver.find_element(By.XPATH, "//h1[contains(text(),'Cucumber 7.0 BDD for')]").text
        expectedCourseName = "Cucumber 7.0 BDD for Selenium & Appium with Live Projects"
        assert courseTitle == expectedCourseName
