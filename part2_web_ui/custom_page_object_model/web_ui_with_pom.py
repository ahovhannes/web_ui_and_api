#
# Author: Hovhannes Atoyan (hovhannes.atoyan@gmail.com)
#
# Validate the HTML presentation layer is correctly displaying the information returned from the api, for given userid
# https://github.com/{userid}
#
import time
import json
import datetime
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class myTestCase(unittest.TestCase):
    def setUp(self):
        self.site_url = 'https://github.com/'
        self.testUserInfo = ''
        #
        self.userNameNickname = '//div[@class="vcard-names-container float-left col-12 py-3 js-sticky js-user-profile-sticky-fields"]/h1'
        self.userLocation = '//span[@class="p-label"]'
        self.userOverviewReposProjPackages = '//a[@class="UnderlineNav-item"]'
        self.userFollowersFollowingStars = '//a[@class="Link--secondary no-underline no-wrap"]'
        # self.userCompany = ''
        # self.userPublicGists = ''
        #
        # FOR WINDOWS
        # #self.driver = webdriver.Firefox()
        # firefox_binary = FirefoxBinary("D:\Programs\Portables\__Browsers\FirefoxPortable_45.0.2\FirefoxPortable.exe")
        # self.driver = webdriver.Firefox(firefox_binary=firefox_binary)
        #
        # FOR LINUX or MAC
        path = '/usr/local/bin/geckodriver'
        profile = webdriver.FirefoxProfile()
        self.driver = webdriver.Firefox(executable_path=path, firefox_profile=profile)
        #self.driver.get(self.site_url)
        #print(self.driver.title)

    def tearDown(self):
        self.driver.close()


    def test_cases(self):
        self.testUserInfo = self.get_user_info_from_file()
        print()
        userId = self.testUserInfo["userid"]
        print('... Detected userId='+userId)
        self.site_url = self.site_url + userId
        print('... self.site_url='+self.site_url)
        #
        print("..... Opening the site "+self.site_url+" .....")
        self.driver.get(self.site_url)
        print("\n..... Executing Test-Cases .....\n")
        self.tc1('Checking if user info appears on the page')
        # self.tc2('Second test-case')

    # This function takes user info from the file
    def get_user_info_from_file(self):
        fileName = 'testuser.json'
        fileName = 'testuser.txt'
        print('... Get user info from the file '+fileName)
        f = open(fileName)
        data = json.load(f)
        # self.testUserInfo = data
        for i in data:
            print(str(i) +'='+ str(data[i]))
        f.close()
        return data


    def tc1(self, testCaseName):
        print("----- Begin TestCase: "+testCaseName+" -----")
        print('... Expected user infos are:')
        expected_name = self.testUserInfo["name"]
        expected_company = self.testUserInfo["company"]
        expected_location = self.testUserInfo["location"]
        expected_public_repos = str(self.testUserInfo["public_repos"])
        expected_public_gists = str(self.testUserInfo["public_gists"])
        expected_followers = str(self.testUserInfo["followers"])
        expected_following = str(self.testUserInfo["following"])
        print('name='+expected_name)
        print('company='+expected_company)
        print('location='+expected_location)
        print('public_repos='+str(expected_public_repos))
        print('public_gists='+str(expected_public_gists))
        print('followers='+str(expected_followers))
        print('following='+str(expected_following))

        print('... Detecting actual values from the web page:')
        userNameNicknameH1 = self.driver.find_element_by_xpath(self.userNameNickname)
        userNameNickname = userNameNicknameH1.find_elements_by_xpath(".//span")
        userName = userNameNickname[0].text
        print('Actual userName=' +str(userName))
        #
        userLocation_el = self.driver.find_element_by_xpath(self.userLocation)
        userLocation = userLocation_el.text
        print('Actual userLocation=' +str(userLocation))
        #
        userOverviewReposProjPackages = self.driver.find_elements_by_xpath(self.userOverviewReposProjPackages)
        userPublicRepos_el = userOverviewReposProjPackages[0]
        public_repos = userPublicRepos_el.find_element_by_xpath(".//span").text
        print('Actual public_repos=' +str(public_repos))
        #
        userFollowersFollowingStars = self.driver.find_elements_by_xpath(self.userFollowersFollowingStars)
        userFollowers_el = userFollowersFollowingStars[0]
        userFollowing_el = userFollowersFollowingStars[1]
        userStars_el = userFollowersFollowingStars[2]
        followers = userFollowers_el.find_element_by_xpath(".//span").text
        following = userFollowing_el.find_element_by_xpath(".//span").text
        print('Actual followers=' +str(followers))
        print('Actual following=' +str(following))

        # Checking
        assert expected_name == userName, "***** ERROR: Expected value for 'name' is: "+str(expected_name)+", but actual result is: "+str(userName)
        assert expected_location == userLocation, "***** ERROR: Expected value for 'location' is: "+str(expected_location)+", but actual result is: "+str(userLocation)
        assert expected_public_repos == public_repos, "***** ERROR: Expected value for 'public_repos' is: "+str(expected_public_repos)+", but actual result is: "+str(public_repos)
        assert expected_followers == followers, "***** ERROR: Expected value for 'followers' is: "+str(expected_followers)+", but actual result is: "+str(followers)
        assert expected_following == following, "***** ERROR: Expected value for 'following' is: "+str(expected_following)+", but actual result is: "+str(following)
        print('***** SUCCES: Test passed')
        print("----- END TestCase: "+testCaseName+" -----\n")


    # #Function for printing on console, or for logging into file
    # def my_print(self, myText):
    #     print(myText)
    #     #
    #     import logging
    #     logging.basicConfig(filename=self.logFile,level=logging.INFO)
    #     logging.info(myText)
    #     #logging.error(myText)

    # #This function will check web page element existance
    # def check_exists_by_xpath(self, xpath):
    #     try:
    #         self.driver.find_element_by_xpath(xpath)
    #     except NoSuchElementException:
    #         return False
    #     return True

if __name__ == "__main__":
    unittest.main()

