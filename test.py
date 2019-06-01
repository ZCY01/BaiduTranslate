#/usr/bin/python
# -*- coding: utf-8 -*-
import BaiduTranslate

if __name__ == "__main__":
    d = BaiduTranslate.Dict()
    # open fanyi.baidu.com to get the code of language
    # https://fanyi.baidu.com/#zh/en/你好
    json = d.dictionary('like a hot knife through butter', src='en', dst='zh')
    print(json)
    json = d.dictionary('青花瓷', src='zh', dst='en')
    print(json)
