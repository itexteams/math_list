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


def bt_dang57_p4_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Tạo các hệ số ngẫu nhiên cho tử số: ax^2 + bx + c
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            c = random.randint(1, 5)

            # Tạo các hệ số ngẫu nhiên cho biểu thức trong căn ở mẫu: dx^3 + ex^2 + f
            d = random.randint(2, 4)
            e = random.randint(1, 4)
            f = 1 # Giữ f=1 để đảm bảo mẫu tại x=0 là 2*sqrt(1) = 2, tránh số phức hoặc mẫu = 0

            # Điểm tính đạo hàm
            x0 = 0

            # Định nghĩa hàm số
            tu_so = a*x**2 + b*x + c
            bieu_thuc_trong_can = d*x**3 + e*x**2 + f
            mau_so = 2 * sqrt(bieu_thuc_trong_can)
            y = tu_so / mau_so

            # B1 & B2: Tính toán đạo hàm theo quy tắc (u/v)'
            u = tu_so
            v = mau_so
            u_prime = diff(u, x)
            v_prime = diff(v, x)

            # Giá trị đạo hàm tại x0
            y_prime_func = diff(y, x)
            kq_val = y_prime_func.subs(x, x0)

            # Chuyển đổi sang LaTeX để trình bày
            # Hàm hiển thị dấu thông minh (tránh + - thành -)
            def format_poly(expr):
                return latex(expr)

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hàm số $y = \frac{%s}{%s}$, tính đạo hàm $y'(%s)$.''' % (format_poly(tu_so), format_poly(mau_so), x0)

            # Tính toán các bước cho lời giải
            step1_u_prime = format_poly(u_prime)
            step1_v_prime = format_poly(v_prime)

            # Đáp án đúng và các đáp án nhiễu
            da_dung = r'$%s$' % latex(kq_val)
            list_distractors = [
                r'$%s$' % latex(kq_val + 1),
                r'$%s$' % latex(kq_val - 1),
                r'$%s$' % latex(kq_val * 2 if kq_val != 0 else 2),
                r'$%s$' % latex(kq_val + sp.Rational(1, 2))
            ]
            random.shuffle(list_distractors)

            da_d = '\\True ' + da_dung
            da_s1 = list_distractors[0]
            da_s2 = list_distractors[1]
            da_s3 = list_distractors[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = r'''Ta có: $y' = \frac{\left(%s\right)' \cdot %s - \left(%s\right) \cdot \left(%s\right)'}{\left(%s\right)^2}$ \\
            $y' = \frac{\left(%s\right) \cdot %s - \left(%s\right) \cdot \frac{%s}{\sqrt{%s}}}{%s}$ \\
            Thay $x = %s$ vào biểu thức đạo hàm, ta được: \\
            $y'(%s) = \frac{\left(%s\right) \cdot %s - \left(%s\right) \cdot 0}{%s} = %s$.''' % (
                format_poly(tu_so), format_poly(mau_so), format_poly(tu_so), format_poly(mau_so), format_poly(mau_so),
                format_poly(u_prime), format_poly(mau_so), format_poly(tu_so), format_poly(diff(bieu_thuc_trong_can, x)), format_poly(bieu_thuc_trong_can), format_poly(mau_so**2),
                x0, x0, u_prime.subs(x, x0), mau_so.subs(x, x0), tu_so.subs(x, x0), (mau_so**2).subs(x, x0), latex(kq_val)
            )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content

