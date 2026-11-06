import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang42_p2_b2_c1_ds12(self):
    # Khai báo biến
    r_sym, h_sym = symbols('r h')

    # Random các tham số
    V_val = random.randint(40, 90) # Thể tích
    C_val = round(random.uniform(1.2, 2.5), 1) # Chi phí, 1 chữ số thập phân
    C_val_str = str(C_val).replace('.', ',')

    # Tính toán các giá trị
    # a) Thể tích
    # b) Diện tích
    # c) r tối ưu
    r_opt_inside = V_val / 2
    # d) Chi phí
    r_opt_val = (V_val / (2 * math.pi))**(1/3)
    S_min_val = 2 * math.pi * r_opt_val**2 + 2 * V_val / r_opt_val
    Cost_min_val = round(S_min_val * C_val)

    # Nội dung câu hỏi
    noidungcauhoi = ('''\\immini{Một trang trại cần xây một bể chứa nước hình trụ bằng bê tông (có nắp đậy) để chứa $%s \\text{ m}^3$ nước tưới tiêu. Chi phí xây dựng chủ yếu phụ thuộc vào diện tích bề mặt bê tông cần sử dụng (diện tích toàn phần của bể tính theo phần bên trong của bể). Theo hợp đồng với nhà thầu xây dựng, chi phí mỗi mét vuông xây dựng theo cách tính trên là $%s$ triệu đồng. Gọi $r$ là bán kính đáy và $h$ là chiều cao của bể (đơn vị tính của $r, h$ là mét).}
                     {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                     	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (21,157.8) .. controls (21,145.57) and (47.64,135.65) .. (80.5,135.65) .. controls (113.36,135.65) and (140,145.57) .. (140,157.8) .. controls (140,170.03) and (113.36,179.95) .. (80.5,179.95) .. controls (47.64,179.95) and (21,170.03) .. (21,157.8) -- cycle ;
                     	\\draw  [fill={rgb, 255:red, 199; green, 206; blue, 215 }  ,fill opacity=1 ] (140,50.8) -- (140,157.8) .. controls (140,168.74) and (117.39,177.6) .. (89.5,177.6) .. controls (61.61,177.6) and (39,168.74) .. (39,157.8) -- (39,50.8) .. controls (39,39.86) and (61.61,31) .. (89.5,31) .. controls (117.39,31) and (140,39.86) .. (140,50.8) .. controls (140,61.74) and (117.39,70.6) .. (89.5,70.6) .. controls (61.61,70.6) and (39,61.74) .. (39,50.8) ;
                     	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 199; green, 206; blue, 204 }  ,fill opacity=1 ] (49.1,51.65) .. controls (49.1,44.33) and (67.12,38.4) .. (89.35,38.4) .. controls (111.58,38.4) and (129.6,44.33) .. (129.6,51.65) .. controls (129.6,58.97) and (111.58,64.9) .. (89.35,64.9) .. controls (67.12,64.9) and (49.1,58.97) .. (49.1,51.65) -- cycle ;
                     	\\draw  [draw opacity=0][fill={rgb, 255:red, 102; green, 208; blue, 245 }  ,fill opacity=1 ] (88.7,48.89) .. controls (103.59,49) and (116.75,52.24) .. (124.9,57.15) .. controls (116.68,61.95) and (103.47,65) .. (88.59,64.89) .. controls (73.71,64.79) and (60.54,61.54) .. (52.4,56.63) .. controls (60.61,51.84) and (73.82,48.78) .. (88.7,48.89) -- cycle ;
                     	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.18 ] (104.6,71.4) -- (89.5,177.6) -- (140.1,163.4) -- (141.1,53.9) -- cycle ;
                     	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.22 ] (107.1,69.9) -- (125.6,64.4) -- (126.6,170.4) -- (108.6,176.4) -- cycle ;
                     	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (125.6,64.4) -- (126.6,170.4) ;
                     	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.28 ] (116.82,34.12) .. controls (130.76,37.63) and (140,43.79) .. (140,50.8) .. controls (140,61.74) and (117.5,70.6) .. (89.75,70.6) .. controls (78.59,70.6) and (68.29,69.17) .. (59.95,66.74) -- cycle ;
                     \\end{tikzpicture}}'''
                     % (V_val, C_val_str))

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Thể tích của bể là $V = \\pi r^2 h = %s \\text{ m}^3$' % V_val
    nb_da_1_s = 'Thể tích của bể là $V = 2\\pi r h = %s \\text{ m}^3$' % V_val
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Công thức tính thể tích khối trụ là $V = \\pi r^2 h = %s \\text{ m}^3$.''' % V_val)

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ######################################################################## Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Diện tích toàn phần $S_{tp}$ của bể chứa nước được biểu diễn theo bán kính $r$ là $S_{tp}(r) = 2\\pi r^2 + \\frac{%s}{r} (\\text{m}^2)$' % (2 * V_val)
    th_da_1_s = 'Diện tích toàn phần $S_{tp}$ của bể chứa nước được biểu diễn theo bán kính $r$ là $S_{tp}(r) = \\pi r^2 + \\frac{%s}{r} (\\text{m}^2)$' % (2 * V_val)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Từ $V = \\pi r^2 h = %s \\Rightarrow h = \\frac{%s}{\\pi r^2}$.\\\\
    Diện tích toàn phần của bể chứa nước (hình trụ có nắp đậy) là:\\\\
    $S_{tp} = 2\\pi r^2 + 2\\pi rh = 2\\pi r^2 + 2\\pi r \\cdot \\frac{%s}{\\pi r^2} = 2\\pi r^2 + \\frac{%s}{r}$.'''
                    % (V_val, V_val, V_val, 2 * V_val))

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Để tiết kiệm chi phí nhất, bể nên được xây với bán kính đáy là $r = \\sqrt[3]{\\frac{%s}{\\pi}} \\text{ m}$' % int(r_opt_inside)
    vd_da_1_s = 'Để tiết kiệm chi phí nhất, bể nên được xây với bán kính đáy là $r = \\sqrt[3]{\\frac{%s}{\\pi}} \\text{ m}$' % (int(r_opt_inside) + 5)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Xét hàm số $S(r) = 2\\pi r^2 + \\frac{%s}{r}$ với $r > 0$.\\\\
    Ta có $S'(r) = 4\\pi r - \\frac{%s}{r^2} = \\frac{4\\pi r^3 - %s}{r^2}$.\\\\
    $S'(r) = 0 \\Leftrightarrow 4\\pi r^3 - %s = 0 \\Leftrightarrow r^3 = \\frac{%s}{\\pi} \\Leftrightarrow r = \\sqrt[3]{\\frac{%s}{\\pi}}$.\\\\
    Lập bảng biến thiên, ta thấy $S(r)$ đạt giá trị nhỏ nhất tại $r = \\sqrt[3]{\\frac{%s}{\\pi}}$.'''
                    % (2 * V_val, 2 * V_val, 2 * V_val, 2 * V_val, int(r_opt_inside), int(r_opt_inside), int(r_opt_inside)))

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Chi phí thấp nhất để xây dựng bể chứa nước nói trên là $%s$ triệu đồng (làm tròn kết quả đến hàng đơn vị)' % Cost_min_val
    vdc_da_1_s = 'Chi phí thấp nhất để xây dựng bể chứa nước nói trên là $%s$ triệu đồng (làm tròn kết quả đến hàng đơn vị)' % (Cost_min_val + random.randint(3, 10))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Diện tích toàn phần nhỏ nhất là $S_{\\min} = 2\\pi \\left(\\sqrt[3]{\\frac{%s}{\\pi}}\\right)^2 + \\frac{%s}{\\sqrt[3]{\\frac{%s}{\\pi}}} \\approx %s \\text{ m}^2$.\\\\
    Chi phí thấp nhất là: $%s \\times %s \\approx %s$ triệu đồng.'''
                     % (int(r_opt_inside), 2 * V_val, int(r_opt_inside), round(S_min_val, 2), str(round(S_min_val, 2)).replace('.', ','), C_val_str, Cost_min_val))

    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vdc)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' +
    str(noidungcauhoi) + 
        '\n\\choiceTFn \n'
        '{' + str(shuffled_answers_nb[0]) + '}\n'
        '{' + str(shuffled_answers_th[0]) + '}\n'
        '{' + str(shuffled_answers_vd[0]) + '}\n'
        '{' + str(shuffled_answers_vdc[0]) + '}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content

