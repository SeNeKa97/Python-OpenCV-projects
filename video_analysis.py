import cv2
import numpy as np

video = cv2.VideoCapture("videos/car.mp4")
ret, frame = video.read()

# Начальные координаты окна для отслеживания объекта
# Выбраны на основе положения объекта в самом начале видео
col, w, row, h = 0, 150, 110, 60
window = (col, row, w, h)

# Определяем минимальные и максимальные пороговые значения для цвета
MIN_COLOR = np.array((20., 35., 33.), np.uint8)
MAX_COLOR = np.array((165., 180., 170.), np.uint8)

# Выбираем "region of interest"-область, интересующую нас
roi = frame[row:row + h, col:col + w]
# конвертируем полученную область в формат HSV
r_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# Получаем маску объекта, попавшего в ROI
msk = cv2.inRange(r_hsv, MIN_COLOR, MAX_COLOR)
roi_hst = cv2.calcHist([r_hsv], [0], msk, [180], [0, 180])

cv2.normalize(roi_hst, roi_hst, 0, 255, cv2.NORM_MINMAX)

# Вводим условие прекращения работы алгоритма (в данном случае производим максимум 10 итераций)
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
count = 0
while video.isOpened():
    ret, frame = video.read()

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Производим "обратную проекцию" нормализированной гистограммы на изображение
        dst = cv2.calcBackProject([hsv], [0], roi_hst, [0, 180], 1)

        # Используем метод непрерывного адаптивного meanshift
        ret, window = cv2.CamShift(dst, window, term_crit)

        # Находим угловые точки окна обнаружения
        edge_pts = cv2.boxPoints(ret)
        edge_pts = np.int0(edge_pts)

        # Поскольку camshift часто дает наклонный прямоугольник, рисуем его через polylines
        img = cv2.polylines(frame, [edge_pts], True, (0, 255, 0), 2)
        cv2.imwrite("images/car/" + str(count) + ".png", img)
        count += 1
    else:
        break

cv2.destroyAllWindows()
