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


def bt_dang17_p2_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo dữ liệu ngẫu nhiên từ bộ ba số Pythagore
            # Danh sách chứa các bộ ba Pythagore (ke, doi, huyen) để cos alpha hữu tỷ đẹp
            pythagorean_triplets = [(11, 60, 61), (3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)]
            triplet = random.choice(pythagorean_triplets)

            ke = triplet[0]
            doi = triplet[1]
            huyen = triplet[2]

            # Vì góc thuộc khoảng (-pi/2 ; 0) nên cos alpha > 0 và sin alpha < 0
            cos_val = Rational(ke, huyen)
            sin_val = -Rational(doi, huyen)
            tan_val = sin_val / cos_val
            cot_val = 1 / tan_val

            # Tính toán các giá trị lượng giác cho các mệnh đề
            # Mệnh đề a: sin(pi/6 - a) = sin(pi/6)cos(a) - cos(pi/6)sin(a)
            sin_pi6 = Rational(1, 2)
            cos_pi6 = sqrt(3)/2
            val_a_d = sin_pi6 * cos_val - cos_pi6 * sin_val
            val_a_d = sp.simplify(val_a_d)

            # Mệnh đề b: cot(a + pi/4) = 1 / tan(a + pi/4) = (1 - tan(a))/(tan(a) + 1)
            val_b_d = (1 - tan_val) / (tan_val + 1)
            val_b_d = sp.simplify(val_b_d)

            # Các giá trị cung nhân đôi phục vụ mệnh đề c và d
            sin2a = 2 * sin_val * cos_val
            cos2a = cos_val**2 - sin_val**2
            tan2a = sin2a / cos2a

            # Mệnh đề c: cos(2a + pi/3) = cos(2a)cos(pi/3) - sin(2a)sin(pi/3)
            cos_pi3 = Rational(1, 2)
            sin_pi3 = sqrt(3)/2
            val_c_d = cos2a * cos_pi3 - sin2a * sin_pi3
            val_c_d = sp.simplify(val_c_d)

            # Mệnh đề d: tan(3pi/4 - 2a) = (tan(3pi/4) - tan(2a)) / (1 + tan(3pi/4)tan(2a)) với tan(3pi/4) = -1
            val_d_d = (-1 - tan2a) / (1 - tan2a)
            val_d_d = sp.simplify(val_d_d)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho $\\cos a = %s$ và $-\\frac{\\pi}{2} < a < 0$. Xét tính đúng sai của các mệnh đề sau:''' 
                             %(latex(cos_val)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án (Gốc cố tình tạo nhiễu sai hệ số hoặc căn thức để làm câu sai)
            sai_val_a = (11 + 30*sqrt(2))/122 if triplet == (11, 60, 61) else val_a_d + 1
            nb_da_1_d = '\\True $\\sin\\left(\\frac{\\pi}{6} - a\\right) = %s$' %(latex(val_a_d))
            nb_da_1_s = '$\\sin\\left(\\frac{\\pi}{6} - a\\right) = %s$' %(latex(sai_val_a))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Vì $-\\frac{\\pi}{2} < a < 0 \\\\Rightarrow \\\\sin a < 0$.\\\\
            Ta có $\\sin a = -\\sqrt{1 - \\cos^2 a} = -\\sqrt{1 - \\left(%s\\right)^2} = %s$.\\\\
            Khi đó: $\\sin\\left(\\frac{\\pi}{6} - a\\right) = \\sin\\frac{\\pi}{6}\\cos a - \\cos\\frac{\\pi}{6}\\sin a = \\frac{1}{2} \\cdot %s - \\frac{\\sqrt{3}}{2} \\cdot \\left(%s\\right) = %s$.'''
                            %(latex(cos_val), latex(sin_val), latex(cos_val), latex(sin_val), latex(val_a_d)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $\\cot\\left(a + \\frac{\\pi}{4}\\right) = %s$' %(latex(val_b_d))
            th_da_1_s = '$\\cot\\left(a + \\frac{\\pi}{4}\\right) = %s$' %(latex(-val_b_d))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $\\tan a = \\frac{\\sin a}{\\cos a} = %s$.\\\\
            $\\cot\\left(a + \\frac{\\pi}{4}\\right) = \\frac{1}{\\tan\\left(a + \\frac{\\pi}{4}\\right)} = \\frac{1 - \\tan a}{\\tan a + 1} = \\frac{1 - \\left(%s\\right)}{%s + 1} = %s$.'''
                            %(latex(tan_val), latex(tan_val), latex(tan_val), latex(val_b_d)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            sai_val_c = (-3479 + 1320*sqrt(3))/7442 if triplet == (11, 60, 61) else val_c_d * 2
            vd_da_1_d = '\\True $\\cos\\left(2a + \\frac{\\pi}{3}\\right) = %s$' %(latex(val_c_d))
            vd_da_1_s = '$\\cos\\left(2a + \\frac{\\pi}{3}\\right) = %s$' %(latex(sai_val_c))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có: $\\sin 2a = 2\\sin a\\cos a = 2 \\cdot \\left(%s\\right) \\cdot %s = %s$.\\\\
            $\\cos 2a = \\cos^2 a - \\sin^2 a = \\left(%s\\right)^2 - \\left(%s\\right)^2 = %s$.\\\\
            Suy ra: $\\cos\\left(2a + \\frac{\\pi}{3}\\right) = \\cos 2a\\cos\\frac{\\pi}{3} - \\sin 2a\\sin\\frac{\\pi}{3} = %s \\cdot \\frac{1}{2} - %s \\cdot \\frac{\\sqrt{3}}{2} = %s$.'''
                            %(latex(sin_val), latex(cos_val), latex(sin2a), latex(cos_val), latex(sin_val), latex(cos2a), latex(cos2a), latex(sin2a), latex(val_c_d)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True $\\tan\\left(\\frac{3\\pi}{4} - 2a\\right) = %s$' %(latex(val_d_d))
            vdc_da_1_s = '$\\tan\\left(\\frac{3\\pi}{4} - 2a\\right) = %s$' %(latex(1 / val_d_d))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $\\tan 2a = \\frac{\\sin 2a}{\\cos 2a} = \\frac{%s}{%s} = %s$.\\\\
            $\\tan\\left(\\frac{3\\pi}{4} - 2a\\right) = \\frac{\\tan\\frac{3\\pi}{4} - \\tan 2a}{1 + \\tan\\frac{3\\pi}{4}\\tan 2a} = \\frac{-1 - %s}{1 + (-1) \\cdot %s} = %s$.'''
                             %(latex(sin2a), latex(cos2a), latex(tan2a), latex(tan2a), latex(tan2a), latex(val_d_d)))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
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
                '\n\\choiceTFn \n'
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

