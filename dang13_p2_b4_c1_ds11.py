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


def bt_dang13_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số bài toán để tạo nhiều biến thể (Bộ 1 là bài gốc, Bộ 2 là bài toán tương đương)
            bo_so = random.choice([1, 2])

            if bo_so == 1:
                a_val, b_val, c_val = 2, -5, 2
                # f(x) = 2t^2 - 5t + 2 với t = sin 2x, t thuộc [-1; 1]
                # Đỉnh parabol t = 5/4 > 1. Hàm số nghịch biến trên [-1; 1]
                # Max = f(-1) = 2 + 5 + 2 = 9; Min = f(1) = 2 - 5 + 2 = -1
                # Tong Max + Min = 8 < 9
                tong_max_min = 8
                menh_de_b_sai = 'Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số là một số lớn hơn 9'
                menh_de_b_dung = '\\True Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số là một số nhỏ hơn 9'
                # f(x) = 2 <=> 2sin^2 2x - 5sin 2x = 0 <=> sin 2x = 0 (vì sin 2x = 5/2 loại) -> Tương đương sin 2x = 0
                # f(x) = 0 <=> sin 2x = 1/2 -> có 2 họ nghiệm tương ứng 4 điểm biểu diễn
                so_diem_bieu_dien = 4
            else:
                a_val, b_val, c_val = 2, -3, 1
                # f(x) = 2t^2 - 3t + 1 với t = sin 2x, t thuộc [-1; 1]
                # Đỉnh parabol t = 3/4. f(3/4) = -1/8. f(-1) = 6. f(1) = 0
                # Max = 6, Min = -1/8. Tong = 47/8 = 5,875 < 9
                tong_max_min = Rational(47, 8)
                menh_de_b_sai = 'Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số là một số lớn hơn 9'
                menh_de_b_dung = '\\True Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số là một số nhỏ hơn 9'
                # f(x) = 1 <=> 2sin^2 2x - 3sin 2x = 0 <=> sin 2x = 0 -> Tương đương sin 2x = 0
                # f(x) = 0 <=> sin 2x = 1/2 hoặc sin 2x = 1 -> sin 2x = 1/2 (4 điểm), sin 2x = 1 (2 điểm) -> Tổng 6 điểm
                so_diem_bieu_dien = 6

            # Chuỗi hiển thị hàm số
            b_dau = '-' if b_val < 0 else '+'
            c_dau = '-' if c_val < 0 else '+'
            bt_goc = '%s\\sin^2 2x %s %s\\sin 2x %s %s' %(latex(a_val), b_dau, latex(abs(b_val)), c_dau, latex(abs(c_val)))

            # Nội dung câu hỏi sử dụng định dạng %s
            noidungcauhoi = ('''Cho hàm số lượng giác $f(x) = %s$.''' %(bt_goc))

            ########################################################################
            # Nhận biết ############################################
            # Ý a: Hàm số lượng giác theo sin 2x có chu kỳ tuần hoàn là \pi (Mẫu khẳng định là 2\pi -> Sai)
            nb_da_1_d = 'Hàm số có chu kỳ tuần hoàn là $2\\pi$'
            nb_da_1_s = '\\True Hàm số có chu kỳ tuần hoàn là $\\pi$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Hàm số $f(x)$ biến đổi theo thành phần biến lượng giác $\\sin 2x$.\\\\'''
                            '''Hàm số $y = \\sin 2x$ tuần hoàn với chu kỳ $T = \\frac{2\\pi}{2} = \\pi$.\\\\'''
                            '''Do đó, chu kỳ tuần hoàn của hàm số $f(x)$ là $\\pi$. Khẳng định chu kỳ bằng $2\\pi$ là sai.''')

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Ý b: Đánh giá tổng GTLN và GTNN của hàm số
            th_da_1_d = menh_de_b_dung
            th_da_1_s = menh_de_b_sai
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            if bo_so == 1:
                loigiai_th_1 = ('''Đặt $t = \\sin 2x$ với điều kiện $t \\in [-1; 1]$, hàm số trở thành $g(t) = 2t^2 - 5t + 2$.\\\\'''
                                '''Xét hàm số $g(t)$ trên đoạn $[-1; 1]$, parabol có hoành độ đỉnh $t_0 = \\frac{5}{4} > 1$.\\\\'''
                                '''Do đó hàm số nghịch biến trên đoạn $[-1; 1]$.\\\\'''
                                '''Giá trị lớn nhất của hàm số là $\\max f(x) = g(-1) = 2(-1)^2 - 5(-1) + 2 = 9$.\\\\'''
                                '''Giá trị nhỏ nhất của hàm số là $\\min f(x) = g(1) = 2(1)^2 - 5(1) + 2 = -1$.\\\\'''
                                '''Tổng giá trị lớn nhất và giá trị nhỏ nhất bằng: $9 + (-1) = 8 < 9$.''')
            else:
                loigiai_th_1 = ('''Đặt $t = \\sin 2x$ with điều kiện $t \\in [-1; 1]$, hàm số trở thành $g(t) = 2t^2 - 3t + 1$.\\\\'''
                                '''Xét hàm số $g(t)$ trên đoạn $[-1; 1]$, parabol có hoành độ đỉnh $t_0 = \\frac{3}{4} \\in [-1; 1]$.\\\\'''
                                '''Ta có: $g\\left(\\frac{3}{4}\\right) = -\\frac{1}{8}$; $g(-1) = 6$; $g(1) = 0$.\\\\'''
                                '''Suy ra giá trị lớn nhất là $\\max f(x) = 6$ và giá trị nhỏ nhất là $\\min f(x) = -\\frac{1}{8}$.\\\\'''
                                '''Tổng giá trị lớn nhất và nhỏ nhất bằng: $6 + \\left(-\\frac{1}{8}\\right) = \\frac{47}{8} = 5,875 < 9$.''')

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Ý c: Hai phương trình f(x) = c_val và sin 2x = 0 là hai phương trình tương đương (Luôn đúng cho cả hai bộ số)
            vd_da_1_d = '\\True Hai phương trình $f(x) = %s$ và $\\sin 2x = 0$ là hai phương trình tương đương' %(latex(c_val))
            vd_da_1_s = 'Hai phương trình $f(x) = %s$ và $\\sin 2x = 0$ không phải là hai phương trình tương đương' %(latex(c_val))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Xét phương trình $f(x) = %s \\Leftrightarrow %s\\sin^2 2x %s %s\\sin 2x + %s = %s \\\\'''
                            '''\\Leftrightarrow \\sin 2x \\left( %s\\sin 2x %s %s \\right) = 0 \\Leftrightarrow \\left[ \\begin{aligned} &\\sin 2x = 0 \\\\ &\\sin 2x = \\frac{%s}{%s} \\end{aligned} \\right.$\\\\'''
                            '''Vì giá trị $\\frac{%s}{%s} > 1$ nên phương trình $\\sin 2x = \\frac{%s}{%s}$ vô nghiệm.\\\\'''
                            '''Do đó phương trình $f(x) = %s$ rút gọn hoàn toàn về $\\sin 2x = 0$.\\\\'''
                            '''Vậy hai phương trình này có cùng tập nghiệm, tức là hai phương trình tương đương.'''
                            %(latex(c_val), latex(a_val), b_dau, latex(abs(b_val)), latex(c_val), latex(c_val), latex(a_val), b_dau, latex(abs(b_val)), latex(abs(b_val)), latex(a_val), latex(abs(b_val)), latex(a_val), latex(abs(b_val)), latex(a_val), latex(c_val)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Ý d: Giải phương trình f(x) = 0 ta thu được số điểm biểu diễn trên đường tròn lượng giác
            vdc_da_1_d = '\\True Giải phương trình $f(x) = 0$ ta thu được %s điểm biểu diễn trên vòng tròn lượng giác' %(latex(so_diem_bieu_dien))
            vdc_da_1_s = 'Giải phương trình $f(x) = 0$ ta thu được 2 điểm biểu diễn trên vòng tròn lượng giác'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            if bo_so == 1:
                loigiai_vdc_1 = ('''Phương trình $f(x) = 0 \\Leftrightarrow 2\\sin^2 2x - 5\\sin 2x + 2 = 0 \\Leftrightarrow \\left[ \\begin{aligned} &\\sin 2x = 2 \\text{ (vô nghiệm)} \\\\ &\\sin 2x = \\frac{1}{2} \\end{aligned} \\right.$\\\\'''
                                 '''Giải $\\sin 2x = \\frac{1}{2} \\Leftrightarrow \\left[ \\begin{aligned} &2x = \\frac{\\pi}{6} + k2\\pi \\\\ &2x = \\frac{5\\pi}{6} + k2\\pi \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} &x = \\frac{\\pi}{12} + k\\pi \\\\ &x = \\frac{5\\pi}{12} + k\\pi \\end{aligned} \\right.$ ($k \\in \\mathbb{Z}$).\\\\'''
                                 '''Mỗi họ nghiệm cộng đuôi $k\\pi$ sẽ tạo ra $2$ điểm biểu diễn đối xứng nhau qua tâm trên vòng tròn lượng giác.\\\\'''
                                 '''Do đó, phương trình có tổng cộng $2 \\cdot 2 = 4$ điểm biểu diễn.''')
            else:
                loigiai_vdc_1 = ('''Phương trình $f(x) = 0 \\Leftrightarrow 2\\sin^2 2x - 3\\sin 2x + 1 = 0 \\Leftrightarrow \\left[ \\begin{aligned} &\\sin 2x = 1 \\\\ &\\sin 2x = \\frac{1}{2} \\end{aligned} \\right.$\\\\'''
                                 '''1. $\\sin 2x = 1 \\Leftrightarrow 2x = \\frac{\\pi}{2} + k2\\pi \\Leftrightarrow x = \\frac{\\pi}{4} + k\\pi$ -> Có $2$ điểm biểu diễn.\\\\'''
                                 '''2. $\\sin 2x = \\frac{1}{2} \\Leftrightarrow x = \\frac{\\pi}{12} + k\\pi$ hoặc $x = \\frac{5\\pi}{12} + k\\pi$ -> Có $4$ điểm biểu diễn.\\\\'''
                                 '''Các điểm này không trùng nhau, do đó tổng số điểm biểu diễn trên vòng tròn lượng giác là $2 + 4 = 6$ điểm biểu diễn.''')

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm tra điều kiện số đáp án đúng nằm từ 1 đến 3
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Đưa vào cấu trúc đồng bộ danh sách sau khi đã lọc điều kiện đạt yêu cầu
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

            # Xuất dữ liệu câu hỏi và lời giải chi tiết theo đúng cấu trúc format mẫu khung chương trình đề ra
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

