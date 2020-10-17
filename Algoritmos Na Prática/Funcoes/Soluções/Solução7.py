def area_triangulo(C1,C2,C3):
    area = (C1[0]*C2[1]+C2[0]*C3[1]-C1[1]*C2[0]-C2[1]*C3[0])/2
    if area < 0:
        area = -area

    return area


area_triangulo([0, 0], [1, 0], [0, -1])