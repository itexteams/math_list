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


def bt_dang13_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các tham số cho hàm số f(x) = a*cos(k*x) + b và g(x) = sin(k*x) + tan(k*x)
            a = randint(2, 4)
            b = randint(1, 3)
            k = random.choice([1, 2]) # k=1 ứng với bài gốc, k=2 tạo biến thể mới bổ sung cho góc lượng giác

            # Nội dung câu hỏi
            if k == 1:
                noidungcauhoi = ('''Cho hàm số $f(x) = %s\\cos x + %s$ và $g(x) = \\sin x + \\tan x$. Khi đó:''' %(latex(a), latex(b)))
            else:
                noidungcauhoi = ('''Cho hàm số $f(x) = %s\\cos 2x + %s$ và $g(x) = \\sin 2x + \\tan 2x$. Khi đó:''' %(latex(a), latex(b)))

            ########################################################################
            # Nhận biết ############################################
            # Ý a: Tập xác định hàm số f(x): D = R
            nb_da_1_d = '\\True Tập xác định hàm số $f(x)$: $D = \\mathbb{R}$'
            nb_da_1_s = 'Tập xác định hàm số $f(x)$: $D = \\mathbb{R} \\setminus \\{0\\}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            if k == 1:
                loigiai_nb_1 = ('''Hàm số $f(x) = %s\\cos x + %s$ xác định với mọi $x \\in \\mathbb{R}$. Do đó tập xác định là $D = \\mathbb{R}$.''' %(latex(a), latex(b)))
            else:
                loigiai_nb_1 = ('''Hàm số $f(x) = %s\\cos 2x + %s$ xác định với mọi $x \\in \\mathbb{R}$. Do đó tập xác định là $D = \\mathbb{R}$.''' %(latex(a), latex(b)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Ý b: Hàm số f(x) là hàm tuần hoàn
            th_da_1_d = '\\True Hàm số $f(x)$ là hàm tuần hoàn'
            th_da_1_s = 'Hàm số $f(x)$ là hàm không tuần hoàn'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            if k == 1:
                loigiai_th_1 = ('''Hàm số $f(x) = %s\\cos x + %s$ là hàm số tuần hoàn với chu kỳ $T = 2\\pi$.''' %(latex(a), latex(b)))
            else:
                loigiai_th_1 = ('''Hàm số $f(x) = %s\\cos 2x + %s$ là hàm số tuần hoàn với chu kỳ $T = \\pi$.''' %(latex(a), latex(b)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Ý c: Tập xác định hàm số g(x)
            # g(x) = sin(kx) + tan(kx) xác định khi cos(kx) != 0 <=> kx != pi/2 + m*pi <=> x != pi/(2k) + m*pi/k
            if k == 1:
                vd_da_1_d = '\\True Tập xác định hàm số $g(x)$: $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + m\\pi \\mid m \\in \\mathbb{Z} \\right\\}$'
                vd_da_1_s = 'Tập xác định hàm số $g(x)$: $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{3} + m\\pi \\mid m \\in \\mathbb{Z} \\right\\}$'
            else:
                vd_da_1_d = '\\True Tập xác định hàm số $g(x)$: $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{4} + \\frac{m\\pi}{2} \\mid m \\in \\mathbb{Z} \\right\\}$'
                vd_da_1_s = 'Tập xác định hàm số $g(x)$: $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + m\\pi \\mid m \\in \\mathbb{Z} \\right\\}$'

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            if k == 1:
                loigiai_vd_1 = ('''Hàm số $g(x) = \\sin x + \\tan x$ xác định khi $\\cos x \\ne 0 \\Leftrightarrow x \\ne \\frac{\\pi}{2} + m\\pi$ ($m \\in \\mathbb{Z}$).\\\\'''
                                '''Do đó, tập xác định của hàm số $g(x)$ là $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + m\\pi \\mid m \\in \\mathbb{Z} \\right\\}$.''')
            else:
                loigiai_vd_1 = ('''Hàm số $g(x) = \\sin 2x + \\tan 2x$ xác định khi $\\cos 2x \\ne 0 \\Leftrightarrow 2x \\ne \\frac{\\pi}{2} + m\\pi \\Leftrightarrow x \\ne \\frac{\\pi}{4} + \\frac{m\\pi}{2}$ ($m \\in \\mathbb{Z}$).\\\\'''
                                '''Do đó, tập xác định của hàm số $g(x)$ là $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{4} + \\frac{m\\pi}{2} \\mid m \\in \\mathbb{Z} \\right\\}$.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Ý d: Hàm số g(x) là hàm số tuần hoàn (Mệnh đề trong ảnh khẳng định g(x) không tuần hoàn -> Sai)
            vdc_da_1_d = 'Hàm số $g(x)$ là hàm không tuần hoàn'
            vdc_da_1_s = '\\True Hàm số $g(x)$ là hàm tuần hoàn'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            if k == 1:
                loigiai_vdc_1 = ('''Hàm số $g(x) = \\sin x + \\tan x$ có hàm thành phần $\\sin x$ tuần hoàn với chu kỳ $T_1 = 2\\pi$, và hàm $\\tan x$ tuần hoàn với chu kỳ $T_2 = \\pi$.\\\\'''
                                 '''Suy ra hàm số $g(x)$ là hàm số tuần hoàn với chu kỳ $T = \\text{BCNN}(2\\pi, \\pi) = 2\\pi$.''')
            else:
                loigiai_vdc_1 = ('''Hàm số $g(x) = \\sin 2x + \\tan 2x$ có hàm thành phần $\\sin 2x$ tuần hoàn với chu kỳ $T_1 = \\pi$, và hàm $\\tan 2x$ tuần hoàn với chu kỳ $T_2 = \\frac{\\pi}{2}$.\\\\'''
                                 '''Suy ra hàm số $g(x)$ là hàm số tuần hoàn với chu kỳ $T = \\text{BCNN}\\left(\\pi, \\frac{\\pi}{2}\\right) = \\pi$.''')

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm tra để đảm bảo có từ 1 đến 3 câu đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại giá trị được chọn sau khi lọc thỏa mãn điều kiện
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

            # Xuất câu hỏi và lời giải chi tiết theo đúng cấu trúc định dạng mẫu
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

