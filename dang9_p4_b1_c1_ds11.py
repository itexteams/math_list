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


def bt_dang9_p4_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            a = random.choice([8, 10, 12])
            b = random.choice([15, 18, 20])

            # Các trường hợp giá trị của sin(theta) để tính diện tích và thời điểm tương ứng
            # (sin_k_latex, angle1_latex, angle2_latex, t_exact_latex, t_approx_str, k_sympy, t_float)
            choices = [
                ('\\frac{1}{2}', '\\frac{\\pi}{6}', '\\frac{5\\pi}{6}', '\\frac{60}{11}', '5,5', Rational(1,2), 60/11),
                ('\\frac{\\sqrt{2}}{2}', '\\frac{\\pi}{4}', '\\frac{3\\pi}{4}', '\\frac{90}{11}', '8,2', sqrt(2)/2, 90/11),
                ('\\frac{\\sqrt{3}}{2}', '\\frac{\\pi}{3}', '\\frac{2\\pi}{3}', '\\frac{120}{11}', '10,9', sqrt(3)/2, 120/11)
            ]

            sin_k_latex, angle1_latex, angle2_latex, t_exact_latex, t_approx_str, k_sympy, t_float = random.choice(choices)

            # Tính diện tích S
            S_sympy = sp.simplify((a * b * k_sympy) / 2)
            if k_sympy == Rational(1,2):
                S_val = (a * b) / 4.0
                if S_val.is_integer():
                    S_latex = str(int(S_val))
                else:
                    S_latex = str(S_val).replace('.', ',')
            else:
                S_latex = latex(S_sympy).replace('.', ',')

            kq4 = round(t_float, 1)

            # Các đáp án trắc nghiệm
            du = ['$%s$'%(t_approx_str)]
            da = random.choice(du)

            # Tạo các phương án sai xung quanh đáp án đúng
            s = [
                '$%s$'%(str(round(kq4 + 0.1, 1)).replace('.', ',')),
                '$%s$'%(str(round(kq4 - 0.1, 1)).replace('.', ',')),
                '$%s$'%(str(round(kq4 + 1.0, 1)).replace('.', ',')),
                '$%s$'%(str(round(kq4 - 1.0, 1)).replace('.', ',')),
                '$%s$'%(str(round(kq4 + 1.1, 1)).replace('.', ',')),
                '$%s$'%(str(round(kq4 - 1.1, 1)).replace('.', ','))
            ]

            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)

            # Mã vẽ TikZ (Đã cập nhật theo mẫu yêu cầu)
            tikz_code = (
            '\\begin{tikzpicture}[thick, scale=0.9]\n'
            '    \\draw[line width=9pt, color=violet] (0,0) circle (2.7cm);\n'
            '    \\draw (0,0) circle (2.5cm);\n'
            '    \\foreach \\i in {0,6,...,354}\n'
            '        \\draw (\\i:2.3cm) -- (\\i:2.5cm);\n'
            '    \\foreach \\i in {0,30,...,330}\n'
            '        \\draw[line width=1.5pt] (\\i:2.2cm) -- (\\i:2.5cm);\n'
            '    \\foreach \\i/\\j in {90/12, 60/1, 30/2, 0/3, -30/4, -60/5, -90/6, -120/7, -150/8, -180/9, -210/10, -240/11}\n'
            '        \\draw (\\i:1.9cm) node{\\textbf{\\j}};\n'
            '    \\draw[dashed] (0,-2.5) -- (0,2.5);\n'
            '    \\node at (82:1.5cm) {$\\Delta$};\n'
            '    \\draw[line width=3pt, color=red] (0,0) -- (75:1.3cm) node[right] {$A$};\n'
            '    \\draw[line width=2pt, color=blue] (0,0) -- (0:2cm) node[right] {$B$};\n'
            '    \\fill (0,0) circle (0.1cm) node[left] {$O$};\n'
            '    \\draw[blue, thick] (75:2.9cm) arc (75:90:2.9cm) node[midway, above] {$l$};\n'
            '\\end{tikzpicture}\n'
            )

            # Câu hỏi
            noidungcauhoi = ('''\\immini{Ngày nay, để giúp xác định nhanh hàng thật hay giả 1 chiếc đồng hồ Rolex, ta dựa vào tốc độ góc thay đổi giữa các kim của đồng hồ (rad/phút). Chiếc đồng hồ Rolex được thẩm định có kích thước chuẩn (loại cho nam) ở kim giờ và kim phút lần lượt là $%s$ mm và $%s$ mm. Biết rằng góc giữa hai kim là hàm $\\theta(t)$ với $t$ là số phút thể hiện sau 12 giờ chiều (tức thời điểm hai kim trùng nhau chỉ vào số 12). Tìm thời điểm $t$ đầu tiên mà diện tích tam giác $OAB$ bằng $%s$ $\\text{mm}^2$ (Kết quả làm tròn đến hàng phần chục).}{%s}'''
                             %(a, b, S_latex, tikz_code))

            # Các đáp án
            da_d = ('\\True ' +str(da))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ('''Tốc độ quay của kim giờ là: $\\frac{360^\\circ}{12 \\cdot 60} = 0,5^\\circ/\\text{phút}$; tốc độ quay của kim phút là $\\frac{360^\\circ}{60} = 6^\\circ/\\text{phút}$\\\\
            Sau thời gian $t$ phút thì kim giờ quay được $0,5t$ (độ), kim phút quay được $6t$ (độ)\\\\
            Góc tạo bởi hai kim là: $\\theta(t) = 6t - 0,5t = 5,5t$ (độ) hay $\\theta(t) = \\frac{11\\pi t}{360}$ (rad)\\\\
            Khi $\\Delta OAB$ có diện tích bằng $%s$ $\\text{mm}^2$\\\\
            $\\Leftrightarrow \\frac{1}{2} \\cdot %s \\cdot %s \\cdot \\sin(\\theta(t)) = %s \\Leftrightarrow \\sin(\\theta(t)) = %s \\Leftrightarrow \\left[ \\begin{array}{l} \\theta(t) = %s \\\\ \\theta(t) = %s \\end{array} \\right.$\\\\
            Thời điểm $t$ nhỏ nhất sẽ ứng với góc $t$ nhỏ nhất nên ta sẽ đi tìm $t$ để $\\theta(t) = %s \\Leftrightarrow \\frac{11\\pi t}{360} = %s$\\\\
            Suy ra $t = %s \\approx %s$ (phút)\\\\
            Vậy tại thời điểm $t = %s \\approx %s$ phút kể từ lúc 12 giờ chiều thì diện tích $\\Delta OAB$ bằng $%s$ $\\text{mm}^2$.'''
            % (S_latex, a, b, S_latex, sin_k_latex, angle1_latex, angle2_latex, angle1_latex, angle1_latex, t_exact_latex, t_approx_str, t_exact_latex, t_approx_str, S_latex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

