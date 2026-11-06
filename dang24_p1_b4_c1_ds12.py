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


def bt_dang24_p1_b4_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tạo hàm số y = ax^3 + bx^2 + cx + d
                # Chọn x1, x2 là hoành độ cực trị (khoảng cách là 2 để tâm đối xứng ra số nguyên)
                x1 = random.randint(-2, 1)
                x2 = x1 + 2

                # Chọn a = 1 hoặc -1 để lật đồ thị ngẫu nhiên
                a_val = random.choice([1, -1])

                # Tính b, c để hàm số có cực trị tại x1, x2
                # Giải từ y' = 3a(x-x1)(x-x2) = 3ax^2 - 3a(x1+x2)x + 3ax1*x2
                b_val = Rational(-3 * a_val * (x1 + x2), 2)
                c_val = 3 * a_val * x1 * x2

                # Random hệ số tự do d
                d_val = random.randint(-2, 2)

                # Tính tọa độ tâm đối xứng xI, yI (chính là x0, y0)
                xI = Rational(x1 + x2, 2)

                # Hàm tính tung độ
                def f(xv):
                    return a_val*(xv**3) + b_val*(xv**2) + c_val*xv + d_val

                y1 = f(x1)
                y2 = f(x2)
                yI = f(xI)

                # Random các hệ số a, b, c cho biểu thức
                a_expr = random.choice([-3, -2, -1, 2, 3])
                b_expr = random.choice([-3, -2, -1, 2, 3])
                c_expr = random.randint(-5, 5)

                # Tính giá trị biểu thức T = a*x0 + b*y0 + c
                T = a_expr * xI + b_expr * yI + c_expr

                # Hàm hỗ trợ định dạng số
                def format_num(val):
                    return latex(val).replace('.', ',')

                # Đáp án đúng
                da = format_num(T)

                # Tạo biểu thức P dạng LaTeX
                X, Y = symbols('x_0 y_0')
                expr_P = a_expr * X + b_expr * Y + c_expr
                P_latex = latex(expr_P)

                # Tạo các phương án nhiễu
                s = [
                    format_num(T + 1), 
                    format_num(T - 1), 
                    format_num(T + 2), 
                    format_num(T - 2), 
                    format_num(-T) if T != 0 else format_num(T + 3),
                    format_num(a_expr * yI + b_expr * xI + c_expr), # nhiễu do hoán vị x0, y0
                    format_num(a_expr * x1 + b_expr * y1 + c_expr)  # nhiễu do lấy nhầm điểm cực trị
                ]

                # Lọc bỏ các phương án nhiễu trùng với đáp án đúng và trùng nhau
                s = list(set(s) - {da})
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Xây dựng code TikZ vẽ đồ thị ngẫu nhiên
                xmin = min(-1, x1 - 1.5, x2 - 1.5)
                xmax = max(1.5, x1 + 1.5, x2 + 1.5)
                ymin = min(-1.5, y1 - 2.5, y2 - 2.5)
                ymax = max(1.5, y1 + 2.5, y2 + 2.5)

                # Vẽ các đường nét đứt, đánh dấu các điểm cực trị trên trục
                tikz_pts = ""
                for pt_x, pt_y in [(x1, y1), (x2, y2)]:
                    nx = "below" if pt_y >= 0 else "above"
                    ny = "left" if pt_x >= 0 else "right"
                    if pt_x != 0 and pt_y != 0:
                        tikz_pts += "\\draw[dashed] (%s, 0) node[%s] {$%s$} -- (%s, %s) -- (0, %s) node[%s] {$%s$};\n" % (pt_x, nx, pt_x, pt_x, pt_y, pt_y, ny, pt_y)
                    elif pt_x == 0 and pt_y != 0:
                        tikz_pts += "\\node[%s] at (0, %s) {$%s$};\n" % (ny, pt_y, pt_y)
                    elif pt_y == 0 and pt_x != 0:
                        tikz_pts += "\\node[%s] at (%s, 0) {$%s$};\n" % (nx, pt_x, pt_x)

                    if (pt_x, pt_y) != (0, 0):
                        tikz_pts += "\\filldraw[blue] (%s,%s) circle (0pt);" % (pt_x, pt_y)

                # Lệnh vẽ đồ thị (độ dày 1pt theo yêu cầu)
                plot_str = "\\draw[smooth, line width=1pt, domain=%s:%s, samples=100] plot (\\x, {%s*(\\x)^3 + %s*(\\x)^2 + %s*(\\x) + %s});" % (xmin, xmax, a_val, b_val, c_val, d_val)

                hinhve = ('''\\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.8]
            \\draw[->] (%s, 0) -- (%s, 0) node[below] {$x$};
            \\draw[->] (0, %s) -- (0, %s) node[right] {$y$};
            \\node[below left] at (0,0) {$O$};
            \\clip (%s, %s) rectangle (%s, %s);
            %s
            %s
            \\end{tikzpicture}
            \\end{center}''' % (xmin, xmax, ymin, ymax, xmin, ymin, xmax, ymax, plot_str, tikz_pts))

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{R}$ và có đồ thị như hình vẽ dưới đây:
            %s
            Biết tâm đối xứng của đồ thị hàm số trên có tọa độ là $(x_0; y_0)$. Giá trị của biểu thức $P = %s$ bằng:''' % (hinhve, P_latex))

                # Các đáp án
                da_d = ('\\True $%s$' % str(da))
                da_s1 = '$%s$' % str(das1)
                da_s2 = '$%s$' % str(das2)
                da_s3 = '$%s$' % str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xử lý hiển thị dấu của hệ số tự do c trong bước thay số
                c_str = f'+ {c_expr}' if c_expr > 0 else (f'- {-c_expr}' if c_expr < 0 else '')

                # Nội dung lời giải
                loigiai = ('''Đồ thị hàm số bậc ba nhận điểm uốn làm tâm đối xứng.\\\\
            Từ đồ thị hàm số, ta quan sát thấy đồ thị có hai điểm cực trị là $A(%s; %s)$ và $B(%s; %s)$.\\\\
            Điểm uốn $I$ là trung điểm của đoạn thẳng nối hai điểm cực trị của đồ thị hàm số.\\\\
            Tọa độ tâm đối xứng $(x_0; y_0)$ được tính bằng công thức:
            $$\\begin{cases} x_0 = \\frac{x_A + x_B}{2} = \\frac{%s + %s}{2} = %s \\\\ y_0 = \\frac{y_A + y_B}{2} = \\frac{%s + %s}{2} = %s \\end{cases}$$
            Thay $x_0 = %s$ và $y_0 = %s$ vào biểu thức $P = %s$, ta được:
            $$P = %s \\cdot \\left(%s\\right) + %s \\cdot \\left(%s\\right) %s = %s$$
            Vậy giá trị của biểu thức là $%s$.''' % 
                (latex(x1), latex(y1), latex(x2), latex(y2), 
                 latex(x1), latex(x2), latex(xI), 
                 latex(y1), latex(y2), latex(yI), 
                 latex(xI), latex(yI), P_latex,
                 latex(a_expr), latex(xI), latex(b_expr), latex(yI), c_str, str(da),
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

