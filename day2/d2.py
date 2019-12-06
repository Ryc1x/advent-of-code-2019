def process(arr):
    arr = arr.copy()
    i = 0
    while True:
        if arr[i] == 1:
            arr[arr[i+3]] = arr[arr[i+1]] + arr[arr[i+2]]
        elif arr[i] == 2:
            arr[arr[i+3]] = arr[arr[i+1]] * arr[arr[i+2]]
        elif arr[i] == 99:
            return arr[0]
        else:
            return 'ERROR'
        i += 4
        print(arr[:10])
    return

if __name__ == "__main__":
    with open('input.txt') as f:
        s = f.readline()
        arr = [int(x) for x in s.split(',')]
        for i in range(100):
            for j in range(100):
                arr[1], arr[2] = i, j
                result = process(arr)
                if process(arr) == 19690720:
                    print(i*100 + j)