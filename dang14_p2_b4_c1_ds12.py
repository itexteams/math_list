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


def bt_dang14_p2_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Random tham số tạo hàm bậc 3: y = (1/k) * (x^3 + B*x^2 + C*x + D)
            # Chọn x1, x2 là 2 hoành độ cực trị sao cho x1 + x2 chẵn (để B nguyên)
            m = random.randint(1, 3) # Khoảng cách từ tâm đối xứng đến cực trị
            xI = random.randint(-2, 2) # Hoành độ tâm đối xứng
            x1 = xI - m
            x2 = xI + m

            B_coeff = -3 * xI
            C_coeff = 3 * x1 * x2
            D_coeff = random.randint(-9, 5)
            k_val = random.choice([2, 4, 8])

            g_expr = x**3 + B_coeff * x**2 + C_coeff * x + D_coeff
            f_expr = Rational(1, k_val) * g_expr

            f_prime = diff(f_expr, x)
            f_double_prime = diff(f_prime, x)

            # Tọa độ tâm đối xứng
            yI = f_expr.subs(x, xI)

            # Đoạn [u, v] nằm bên phải x2 (hàm số đồng biến)
            u = x2 + random.randint(1, 2)
            v = u + random.randint(2, 4)

            # Tiếp tuyến có hệ số góc nhỏ nhất tại I(xI, yI)
            k_min = f_prime.subs(x, xI)
            # Phương trình tiếp tuyến: y = k_min*(x - xI) + yI
            tangent_expr = simplify(k_min * (x - xI) + yI)
            y_int = tangent_expr.subs(x, 0) # Giao điểm với trục Tung

            # Điểm sai cho phương án nhiễu
            y_int_wrong = y_int + random.choice([Rational(-5, 3), Rational(-2, 3), Rational(1, 3), Rational(4, 3)])

            # Dạng bình phương hoàn chỉnh của y'
            f_prime_sq = Rational(3, k_val) * (x - xI)**2 + k_min

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=\\frac{1}{%s}\\left(%s\\right)$ có đồ thị là $(C)$.'''
                             %(latex(k_val), latex(g_expr)))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đồ thị hàm số có $2$ điểm cực trị'
            nb_da_1_s = 'Đồ thị hàm số không có điểm cực trị'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $y'=%s$. \\\\
            $y'=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\left[ \\begin{array}{l} x=%s \\\\ x=%s \\end{array} \\right.$. \\\\
            Vì phương trình $y'=0$ có $2$ nghiệm phân biệt và $y'$ đổi dấu khi qua $2$ nghiệm đó nên đồ thị hàm số có $2$ điểm cực trị.'''
                            %(latex(f_prime), latex(f_prime), latex(x1), latex(x2)))

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
            th_da_1_d = '\\True Tâm đối xứng của đồ thị hàm số có tọa độ là $\\left(%s; %s\\right)$' %(latex(xI), latex(yI))
            th_da_1_s = 'Tâm đối xứng của đồ thị hàm số có tọa độ là $\\left(%s; %s\\right)$' %(latex(xI), latex(yI + 1))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $y''=%s$. \\\\
            $y''=0 \\Leftrightarrow %s=0 \\Leftrightarrow x=%s$. \\\\
            Thay $x=%s$ vào hàm số ban đầu ta được $y=%s$. \\\\
            Vậy tâm đối xứng của đồ thị hàm số có tọa độ là $\\left(%s; %s\\right)$.'''
                            %(latex(f_double_prime), latex(f_double_prime), latex(xI), latex(xI), latex(yI), latex(xI), latex(yI)))

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
            vd_da_1_d = '\\True Trên đoạn $\\left[%s; %s\\right]$ thì giá trị lớn nhất của hàm số đạt được tại $x=%s$' %(latex(u), latex(v), latex(v))
            vd_da_1_s = 'Trên đoạn $\\left[%s; %s\\right]$ thì giá trị lớn nhất của hàm số đạt được tại $x=%s$' %(latex(u), latex(v), latex(u))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Với mọi $x \\in \\left[%s; %s\\right]$, ta có $y' = %s > 0$. \\\\
            Do đó hàm số đồng biến trên đoạn $\\left[%s; %s\\right]$. \\\\
            Vậy giá trị lớn nhất của hàm số trên đoạn $\\left[%s; %s\\right]$ đạt được tại $x=%s$.'''
                            %(latex(u), latex(v), latex(f_prime), latex(u), latex(v), latex(u), latex(v), latex(v)))

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
            vdc_da_1_d = '\\True Phương trình tiếp tuyến có hệ số góc nhỏ nhất của đồ thị $(C)$ đi qua điểm $A\\left(0; %s\\right)$' %(latex(y_int))
            vdc_da_1_s = 'Phương trình tiếp tuyến có hệ số góc nhỏ nhất của đồ thị $(C)$ đi qua điểm $A\\left(0; %s\\right)$' %(latex(y_int_wrong))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $y' = %s = %s \\ge %s$ với mọi $x \\in \\mathbb{R}$. \\\\
            Đẳng thức xảy ra khi $x = %s$. \\\\
            Khi đó tiếp tuyến có hệ số góc nhỏ nhất là $k_{min} = %s$ tại điểm $I\\left(%s; %s\\right)$. \\\\
            Phương trình tiếp tuyến tại $I$ là: $y = %s\\left(x - %s\\right) + \\left(%s\\right) \\Leftrightarrow y = %s$. \\\\
            Thay $x = 0$ vào phương trình tiếp tuyến ta được $y = %s$. \\\\
            Vậy tiếp tuyến có hệ số góc nhỏ nhất đi qua điểm $A\\left(0; %s\\right)$.'''
                             %(latex(f_prime), latex(f_prime_sq), latex(k_min), latex(xI), latex(k_min), latex(xI), latex(yI), latex(k_min), latex(xI), latex(yI), latex(tangent_expr), latex(y_int), latex(y_int)))

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

