import re

def makexcerpt(string):
    '''
    [^>]    匹配非>的所有字符
    /?      匹配自闭标签（可选）
    \s      匹配空白区间
    :param string:
    :return:
    '''
    x = re.compile(r'</?[^>]+>')
    y = re.compile(r'\s')
    res = x.sub('', string)
    # res = y.sub('',res)
    return res

