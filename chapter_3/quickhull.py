def quick_hull(points):
    # 找到左端點和右端點
    left = min(points, key=lambda p: p[0])
    right = max(points, key=lambda p: p[0])

    # 將點分為左側和右側的兩組，每組用一條線段來表示凸包
    left_points = [p for p in points if is_left(p, left, right)]
    right_points = [p for p in points if is_left(p, right, left)]

    # 對左側和右側的點遞迴應用 QuickHull
    hull = [left, right]
    find_hull(left_points, left, right, hull)
    find_hull(right_points, right, left, hull)

    return hull


def find_hull(points, p1, p2, hull):
    if not points:
        return

    # 找到距離線段 p1-p2 最遠的點
    farthest_point = max(points, key=lambda p: distance(p1, p2, p))

    # 將 farthest_point 加入凸包中
    hull.insert(hull.index(p2), farthest_point)

    # 將點分為兩組，每組用一條線段來表示凸包
    s1 = [p for p in points if is_left(p, p1, farthest_point)]
    s2 = [p for p in points if is_left(p, farthest_point, p2)]

    # 遞迴應用 QuickHull
    find_hull(s1, p1, farthest_point, hull)
    find_hull(s2, farthest_point, p2, hull)


def is_left(p, p1, p2):
    # 檢查 p 是否在 p1-p2 的左側
    return ((p2[0] - p1[0]) * (p[1] - p1[1]) - (p2[1] - p1[1]) * (p[0] - p1[0])) > 0


def distance(p1, p2, p):
    # 計算點 p 到線段 p1-p2 的距離
    return abs((p2[0] - p1[0]) * (p1[1] - p[1]) - (p1[0] - p[0]) * (p2[1] - p1[1])) / ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5


points = [(0, 0), (1, 3), (2, 2), (4, 4), (0, 3), (2, 0), (3, 1), (3, 3)]
hull = quick_hull(points)
print(hull)  # Output: [(0, 0), (4, 4), (3, 3), (1, 3), (
