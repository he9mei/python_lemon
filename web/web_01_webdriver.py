from selenium import webdriver   # ctrl+b查看import可以看到支持的浏览器


# 启动与浏览器的会话---全新的浏览器---不带任何用户数据
driver = webdriver.Chrome(service_log_path="E:\\chromedriver.log")
driver.find_element_by_id()

'''
Chrome(),ctr+b可以看到以下Chrome()初始化
   def __init__(self, executable_path="chromedriver", port=0,
                 options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None, keep_alive=True):             
总结1：
1.如果要查看chromedriver的日志信息，可以指定service_log_path。chromedriver就是service
2.从D:\Program Files\Python38文件进入cmd
-->D:\Program Files\Python38>chromedriver --help
能看到chromedriver相关的参数信息service_args。
'''

'''
# 启动服务

self.service = Service(
            executable_path,
            port=port,
            service_args=service_args,
            log_path=service_log_path)
        self.service.start()
        
# 远程连接

        try:
            RemoteWebDriver.__init__(
                self,
                command_executor=ChromeRemoteConnection(     # chtr+b查看self._commands，再查看commond类
                    remote_server_addr=self.service.service_url,
                    keep_alive=keep_alive),
                desired_capabilities=desired_capabilities)
        except Exception:
            self.quit()
            raise
        self._is_remote = False

# self._commands
Command.FIND_ELEMENT: ('POST', '/session/$sessionId/element'),

总结2：
1.driver=webdriver.Chrome() 这一句代码做了很多事情：
2.driver.find_element_by_id()查看源码实际上就是执行了Command.FIND_ELEMENT
也就是说一个函数/一个对外api：就是一条命令；就是一个HTTP请求。
'''

'''
# 关闭服务

   def quit(self):
        """
        Closes the browser and shuts down the ChromeDriver executable
        that is started when starting the ChromeDriver
        """
        try:
            RemoteWebDriver.quit(self)
        except Exception:
            # We don't care about the message because something probably has gone wrong
            pass
        finally:
            self.service.stop()
'''
