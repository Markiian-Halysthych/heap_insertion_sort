class Refrigerator:
    def __init__(self, firm, capacity, weight, power_consumption):
        self.firm = str(firm)
        self.capacity = float(capacity)
        self.weight = float(weight)
        self.power_consumption = float(power_consumption)


refrigerator1 = Refrigerator("LG", 14.12, 250.0, 50.0)
refrigerator2 = Refrigerator("Samsung", 15.13, 200.97, 28.16)
refrigerator3 = Refrigerator("Libher", 13.67, 300.54, 97.54)
refrigerator4 = Refrigerator("Gorenja", 16.09, 100.30, 54.6)
refrigerator5 = Refrigerator("Libher", 9.47, 400.20, 96.15)
refrigerator6 = Refrigerator("LG", 30.86, 700.60, 75.98)
refrigerator7 = Refrigerator("Samsung", 18.09, 10.60, 17.3)
refrigerator8 = Refrigerator("Gorenja", 28.18, 600.50, 85.98)

refrigerator_capacity = [
    refrigerator1.capacity,
    refrigerator2.capacity,
    refrigerator3.capacity,
    refrigerator4.capacity,
    refrigerator5.capacity,
    refrigerator6.capacity,
    refrigerator7.capacity,
    refrigerator8.capacity
]

refrigerator_power_consumption = [
    refrigerator1.power_consumption,
    refrigerator2.power_consumption,
    refrigerator3.power_consumption,
    refrigerator4.power_consumption,
    refrigerator5.power_consumption,
    refrigerator6.power_consumption,
    refrigerator7.power_consumption,
    refrigerator8.power_consumption
]


def insertion_sort(arr):
    for i in range(len(arr)):
        j = i - 1
        key = arr[i]
        while arr[j] < key and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


insertion_sort(refrigerator_capacity)
heap_sort(refrigerator_power_consumption)
print("Refrigerators sorted by capacity descending (insertion sort)")
print(refrigerator_capacity)
print()
print("refrigerators sorted by power consumption (heap sort)")
print(refrigerator_power_consumption)

