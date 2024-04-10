# List
print('----------- List -----------')
my_list=['potato', 'tomato', 'beet', 'cabbage', 'carrot', 'onion']
print('List: ', my_list)
print('First element: ', my_list[0])
print('Last element:  ', my_list[-1])
print('Sublist: ', my_list[2:5]) # show from 3rd to 5th item
my_list[2]='zucchini' # modify 3rd item
print('Modified list: ', my_list)
# Dictionary
print('-------- Dictionary --------')
my_dict={'potato':'картофель','tomato':'томат','beet':'свекла', 'cabbage':'капуста', 'carrot':'морковь', 'onion':'лук'}
print('Dictionary: ', my_dict)
print('Translation for "beet": ', my_dict.get('beet')) # get value for key='beet'
my_dict['onion']='лук-порей' # modify value for key='onion'
print('Modified dictionary: ',my_dict)