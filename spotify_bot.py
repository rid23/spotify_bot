import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from password_generator import PasswordGenerator
from captcha import solve2


class spotify:
    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver")
        self.pass_generator = PasswordGenerator()
        self.pass_generator.minlength = 10


    def account(self,data_list):

        mail,name,gender,DOB,passwd = data_list[0],data_list[1],data_list[2],data_list[3],self.pass_generator.generate() 
        
        self.driver.get('https://spotify.com/in-en/signup')
        wait_till_page_load = WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH,"(//div[@class='LabelGroup-sc-1ibddrg-0 biNheR'])[1]")))

        email = self.driver.find_element_by_id('email')
        sleep(0.5)
        email.send_keys(mail)
        
        confirm_mail = self.driver.find_element_by_id('confirm')
        sleep(0.5)
        confirm_mail.send_keys(mail)

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        dname = self.driver.find_element_by_id('displayname')
        sleep(0.5)
        dname.send_keys(name)

        password = self.driver.find_element_by_xpath("//input[@type='password']")
        sleep(0.5)
        password.send_keys(passwd)


        #date OF birth ------------------------------------------------
        
        yr = self.driver.find_element_by_xpath("//input[@id='year']")
        day = self.driver.find_element_by_xpath("//input[@id='day']")
        
        #SPLITTING THE DOB (yyyy/mm/dd)
        dob_list = DOB.split('/')
        month = dob_list.pop(1)
        dob_web_elements = [yr,day]

        for i in range(2):
            dob_web_elements[i].send_keys(dob_list[i])
            sleep(1)

        month_element = self.driver.find_element_by_xpath("//select[@id='month']//option[@value='09']")
        sleep(0.5)
        month_element.click()
        if gender == "M":
            male = self.driver.find_element_by_xpath("(//span[@class='Indicator-hjfusp-0 kLhpUW'])[1]")
            male.click()
        if gender == "F":
            female = self.driver.find_element_by_xpath("(//span[@class='Indicator-hjfusp-0 kLhpUW'])[2]")
            female.click()

        checker1 = self.driver.find_element_by_xpath("(//span[@class='Indicator-sc-1airx73-0 hmDuGC'])[1]")
        checker2 = self.driver.find_element_by_xpath("(//span[@class='Indicator-sc-1airx73-0 hmDuGC'])[2]")
        checker1.click()
        checker2.click()


        recap = self.driver.find_element_by_xpath("//iframe[@title='reCAPTCHA']")
        url = recap.get_attribute('src')

        try:
            solved = solve2(url)
            #print(solved)
            self.driver.execute_script(f'document.getElementById("g-recaptcha-response").textContent="{solved}";')
        except:
            pass
        sleep(1)

        sign_up = self.driver.find_element_by_xpath("//div[@class='ButtonInner-sc-14ud5tc-0 flmFpd encore-bright-accent-set SignupButton___StyledButtonPrimary-cjcq5h-1 gzFCtx']")
        sign_up.click()

        sleep(1)


    def main():

        data_file = open("./user_data.txt",'r')
        data_ = data_file.readlines()

        for row in data_:
            user = spotify()
            password_ = user.pass_generator.generate()
            print(password_)

            data_list = row.split(",")
            data_list.append(password_)

            user.account(data_list)


        #--------------------------------------------------------------





if __name__ == '__main__':

    spotify.main()
