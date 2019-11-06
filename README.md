# BaiduTranslate
## 欢迎各位同学 Star
## 百度翻译 API
### 依赖库
* execjs
* requests
* re

### Linux 系统安装依赖
```
# For Debian or Ubuntu
sudo apt-get install nodejs
pip3 install PyExecJS 
pip3 install requests
```
### 相关疑问
* token, sign的提取方式详见[百度翻译接口 破解](https://blog.csdn.net/hujingshuang/article/details/80180294)


* 观察觉得，token持续的时间比较短，而gtk持续的时间相对来说比较长。如果查询 https://fanyi.baidu.com/v2transapi 返回998的error则重新获取token即可。

### 不需要填写任何cookie信息，使用requests.Session就可以保存足够的cookies信息了。 
