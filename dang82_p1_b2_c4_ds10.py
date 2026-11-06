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


def bt_dang82_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Khởi tạo dữ liệu ngẫu nhiên (chọn số để tính toán ra số hữu tỉ đẹp)
                # Tọa độ A(0; yA), B(xB; yB)
                yA = random.choice([100, 120, 150])
                xB = random.choice([60, 30, 80])
                yB = random.choice([80, 40, 60])

                # Vận tốc
                v1 = random.choice([5, 4, 6])
                v2 = random.choice([10, 5, 12])

                # Tính toán các thông số hình học cho B
                distB = int(math.sqrt(xB**2 + yB**2))
                k_frac = Rational(yB, xB) # Hệ số góc tan(alpha)
                cos_a = Rational(xB, distB)
                sin_a = Rational(yB, distB)

                # Tọa độ di động theo t
                # Con 1: A'(0; yA - v1*t)
                # Con 2: B'(xB - v2*cos_a*t; yB - v2*sin_a*t)
                vx2 = v2 * cos_a
                vy2 = v2 * sin_a

                # Vectơ A'B' = (xB - vx2*t ; (yB - vy2*t) - (yA - v1*t))
                # A'B' = (xB - vx2*t ; (yB - yA) + (v1 - vy2)*t)
                dy0 = yB - yA
                dv = v1 - vy2

                # Khai triển d^2 = f(t) = (xB - vx2*t)^2 + (dy0 + dv*t)^2
                # f(t) = (vx2^2 + dv^2)t^2 + 2*(-xB*vx2 + dy0*dv)t + (xB^2 + dy0^2)
                a_f = vx2**2 + dv**2
                b_f = 2 * (-xB * vx2 + dy0 * dv)
                c_f = xB**2 + dy0**2

                # Tìm đỉnh t_min = -b / 2a
                t_min = Rational(-b_f, 2 * a_f)
                f_min = a_f * (t_min**2) + b_f * t_min + c_f
                d_min_val = math.sqrt(float(f_min))

                # Định dạng hiển thị dấu phẩy
                def f_str(num):
                    return str(round(float(num), 2)).replace('.', ',')

                # Đáp án
                kq_chinh_xac = f_str(d_min_val)
                da_dung = f"${kq_chinh_xac}$ m"

                # Tạo đáp án sai
                s = []
                while len(s) < 3:
                    sai_val = round(d_min_val + random.uniform(-15, 15), 2)
                    sai_str = f"${str(sai_val).replace('.', ',')}$ m"
                    if sai_str != da_dung and sai_str not in s:
                        s.append(sai_str)

                # Nội dung câu hỏi
                noidungcauhoi = (f"Hai con chuồn chuồn bay trên hai quỹ đạo khác nhau, xuất phát cùng thời điểm. "
                                 f"Một con bay trên quỹ đạo là đường thẳng từ điểm $A(0;{yA})$ đến điểm $O(0;0)$ với vận tốc ${v1}$ m/s. "
                                 f"Con còn lại bay trên quỹ đạo là đường thẳng từ $B({xB};{yB})$ đến điểm $O(0;0)$ với vận tốc ${v2}$ m/s. "
                                 f"Hỏi trong quá trình bay thì khoảng cách ngắn nhất hai con đạt được là bao nhiêu?")

                # Lời giải chi tiết theo mẫu ảnh
                loigiai = (f"Xét tại thời điểm $t$ (giây), con chuồn chuồn bay từ $A$ về $O$ có tọa độ là $A'(0; {yA} - {v1}t)$.\\\\ "
                           f"Con chuồn chuồn bay từ $B({xB};{yB})$ về $O(0;0)$ trên quỹ đạo là đường thẳng có hệ số góc là "
                           f"$k = \\tan \\alpha = {latex(k_frac)} \\Rightarrow \\cos \\alpha = {latex(cos_a)}, \\sin \\alpha = {latex(sin_a)}$.\\\\ "
                           f"Do đó tại thời điểm $t$, nó có tọa độ là "
                           f"$\\begin{{cases}} x = {xB} - {v2}t \\cdot \\cos \\alpha \\\\ y = {yB} - {v2}t \\cdot \\sin \\alpha \\end{{cases}} "
                           f"\\Leftrightarrow \\begin{{cases}} x = {xB} - {f_str(vx2)}t \\\\ y = {yB} - {f_str(vy2)}t \\end{{cases}} \\Rightarrow B'({xB} - {f_str(vx2)}t; {yB} - {f_str(vy2)}t)$.\\\\ "
                           f"Ta có: $\\overrightarrow{{A'B'}} = ({xB} - {f_str(vx2)}t; {f_str(dy0)} + {f_str(dv)}t)$.\\\\ "
                           f"Khi đó, khoảng cách giữa hai con chuồn chuồn là:\\\\ "
                           f"$d = A'B' = \\sqrt{{({xB} - {f_str(vx2)}t)^2 + ({f_str(dy0)} + {f_str(dv)}t)^2}} \\Leftrightarrow d = \\sqrt{{{f_str(a_f)}t^2 + ({f_str(b_f)})t + {c_f}}}$.\\\\ "
                           f"$d$ nhỏ nhất khi hàm số $f(t) = {f_str(a_f)}t^2 + ({f_str(b_f)})t + {c_f}$ đạt giá trị nhỏ nhất.\\\\ "
                           f"Ta có: $f(t) = {f_str(a_f)}(t - {f_str(t_min)})^2 + {f_str(f_min)} \\ge {f_str(f_min)}$.\\\\ "
                           f"$\\Rightarrow \\min f(t) = f({f_str(t_min)}) = {f_str(f_min)}$.\\\\ "
                           f"Vậy khoảng cách ngắn nhất của hai con chuồn chuồn trong quá trình bay là $\\sqrt{{{f_str(f_min)}}} \\approx {kq_chinh_xac}$ m.")

                # Đóng gói kết quả
                list_1 = ['\\True ' + da_dung, s[0], s[1], s[2]]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

