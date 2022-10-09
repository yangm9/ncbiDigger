from selenium.webdriver.chrome.options import Options # 实现无可视化界面

def setoption():
    """
    谷歌浏览器常规反反爬的参数设置,无可视化界面的操作
    """
    ChromeOpts=Options()
    ChromeOpts.add_experimental_option('useAutomationExtension',False)
    ChromeOpts.add_experimental_option('excludeSwitches',['enable-logging','enable-automation'])
    ChromeOpts.add_argument("--headless")
    ChromeOpts.add_argument("--disable-gpu")
    ChromeOpts.add_argument('--hide-scrollbars')# 不加载图片, 提升速度
    return ChromeOpts
