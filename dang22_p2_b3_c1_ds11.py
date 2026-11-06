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


def bt_dang22_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các tham số cho từng ý trong bài toán để tạo biến thể mới
            # Ý a: y = tan(x - pi/2) hoặc tan(x - pi/4)
            phi_a = random.choice([2, 4]) 

            # Ý c: y = cot(a3*x - pi/4)
            a3 = random.choice([2, 3, 5])

            # Ý d: y = cot(x) / (sqrt(3)*tan(x) - m)
            m = random.choice([1, 3])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Các mệnh đề sau đúng hay sai?''')

            ########################################################################
            # Nhận biết (Ý a) ############################################
            nb_da_1_d = '\\True Hàm số $y = \\tan \\left( x - \\frac{\\pi}{%s} \\right)$ xác định $\\Leftrightarrow \\cos \\left( x - \\frac{\\pi}{%s} \\right) \\ne 0$' %(latex(phi_a), latex(phi_a))
            nb_da_1_s = 'Hàm số $y = \\tan \\left( x - \\frac{\\pi}{%s} \\right)$ xác định $\\Leftrightarrow \\sin \\left( x - \\frac{\\pi}{%s} \\right) \\ne 0$' %(latex(phi_a), latex(phi_a))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Hàm số $y = \\tan P(x)$ xác định khi và chỉ khi $\\cos P(x) \\ne 0$.\\\\'''
                            '''Do đó, hàm số $y = \\tan \\left( x - \\frac{\\pi}{%s} \\right)$ xác định khi và chỉ khi $\\cos \\left( x - \\frac{\\pi}{%s} \\right) \\ne 0$.''' 
                            %(latex(phi_a), latex(phi_a)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Ý b) ############################################
            th_da_1_d = '\\True Hàm số $y = \\frac{1 + \\cos x}{\\sin x}$ có tập xác định là $D = \\mathbb{R} \\setminus \\{k\\pi \\mid k \\in \\mathbb{Z}\\}$'
            th_da_1_s = 'Hàm số $y = \\frac{1 + \\cos x}{\\sin x}$ có tập xác định là $D = \\mathbb{R} \\setminus \\left\\{\\frac{\\pi}{2} + k\\pi \\mid k \\in \\mathbb{Z}\\right\\}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Hàm số $y = \\frac{1 + \\cos x}{\\sin x}$ xác định khi và chỉ khi mẫu số khác $0$:\\\\'''
                            '''$\\sin x \\ne 0 \\Leftrightarrow x \\ne k\\pi$ ($k \\in \\mathbb{Z}$).\\\\'''
                            '''Vậy tập xác định của hàm số là $D = \\mathbb{R} \\setminus \\{k\\pi \\mid k \\in \\mathbb{Z}\\}$.''')

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng (Ý c) ############################################
            mau_c = 4 * a3
            vd_da_1_d = '\\True Hàm số $y = \\cot \\left( %sx - \\frac{\\pi}{4} \\right)$ xác định $x \\ne \\frac{\\pi}{%s} + \\frac{k\\pi}{%s}$ ($k \\in \\mathbb{Z}$)' %(latex(a3), latex(mau_c), latex(a3))
            vd_da_1_s = 'Hàm số $y = \\cot \\left( %sx - \\frac{\\pi}{4} \\right)$ xác định $x \\ne \\frac{\\pi}{4} + k\\pi$ ($k \\in \\mathbb{Z}$)' %(latex(a3))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Hàm số $y = \\cot \\left( %sx - \\frac{\\pi}{4} \\right)$ xác định khi và chỉ khi:\\\\'''
                            '''$\\sin \\left( %sx - \\frac{\\pi}{4} \\right) \\ne 0 \\Leftrightarrow %sx - \\frac{\\pi}{4} \\ne k\\pi \\Leftrightarrow %sx \\ne \\frac{\\pi}{4} + k\\pi \\Leftrightarrow x \\ne \\frac{\\pi}{%s} + \\frac{k\\pi}{%s}$ ($k \\in \\mathbb{Z}$).'''
                            %(latex(a3), latex(a3), latex(a3), latex(a3), latex(mau_c), latex(a3)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao (Ý d) ############################################
            vdc_da_1_d = 'Hàm số $y = \\frac{\\cot x}{\\sqrt{3}\\tan x - %s}$ xác định $\\Leftrightarrow \\begin{cases} \\sin x \\ne 0 \\\\ \\cos x \\ne 0 \\end{cases}$' %(latex(m))
            vdc_da_1_s = '\\True Hàm số $y = \\frac{\\cot x}{\\sqrt{3}\\tan x - %s}$ xác định $\\Leftrightarrow \\begin{cases} \\sin x \\ne 0 \\\\ \\cos x \\ne 0 \\\\ \\tan x \\ne \\frac{%s}{\\sqrt{3}} \\end{cases}$' %(latex(m), latex(m))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Hàm số xác định khi và chỉ khi đồng thời thỏa mãn các điều kiện sau:\\\\'''
                             '''1. $\\cot x$ xác định $\\Leftrightarrow \\sin x \\ne 0$.\\\\'''
                             '''2. $\\tan x$ xác định $\\Leftrightarrow \\cos x \\ne 0$.\\\\'''
                             '''3. Mẫu số khác $0$ $\\Leftrightarrow \\sqrt{3}\\tan x - %s \\ne 0 \\Leftrightarrow \\tan x \\ne \\frac{%s}{\\sqrt{3}}$.\\\\'''
                             '''Vậy điều kiện xác định đầy đủ của hàm số là: $\\begin{cases} \\sin x \\ne 0 \\\\ \\cos x \\ne 0 \\\\ \\tan x \\ne \\frac{%s}{\\sqrt{3}} \\end{cases}$ (Mệnh đề chỉ có 2 điều kiện là thiếu và sai).'''
                             %(latex(m), latex(m), latex(m)))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm tra để đảm bảo số lượng đáp án đúng nằm trong khoảng từ 1 đến 3
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

            # Xuất dữ liệu câu hỏi và lời giải chi tiết theo định dạng khung chương trình mẫu
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

