#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import BaiduTranslate

if __name__ == "__main__":
    d = BaiduTranslate.Dict()
    # open fanyi.baidu.com to get the code of language
    # https://fanyi.baidu.com/#zh/en/你好
    json = d.dictionary('like a hot knife through butter', dst='zh', src='en')
    print(json)
    json = d.dictionary('青花瓷', dst='en', src='zh')
    print(json['trans_result']['data'][0]['dst'])
