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


def bt_dang26_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Thiết lập bộ sinh số ngẫu nhiên cho bài toán
            # a1: hệ số của x trong góc hàm tan ở câu a
            a1 = random.choice([2, 3, 4]) 
            # a2: hệ số của x trong góc hàm cot ở câu b
            a2 = random.choice([1, 2])
            # a4: hệ số của x trong tử số ở câu d
            a4 = random.choice([2, 3, 4])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Tìm được tập xác định của các hàm số sau. Khi đó:''')

            ########################################################################
            # Nhận biết ############################################
            # Ý a: Hàm số y = tan(a1*x - pi/6) xác định khi a1*x - pi/6 != pi/2 + k*pi <=> a1*x != 2*pi/3 + k*pi <=> x != 2*pi/(3*a1) + k*pi/a1
            mau_a_dung_1 = 3 * a1
            mau_a_dung_2 = a1

            nb_da_1_d = '\\True Hàm số $y = \\tan \\left( %sx - \\frac{\\pi}{6} \\right)$ xác định khi: $x \\ne \\frac{2\\pi}{%s} + k\\frac{\\pi}{%s}$ ($k \\in \\mathbb{Z}$)' %(latex(a1) if a1 != 1 else '', latex(mau_a_dung_1), latex(mau_a_dung_2))
            nb_da_1_s = 'Hàm số $y = \\tan \\left( %sx - \\frac{\\pi}{6} \\right)$ xác định khi: $x \\ne \\frac{\\pi}{3} + k\\frac{\\pi}{2}$ ($k \\in \\mathbb{Z}$)' %(latex(a1) if a1 != 1 else '')
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Hàm số $y = \\tan \\left( %sx - \\frac{\\pi}{6} \\right)$ xác định khi $\\cos \\left( %sx - \\frac{\\pi}{6} \\right) \\ne 0$ \\\\'''
                            '''$\\Leftrightarrow %sx - \\frac{\\pi}{6} \\ne \\frac{\\pi}{2} + k\\pi \\Leftrightarrow %sx \\ne \\frac{2\\pi}{3} + k\\pi \\Leftrightarrow x \\ne \\frac{2\\pi}{%s} + k\\frac{\\pi}{%s}$ ($k \\in \\mathbb{Z}$).'''
                            %(latex(a1) if a1 != 1 else '', latex(a1) if a1 != 1 else '', latex(a1) if a1 != 1 else '', latex(a1) if a1 != 1 else '', latex(mau_a_dung_1), latex(mau_a_dung_2)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Ý b: Hàm số y = cot(a2*x + pi/3) xác định khi a2*x + pi/3 != k*pi
            th_da_1_d = '\\True Hàm số $y = \\cot \\left( %sx + \\frac{\\pi}{3} \\right)$ xác định khi: $\\Leftrightarrow %sx + \\frac{\\pi}{3} \\ne k\\pi$ ($k \\in \\mathbb{Z}$)' %(latex(a2) if a2 != 1 else '', latex(a2) if a2 != 1 else '')
            th_da_1_s = 'Hàm số $y = \\cot \\left( %sx + \\frac{\\pi}{3} \\right)$ xác định khi: $\\Leftrightarrow %sx + \\frac{\\pi}{3} \\ne \\frac{\\pi}{2} + k\\pi$ ($k \\in \\mathbb{Z}$)' %(latex(a2) if a2 != 1 else '', latex(a2) if a2 != 1 else '')
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Hàm số $y = \\cot \\left( %sx + \\frac{\\pi}{3} \\right)$ xác định khi $\\sin \\left( %sx + \\frac{\\pi}{3} \\right) \\ne 0$ \\\\'''
                            '''$\\Leftrightarrow %sx + \\frac{\\pi}{3} \\ne k\\pi$ ($k \\in \\mathbb{Z}$).'''
                            %(latex(a2) if a2 != 1 else '', latex(a2) if a2 != 1 else '', latex(a2) if a2 != 1 else ''))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Ý c: Hàm số y = (1 - cos x)/sin x có tập xác định là D = R \ {k*pi}
            vd_da_1_d = '\\True Hàm số $y = \\frac{1 - \\cos x}{\\sin x}$ có tập xác định là $D = \\mathbb{R} \\setminus \\{k\\pi \\mid k \\in \\mathbb{Z}\\}$'
            vd_da_1_s = 'Hàm số $y = \\frac{1 - \\cos x}{\\sin x}$ có tập xác định là $D = \\mathbb{R} \\setminus \\{2k\\pi \\mid k \\in \\mathbb{Z}\\}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Hàm số $y = \\frac{1 - \\cos x}{\\sin x}$ xác định khi $\\sin x \\ne 0 \\Leftrightarrow x \\ne k\\pi$ ($k \\in \\mathbb{Z}$). \\\\'''
                            '''Vậy tập xác định của hàm số là $D = \\mathbb{R} \\setminus \\{k\\pi \\mid k \\in \\mathbb{Z}\\}$.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Ý d: Hàm số y = tan(a4*x)/cos x xác định khi cos(a4*x) != 0 và cos x != 0
            # cos(a4*x) != 0 <=> a4*x != pi/2 + k*pi <=> x != pi/(2*a4) + k*pi/a4
            # cos x != 0 <=> x != pi/2 + m*pi
            mau_d_1 = 2 * a4
            mau_d_2 = a4

            vdc_da_1_d = '\\True Hàm số $y = \\frac{\\tan %sx}{\\cos x}$ có tập xác định là $D = \\mathbb{R} \\setminus \\left( \\left\\{ \\frac{\\pi}{%s} + k\\frac{\\pi}{%s} \\mid k \\in \\mathbb{Z} \\right\\} \\cup \\left\\{ \\frac{\\pi}{2} + m\\pi \\mid m \\in \\mathbb{Z} \\right\\} \\right)$' %(latex(a4), latex(mau_d_1), latex(mau_d_2))
            vdc_da_1_s = 'Hàm số $y = \\frac{\\tan %sx}{\\cos x}$ có tập xác định là $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{8} + k\\frac{\\pi}{3} \\mid k \\in \\mathbb{Z} \\right\\}$' %(latex(a4))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Hàm số $y = \\frac{\\tan %sx}{\\cos x}$ xác định khi và chỉ khi cả tử số và mẫu số có nghĩa, mẫu số khác $0$: \\\\'''
                             '''$\\begin{cases} \\cos %sx \\ne 0 \\text{ (để } \\tan %sx \\text{ có nghĩa)} \\\\ \\cos x \\ne 0 \\text{ (mẫu thức khác } 0) \\end{cases} \\Leftrightarrow \\begin{cases} %sx \\ne \\frac{\\pi}{2} + k\\pi \\\\ x \\ne \\frac{\\pi}{2} + m\\pi \\end{cases} \\Leftrightarrow \\begin{cases} x \\ne \\frac{\\pi}{%s} + k\\frac{\\pi}{%s} \\\\ x \\ne \\frac{\\pi}{2} + m\\pi \\end{cases}$ ($k, m \\in \\mathbb{Z}$). \\\\'''
                             '''Vậy tập xác định của hàm số là $D = \\mathbb{R} \\setminus \\left( \\left\\{ \\frac{\\pi}{%s} + k\\frac{\\pi}{%s} \\mid k \\in \\mathbb{Z} \\right\\} \\cup \\left\\{ \\frac{\\pi}{2} + m\\pi \\mid m \\in \\mathbb{Z} \\right\\} \\right)$'''
                             %(latex(a4), latex(a4), latex(a4), latex(a4), latex(mau_d_1), latex(mau_d_2), latex(mau_d_1), latex(mau_d_2)))

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

