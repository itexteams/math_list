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


def bt_dang9_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến thời gian t
            t = symbols('t')

            # Biến ngẫu nhiên để tạo ra nhiều câu hỏi khác nhau:
            # A là biên độ sóng (ví dụ bài mẫu là 75)
            A = random.choice([60, 70, 75, 80])
            # k là tham số ở mẫu số góc (ví dụ bài mẫu là 8)
            k = random.choice([6, 8, 12])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Chiều cao so với mực nước biển trung bình tại thời điểm $t$ (giây) của mỗi cơn sóng được cho bởi hàm số $h(t) = %s \\sin \\left( \\frac{\\pi t}{%s} \\right)$, trong đó $h(t)$ được tính bằng centimét.''' 
                             %(latex(A), latex(k)))

            ########################################################################
            # Nhận biết (Ý a) ############################################
            # Tính h(5) cho bài toán ngẫu nhiên
            val_t1 = 5
            h_val1 = A * math.sin((math.pi * val_t1) / k)
            h_val1_round = round(h_val1, 1)
            # Định dạng dấu phẩy cho số thập phân
            h_val1_str = str(h_val1_round).replace('.', ',')

            nb_da_1_d = '\\True Chiều cao của sóng tại thời điểm $%s$ giây bằng $%s$ (cm)' %(latex(val_t1), h_val1_str)
            nb_da_1_s = 'Chiều cao của sóng tại thời điểm $%s$ giây bằng $%s$ (cm)' %(latex(val_t1), str(round(h_val1 + 5, 1)).replace('.', ','))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Lời giải chi tiết tính h(5)
            loigiai_nb_1 = ('''Tại thời điểm $t = %s$ giây, chiều cao của sóng là:\\\\'''
                            '''$h(%s) = %s \\cdot \\sin \\left( \\frac{%s\\pi}{%s} \\right) \\approx %s$ (cm).'''
                            %(latex(val_t1), latex(val_t1), latex(A), latex(val_t1), latex(k), h_val1_str))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Ý b) ############################################
            # Tính h(20) cho bài toán ngẫu nhiên
            val_t2 = 20
            h_val2 = A * math.sin((math.pi * val_t2) / k)
            h_val2_round = round(h_val2, 1)
            h_val2_str = str(h_val2_round).replace('.', ',')

            th_da_1_d = '\\True Chiều cao của sóng tại thời điểm $%s$ giây bằng $%s$ (cm)' %(latex(val_t2), h_val2_str)
            th_da_1_s = 'Chiều cao của sóng tại thời điểm $%s$ giây bằng $%s$ (cm)' %(latex(val_t2), latex(A))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Tại thời điểm $t = %s$ giây, chiều cao của sóng là:\\\\'''
                            '''$h(%s) = %s \\cdot \\sin \\left( \\frac{%s\\pi}{%s} \\right) = %s$ (cm).'''
                            %(latex(val_t2), latex(val_t2), latex(A), latex(val_t2), latex(k), h_val2_str))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng (Ý c) ############################################
            # Sóng đạt chiều cao lớn nhất khi sin(...) = 1 => pi*t/k = pi/2 + k_nguyen * 2*pi => t = k/2 + 2*k*k_nguyen
            # k_nguyen = 0 => t = k/2. k_nguyen = 1 => t = k/2 + 2*k
            t_max1 = Rational(k, 2)
            t_max2 = Rational(k, 2) + 2*k

            vd_da_1_d = '\\True Trong $30$ giây đầu tiên (kể từ mốc $t = 0$ giây), thời điểm để sóng đạt chiều cao lớn nhất là $%s$ giây' %(latex(t_max1))
            vd_da_1_s = 'Trong $30$ giây đầu tiên (kể từ mốc $t = 0$ giây), thời điểm để sóng đạt chiều cao lớn nhất là $%s$ giây' %(latex(t_max1 + 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Sóng đạt chiều cao lớn nhất khi $\\sin \\left( \\frac{\\pi t}{%s} \\right) = 1 \\Leftrightarrow \\frac{\\pi t}{%s} = \\frac{\\pi}{2} + m2\\pi \\Leftrightarrow t = %s + %sm$ ($m \\in \\mathbb{Z}$).\\\\'''
                            '''Vì xét trong $30$ giây đầu tiên nên $0 \\le t \\le 30 \\Leftrightarrow 0 \\le %s + %sm \\le 30$.\\\\'''
                            '''Do $m \\in \\mathbb{Z}$ nên ta chọn được $m = 0$ tương ứng với thời điểm $t = %s$ giây.'''
                            %(latex(k), latex(k), latex(t_max1), latex(2*k), latex(t_max1), latex(2*k), latex(t_max1)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao (Ý d) ############################################
            # Thời điểm tiếp theo sóng đạt cực đại (với m = 1)
            vdc_da_1_d = '\\True Trong $30$ giây đầu tiên (kể từ mốc $t = 0$ giây), thời điểm để sóng đạt chiều cao lớn nhất còn có $%s$ giây' %(latex(t_max2))
            vdc_da_1_s = 'Trong $30$ giây đầu tiên (kể từ mốc $t = 0$ giây), thời điểm để sóng đạt chiều cao lớn nhất còn có $%s$ giây' %(latex(t_max2 + 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Từ họ nghiệm thời điểm sóng đạt cực đại $t = %s + %sm$ ($m \\in \\mathbb{Z}$).\\\\'''
                             '''Với $m = 1$, ta tìm được thời điểm tiếp theo là $t = %s + %s \\cdot 1 = %s$ giây.\\\\'''
                             '''Giá trị này vẫn thỏa mãn điều kiện thuộc khoảng $30$ giây đầu tiên ($0 \\le %s \\le 30$).'''
                             %(latex(t_max1), latex(2*k), latex(t_max1), latex(2*k), latex(t_max2), latex(t_max2)))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo số lượng đáp án đúng ngẫu nhiên nằm trong khoảng từ 1 đến 3
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Thiết lập lại danh sách sau khi lọc thỏa mãn điều kiện
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

            # Xuất câu hỏi và lời giải chi tiết theo đúng định dạng mẫu
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

