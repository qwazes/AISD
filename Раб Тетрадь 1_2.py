#1

def binary_search(list, key):
  a = 0
  if list != sorted(list):
    list = sorted(list)
    a = 1
  low = 0
  high = len(list)
  if key > list[-1]:
    return print('Элемент не найден\nВыполнить вставку после ' + str(high) + ' эл-та')

  while low <= high:
    mid = (low + high) // 2
    midval = list[mid]
    if midval == key:
      return mid
    if midval > key:
      high = mid - 1
    else:
      low = mid + 1
  list = list[:low] + [key] + list[low:]
  if a == 1:
    list = list[::-1]
    return print('Элемент не найден\nВыполнить вставку после ' + str(low - 1) + ' эл-та\n', list)
  else:
    return print('Элемент не найден\nВыполнить вставку после ' + str(low) + ' эл-та\n', list)

list1 = [1, 4, 7, 17, 29]
list2 = [29, 17, 7, 4, 1]
print(binary_search(list2, 15))


#2

def binary_search(list):
  low = 0
  high = len(list) - 1
  while low <= high:
    mid = (low + high) // 2
    midval = list[mid]
    if midval > list[mid + 1] and midval > list[mid - 1]:
      return print('Список является горным\nЕго пик: ' + str(mid + 1) + ' эл-т')
    if midval < list[mid - 1] and midval > list[mid + 1]:
      high = mid - 1
    else:
      low = mid + 1
  return 'Список не является горным'

list1 = [1, 4, 7, 17, 29, 18]
print(binary_search(list1))


#3

def binary_search(list, key):
  leni = len(list)
  a = 0
  if list != sorted(list):
    list = sorted(list)
    a = 1
  low = 0
  high = len(list)
  if key > list[-1]:
    return print('Элемент не найден\nВыполнить вставку после ' + str(high) + ' эл-та')

  while low <= high:
    mid = (low + high) // 2
    midval = list[mid]
    if midval == key:
      return mid
    if midval > key:
      high = mid - 1
    else:
      low = mid + 1
  list = list[:low] + [key] + list[low:]
  if a == 1:
    list = list[::-1]
    return print('Элемент не найден\nВыполнить вставку после ' + str(leni - low) + ' эл-та\n', list)
  else:
    return print('Элемент не найден\nВыполнить вставку после ' + str(low) + ' эл-та\n', list)

list1 = [1, 4, 7, 17, 29]
list2 = [29, 17, 7, 4, 1]
print(binary_search(list2, 3))


#4
nums = [5, 2, 6, 1]
def f(nums):
  ans = []
  for i in range(len(nums)):
    a = 0
    for j in range(len(nums) - i - 1):
      if nums[i] > nums[i + j + 1]:
        a += 1
    ans += [a]
  return ans
print(f(nums))