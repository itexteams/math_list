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


def bt_dang13_p2_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các nghiệm để tạo hàm bậc 3 dạng f(x) = (x - x1)(x - x2)^2
            valid_pairs = []
            for x1_iter in range(-4, 5):
                for x2_iter in range(-4, 5):
                    if x1_iter != x2_iter and (2 * x1_iter + x2_iter) % 3 == 0:
                        valid_pairs.append((x1_iter, x2_iter))

            x1_val, x2_val = random.choice(valid_pairs)

            f_expr = expand((x - x1_val) * (x - x2_val)**2)
            f_prime = diff(f_expr, x)

            # Tọa độ các điểm cực trị
            x_A = (2 * x1_val + x2_val) // 3
            x_B = x2_val

            x_min = min(x_A, x_B)
            x_max = max(x_A, x_B)
            y_cd = f_expr.subs(x, x_min)
            y_ct = f_expr.subs(x, x_max)

            tu_so = x - x1_val

            yA = f_expr.subs(x, x_A)
            yB = f_expr.subs(x, x_B)
            AB_sq = (x_B - x_A)**2 + (yB - yA)**2
            AB_len = sp.simplify(sp.sqrt(AB_sq))
            AB_false = sp.simplify(sp.sqrt(AB_sq + random.choice([1, 2, 3])))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=f(x)=%s$.''' 
                             % (latex(f_expr)))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Hàm số $y=f(x)$ nghịch biến trên khoảng $\\left(%s; %s\\right)$' % (latex(x_min), latex(x_max))
            nb_da_1_s = 'Hàm số $y=f(x)$ đồng biến trên khoảng $\\left(%s; %s\\right)$' % (latex(x_min), latex(x_max))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $y'=%s$. \\\\
            $y'=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\left[ \\begin{array}{l} x=%s \\\\ x=%s \\end{array} \\right.$. \\\\
            Bảng biến thiên: \\\\
            \\begin{tikzpicture}
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$x$/1,$y'$/0.7,$y$/2.1}
            {$-\\infty$,$%s$,$%s$,$+\\infty$}
            \\tkzTabLine{,+,0,-,0,+}
            \\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$}
            \\end{tikzpicture} \\\\
            Dựa vào bảng biến thiên, hàm số nghịch biến trên khoảng $\\left(%s; %s\\right)$.''' % 
            (latex(f_prime), latex(f_prime), latex(x_min), latex(x_max), latex(x_min), latex(x_max), latex(y_cd), latex(y_ct), latex(x_min), latex(x_max)))

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
            th_da_1_d = '\\True Giới hạn $\\lim_{x \\to +\\infty} f(x) = +\\infty$' 
            th_da_1_s = 'Giới hạn $\\lim_{x \\to +\\infty} f(x) = -\\infty$' 
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $\\lim_{x \\to +\\infty} f(x) = \\lim_{x \\to +\\infty} \\left(%s\\right) = +\\infty$.''' 
                            % (latex(f_expr)))

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
            vd_da_1_d = '\\True Gọi $A, B$ lần lượt là hai điểm cực trị của đồ thị hàm số $y=f(x)$. Khi đó độ dài $AB$ bằng $%s$' % (latex(AB_len))
            vd_da_1_s = 'Gọi $A, B$ lần lượt là hai điểm cực trị của đồ thị hàm số $y=f(x)$. Khi đó độ dài $AB$ bằng $%s$' % (latex(AB_false))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Các điểm cực trị của đồ thị hàm số là $A\\left(%s; %s\\right)$ và $B\\left(%s; %s\\right)$. \\\\
            Độ dài $AB = \\sqrt{\\left(%s - %s\\right)^2 + \\left(%s - %s\\right)^2} = %s$.''' % 
            (latex(x_A), latex(yA), latex(x_B), latex(yB), latex(x_B), latex(x_A), latex(yB), latex(yA), latex(AB_len)))

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
            vdc_da_1_d = '\\True Đồ thị hàm số $y = \\frac{%s}{f(x)}$ có đúng một đường tiệm cận đứng' % (latex(tu_so))
            vdc_da_1_s = 'Đồ thị hàm số $y = \\frac{%s}{f(x)}$ có đúng hai đường tiệm cận đứng' % (latex(tu_so))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có hàm số $y = \\frac{%s}{f(x)} = \\frac{%s}{%s}$. \\\\
            Hàm số xác định khi $f(x) \\neq 0 \\Leftrightarrow \\left[ \\begin{array}{l} x \\neq %s \\\\ x \\neq %s \\end{array} \\right.$. \\\\
            Khi đó $y = \\frac{%s}{ %s \\cdot %s } = \\frac{1}{%s}$. \\\\
            Ta thấy $\\lim_{x \\to %s} y = +\\infty$ nên $x = %s$ là đường tiệm cận đứng duy nhất của đồ thị hàm số. \\\\
            Vậy đồ thị hàm số có đúng một đường tiệm cận đứng.''' % 
            (latex(tu_so), latex(tu_so), latex(f_expr), latex(min(x1_val, x2_val)), latex(max(x1_val, x2_val)), latex(tu_so), latex(x - x1_val), latex((x - x2_val)**2), latex((x - x2_val)**2), latex(x2_val), latex(x2_val)))

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
            str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

