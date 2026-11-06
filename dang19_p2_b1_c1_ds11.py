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


def bt_dang19_p2_b1_c1_ds11(self):
            # Khai báo biến
            # B3-Suy nghĩ tìm cách random bài toán
            # Random số lẻ nhân với pi và số bán nguyên nhân với pi để tạo ra các hệ thức rút gọn tương đương
            k_a1 = random.choice([3, 5, 7])
            k_a2 = random.choice([5, 9, 13])
            k_b1 = random.choice([11, 13, 15])
            k_b2 = random.choice([3, 7, 11])
            k_c1 = random.choice([1, 3, 5])
            k_c2 = random.choice([5, 9, 13])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Xét tính đúng sai của các mệnh đề sau:''')

            ########################################################################
            # Nhận biết ############################################
            # Biến đổi: sin^2(k_a1*pi - a) = sin^2(a), sin^2(a + k_a2*pi/2) = cos^2(a) => Tổng = 1
            nb_da_1_d = '\\True $\\sin^2 (%s\\pi - a) + \\sin^2 \\left(a + \\frac{%s\\pi}{2}\\right) = 1$' %(k_a1, k_a2)
            nb_da_1_s = '$\\sin^2 (%s\\pi - a) + \\sin^2 \\left(a + \\frac{%s\\pi}{2}\\right) = -1$' %(k_a1, k_a2)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ta có: $\\sin (%s\\pi - a) = \\sin a \\Rightarrow \\sin^2 (%s\\pi - a) = \\sin^2 a$.\\\\
            $\\sin \\left(a + \\frac{%s\\pi}{2}\\right) = \\sin \\left(a + \\frac{\\pi}{2} + 2\\pi\\right) = \\cos a \\Rightarrow \\sin^2 \\left(a + \\frac{%s\\pi}{2}\\right) = \\cos^2 a$.\\\\
            Do đó: $\\sin^2 (%s\\pi - a) + \\sin^2 \\left(a + \\frac{%s\\pi}{2}\\right) = \\sin^2 a + \\cos^2 a = 1$.'''
                            %(k_a1, k_a1, k_a2, k_a2, k_a1, k_a2))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Biến đổi: 1 + tan^2(-a + k_b1*pi) = 1/cos^2(a), sin^2(a - k_b2*pi/2) = cos^2(a) => Tích = 1
            th_da_1_d = '$\\left[1 + \\tan^2 (-a + %s\\pi)\\right] \\cdot \\sin^2 \\left(a - \\frac{%s\\pi}{2}\\right) = -1$' %(k_b1, k_b2)
            th_da_1_s = '\\True $\\left[1 + \\tan^2 (-a + %s\\pi)\\right] \\cdot \\sin^2 \\left(a - \\frac{%s\\pi}{2}\\right) = 1$' %(k_b1, k_b2)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Ta có: $\\tan (-a + %s\\pi) = \\tan (-a) = -\\tan a \\Rightarrow 1 + \\tan^2 (-a + %s\\pi) = 1 + \\tan^2 a = \\frac{1}{\\cos^2 a}$.\\\\
            $\\sin \\left(a - \\frac{%s\\pi}{2}\\right) = -\\sin \\left(\\frac{%s\\pi}{2} - a\\right) = -\\cos a \\Rightarrow \\sin^2 \\left(a - \\frac{%s\\pi}{2}\\right) = \\cos^2 a$.\\\\
            Do đó: $\\left[1 + \\tan^2 (-a + %s\\pi)\\right] \\cdot \\sin^2 \\left(a - \\frac{%s\\pi}{2}\\right) = \\frac{1}{\\cos^2 a} \\cdot \\cos^2 a = 1$.'''
                            %(k_b1, k_b1, k_b2, k_b2, k_b2, k_b1, k_b2))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Biến đổi: cos(a+pi) = -cos(a), sin(a+k_c2*pi/2) = cos(a) => Tổng = 0. -tan(a+pi/2)*tan(pi-a) = -(-cot a)*(-tan a) = -1. Kết quả = -1
            vd_da_1_d = '$\\cos (a + %s\\pi) + \\sin \\left(a + \\frac{%s\\pi}{2}\\right) - \\tan \\left(a + \\frac{\\pi}{2}\\right) \\cdot \\tan (\\pi - a) = 1$' %(k_c1, k_c2)
            vd_da_1_s = '\\True $\\cos (a + %s\\pi) + \\sin \\left(a + \\frac{%s\\pi}{2}\\right) - \\tan \\left(a + \\frac{\\pi}{2}\\right) \\cdot \\tan (\\pi - a) = -1$' %(k_c1, k_c2)
            list_vd_da_1 = [vd_da_1_d, vdc_da_1_s] if 'vdc_da_1_s' in locals() else [vd_da_1_d, vd_da_1_d] # Đảm bảo biến hợp lệ
            list_vd_da_1 = [vd_da_1_d, '\\True $\\cos (a + %s\\pi) + \\sin \\left(a + \\frac{%s\\pi}{2}\\right) - \\tan \\left(a + \\frac{\\pi}{2}\\right) \\cdot \\tan (\\pi - a) = -1$' %(k_c1, k_c2)]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Ta có: $\\cos (a + %s\\pi) = -\\cos a$.\\\\
            $\\sin \\left(a + \\frac{%s\\pi}{2}\\right) = \\cos a$.\\\\
            $\\tan \\left(a + \\frac{\\pi}{2}\\right) = -\\cot a$; $\\tan (\\pi - a) = -\\tan a$.\\\\
            Do đó: $-\\cos a + \\cos a - (-\\cot a) \\cdot (-\\tan a) = 0 - 1 = -1$.'''
                            %(k_c1, k_c2))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Biến đổi: cos(pi/2 - a) = sin a, sin(beta + pi) = -sin beta => -sin a * sin beta
            # sin(2*pi - a) = -sin a, cos(beta - pi/2) = sin beta => -(-sin a) * sin beta = sin a * sin beta. Tổng = 0
            vdc_da_1_d = '\\True $\\cos \\left(\\frac{\\pi}{2} - a\\right) \\cdot \\sin (\\beta + \\pi) - \\sin (2\\pi - a) \\cdot \\cos \\left(\\beta - \\frac{\\pi}{2}\\right) = 0$'
            vdc_da_1_s = '$\\cos \\left(\\frac{\\pi}{2} - a\\right) \\cdot \\sin (\\beta + \\pi) - \\sin (2\\pi - a) \\cdot \\cos \\left(\\beta - \\frac{\\pi}{2}\\right) = 2\\sin a \\sin \\beta$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Ta có: $\\cos \\left(\\frac{\\pi}{2} - a\\right) = \\sin a$; $\\sin (\\beta + \\pi) = -\\sin \\beta$.\\\\
            $\\sin (2\\pi - a) = -\\sin a$; $\\cos \\left(\\beta - \\frac{\\pi}{2}\\right) = \\cos \\left(\\frac{\\pi}{2} - \\beta\\right) = \\sin \\beta$.\\\\
            Biểu thức tương đương: $\\sin a \\cdot (-\\sin \\beta) - (-\\sin a) \\cdot \\sin \\beta = -\\sin a \\sin \\beta + \\sin a \\sin \\beta = 0$.''')
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
            str(noidungcauhoi)+ '\n'
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

