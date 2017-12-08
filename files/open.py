with open('../tom.txt', 'r') as f:   #自动调用close(), 省去了写f.close()
    print(f.read())
