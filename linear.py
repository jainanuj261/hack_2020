def linear_search(array,search_element):
    for position,element in enumerate(array,1):
        if element == search_element:
            return position
    return -1       


print("Enter array nos.")
array = ma(int,input().split())
print("Enter search element:")
search_element = int(input())

print("Position of element is :",linear_search(array,search_element))

