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


def bt_dang4_p3_b1_c2_ds10(self):
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
            noidungcauhoi = ('''Cho bất phương trình $%sx + %sy \\le %s$ (1). Cho $a_n; b_n$ ($n \\in \\mathbb{N}^*$) là các số nguyên dương và các cặp số $(a_n; b_n)$ là các nghiệm của bất phương trình (1). Cho tổng $S_n = a_n + b_n$. Giá trị $P_n = S_1 + S_2 + \\dots + S_n$ bằng bao nhiêu?'''
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

            # ==========================================
            # Xây dựng code TikZ tự động
            # ==========================================
            # Tính toán giới hạn của lưới và trục để vẽ vừa vặn
            xmax_val = int(c/a) + 3
            ymax_val = int(c/b) + 3

            # Tọa độ giới hạn đường thẳng y = (c - ax) / b tại biên x = -2 và x = xmax_val
            y_start = (c + 2 * a) / b  
            y_end = (c - a * xmax_val) / b  

            tikz_str = "\\begin{center}\n"
            tikz_str += "\\begin{tikzpicture}[>=stealth, scale=0.8, line width=1pt]\n"


            # Lệnh clip để giới hạn vùng hiển thị
            tikz_str += f"\\clip (-2,-2) rectangle ({xmax_val},{ymax_val});\n"

            # Tô mẫu (pattern) gạch chéo cho toàn bộ vùng
            tikz_str += f"\\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle ({xmax_val},{ymax_val});\n"

            # Tô màu trắng cho phần miền nghiệm (phần dưới đường thẳng ax + by = c)
            tikz_str += f"\\fill[white] (-2,-2) -- ({xmax_val},-2) -- ({xmax_val},{y_end:.2f}) -- (-2,{y_start:.2f}) -- cycle;\n"

            # Vẽ đường thẳng biên
            tikz_str += f"\\draw[black] (-2, {y_start:.2f}) -- ({xmax_val}, {y_end:.2f});\n"

            # Vẽ và đánh dấu các điểm nghiệm
            letters = ["A", "B", "C", "D", "E", "F"]
            for i, (x_val, y_val) in enumerate(sols):
                point_name = letters[i % len(letters)]
                tikz_str += f"\\coordinate ({point_name}) at ({x_val},{y_val});\n"
                # Đánh dấu điểm với tọa độ
                tikz_str += f"\\fill ({point_name}) circle (0.5pt) node[above right] {{$({x_val}; {y_val})$}};\n"

            # Vẽ trục tọa độ
            tikz_str += f"\\draw[->] (-2, 0) -- ({xmax_val}, 0) node[below] {{$x$}};\n"
            tikz_str += f"\\draw[->] (0, -2) -- (0, {ymax_val}) node[left] {{$y$}};\n"
            tikz_str += "\\node at (0,0) [below left] {$O$};\n"                

            tikz_str += "\\end{tikzpicture}\n"
            tikz_str += "\\end{center}"

            # ==========================================
            # Xây dựng nội dung lời giải
            # ==========================================
            loigiai_header = ('''Vẽ đường thẳng $%sx + %sy = %s$ và gạch bỏ miền không thỏa mãn bất phương trình (1). \\\\
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
                calc_str += f'$S_{i+1} = {sols[i][0]} + {sols[i][1]} = {s_val}$'
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
            dapan='\\shortans[0]{$%s$}\n'%(str(da))

            # ==========================================
            # Xuất câu trắc nghiệm
            # ==========================================
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

