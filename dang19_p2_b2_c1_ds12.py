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


def bt_dang19_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')

            # Hàm phụ trợ xử lý định dạng số thập phân (dấu phẩy)
            def format_vn(val):
                s = str(round(float(val), 1)).replace('.', ',')
                if s.endswith(',0'):
                    s = s[:-2]
                return s

            # Random các hệ số sinh ra bài toán
            A = random.choice([1, 2, 3])
            B = 3 * A
            C = random.choice([10, 15, 20])

            a_str = f"-0,{A}"
            a3_str = f"-0,{3*A}"

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một giống cây tre cảnh khi mới trồng có chiều cao $%s$ cm. Gọi $h(t)$ là chiều cao của cây (tính bằng cm) ở thời điểm $t$ kể từ khi được trồng, với $t$ được tính theo tuần. Quá trình sinh trưởng của cây tre này được mô hình hoá bởi hàm số: $h(t) = %st^3 + %st^2 + %s$ (cm).''' 
                             % (C, a_str, B, C))

            ######################################################################## Nhận biết ############################################
            t_1 = random.choice([2, 3, 4])
            h_t1 = -A*0.1 * t_1**3 + B * t_1**2 + C
            h_t1_str = format_vn(h_t1)

            h_t1_false_val = h_t1 + random.choice([-2.5, 1.5, 2.2, -1.8])
            h_t1_false_str = format_vn(h_t1_false_val)

            # Các đáp án
            nb_da_1_d = '\\True Cây tre đạt chiều cao $%s$ cm sau đúng $%s$ tuần' % (h_t1_str, t_1)
            nb_da_1_s = 'Cây tre đạt chiều cao $%s$ cm sau đúng $%s$ tuần' % (h_t1_false_str, t_1)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Xét mệnh đề a)\\\\
            Ta có: $h(%s) = %s \\cdot %s^3 + %s \\cdot %s^2 + %s = %s$ cm.'''
                        % (t_1, a_str, t_1, B, t_1, C, h_t1_str))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            t_2 = random.choice([4, 5, 6])
            v_t2 = -0.3*A * t_2**2 + 2*B * t_2
            v_t2_str = format_vn(v_t2)

            v_t2_false_val = v_t2 + random.choice([-1.5, 2.5, -2.1])
            v_t2_false_str = format_vn(v_t2_false_val)

            # Các đáp án
            th_da_1_d = '\\True Tốc độ tăng chiều cao của cây tre ở tuần thứ $%s$ là $%s$ cm/tuần' % (t_2, v_t2_str)
            th_da_1_s = 'Tốc độ tăng chiều cao của cây tre ở tuần thứ $%s$ là $%s$ cm/tuần' % (t_2, v_t2_false_str)
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Xét mệnh đề b)\\\\
            Tốc độ tăng chiều cao là $h'(t) = %st^2 + %st \\Rightarrow h'(%s) = %s \\cdot %s^2 + %s \\cdot %s = %s$ (cm/tuần).'''
                        % (a3_str, 2*B, t_2, a3_str, t_2, 2*B, t_2, v_t2_str))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            t_3 = 10
            t_3_false = random.choice([8, 12, 15])

            # Các đáp án
            vd_da_1_d = '\\True Cây tre đạt tốc độ tăng trưởng lớn nhất ở tuần thứ $%s$' % (t_3)
            vd_da_1_s = 'Cây tre đạt tốc độ tăng trưởng lớn nhất ở tuần thứ $%s$' % (t_3_false)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xét mệnh đề c)\\\\
            Ta có $h'(t) = %st^2 + %st$ (với $t \\ge 0$) đạt giá trị lớn nhất tại $x = -\\frac{b}{2a} = -\\frac{%s}{2 \\cdot (%s)} = 10$\\\\
            Vậy cây tre đạt tốc độ tăng trưởng lớn nhất ở tuần thứ $10$.'''
                        % (a3_str, 2*B, 2*B, a3_str))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            d_max_exact = A * 200 * math.sqrt(3) / 9
            d_max_str = format_vn(d_max_exact)

            d_max_false_val = d_max_exact - random.choice([2.7, 3.1, 1.5, 4.2])
            d_max_false_str = format_vn(d_max_false_val)

            h_20 = int(-A*800 + B*400 + C)
            v_tb = 20*A

            # Các đáp án
            vdc_da_1_d = '\\True Nếu so sánh với một cây bạch đàn cũng cao $%s$ cm lúc mới trồng nhưng có tốc độ tăng trưởng không đổi và bằng với tốc độ tăng trưởng trung bình của cây tre trong suốt vòng đời phát triển của nó thì khoảng cách chênh lệch chiều cao lớn nhất giữa hai cây là $%s$ cm (Kết quả làm tròn đến hàng phần chục)' % (C, d_max_str)
            vdc_da_1_s = 'Nếu so sánh với một cây bạch đàn cũng cao $%s$ cm lúc mới trồng nhưng có tốc độ tăng trưởng không đổi và bằng với tốc độ tăng trưởng trung bình của cây tre trong suốt vòng đời phát triển của nó thì khoảng cách chênh lệch chiều cao lớn nhất giữa hai cây là $%s$ cm (Kết quả làm tròn đến hàng phần chục)' % (C, d_max_false_str)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Xét mệnh đề d)\\\\
            Vòng đời phát triển là khoảng thời gian cây tre còn co lên, tức là khi tốc độ tăng trưởng của cây tre là $h'(t) \\ge 0 \\Leftrightarrow %st^2 + %st \\ge 0 \\Leftrightarrow t \\le 20$\\\\
            Vậy vòng đời phát triển theo mô hình này là từ $t=0$ tuần đến $t=20$ tuần\\\\
            Tốc độ tăng trưởng trung bình của cây tre là: $V_{TB} = \\frac{h(20) - h(0)}{20 - 0} = \\frac{%s - %s}{20} = %s$ (cm/tuần)\\\\
            Khi đó cây bạch đàn có chiều cao ban đầu là $%s$ cm và tốc độ tăng trưởng là $%s$ (cm/tuần)\\\\
            Suy ra hàm biểu thị quá trình sinh trưởng của cây bạch đàn là: $g(t) = %s + %st$ (cm)\\\\
            Sự chênh lệch chiều cao giữa hai cây khi đó là: $D(t) = h(t) - g(t) = %st^3 + %st^2 - %st$\\\\
            Khảo sát hàm số $D(t)$ trên đoạn $[0; 20]$ có $D'(t) = %st^2 + %st - %s = 0 \\Leftrightarrow \\left[ \\begin{array}{l} t_1 = \\frac{30 - 10\\sqrt{3}}{3} \\\\ t_2 = \\frac{30 + 10\\sqrt{3}}{3} \\end{array} \\right.$\\\\
            Tính giá trị tại các đầu mút, suy ra khoảng cách lớn nhất là: $d_{\\max} = \\left| D\\left( \\frac{30 + 10\\sqrt{3}}{3} \\right) \\right| \\approx %s$ (cm).'''
                        % (a3_str, 2*B, h_20, C, v_tb, C, v_tb, C, v_tb, a_str, B, v_tb, a3_str, 2*B, v_tb, d_max_str))

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
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ '\n' +
                '\\choiceTFn \n'
               '{'+str(shuffled_answers_nb[0])+'}\n'
               '{'+str(shuffled_answers_th[0])+'}\n'
               '{'+str(shuffled_answers_vd[0])+'}\n'
               '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

