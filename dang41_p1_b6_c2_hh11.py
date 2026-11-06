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


def bt_dang41_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            a = symbols('a')

            # B3-Suy nghĩ tìm cách random bài toán
            # Random các hệ số của các cạnh m (AB), n (BC), p (CC')
            # Sao cho m, n, p là các số nguyên dương để kết quả đẹp như trong hình
            m = random.randint(1, 2)
            n = random.randint(m + 1, 4)
            p = random.randint(2, 5)

            # Các kích thước của khối hộp
            ab = m * a
            bc = n * a
            cc = p * a

            # Tính toán các đại lượng trung gian (giống lời giải trong ảnh)
            ac_sq = (m**2 + n**2) * a**2
            ac = sqrt(ac_sq)

            ac_prime_sq = (m**2 + n**2 + p**2) * a**2
            ac_prime = sqrt(ac_prime_sq)

            volume = m * n * p * a**3

            # B4-Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            da_val = m * n * p
            da_tex = '$%s$' % (latex(volume).replace('.', ','))

            s = set()
            # Tạo các phương án nhiễu
            s.add('$%s$' % (latex(Rational(da_val, 3) * a**3)).replace('.', ',')) # Công thức chóp
            s.add('$%s$' % (latex(2 * da_val * a**3)).replace('.', ','))
            s.add('$%s$' % (latex((m * n * p + 2) * a**3)).replace('.', ','))
            s.add('$%s$' % (latex(m * n * a**3)).replace('.', ',')) # Chỉ tính diện tích đáy
            s.add('$%s$' % (latex((m + n + p) * a**3)).replace('.', ',')) # Tổng các cạnh

            # Loại bỏ đáp án đúng nếu lỡ trùng và lấy 3 phương án
            if da_tex in s:
                s.remove(da_tex)
            list_wrong = random.sample(list(s), 3)

            da_d = '\\True ' + da_tex
            da_s1 = list_wrong[0]
            da_s2 = list_wrong[1]
            da_s3 = list_wrong[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ (Bản sao 100% từ ảnh)
            tikz_code = (
                "\\begin{center}\n"
                "\\begin{tikzpicture}[line width=1pt, scale=1, font=\\footnotesize, line join=round, line cap=round]\n"
                "\\coordinate (B) at (0,0);\n"
                "\\coordinate (C) at (3.5,0);\n"
                "\\coordinate (D) at (4.7,1.2);\n"
                "\\coordinate (A) at (1.2,1.2);\n"
                "\\coordinate (B1) at (0,2.8);\n"
                "\\coordinate (C1) at (3.5,2.8);\n"
                "\\coordinate (D1) at (4.7,4);\n"
                "\\coordinate (A1) at (1.2,4);\n"
                "\\draw (B)--(C)--(D) (B1)--(C1)--(D1)--(A1)--cycle (B)--(B1) (C)--(C1) (D)--(D1);\n"
                "\\draw[dashed] (A)--(B) (A)--(D) (A)--(A1) (A)--(C) (A)--(C1);\n"
                "\\draw (B) node[below left] {$B$} (C) node[below right] {$C$} (D) node[right] {$D$} (A) node[above left] {$A$};\n"
                "\\draw (B1) node[above left] {$B'$} (C1) node[above] {$C'$} (D1) node[above right] {$D'$} (A1) node[above left] {$A'$};\n"
                "\\node at ($(B)!0.5!(C)$)[below]{$%s$};\n"
                "\\node at ($(B)!0.5!(A)$)[left]{$%s$};\n"
                "\\end{tikzpicture}\n"
                "\\end{center}" % (latex(bc), latex(ab))
            )

            # Câu hỏi
            noidungcauhoi = (
                "Cho khối hộp chữ nhật $ABCD.A'B'C'D'$, biết $AB = %s$; $BC = %s$; $AC' = %s$. Thể tích $V$ của khối hộp đó bằng"
                % (latex(ab), latex(bc), latex(ac_prime))
            )

            # Lời giải chi tiết theo mẫu ảnh
            loigiai = (
                "Xét tam giác vuông $ABC$, ta có: $AC = \\sqrt{AB^2 + BC^2} = \\sqrt{\\left(%s\\right)^2 + \\left(%s\\right)^2} = %s$.\\\\\n"
                "Xét tam giác vuông $ACC'$, ta có: $CC' = \\sqrt{AC'^2 - AC^2} = \\sqrt{\\left(%s\\right)^2 - \\left(%s\\right)^2} = %s$.\\\\\n"
                "Vậy thể tích của khối hộp chữ nhật $ABCD.A'B'C'D'$ là: $V = AB \\cdot BC \\cdot CC' = %s \\cdot %s \\cdot %s = %s$."
                % (latex(ab), latex(bc), latex(ac), 
                   latex(ac_prime), latex(ac), latex(cc),
                   latex(ab), latex(bc), latex(cc), latex(volume))
            )

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' +tikz_code+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

