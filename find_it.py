def find_index_of_largest_number(number_list=None):
    sort_list_number = list(number_list)
    sort_list_number.sort()
    largest_number = sort_list_number[-1]
    print('Largest number is : ', largest_number)
    print(number_list)
    return number_list.index(largest_number)


def get_list():
    try:
        number_list = input('ENTER ARRAY OF NUMBER HERE  (ex. 1,2,2,3,4,5,6,7,8): ').strip().split(',')
        number_list = [int(i) for i in number_list]
    except Exception as e:
        print(e, 'PLEASE FILL CORRECT DATA!!')
        get_list()
    return number_list

data_list = get_list()
print('YOUR NUMBER LIST IS : %s' % data_list)
index = int(find_index_of_largest_number(number_list=data_list))
print('INDEX (IN PROGRAMMER LANGUAGE) IS : ', index)
print('INDEX (IN PEOPLE LANGUAGE) IS : ', index+1)
