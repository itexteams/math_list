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


def bt_dang31_p2_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random cấu trúc góc lượng giác đặc biệt để sinh nhiều bài toán khác nhau
            # Chọn mẫu số là 3 (góc pi/3), 6 (góc pi/6) hoặc 4 (góc pi/4)
            mau_so = random.choice([3, 4, 6])

            if mau_so == 3:
                goc_latex = '\\frac{\\pi}{3}'
                val_sin = Rational(1, 2) * sqrt(3)
                val_cos = Rational(1, 2)
                val_tan = sqrt(3)
                # Tính sin(2*alpha) = sin(2*pi/3) = sqrt(3)/2
                val_sin2a = Rational(1, 2) * sqrt(3)
                val_sin2a_float = math.sqrt(3) / 2
            elif mau_so == 6:
                goc_latex = '\\frac{\\pi}{6}'
                val_sin = Rational(1, 2)
                val_cos = Rational(1, 2) * sqrt(3)
                val_tan = Rational(1, 3) * sqrt(3)
                # Tính sin(2*alpha) = sin(pi/3) = sqrt(3)/2
                val_sin2a = Rational(1, 2) * sqrt(3)
                val_sin2a_float = math.sqrt(3) / 2
            else:
                goc_latex = '\\frac{\\pi}{4}'
                val_sin = Rational(1, 2) * sqrt(2)
                val_cos = Rational(1, 2) * sqrt(2)
                val_tan = 1
                # Tính sin(2*alpha) = sin(pi/2) = 1
                val_sin2a = 1
                val_sin2a_float = 1.0

            # Nội dung câu hỏi
            noidungcauhoi = ('''Tính được các giá trị lượng giác của góc $\\alpha = %s + k2\\pi$ (biết $k \\in \\mathbb{Z}$). Xác định tính đúng, sai của các khẳng định''' 
                             %(goc_latex))

            ########################################################################
            # Nhận biết ############################################
            # Khẳng định về sin(alpha)
            nb_da_1_d = '\\True $\\sin \\alpha = %s$' %(latex(val_sin))
            nb_da_1_s = '$\\sin \\alpha = -%s$' %(latex(val_sin))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Do $\\alpha = %s + k2\\pi$ ($k \\in \\mathbb{Z}$) nên $\\sin \\alpha = \\sin \\left( %s + k2\\pi \\right) = \\sin \\frac{\\pi}{%s} = %s$.'''
                            %(goc_latex, goc_latex, latex(mau_so), latex(val_sin)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Khẳng định về cos(alpha)
            th_da_1_d = '\\True $\\cos \\alpha = %s$' %(latex(val_cos))
            th_da_1_s = '$\\cos \\alpha = -%s$' %(latex(val_cos))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Do $\\alpha = %s + k2\\pi$ ($k \\in \\mathbb{Z}$) nên $\\cos \\alpha = \\cos \\left( %s + k2\\pi \\right) = \\cos \\frac{\\pi}{%s} = %s$.'''
                            %(goc_latex, goc_latex, latex(mau_so), latex(val_cos)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Khẳng định về tan(alpha)
            vd_da_1_d = '\\True $\\tan \\alpha = %s$' %(latex(val_tan))
            vd_da_1_s = '$\\tan \\alpha = -%s$' %(latex(val_tan))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Do $\\alpha = %s + k2\\pi$ ($k \\in \\mathbb{Z}$) nên $\\tan \\alpha = \\tan \\left( %s + k2\\pi \\right) = \\tan \\frac{\\pi}{%s} = %s$.'''
                            %(goc_latex, goc_latex, latex(mau_so), latex(val_tan)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Khẳng định so sánh: ví dụ biểu thức 3*sin(2*alpha) > 2 hay không
            # Đối với mau_so = 3 hoặc 6: sin(2*alpha) = sqrt(3)/2 -> 3*sqrt(3)/2 \approx 2.598 > 2 (Đúng)
            # Đối với mau_so = 4: sin(2*alpha) = 1 -> 3*1 = 3 > 2 (Đúng)
            val_left = 3 * val_sin2a_float
            vdc_da_1_d = '\\True $3\\sin 2\\alpha > 2$'
            vdc_da_1_s = '$3\\sin 2\\alpha < 2$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            if mau_so in [3, 6]:
                goc_2a_latex = '\\frac{2\\pi}{3}' if mau_so == 3 else '\\frac{\\pi}{3}'
                loigiai_vdc_1 = ('''Ta có $2\\alpha = 2 \\left( %s + k2\\pi \\right) = %s + k4\\pi$. \\\\'''
                                 '''Do đó $\\sin 2\\alpha = \\sin %s = %s$. \\\\'''
                                 '''Suy ra $3\\sin 2\\alpha = 3 \\cdot %s = \\frac{3\\sqrt{3}}{2} \\approx 2,60 > 2$. Khẳng định $3\\sin 2\\alpha > 2$ là đúng.'''
                                 %(goc_latex, goc_2a_latex, goc_2a_latex, latex(val_sin2a), latex(val_sin2a)))
            else:
                loigiai_vdc_1 = ('''Ta có $2\\alpha = 2 \\left( \\frac{\\pi}{4} + k2\\pi \\right) = \\frac{\\pi}{2} + k4\\pi$. \\\\'''
                                 '''Do đó $\\sin 2\\alpha = \\sin \\frac{\\pi}{2} = 1$. \\\\'''
                                 '''Suy ra $3\\sin 2\\alpha = 3 \\cdot 1 = 3 > 2$. Khẳng định $3\\sin 2\\alpha > 2$ là đúng.''')

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

