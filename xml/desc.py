"""
python对XML的解析
常见的XML编程接口有DOM和SAX，这两种接口处理XML文件的方式不同，当然使用场合也不同。
    python有三种方法解析XML，SAX，DOM，以及ElementTree:
1.SAX (simple API for XML )
    python 标准库包含SAX解析器，SAX用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。
2.DOM(Document Object Model)
    将XML数据在内存中解析成一个树，通过对树的操作来操作XML。
"""