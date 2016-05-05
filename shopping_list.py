shoppin_list =[]

def add(item):
    global shoppin_list
    if item.upper() in shoppin_list or item.lower() in shoppin_list:
        print "That item already exist"
        shoppin_list.sort()
    else:
        shoppin_list.append(item)
        return shoppin_list

def remove(item):
    global shoppin_list
    if item.upper() in shoppin_list or item.lower() in shoppin_list:
        shoppin_list.remove(item)
        print "The item was removed"
        return shoppin_list.sort()
    elif item not in shoppin_list:
        print "That item does not exist"
    

def main():
    item = "avocado"
    item1 = "arugula"
    item2 = "beans"
    item3 = "pizza"
    add(item)
    print shoppin_list
    add(item1)
    print shoppin_list
    add(item2)
    print shoppin_list
    add(item3)
    print shoppin_list
    add(item1)
    print shoppin_list

    remove(item)
    print shoppin_list
    remove(item1)
    print shoppin_list
    remove(item2)
    print shoppin_list
    remove(item)
    print shoppin_list
    remove(item3)
    print shoppin_list
    remove(item1)
    print shoppin_list

if __name__ == '__main__':
    main()
