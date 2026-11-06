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


def bt_dang5_p4_b1_c2_ds10(self):
            # Khai báo biến
            # ==========================================

            while True:
                # Random các hệ số a, b của bất phương trình ax + by <= c
                a = random.randint(2, 5) # Hệ số x
                b = random.randint(2, 5) # Hệ số y
                if a == b: # Tránh trường hợp a=b để bài toán đa dạng
                    continue

                # Ràng buộc c để đảm bảo có nghiệm nguyên dương
                c = random.randint(a + b, a + b + 6) 

                # Thuật toán tìm nghiệm nguyên dương
                sols = []
                for x_val in range(1, math.floor(c / a) + 1):
                    rem_c = c - a * x_val
                    for y_val in range(1, math.floor(rem_c / b) + 1):
                        sols.append((x_val, y_val))

                # Chỉ lấy các trường hợp có từ 1 đến 3 nghiệm
                if 1 <= len(sols) <= 3:
                    if len(sols) > 1:
                        random.shuffle(sols)
                    break

            # Tính toán các giá trị S_i và P_n
            s_list = []
            for x_val, y_val in sols:
                s_list.append(x_val + y_val)

            P_n = sum(s_list)
            n_nghiem = len(sols)

            # Các đáp án trắc nghiệm
            du = ['$%s$'%(P_n)]
            da = random.choice(du)

            # Tạo các đáp án gây nhiễu
            s_distract = [P_n + 1, P_n + 2, P_n - 1, P_n + 3, P_n - 2, P_n + 4, P_n - 3]
            s_distract = [val for val in s_distract if val > 0] # Đảm bảo đáp án nhiễu dương
            s_distract = list(set(s_distract))
            if P_n in s_distract:
                s_distract.remove(P_n)
            random.shuffle(s_distract)

            das1 = '$%s$'%(s_distract[0])
            das2 = '$%s$'%(s_distract[1])
            das3 = '$%s$'%(s_distract[2])

            # ==========================================
            # Câu hỏi
            # ==========================================
            noidungcauhoi = ('''Cho bất phương trình $%sx + %sy \\le %s$ (1). Cho $a_n; b_n$ ($n \\in \\mathbb{N}^*$) là các số nguyên dương và các cặp số $(a_n; b_n)$ là các nghiệm của bất phương trình (1). Cho tổng $S_n = a_n + b_n$. Tính $P_n = S_1 + S_2 + \\dots + S_n$.'''
                                 %(a, b, c))

            # ==========================================
            # Trộn các đáp án
            # ==========================================
            da_d = ('\\True ' +str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            dapan_str = "\\shortans[0]{$" + str(P_n) + "$}\n"

            # ==========================================
            # Xây dựng code TikZ tự động
            # ==========================================
            # Tính toán giới hạn của lưới và trục để vẽ vừa vặn
            xmax_val = int(c/a) + 2
            ymax_val = int(c/b) + 2

            # Tọa độ giới hạn đường thẳng y = (c - ax) / b
            y_start = (c + 1.5 * a) / b
            y_end = (c - a * (xmax_val + 1)) / b

            # Tạo danh sách các số trên trục tọa độ (bỏ qua số 0 vì đã đánh dấu O)
            x_ticks = "-1, 1"
            for i in range(2, xmax_val): x_ticks += f", {i}"
            y_ticks = "-1, 1"
            for i in range(2, ymax_val): y_ticks += f", {i}"

            # Sinh mã TikZ theo phong cách yêu cầu
            tikz_str = "\\begin{center}\n"
            tikz_str += "\\begin{tikzpicture}[>=stealth, scale=0.8, line width=1pt]\n"


            # Cắt viền và tô miền bị gạch
            tikz_str += f"\\clip (-1.5, -1.5) rectangle ({xmax_val}, {ymax_val});\n"
            tikz_str += f"\\fill[pattern=north east lines, pattern color=black] (-1.5,-1.5) rectangle ({xmax_val},{ymax_val});\n"

            # Tô trắng phần miền nghiệm (nửa mặt phẳng chứa O(0,0))
            tikz_str += f"\\fill[white] (-1.5, -1.5) -- ({xmax_val + 1}, -1.5) -- ({xmax_val + 1}, {y_end:.2f}) -- (-1.5, {y_start:.2f}) -- cycle;\n"

            # Vẽ lưới đứt nét để dễ nhìn (tuỳ chọn)
            tikz_str += f"\\draw[lightgray, dashed, line width=0.5pt] (-1,-1) grid ({xmax_val},{ymax_val});\n"

            # Vẽ đường thẳng bờ
            tikz_str += f"\\draw[black] (-1.5, {y_start:.2f}) -- ({xmax_val + 1}, {y_end:.2f});\n"

            # Số chia trên trục
            tikz_str += f"\\foreach \\x in {{ {x_ticks} }} \\draw[black] (\\x, 0.1) -- (\\x, -0.1) node[below, font=\\footnotesize] {{$\\x$}};\n"
            tikz_str += f"\\foreach \\y in {{ {y_ticks} }} \\draw[black] (0.1, \\y) -- (-0.1, \\y) node[left, font=\\footnotesize] {{$\\y$}};\n"

            # Vẽ và ghi tọa độ điểm nghiệm
            for x_val, y_val in sols:
                tikz_str += f"\\fill[black] ({x_val}, {y_val}) circle (1pt) node[above right, font=\\footnotesize] {{$({x_val}; {y_val})$}};\n"

            # Vẽ trục
            tikz_str += f"\\draw[->] (-1.5, 0) -- ({xmax_val + 1}, 0) node[below] {{$x$}};\n"
            tikz_str += f"\\draw[->] (0, -1.5) -- (0, {ymax_val + 1}) node[left] {{$y$}};\n"
            tikz_str += "\\node at (0,0) [below left] {$O$};\n"                

            tikz_str += "\\end{tikzpicture}\n"
            tikz_str += "\\end{center}"

            # ==========================================
            # Xây dựng nội dung lời giải
            # ==========================================
            loigiai_header = ('''Vẽ đường thẳng $%sx + %sy = %s$ và biểu diễn miền nghiệm của bất phương trình (1) (phần không bị gạch). \\\\
                Khi đó ta dễ dàng thấy rằng có %s nghiệm nguyên dương thỏa mãn là '''
                    %(a, b, c, n_nghiem if n_nghiem > 1 else 'duy nhất'))

            loigiai_nghiem = ""
            for i, (x_val, y_val) in enumerate(sols):
                loigiai_nghiem += f'$({x_val}; {y_val})$'
                if i < n_nghiem - 1:
                    loigiai_nghiem += ", "
            loigiai_nghiem += ". \\\\"

            calc_str = ""
            for i, s_val in enumerate(s_list):
                calc_str += f'$S_{{{i+1}}} = {sols[i][0]} + {sols[i][1]} = {s_val}$'
                if i < n_nghiem - 1:
                    calc_str += ", "
            calc_str += ". "

            loigiai_sum = ""
            if n_nghiem == 1:
                loigiai_sum = f'Vậy $P_1 = S_1 = {sols[0][0]} + {sols[0][1]} = {P_n}$.'
            else:
                sum_list_str = " + ".join([str(val) for val in s_list])
                loigiai_sum = f'Ta có {calc_str} \\\\ Vậy $P_n = {sum_list_str} = {P_n}$.'

            # Ghép toàn bộ nội dung lời giải
            loigiai = loigiai_header + loigiai_nghiem + "\n" + tikz_str + "\n" + loigiai_sum

            # Xử lý hiển thị dấu: - - là +, + - là -
            noidungcauhoi = noidungcauhoi.replace('+ -', '-').replace('- -', '+')
            loigiai = loigiai.replace('+ -', '-').replace('- -', '+')

            # ==========================================
            # Xuất câu trắc nghiệm
            # ==========================================
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

