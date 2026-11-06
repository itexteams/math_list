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


def bt_dang23_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các tham số cho từng ý trong bài toán để tạo nhiều biến thể khác nhau
            # Ý a: y = cot(a1*x - pi/4)
            a1 = random.choice([2, 3, 5])

            # Ý d: y = tan(a4*x) + cot(a4*x)
            a4 = random.choice([2, 3])

            # Ý vdc: y = c4 / (sin^4 x - cos^4 x)
            c4 = randint(2, 5)

            # Nội dung câu hỏi chính
            noidungcauhoi = ('''Các mệnh đề sau đúng hay sai?''')

            ########################################################################
            # Nhận biết (Ý a) ############################################
            mẫu_a1 = 4 * a1
            nb_da_1_d = '\\True Hàm số $y = \\cot \\left( %sx - \\frac{\\pi}{4} \\right)$ xác định khi $x \\ne \\frac{\\pi}{%s} + \\frac{k\\pi}{%s}$ ($k \\in \\mathbb{Z}$)' %(latex(a1) if a1 != 1 else '', latex(mẫu_a1), latex(a1))
            nb_da_1_s = 'Hàm số $y = \\cot \\left( %sx - \\frac{\\pi}{4} \\right)$ xác định khi $x \\ne \\frac{\\pi}{4} + k\\pi$ ($k \\in \\mathbb{Z}$)' %(latex(a1) if a1 != 1 else '')
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Hàm số $y = \\cot \\left( %sx - \\frac{\\pi}{4} \\right)$ xác định khi:\\\\'''
                            '''$\\sin \\left( %sx - \\frac{\\pi}{4} \\right) \\ne 0 \\Leftrightarrow %sx - \\frac{\\pi}{4} \\ne k\\pi \\Leftrightarrow %sx \\ne \\frac{\\pi}{4} + k\\pi \\Leftrightarrow x \\ne \\frac{\\pi}{%s} + \\frac{k\\pi}{%s}$ ($k \\in \\mathbb{Z}$).'''
                            %(latex(a1) if a1 != 1 else '', latex(a1) if a1 != 1 else '', latex(a1) if a1 != 1 else '', latex(a1) if a1 != 1 else '', latex(mẫu_a1), latex(a1)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Ý b) ############################################
            th_da_1_d = 'Hàm số $y = \\sqrt{\\sin x - 1}$ có tập xác định là $D = \\mathbb{R}$'
            th_da_1_s = '\\True Hàm số $y = \\sqrt{\\sin x - 1}$ có tập xác định khác $\\mathbb{R}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Hàm số $y = \\sqrt{\\sin x - 1}$ xác định khi và chỉ khi:\\\\'''
                            '''$\\sin x - 1 \\ge 0 \\Leftrightarrow \\sin x \\ge 1$.\\\\'''
                            '''Mà ta luôn có $\\sin x \\le 1$ với mọi $x \\in \\mathbb{R}$, do đó $\\sin x = 1 \\Leftrightarrow x = \\frac{\\pi}{2} + k2\\pi$ ($k \\in \\mathbb{Z}$).\\\\'''
                            '''Suy ra tập xác định của hàm số là $D = \\left\\{ \\frac{\\pi}{2} + k2\\pi \\mid k \\in \\mathbb{Z} \\right\\} \\ne \\mathbb{R}$. Khẳng định $D = \\mathbb{R}$ là sai.''')

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng (Ý c) ############################################
            vd_da_1_d = '\\True Hàm số $y = \\frac{\\sin x}{2 - \\cos x}$ có tập xác định là $D = \\mathbb{R}$'
            vd_da_1_s = 'Hàm số $y = \\frac{\\sin x}{2 - \\cos x}$ có tập xác định là $D = \\mathbb{R} \\setminus \\{0\\}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Hàm số $y = \\frac{\\sin x}{2 - \\cos x}$ xác định khi và chỉ khi $2 - \\cos x \\ne 0 \\Leftrightarrow \\cos x \\ne 2$.\\\\'''
                            '''Vì $-1 \\le \\cos x \\le 1$ với mọi $x \\in \\mathbb{R}$ nên $\\cos x \\ne 2$ luôn đúng với mọi $x \\in \\mathbb{R}$.\\\\'''
                            '''Vậy tập xác định của hàm số là $D = \\mathbb{R}$.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao (Ý d) ############################################
            vdc_da_1_d = 'Hàm số $y = \\frac{%s}{\\sin^4 x - \\cos^4 x}$ xác định khi $\\sin 2x \\ne 0$' %(latex(c4))
            vdc_da_1_s = '\\True Hàm số $y = \\frac{%s}{\\sin^4 x - \\cos^4 x}$ xác định khi $\\cos 2x \\ne 0$' %(latex(c4))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Sửa lỗi chèn %s tương ứng với latex(c4) vào chuỗi
            loigiai_vdc_1 = ('''Ta biến đổi mẫu thức: $\\sin^4 x - \\cos^4 x = (\\sin^2 x - \\cos^2 x)(\\sin^2 x + \\cos^2 x) = -\\cos 2x \\cdot 1 = -\\cos 2x$.\\\\'''
                             '''Hàm số $y = \\frac{%s}{\\sin^4 x - \\cos^4 x}$ xác định khi mẫu số khác $0 \\Leftrightarrow -\\cos 2x \\ne 0 \\Leftrightarrow \\cos 2x \\ne 0$. Khẳng định mẫu thức xác định khi $\\sin 2x \\ne 0$ là sai.'''
                             %(latex(c4)))

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

            # Xuất câu hỏi và lời giải chi tiết theo đúng định dạng khung chương trình mẫu
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

