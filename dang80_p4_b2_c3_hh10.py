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


def bt_dang80_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến ký hiệu
            x, y = symbols('x y')

            # B1 & B3: Nghiên cứu và tìm cách random bài toán
            # Điểm M(x0; y0). Để d cắt tia Ox, Oy thì x0, y0 phải dương.
            x0 = randint(1, 6)
            y0 = randint(1, 6)

            # Tránh trường hợp trùng hoàn toàn với đề gốc (2, 1) nếu muốn đa dạng
            if x0 == 2 and y0 == 1:
                x0, y0 = 3, 2

            # Tính toán các giá trị cho lời giải
            # Theo AM-GM: x0/a + y0/b = 1 >= 2*sqrt(x0*y0/ab) => ab >= 4*x0*y0
            # Diện tích S = 1/2*ab >= 2*x0*y0. Dấu "=" khi x0/a = y0/b = 1/2
            a_val = 2 * x0
            b_val = 2 * y0
            s_min = 2 * x0 * y0

            # Phương trình đường thẳng d: y0*x + x0*y - 2*x0*y0 = 0
            expr_d = y0*x + x0*y - 2*x0*y0

            # B4: Tạo các phương án sai (đảm bảo không trùng đáp án đúng)
            # Đáp án đúng
            da_dung_str = '$' + latex(expr_d) + ' = 0$'

            # Các phương án nhiễu
            s = []
            # Nhiễu 1: Nhầm hệ số (x0*x + y0*y)
            expr_s1 = x0*x + y0*y - (x0**2 + y0**2)
            s.append('$' + latex(expr_s1) + ' = 0$')

            # Nhiễu 2: Phương trình đi qua O (y0*x - x0*y = 0)
            expr_s2 = y0*x - x0*y
            s.append('$' + latex(expr_s2) + ' = 0$')

            # Nhiễu 3: Nhầm diện tích (không nhân 2) -> x/x0 + y/y0 = 1
            expr_s3 = y0*x + x0*y - x0*y0
            s.append('$' + latex(expr_s3) + ' = 0$')

            # Nhiễu 4: Đường thẳng đi qua M nhưng không tối ưu (x - y)
            expr_s4 = x - y - (x0 - y0)
            s.append('$' + latex(expr_s4) + ' = 0$')

            # Loại bỏ trùng lặp nếu có và chọn 3 đáp án sai
            s = list(set([i for i in s if i != da_dung_str]))
            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng $Oxy$, cho điểm $M(%s;%s)$. Đường thẳng $d$ đi qua $M$, cắt các tia $Ox$, $Oy$ lần lượt tại $A$ và $B$ ($A, B$ khác $O$) sao cho tam giác $OAB$ có diện tích nhỏ nhất. Lập phương trình đường thẳng $d$.'''
                              %(latex(x0), latex(y0)))

            # Các đáp án
            da_d = '\\True ' + da_dung_str
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # B2: Nội dung lời giải chi tiết giống trong ảnh
            loigiai = ('''Gọi đường thẳng $d$ cắt tia $Ox$, $Oy$ lần lượt tại $A(a;0)$ và $B(0;b)$ với $a, b > 0$. \\\\
                        Phương trình đường thẳng $d$ theo đoạn chắn là: $(d): \\frac{x}{a} + \\frac{y}{b} = 1$. \\\\
                        Vì $(d)$ đi qua $M(%s;%s) \\Rightarrow \\frac{%s}{a} + \\frac{%s}{b} = 1$. \\\\
                        Áp dụng bất đẳng thức Cauchy (AM-GM), ta có: \\\\
                        $1 = \\frac{%s}{a} + \\frac{%s}{b} \\ge 2\\sqrt{\\frac{%s \\cdot %s}{ab}} = 2\\sqrt{\\frac{%s}{ab}} \\Rightarrow 1 \\ge \\frac{4 \\cdot %s}{ab} \\Rightarrow ab \\ge %s$. \\\\
                        Ta có diện tích tam giác vuông $OAB$ tại $O$ là $S = \\frac{1}{2}OA \\cdot OB = \\frac{1}{2}ab \\ge \\frac{1}{2} \\cdot %s = %s$. \\\\
                        Diện tích tam giác vuông $OAB$ đạt giá trị nhỏ nhất $S = %s$ khi và chỉ khi: \\\\
                        $\\frac{%s}{a} = \\frac{%s}{b} = \\frac{1}{2} \\Leftrightarrow \\begin{cases} a = 2 \\cdot %s = %s \\\\ b = 2 \\cdot %s = %s \\end{cases}$. \\\\
                        Khi đó phương trình đường thẳng $(d)$ là: $\\frac{x}{%s} + \\frac{y}{%s} = 1 \\Leftrightarrow %s$.'''
                        %(latex(x0), latex(y0), latex(x0), latex(y0),
                          latex(x0), latex(y0), latex(x0), latex(y0), latex(x0*y0), latex(x0*y0), latex(4*x0*y0),
                          latex(4*x0*y0), latex(s_min), latex(s_min),
                          latex(x0), latex(y0), latex(x0), latex(a_val), latex(y0), latex(b_val),
                          latex(a_val), latex(b_val), latex(expr_d) + ' = 0'
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

