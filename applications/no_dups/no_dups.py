def no_dups(s):
    # Your code here
    list_keys = []

    if s == '':
        return ''
    l = s.split(' ')

    x = dict.fromkeys(l)

    for key in x.keys():
        list_keys.append(key)
    return ' '.join(list_keys)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))