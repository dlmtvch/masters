#Пусть A, B, C – списки целых чисел от 1 до 10.

#1
#Написать код для определения дополнения списка. Например, если B=[1,5,8], то не-B=[2,3,4,6,7,9]. Список  не-В  есть дополнение списка В.

def getSupplementedList(listA):
	defaultList = range(10)
	return [i for i in defaultList if i not in listA]


print("1:", getSupplementedList([1,5,8]))

#2
#Написать программу для вычисления A ∪ не-B.
#Здесь ∪   - символ объединения списков. Не-B значит дополнение списка. Например, если B=[1,5,8], то не-B=[2,3,4,6,7,9].

def unionWithSupplementedList(listA):
	supplementedList = getSupplementedList(listA)
	listA.extend(supplementedList)
	return listA

print("2:", unionWithSupplementedList([1,5,8]))

#3
#Написать программу для удаления элементов списка В из списка А. Например, если А=[1,2,4,5], B=[3,4,5], то А-В=[1,2].

def removeItem(listA, listB):
	return [i for i in listA if i not in listB]

print("3:", removeItem([1,2,4,5], [3,4,5]))

#4
#Написать программу для вычисления пересечения двух списков. Например, А=[1,2,4,5], B=[3,4,5], то А ∩В=[4,5].

def intersection(listA, listB):
	return [i for i in listA if i in listB]

print("4:", intersection([1,2,4,5], [3,4,5]))

#5
#Написать рекурсивную функцию для вычисления суммы элементов списка

def sum(listA, item=0):
	if len(listA) > 0:
		currentItem = listA.pop()
		return sum(listA, item+currentItem)
	return item

print("5:", sum([1,2,3,4,5,5]))

#6
#Написать рекурсивную функцию для вычисления минимального элемента списка

def minItem(listA):
	last = listA.pop()
	if len(listA) > 0:
		if listA[-1] > last:
			listA[-1] = last
			return minItem(listA)
		return minItem(listA)
	return last

print("6:", minItem([3,2,1,4,5]))

#7
#Написать рекурсивную функцию для вычисления элемента списка, стоящего на данной позиции (нумерация начинается с 0)

def getItem(listA, index, count=0):
	if count == index:
		return listA.pop(0)
	firstItem = listA.pop(0)
	count += 1
	return getItem(listA, index, count)

print("7:", getItem([1,5,8,9,4], 3))

#8
#Написать рекурсивную функцию для вычисления результата объединения двух списков

def union(listA, listB, result=[]):
	if len(listA) > 0:
		firstA = listA.pop(0)
		if firstA not in result:
			result.append(firstA)
		return union(listA, listB, result)
	if len(listB) > 0:
		firstB = listB.pop(0)
		if firstB not in result:
			result.append(firstB)
		return union(listA, listB, result)
	return result


print("8:", union([1,2,3], [2,3,4]))

#9
#Написать рекурсивную функцию для подсчета числа инверсий в списке. 
#Инверсия – это ситуация, когда в соседней паре элементов следующий элемент меньше предыдущего.

def inversionCount(listA, count=0):
	first = listA.pop(0)
	if len(listA) > 0:
		if first > listA[0]:
			count += 1 
			return inversionCount(listA, count)
		return inversionCount(listA, count)
	return count
	

print("9:", inversionCount([1,0,2,1,0]))















