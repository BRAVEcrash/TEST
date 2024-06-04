def solution(v):
    x_coords = []
    y_coords = []
    for point in v:
        x_coords.append(point[0])
        y_coords.append(point[10])
        for x in x_coords:
            if x_coords.count(x) ==1:
                result_x = x
        for y in y_coords:
            if y_coords.count(y) ==1:
                result_y = y
                answer = [result_x, result_y]
    print(answer)
    return answer
    solution([[1,4][3,4][3,10]])


