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


def bt_dang21_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- BƯỚC 1: NGẪU NHIÊN DỮ LIỆU ---
            start_year = random.choice([1959, 1969, 1979, 1989])
            years = [start_year + i*10 for i in range(5)]
            pop = [random.randint(40, 50)]
            for i in range(4):
                pop.append(pop[-1] + random.randint(6, 14))

            # --- BƯỚC 2: TẠO HÌNH VẼ TIKZ (Sử dụng \\ thay cho r) ---
            tikz_code = '\\begin{center}\n\\begin{tikzpicture}[font=\\footnotesize, yscale=0.04, xscale=1.2, line join=round, line cap=round,>=stealth,thick]\n'
            tikz_code += '    \\draw[->] (0,0) -- (6,0) node[below] {Năm};\n'
            tikz_code += '    \\draw[->] (0,0) -- (0,110) node[above] {\\begin{tabular}{c} Dân số \\\\ (triệu người) \\end{tabular}};\n'
            tikz_code += '    \\foreach \\y in {0,20,40,60,80,100} \\draw (0.1,\\y) -- (-0.1,\\y) node[left] {\\y};\n'
            for i, (year, p) in enumerate(zip(years, pop)):
                tikz_code += '    \\draw[fill=blue!70] (' + str(i+1) + '-0.3,0) rectangle (' + str(i+1) + '+0.3,' + str(p) + ');\n'
                tikz_code += '    \\node[above] at (' + str(i+1) + ',' + str(p) + ') {' + str(p) + '};\n'
                tikz_code += '    \\node[below] at (' + str(i+1) + ',0) {' + str(year) + '};\n'
            tikz_code += '\\end{tikzpicture}\n\\end{center}'

            # --- BƯỚC 3: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Cho biểu đồ ước tính dân số Việt Nam qua một số thập niên như sau:
            %s
            Nếu coi $x$ là năm và $y$ là số dân Việt Nam thì $x$ là biến số và $y$ là hàm số của $x$.''' % (tikz_code))

            ########################################################################
            # Nhận biết
            nb_da_1_d = '\\True Tập xác định của hàm số là $D = \\{' + "; ".join(map(str, years)) + '\\}$'
            nb_da_1_s = 'Tập xác định của hàm số là $D = \\mathbb{R}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            loigiai_nb_1 = ('Tập xác định của hàm số là $D = \\{' + "; ".join(map(str, years)) + '\\}$.')

            ########################################################################
            # Thông hiểu
            th_da_1_d = '\\True Tập giá trị của hàm số là $T = \\{' + "; ".join(map(str, pop)) + '\\}$'
            th_da_1_s = 'Tập giá trị của hàm số là $T = \\{0; ' + str(max(pop)) + '\\}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            loigiai_th_1 = ('Tập giá trị của hàm số là $T =\\{' + "; ".join(map(str, pop)) + '\\}$.')

            ########################################################################
            # Vận dụng
            vd_da_1_d = '\\True Quan sát biểu đồ ta thấy khi $x$ tăng thì giá trị $y$ tăng nên hàm số đồng biến trên tập xác định.'
            vd_da_1_s = 'Quan sát biểu đồ ta thấy khi $x$ tăng thì giá trị $y$ giảm nên hàm số nghịch biến.'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            loigiai_vd_1 = ('Quan sát biểu đồ ta thấy khi $x$ tăng thì giá trị $y$ tăng nên hàm số đồng biến trên tập xác định.')

            ########################################################################
            # Vận dụng cao
            diffs = [pop[i+1] - pop[i] for i in range(4)]
            max_diff = max(diffs)
            max_idx = diffs.index(max_diff)
            best_period = str(years[max_idx]) + ' đến ' + str(years[max_idx+1])

            vdc_da_1_d = '\\True Trong khoảng thời gian từ ' + best_period + ' dân số Việt Nam tăng nhanh nhất.'
            vdc_da_1_s = 'Trong khoảng thời gian từ ' + str(years[0]) + ' đến ' + str(years[1]) + ' dân số Việt Nam tăng nhanh nhất.'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            calc_steps = ""
            for i in range(4):
                calc_steps += 'Trong khoảng thời gian từ ' + str(years[i]) + ' đến ' + str(years[i+1]) + ' dân số Việt Nam ' + str(pop[i+1]) + ' $-$ ' + str(pop[i]) + ' = ' + str(diffs[i]) + '.\\\\ '
            loigiai_vdc_1 = (calc_steps + 'Vậy trong khoảng thời gian từ ' + best_period + ' dân số Việt Nam tăng nhanh nhất.')

            ########################################################################
            # Lặp chọn đáp án đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= sum('\\True' in a for a in [nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # --- BƯỚC 4: XUẤT NỘI DUNG (KHÔNG DÙNG r) ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(nb_sel)+'}\n'
                '{'+str(th_sel)+'}\n'
                '{'+str(vd_sel)+'}\n'
                '{'+str(vdc_sel)+'}\n'
                ' \\loigiai{ \n'
                ' \\begin{enumEX}[a)]{1} \n'
                ' \\item '+str(loigiai_nb_1)+'\n'
                ' \\item '+str(loigiai_th_1)+'\n'
                ' \\item '+str(loigiai_vd_1)+'\n'
                ' \\item '+str(loigiai_vdc_1)+'\n'
                ' \\end{enumEX}} \n'
                ' \\end{ex}\n \\end{minipage} \n\n')
            return content

