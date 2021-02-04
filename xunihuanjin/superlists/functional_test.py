# coding:utf-8

# 代码调试正确可以使用2021/2/4
# from selenium import webdriver

# browser = webdriver.Chrome('/Users/chaomingdai/Documents/pytestdriven/xunihuanjin/webdriver/chromedriver')
# browser.get('http://127.0.0.1:8000/')
# assert 'Djangofff' in browser.title


from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = browser = webdriver.Chrome('/Users/chaomingdai/Documents/pytestdriven/xunihuanjin/webdriver/chromedriver')
    def tearDown(self) -> None:
        self.browser.quit()
        
    def test_can_start_a_list_and_retriev_it_later(self):
        # 伊迪丝听说有一个很酷的在线代办事项应用
        # 她去看了这个应用的首页
        self.browser.get('http://127.0.0.1:8000/')
        

         # 她注意到网页的标题和头部都包含To-DO这个词
        self.assertIn("To-Do",self.browser.titile)
        self.fail('finish the test! ')
    
if __name__ == '__main__':
    unittest.main(warnings='ignore')
    


# 第二章内容
# 伊迪丝听说有一个很酷的在线代办事项应用
# 她去看了这个应用的首页
# browser.get('http://127.0.0.1:8000/')

# 她注意到网页的标题和头部都包含To-DO这个词
# assert 'To-Do' in browser.title

# 应用邀请她输入一个待办事项

# 她在一个文本框中输入了 Buy peacock feathers 购买孔雀羽毛
# 伊迪丝的爱好是使用假蝇作饵钓鱼

# 她按回车键后，页面更新了
# 待办事项表格中显示了1：Buy peacock feathers

# 页面中又显示了一个文本框，可以输入其他的待办事项。
# 她输入了 Use peacock feathers to make a fly
# 伊迪丝做事很有调理

# 页面再次更新，她的清单中显示了这两个待办事项。

# 伊迪丝想知道这个网站是否会记住她的清单
# 她看到网站为她生成了一个唯一的URl
# 而且页面中又一些文字解说这个功能

# 她访问那个URL，发现她的待办事项列表还在。

# 她很满意，去睡觉了
# browser.quit()


