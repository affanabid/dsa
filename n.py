def reverse(name, i):
    if i == len(name):
        return 0
    
    reverse(name, i+1)
    print(name[i], end=' ')

reverse('affan', 0)
