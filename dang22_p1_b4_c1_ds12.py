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


def bt_dang22_p1_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hoành độ cực trị (x1, x2) và tung độ cực trị (y1, y2)
                x1 = random.randint(-4, 2)
                x2 = x1 + random.randint(1, 5)
                y1 = random.randint(1, 6)
                y2 = y1 - random.randint(2, 8)

                # Tính tọa độ tâm đối xứng (x0, y0)
                x0 = Rational(x1 + x2, 2)
                y0 = Rational(y1 + y2, 2)

                # Random các hệ số a, b, c cho biểu thức
                a = random.choice([-3, -2, -1, 2, 3])
                b = random.choice([-3, -2, -1, 2, 3])
                c = random.randint(-5, 5)

                # Tính giá trị biểu thức T = a*x0 + b*y0 + c
                T = a * x0 + b * y0 + c

                # Hàm hỗ trợ định dạng số
                def format_num(val):
                    return latex(val).replace('.', ',')

                # Đáp án đúng
                da = format_num(T)

                # Tạo biểu thức P dạng LaTeX
                X, Y = symbols('x_0 y_0')
                expr_P = a * X + b * Y + c
                P_latex = latex(expr_P)

                # Tạo các phương án nhiễu
                s = [
                    format_num(T + 1), 
                    format_num(T - 1), 
                    format_num(T + 2), 
                    format_num(T - 2), 
                    format_num(-T) if T != 0 else format_num(T + 3),
                    format_num(a * y0 + b * x0 + c), # nhiễu do hoán vị x0, y0
                    format_num(a * x1 + b * y1 + c)  # nhiễu do lấy nhầm điểm cực trị
                ]

                # Lọc bỏ các phương án nhiễu trùng với đáp án đúng và trùng nhau
                s = list(set(s) - {da})
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Vẽ bảng biến thiên bằng TikZ (tkz-tab), giữ khung
                bbt = ('''\\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[lgt=1.2,espcl=2.5]
            {$x$ /0.7, $y'$ /0.7, $y$ /2}
            {$-\\infty$, $%s$, $%s$, $+\\infty$}
            \\tkzTabLine{ ,+, 0, -, 0, +, }
            \\tkzTabVar{-/ $-\\infty$, +/ $%s$, -/ $%s$, +/ $+\\infty$}
            \\end{tikzpicture}
            \\end{center}''' % (latex(x1), latex(x2), latex(y1), latex(y2)))

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = ax^3 + bx^2 + cx + d$ có bảng biến thiên như sau:
            %s
            Biết tâm đối xứng của đồ thị hàm số trên có tọa độ là $(x_0; y_0)$. Giá trị của biểu thức $P = %s$ bằng''' % (bbt, P_latex))

                # Các đáp án
                da_d = ('\\True $%s$' % str(da))
                da_s1 = '$%s$' % str(das1)
                da_s2 = '$%s$' % str(das2)
                da_s3 = '$%s$' % str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xử lý hiển thị dấu của hệ số tự do c trong bước thay số
                c_str = f'+ {c}' if c > 0 else (f'- {-c}' if c < 0 else '')

                # Nội dung lời giải
                loigiai = ('''Đồ thị hàm số bậc ba nhận điểm uốn làm tâm đối xứng.\\\\
            Tọa độ điểm uốn là trung bình cộng tọa độ hai điểm cực trị của đồ thị hàm số.\\\\
            Từ bảng biến thiên, đồ thị hàm số có hai điểm cực trị là $A(%s; %s)$ và $B(%s; %s)$.\\\\
            Tọa độ tâm đối xứng $(x_0; y_0)$ là:
            $$\\begin{cases} x_0 = \\frac{x_A + x_B}{2} = \\frac{%s + %s}{2} = %s \\\\ y_0 = \\frac{y_A + y_B}{2} = \\frac{%s + %s}{2} = %s \\end{cases}$$
            Thay $x_0 = %s$ và $y_0 = %s$ vào biểu thức $P = %s$, ta được:
            $$P = %s \\cdot \\left(%s\\right) + %s \\cdot \\left(%s\\right) %s = %s$$
            Vậy giá trị của biểu thức là $%s$.''' % 
                (latex(x1), latex(y1), latex(x2), latex(y2), 
                 latex(x1), latex(x2), latex(x0), 
                 latex(y1), latex(y2), latex(y0),
                 latex(x0), latex(y0), P_latex,
                 latex(a), latex(x0), latex(b), latex(y0), c_str, str(da),
                 str(da)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n').replace('+ -', '-')
            return content

