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


def bt_dang11_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random cấu trúc giá trị vế phải của phương trình cot(3x) = val
            kieu_val = random.choice([1, 2, 3, 4])

            if kieu_val == 1:
                # Bài gốc: cot 3x = -1/sqrt(3) <=> 3x = -pi/3 + k*pi <=> x = -pi/9 + k*pi/3 (hoặc 2pi/9 + k*pi/3)
                val_latex = '-\\frac{1}{\\sqrt{3}}'
                goc_tuong_duong = '-\\frac{\\pi}{3}'
                goc_sai_latex = '-\\frac{\\pi}{6}'
                goc_nghiem_bandau = Rational(2, 9) # dạng chuẩn dương nhỏ nhất hoặc họ nghiệm chuẩn
                max_nghiem_duong_min = '\\frac{2\\pi}{9}'
                # Nghiệm thuộc (-pi/2; 0): 2pi/9 + k*pi/3 => k=-1: -pi/9 (thỏa); k=-2: -4pi/9 (thỏa). Tổng = -5pi/9
                tong_nghiem_latex = '\\frac{-5\\pi}{9}'
                họ_nghiem_dung_latex = '\\frac{2\\pi}{9} + k\\frac{\\pi}{3}'
                họ_nghiem_sai_latex = '\\frac{\\pi}{9} + k\\frac{\\pi}{3}'
                k_list = [-1, -2]
                nghiem_goc_list = [Rational(-1, 9), Rational(-4, 9)]
            elif kieu_val == 2:
                # Biến thể 2: cot 3x = 1/sqrt(3) <=> 3x = pi/3 + k*pi <=> x = pi/9 + k*pi/3
                val_latex = '\\frac{1}{\\sqrt{3}}'
                goc_tuong_duong = '\\frac{\\pi}{3}'
                goc_sai_latex = '\\frac{\\pi}{4}'
                max_nghiem_duong_min = '\\frac{\\pi}{9}'
                # Nghiệm thuộc (-pi/2; 0): pi/9 - pi/3 = -2pi/9 (thỏa); pi/9 - 2pi/3 = -5pi/9 (không thỏa vì < -pi/2). Tổng = -2pi/9
                tong_nghiem_latex = '-\\frac{2\\pi}{9}'
                họ_nghiem_dung_latex = '\\frac{\\pi}{9} + k\\frac{\\pi}{3}'
                họ_nghiem_sai_latex = '\\frac{2\\pi}{9} + k\\frac{\\pi}{3}'
                k_list = [-1]
                nghiem_goc_list = [Rational(-2, 9)]
            elif kieu_val == 3:
                # Biến thể 3: cot 3x = -sqrt(3) <=> 3x = -pi/6 + k*pi <=> x = -pi/18 + k*pi/3 (hoặc 5pi/18 + k*pi/3)
                val_latex = '-\\sqrt{3}'
                goc_tuong_duong = '-\\frac{\\pi}{6}'
                goc_sai_latex = '-\\frac{\\pi}{3}'
                max_nghiem_duong_min = '\\frac{5\\pi}{18}'
                # Nghiệm thuộc (-pi/2; 0): 5pi/18 - pi/3 = -pi/18 (thỏa); 5pi/18 - 2pi/3 = -7pi/18 (thỏa). Tổng = -8pi/18 = -4pi/9
                tong_nghiem_latex = '-\\frac{4\\pi}{9}'
                họ_nghiem_dung_latex = '\\frac{5\\pi}{18} + k\\frac{\\pi}{3}'
                họ_nghiem_sai_latex = '\\frac{\\pi}{18} + k\\frac{\\pi}{3}'
                k_list = [-1, -2]
                nghiem_goc_list = [Rational(-1, 18), Rational(-7, 18)]
            else:
                # Biến thể 4: cot 3x = sqrt(3) <=> 3x = pi/6 + k*pi <=> x = pi/18 + k*pi/3
                val_latex = '\\sqrt{3}'
                goc_tuong_duong = '\\frac{\\pi}{6}'
                goc_sai_latex = '\\frac{\\pi}{2}'
                max_nghiem_duong_min = '\\frac{\\pi}{18}'
                # Nghiệm thuộc (-pi/2; 0): pi/18 - pi/3 = -5pi/18 (thỏa); pi/18 - 2pi/3 = -11pi/18 (loại). Tổng = -5pi/18
                tong_nghiem_latex = '-\\frac{5\\pi}{18}'
                họ_nghiem_dung_latex = '\\frac{\\pi}{18} + k\\frac{\\pi}{3}'
                họ_nghiem_sai_latex = '\\frac{5\\pi}{18} + k\\frac{\\pi}{3}'
                k_list = [-1]
                nghiem_goc_list = [Rational(-5, 18)]

            # Nội dung câu hỏi chính
            noidungcauhoi = ('''Cho phương trình lượng giác $\\cot 3x = %s$ (*).''' 
                             %(val_latex))

            ########################################################################
            # Nhận biết ############################################
            # Ý a: Khẳng định tương đương của phương trình phương án sai lấy góc từ hình mẫu gốc hoặc tùy biến
            nb_da_1_d = 'Phương trình (*) tương đương $\\cot 3x = \\cot \\left( %s \\right)$' %(goc_sai_latex)
            nb_da_1_s = '\\True Phương trình (*) tương đương $\\cot 3x = \\cot \\left( %s \\right)$' %(goc_tuong_duong)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ta có $%s = \\cot \\left( %s \\right)$, do đó phương trình (*) tương đương với $\\cot 3x = \\cot \\left( %s \\right)$. Khẳng định phương trình tương đương với $\\cot \\left( %s \\right)$ là khẳng định sai.'''
                            %(val_latex, goc_tuong_duong, goc_tuong_duong, goc_sai_latex))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Ý b: Khẳng định nghiệm tổng quát của phương trình
            th_da_1_d = '\\True Phương trình (*) có nghiệm $x = %s$ ($k \\in \\mathbb{Z}$)' %(họ_nghiem_dung_latex)
            th_da_1_s = 'Phương trình (*) có nghiệm $x = %s$ ($k \\in \\mathbb{Z}$)' %(họ_nghiem_sai_latex)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Phương trình $\\cot 3x = \\cot \\left( %s \\right) \\Leftrightarrow 3x = %s + k\\pi \\Leftrightarrow x = \\frac{%s}{3} + k\\frac{\\pi}{3}$ ($k \\in \\mathbb{Z}$).\\\\'''
                            '''Biểu diễn dưới dạng góc dương cơ bản tương đương ta được họ nghiệm: $x = %s$ ($k \\in \\mathbb{Z}$).'''
                            %(goc_tuong_duong, goc_tuong_duong, goc_tuong_duong, họ_nghiem_dung_latex))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Ý c: Tổng các nghiệm của phương trình trong khoảng (-pi/2; 0)
            vd_da_1_d = '\\True Tổng các nghiệm của phương trình trong khoảng $\\left( -\\frac{\\pi}{2}; 0 \\right)$ bằng $%s$' %(tong_nghiem_latex)
            vd_da_1_s = 'Tổng các nghiệm của phương trình trong khoảng $\\left( -\\frac{\\pi}{2}; 0 \\right)$ bằng $-\\frac{\\pi}{3}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Tạo chuỗi liệt kê nghiệm cho lời giải chi tiết
            nghiem_chi_tiet = ' và '.join(['$%s\\pi$' % latex(v) for v in nghiem_goc_list])
            loigiai_vd_1 = ('''Xét họ nghiệm $x = %s$ ($k \\in \\mathbb{Z}$), cho nghiệm thuộc khoảng $\\left( -\\frac{\\pi}{2}; 0 \\right)$:\\\\'''
                            '''Ta tìm được các giá trị nguyên của $k$ tương ứng là %s, cho ra các nghiệm cụ thể là: %s.\\\\'''
                            '''Tổng các nghiệm này bằng: $%s = %s$.'''
                            %(họ_nghiem_dung_latex, ' và '.join(['$k = %s$' % k for k in k_list]), nghiem_chi_tiet, ' + '.join(['\\left(%s\\pi\\right)' % latex(v) for v in nghiem_goc_list]), tong_nghiem_latex))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Ý d: Nghiệm dương nhỏ nhất của phương trình
            vdc_da_1_d = '\\True Phương trình có nghiệm dương nhỏ nhất bằng $%s$' %(max_nghiem_duong_min)
            vdc_da_1_s = 'Phương trình có nghiệm dương nhỏ nhất bằng $\\frac{\\pi}{3}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Để tìm nghiệm dương nhỏ nhất, ta xét họ nghiệm tổng quát $x = %s$ ($k \\in \\mathbb{Z}$) với điều kiện $x > 0$.\\\\'''
                             '''Cho lần lượt các giá trị nguyên $k$ sao cho nhận được giá trị dương nhỏ nhất của $x$.\\\\'''
                             '''Kết quả nghiệm dương nhỏ nhất tìm được là $%s$.'''
                             %(họ_nghiem_dung_latex, max_nghiem_duong_min))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm tra để đảm bảo số lượng đáp án đúng ngẫu nhiên nằm trong khoảng từ 1 đến 3
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại đồng bộ vào list tương ứng sau khi lọc điều kiện đạt yêu cầu
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

            # Xuất câu hỏi và lời giải chi tiết theo đúng định dạng mẫu khung chương trình đề ra
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

