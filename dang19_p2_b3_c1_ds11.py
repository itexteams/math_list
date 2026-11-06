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


def bt_dang19_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số cho hàm số f(x) = sqrt(a - b*sin^2 x) sao cho a > b > 0 để tập xác định luôn là R
            b = randint(2, 4)
            a = b + randint(1, 3)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho các hàm số sau: $f(x) = \\sqrt{%s - %s\\sin^2 x}$; $g(x) = \\tan x - x\\cos x$. Khi đó:''' 
                             %(latex(a), latex(b)))

            ########################################################################
            # Nhận biết ############################################
            # Ý a: Tập xác định hàm số f(x) là D = R
            nb_da_1_d = '\\True Tập xác định hàm số $f(x)$ là: $D = \\mathbb{R}$'
            nb_da_1_s = 'Tập xác định hàm số $f(x)$ là: $D = [0; +\\infty)$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Hàm số $f(x) = \\sqrt{%s - %s\\sin^2 x}$ xác định khi và chỉ khi $%s - %s\\sin^2 x \\ge 0 \\Leftrightarrow \\sin^2 x \\le \\frac{%s}{%s}$.\\\\'''
                            '''Vì $0 \\le \\sin^2 x \\le 1$ với mọi $x \\in \\mathbb{R}$ và $\\frac{%s}{%s} > 1$, nên bất phương trình này luôn đúng với mọi $x \\in \\mathbb{R}$.\\\\'''
                            '''Do đó tập xác định của hàm số $f(x)$ là $D = \\mathbb{R}$.'''
                            %(latex(a), latex(b), latex(a), latex(b), latex(a), latex(b), latex(a), latex(b)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Ý b: Hàm số f(x) đã cho là hàm số lẻ (Sai vì f(-x) = f(x) nên f là hàm số chẵn)
            th_da_1_d = 'Hàm số $f(x)$ đã cho là hàm số lẻ'
            th_da_1_s = '\\True Hàm số $f(x)$ đã cho là hàm số chẵn'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Hàm số $f(x)$ có tập xác định $D = \\mathbb{R}$ là tập đối xứng.\\\\'''
                            '''Với mọi $x \\in \\mathbb{R}$, ta có $-x \\in \\mathbb{R}$ và:\\\\'''
                            '''$f(-x) = \\sqrt{%s - %s\\sin^2(-x)} = \\sqrt{%s - %s[-\\sin x]^2} = \\sqrt{%s - %s\\sin^2 x} = f(x)$.\\\\'''
                            '''Vì $f(-x) = f(x)$ nên hàm số $f(x)$ đã cho là hàm số chẵn (khẳng định là hàm số lẻ là sai).'''
                            %(latex(a), latex(b), latex(a), latex(b), latex(a), latex(b)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Ý c: Tập xác định hàm số g(x) là D = R \ {pi/2 + k*pi}
            vd_da_1_d = '\\True Tập xác định hàm số $g(x)$ là: $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
            vd_da_1_s = 'Tập xác định hàm số $g(x)$ là: $D = \\mathbb{R} \\setminus \\left\\{ k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Hàm số $g(x) = \\tan x - x\\cos x$ xác định khi và chỉ khi thành phần $\\tan x$ có nghĩa,\\\\'''
                            '''tức là $\\cos x \\ne 0 \\Leftrightarrow x \\ne \\frac{\\pi}{2} + k\\pi$ ($k \\in \\mathbb{Z}$).\\\\'''
                            '''Vậy tập xác định của hàm số $g(x)$ là $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Ý d: Hàm số g(x) đã cho là hàm số lẻ
            vdc_da_1_d = '\\True Hàm số $g(x)$ đã cho là hàm số lẻ'
            vdc_da_1_s = 'Hàm số $g(x)$ đã cho là hàm số chẵn'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Hàm số $g(x)$ có tập xác định $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\mid k \\in \\mathbb{Z} \\right\\}$ là tập đối xứng.\\\\'''
                             '''Với mọi $x \\in D$, ta có $-x \\in D$ và:\\\\'''
                             '''$g(-x) = \\tan(-x) - (-x)\\cos(-x) = -\\tan x + x\\cos x = -(\\tan x - x\\cos x) = -g(x)$.\\\\'''
                             '''Vì $g(-x) = -g(x)$ nên hàm số $g(x)$ đã cho là hàm số lẻ.''')

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

            # Gán lại vào list sau khi lọc điều kiện đạt yêu cầu
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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn theo đúng cấu trúc format mẫu
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

