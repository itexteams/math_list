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


def bt_dang11_p3_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các số liệu cho đồ thị hàm bậc 3 (điểm cực đại và cực tiểu)
                # Để giống chuẩn hình vẽ, giữ nguyên đỉnh cực đại trên trục Oy (x1 = 0)
                x1 = 0
                x2 = random.choice([1, 2, 3])
                y1 = random.choice([2, 3, 4, 5])
                y2 = random.choice([-2, -1, 0, 1])

                # Đảm bảo hoành độ và tung độ hợp lý (Cực đại cao hơn cực tiểu)
                if y1 <= y2:
                    y1 = y2 + 2

                # Tính tọa độ điểm uốn I(x0, y0) là trung điểm của 2 điểm cực trị
                x0 = Rational(x1 + x2, 2)
                y0 = Rational(y1 + y2, 2)

                # Tính giá trị biểu thức đích: T = x0 + 3*y0
                kq = x0 + 3 * y0

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq).replace('.', ','))]
                da = random.choice(du)

                # Tạo danh sách các đáp án sai độc nhất
                s_set = set()
                for delta in [-2, -1, 1, 2, 3, Rational(1, 2), Rational(-1, 2)]:
                    wrong_val = kq + delta
                    if wrong_val != kq:
                        s_set.add('$%s$' % (latex(wrong_val).replace('.', ',')))

                s = list(s_set)
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Tính toán các hệ số của hàm số bậc 3: y = ax^3 + bx^2 + cx + d để vẽ TikZ
                # y = a*x^3 + b*x^2 + y1
                a_coef = float(2 * (y1 - y2)) / (x2**3)
                b_coef = float(-3 * (y1 - y2)) / (x2**2)
                d_coef = float(y1)

                # Định nghĩa ranh giới trục tọa độ cho TikZ
                x_min_val = -2.0
                x_max_val = x2 + 1.5
                y_min_val = y2 - 1.5
                y_max_val = y1 + 1.5

                # Tạo tick marks cho trục x và trục y tự động
                x_ticks_list = [i for i in range(int(math.ceil(x_min_val)), int(math.floor(x_max_val)) + 1) if i != 0]
                y_ticks_list = [i for i in range(int(math.ceil(y_min_val)), int(math.floor(y_max_val)) + 1) if i != 0]

                x_ticks_str = ",".join(["%s/%s" % (i, i) for i in x_ticks_list])
                y_ticks_str = ",".join(["%s/%s" % (i, i) for i in y_ticks_list])

                x_ticks_code = "\\foreach \\x/\\nx in {%s} \\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$};" % x_ticks_str if x_ticks_list else ""
                y_ticks_code = "\\foreach \\y/\\ny in {%s} \\draw[thin] (1pt,\\y)--(-1pt,\\y) node [left] {$\\ny$};" % y_ticks_str if y_ticks_list else ""

                # Dựng mã TikZ động theo dữ liệu đã random
                tikz_code = ('''\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt]
            \\tikzset{every node/.style={scale=0.9}}
            \\draw[->] (%s,0)--(%s,0) node[below left] {$x$};
            \\draw[->] (0,%s)--(0,%s) node[below left] {$y$};
            \\draw (0,0) node [below left] {$O$};
            %s
            %s
            \\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s);
            \\begin{scope}
            \\clip (%s,%s) rectangle (%s,%s);
            \\draw[samples=200,domain=%s:%s,smooth,variable=\\x] plot (\\x,{%s*(\\x)^3 + %s*(\\x)^2 + %s});
            \\end{scope}
            \\end{tikzpicture}''' % (
                    str(x_min_val), str(x_max_val),
                    str(y_min_val), str(y_max_val),
                    x_ticks_code,
                    y_ticks_code,
                    latex(x2), latex(x2), latex(y2), latex(y2),
                    str(x_min_val), str(y_min_val), str(x_max_val), str(y_max_val),
                    str(x_min_val), str(x_max_val),
                    str(a_coef), str(b_coef), str(d_coef)
                ))

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = ax^3 + bx^2 + cx + d$ có đồ thị như hình vẽ.
            \\begin{center}
            %s
            \\end{center}
            Gọi $I(x_0; y_0)$ là tọa độ điểm đối xứng của đồ thị hàm số trên. Giá trị $x_0 + 3y_0$ bằng bao nhiêu?''' % (tikz_code))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Từ đồ thị hàm số, ta thấy hàm số đạt cực đại tại điểm $A(%s; %s)$ và đạt cực tiểu tại điểm $B(%s; %s)$. \\\\
            Đồ thị hàm số bậc ba nhận điểm uốn làm tâm đối xứng. Điểm uốn $I(x_0; y_0)$ của đồ thị là trung điểm của đoạn thẳng nối hai điểm cực trị $A$ và $B$. \\\\
            Do đó, tọa độ điểm $I$ được tính như sau: \\\\
            $x_0 = \\frac{x_A + x_B}{2} = \\frac{%s + %s}{2} = %s$ \\\\
            $y_0 = \\frac{y_A + y_B}{2} = \\frac{%s + %s}{2} = %s$ \\\\
            Suy ra tọa độ điểm đối xứng là $I(%s; %s)$. \\\\
            Vậy giá trị của biểu thức $x_0 + 3y_0 = %s + 3 \\cdot \\left(%s\\right) = %s$.''' % (
                    latex(x1), latex(y1), latex(x2), latex(y2),
                    latex(x1), latex(x2), latex(x0),
                    latex(y1), latex(y2), latex(y0),
                    latex(x0), latex(y0),
                    latex(x0), latex(y0), latex(kq).replace('.', ',')
                ))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

