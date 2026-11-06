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


def bt_dang29_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Tìm bộ số ngẫu nhiên đẹp
            while True:
                r = random.choice([40, 45, 48, 49, 50, 52])  # Năng suất gặt (kg/giờ)
                K = random.choice([300, 320, 340, 360, 400]) # Thời gian cơ sở K = W / r
                W = K * r                                    # Tổng sản lượng cần gặt (kg)
                c1 = random.choice([60000, 70000, 80000])    # Chi phí vận hành mỗi máy (đồng)
                c2 = random.choice([40000, 50000, 60000])    # Chi phí thuê kỹ sư (đồng/giờ)

                A = K * c2 # Tử số của chi phí giám sát: A / x
                x_continuous = math.sqrt(A / c1)

                if 11 <= x_continuous <= 17:
                    # Tìm giá trị nguyên tối ưu thực tế
                    x_floor = int(math.floor(x_continuous))
                    candidates = [x_floor - 2, x_floor - 1, x_floor, x_floor + 1, x_floor + 2]
                    best_x = None
                    min_cost = float('inf')
                    costs = {}
                    for cx in candidates:
                        if cx > 0:
                            cost_val = c1 * cx + A / cx
                            costs[cx] = cost_val
                            if cost_val < min_cost:
                                min_cost = cost_val
                                best_x = cx

                    # Đảm bảo các giá trị khảo sát x lân cận đều lớn hơn 0
                    disp_xs = [best_x - 2, best_x - 1, best_x]
                    if all(dx > 0 for dx in disp_xs):
                        break

            M = best_x + randint(3, 6) # Tổng số máy nông trại có

            # Các phương án nhiễu sai biệt
            c1_wrong = c1 - randint(1, 9) * 11
            K_wrong = K + randint(5, 25)
            A_wrong = A + randint(1, 9)

            # Biểu diễn dấu phẩy cho số thập phân Việt Nam
            str_x_continuous = f"{x_continuous:.1f}".replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một nông trại có %s máy gặt lúa tự động và được giám sát bởi một kỹ sư, mỗi máy gặt có thể gặt được %s kg lúa trong 1 giờ. Chi phí vận hành cho mỗi máy gặt cho một vụ là %s đồng. Chi phí thuê kỹ sư giám sát là %s đồng/giờ. Vụ lúa này cần gặt %s kg lúa. Hỏi nên sử dụng bao nhiêu máy để tổng chi phí thấp nhất. Gọi $x$ là số lượng máy gặt cần sử dụng. Xét tính đúng-sai của các khẳng định sau:'''              
                             %(M, r, c1, c2, W))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Chi phí vận hành cho vụ lúa là %sx' % (c1)
            nb_da_1_s = 'Chi phí vận hành cho vụ lúa là %sx' % (c1_wrong)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Chi phí vận hành cho vụ lúa mỗi máy gặt trong một vụ là %s đồng. \\\\ Có $x$ máy thì chi phí vận hành là %sx.'''
                        % (c1, c1))

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
            th_da_1_d = '\\True Thời gian cần dùng để gặt hết %s kg lúa là $\\frac{%s}{x}$' % (W, K)  
            th_da_1_s = 'Thời gian cần dùng để gặt hết %s kg lúa là $\\frac{%s}{x}$' % (W, K_wrong)   
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Trong một giờ, với $x$ máy gặt thì gặt được số kg lúa là %sx. \\\\ Số giờ để gặt hết %s kg lúa là: $\\frac{%s}{%sx} = \\frac{%s}{x}$.'''       
                       % (r, W, W, r, K))

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
            vd_da_1_d = '\\True Chi phí thuê kỹ sư giám sát là $\\frac{%s}{x}$' % (A)  
            vd_da_1_s = 'Chi phí thuê kỹ sư giám sát là $\\frac{%s}{x}$' % (A_wrong)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Chi phí thuê kỹ sư giám sát: $\\frac{%s}{x} \\cdot %s = \\frac{%s}{x}$.'''  
                       % (K, c2, A))

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
            vdc_da_1_d = '\\True Số máy để tổng chi phí nhỏ nhất là %s' % (best_x) 
            vdc_da_1_s = 'Số máy để tổng chi phí nhỏ nhất là %s' % (best_x + random.choice([-1, 1])) 
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Gọi $x$ là số lượng máy gặt cần sử dụng. \\\\
            Chi phí vận hành là %sx. \\\\
            Trong một giờ, với $x$ máy gặt thì gặt được số kg lúa là %sx. \\\\
            Số giờ để gặt hết %s kg lúa là: $\\frac{%s}{%sx} = \\frac{%s}{x}$. \\\\
            Chi phí cho giám sát là: $\\frac{%s}{x} \\cdot %s = \\frac{%s}{x}$. \\\\
            Xét hàm số: $f(x) = %sx + \\frac{%s}{x}$. \\\\
            $f\'(x) = %s - \\frac{%s}{x^2} = \\frac{%sx^2 - %s}{x^2}$. \\\\
            $f\'(x) = 0 \\Leftrightarrow x = \\sqrt{\\frac{%s}{%s}} \\approx %s$. \\\\
            Vì số máy là số nguyên nên ta có: \\\\
            $f(%s) = %s$. \\\\
            $f(%s) = %s$. \\\\
            $f(%s) = %s$. \\\\
            Số máy để tổng chi phí nhỏ nhất là %s.'''
                       % (c1, r, W, W, r, K, K, c2, A, c1, A, c1, A, c1, A, A, c1, str_x_continuous,
                          best_x - 2, int(costs[best_x - 2]),
                          best_x - 1, int(costs[best_x - 1]),
                          best_x, int(costs[best_x]),
                          best_x))

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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

