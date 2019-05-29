## 自动缩进

无意中发现，在ipython中，如果函数写了return，则回车就不会缩进。

```
def getText(filename):
    doc = docx.Document(os.path.dirname(os.getcwd()) + '/files/word/' + filename)
    for para in doc.paragraphs:
        for run in para.runs:
            print(run.text)
    return None
getText('demo.docx')
```
写完`None`，回车，光标在get的g位置。

写完`text)`回车，默认为函数没有写完，光标在`print`的p下方


