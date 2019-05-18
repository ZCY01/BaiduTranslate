import BaiduTranslate

if __name__ == "__main__":
    d = BaiduTranslate.Dict()
    json = d.dictionary('hello')
    print(json)
