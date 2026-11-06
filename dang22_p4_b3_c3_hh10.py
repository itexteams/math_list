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


def bt_dang22_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y, m = symbols('x y m')

            # B3- Suy nghĩ tìm cách random bài toán
            # 1. Random tâm I(xI, yI) và bán kính R (nguyên)
            xI = random.randint(-6, 6)
            yI = random.randint(-6, 6)
            R = random.randint(2, 6)
            # Tính c để phương trình đường tròn đẹp: x^2 + y^2 - 2ax - 2by + c = 0
            c_val = xI**2 + yI**2 - R**2

            # 2. Hệ số khai triển: a_coeff = -2*xI, b_coeff = -2*yI
            a_c = -2 * xI
            b_c = -2 * yI

            # Hàm xử lý hiển thị số kèm dấu chuẩn LaTeX
            def format_sign(n, var=""):
                if n == 0: return ""
                symbol = "+" if n > 0 else "-"
                abs_n = abs(n)
                coeff = "" if (abs_n == 1 and var != "") else str(abs_n)
                return f" {symbol} {coeff}{var}"

            # Chuỗi phương trình đường tròn (C)
            circle_str = f"x^2 + y^2{format_sign(a_c, 'x')}{format_sign(b_c, 'y')}{format_sign(c_val)} = 0"

            # 3. Cấu trúc đường thẳng d: x + my + Am + B = 0 (giống mẫu ảnh)
            A = random.randint(-8, 8)
            B = random.randint(-8, 8)

            # Đảm bảo mẫu số (yI + A) khác 0 để có nghiệm m duy nhất
            while (yI + A) == 0:
                A = random.randint(-8, 8)

            line_str = f"x + my{format_sign(A, 'm')}{format_sign(B)} = 0"

            # 4. Tính toán logic chuyển vế
            # Thay I vào d: xI + m*yI + A*m + B = 0  =>  m(yI + A) + (xI + B) = 0
            # => (ve_trai) * m = (ve_phai)
            ve_trai = yI + A
            hang_so_tong = xI + B
            ve_phai = -hang_so_tong # Chuyển vế đổi dấu

            m_val = Rational(ve_phai, ve_trai)

            # --- Tạo đáp án ---
            da_dung = f"${latex(m_val)}$"
            distractors = set()
            while len(distractors) < 3:
                # Tạo các nghiệm giả quanh nghiệm đúng
                fake = m_val + random.choice([1, -1, Rational(1, 2), -Rational(1, 2)])
                if fake != m_val:
                    distractors.add(f"${latex(fake)}$")
            list_distractors = list(distractors)

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (f"Trong mặt phẳng với hệ trục tọa độ $Oxy$, cho đường tròn $(C): {circle_str}$ "
                             f"và đường thẳng $d: {line_str}$. Gọi $I$ là tâm của $(C)$. "
                             f"Tìm $m$ để $d$ cắt $(C)$ tại hai điểm phân biệt $A, B$ thỏa mãn $AB$ lớn nhất.")

            # --- Nội dung lời giải (Logic chuẩn xác) ---
            step_replace = f"{xI} + m({yI}{format_sign(A)}){format_sign(B)} = 0"
            loigiai = (f"Đường tròn $(C)$ có tâm $I({xI}; {yI})$, bán kính $R = {R}$.\\\\ "
                       f"Dây cung $AB$ lớn nhất khi và chỉ khi $AB$ là đường kính của $(C)$, "
                       f"nghĩa là đường thẳng $d$ đi qua tâm $I$.\\\\ "
                       f"Thay tọa độ $I({xI}; {yI})$ vào phương trình $d$, ta có:\\\\ "
                       f"${step_replace} \\Leftrightarrow {ve_trai}m = {ve_phai} \\Leftrightarrow m = {latex(m_val)}$.\\\\ "
                       f"Vậy $m = {latex(m_val)}$ là giá trị cần tìm.")

            # --- Xuất câu trắc nghiệm ---
            da_d = '\\True ' + da_dung
            list_1 = [da_d] + list_distractors
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

