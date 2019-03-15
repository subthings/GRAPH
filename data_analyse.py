
delta_components11 = 0
delta_components22 = 0
j = 0
l0 = 8
l1 = 18
l2 = 28
i = 0
def read_from_file(which):
    with open(which) as file:
        for line in file:
            line = file.readline()
            if i == l0:
                components0 = line
                l0 += 30
                components00 = components0.replace('Number of connected components: ', '')
            elif i == l1:
                components1 = line
                l1 += 30
                components11 = components1.replace('Number of connected components: ', '')
            elif i == l2:
                components2 = line
                l2 += 30
                components22 = components0.replace('Number of connected components: ', '')
                j+=1
                delta_components11 += (components11 - components00)
                delta_components22 += (components22 - components00)

            i +=1

    file.close()


read_from_file('data.txt')
print(delta_components22/j)
print(delta_components11/j)