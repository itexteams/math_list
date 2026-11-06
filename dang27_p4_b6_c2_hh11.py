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


def bt_dang27_p4_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            a = symbols('a')

            # B1 & B3: Nghiên cứu đề bài và thiết lập thông số random
            # Giả sử AB = m*a, AC = n*a, A'B = k*a
            # Để bài toán có nghĩa và số đẹp, ta chọn các số nguyên dương
            m = random.randint(1, 3)  # Hệ số của AB
            n = random.randint(2, 4)  # Hệ số của AC
            # Điều kiện tam giác ABA' vuông tại A: AA'^2 = A'B^2 - AB^2 -> k > m
            k = m + random.randint(2, 4) # Hệ số của A'B

            # B2: Tính toán các đại lượng
            # Diện tích đáy ABC (vuông tại A)
            S_day_val = Rational(1, 2) * m * n
            S_day_tex = latex(S_day_val * a**2)

            # Chiều cao AA' = sqrt(A'B^2 - AB^2)
            h_sq = k**2 - m**2
            h_val = sqrt(h_sq)
            h_tex = latex(h_val * a)

            # Thể tích V = S_day * h
            V_val = S_day_val * h_val
            V_tex = latex(V_val * a**3)

            # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
            da_dung = '$%s$' % V_tex

            # Tạo các phương án nhiễu
            wrong_1 = latex(Rational(1, 3) * V_val * a**3) # Nhầm sang hình chóp
            wrong_2 = latex(m * n * h_val * a**3)          # Quên chia 2 diện tích tam giác
            # Nhầm Pythagoras hoặc cạnh
            h_wrong = sqrt(k**2 + m**2)
            wrong_3 = latex(S_day_val * h_wrong * a**3)

            list_s = [
                '$%s$' % wrong_1,
                '$%s$' % wrong_2,
                '$%s$' % wrong_3,
                '$%s$' % latex(S_day_val * sqrt(abs(k**2 - n**2)) * a**3)
            ]

            # Loại bỏ trùng lặp nếu có và chọn 3 đáp án sai
            list_s = list(set(list_s))
            if da_dung in list_s:
                list_s.remove(da_dung)
            while len(list_s) < 3:
                list_s.append('$%s$' % latex((V_val + random.randint(1, 5)) * a**3))
            random.shuffle(list_s)

            das1, das2, das3 = list_s[:3]

            # Nội dung câu hỏi
            noidungcauhoi = ('Cho hình lăng trụ đứng $ABC.A\'B\'C\'$ có đáy $ABC$ là tam giác vuông tại $A$, biết $AB = %s$, $AC = %s$ và $A\'B = %s$. Tính thể tích của khối lăng trụ $ABC.A\'B\'C\'$.' 
                             % (latex(m*a), latex(n*a), latex(k*a)))

            # Nội dung lời giải chi tiết
            loigiai = ('Diện tích đáy là $S_{ABC} = \\frac{1}{2} AB \\cdot AC = \\frac{1}{2} \\cdot %s \\cdot %s = %s$. \\\\\n'
                       'Tam giác $ABA\'$ vuông tại $A$ nên có $AA\' = \\sqrt{A\'B^2 - AB^2} = \\sqrt{\\left(%s\\right)^2 - \\left(%s\\right)^2} = %s$. \\\\\n'
                       'Thể tích cần tính là: $V = S_{ABC} \\cdot AA\' = %s \\cdot %s = %s$.'
                       % (latex(m*a), latex(n*a), S_day_tex, 
                          latex(k*a), latex(m*a), h_tex,
                          S_day_tex, h_tex, V_tex))

            # TikZ giống 100% hình ảnh (độ dày 1pt)
            tikz_code = (
                '\\begin{center} \\begin{tikzpicture}[line join=round, line cap=round, font=\\footnotesize, scale=0.8, line width=1pt]\n'
                '\\coordinate (A) at (0,0);\n'
                '\\coordinate (C) at (4,0);\n'
                '\\coordinate (B) at (1.5,-1.5);\n'
                '\\coordinate (A1) at (0,4);\n'
                '\\coordinate (C1) at (4,4);\n'
                '\\coordinate (B1) at (1.5,2.5);\n'
                '\\draw (A1)--(B1)--(C1)--cycle (A1)--(A) (A)--(B) (B1)--(B) (C1)--(C) (B)--(C) (A1)--(B);\n'
                '\\draw[dashed]  (A)--(C);\n'
                '\\draw (0,0.2) -- (0.2,0.2) -- (0.2,0);\n' # Ký hiệu vuông góc tại A
                '\\node[left] at (A) {$A$};\n'
                '\\node[below] at (B) {$B$};\n'
                '\\node[right] at (C) {$C$};\n'
                '\\node[left] at (A1) {$A\'$};\n'
                '\\node[right] at (B1) {$B\'$};\n'
                '\\node[right] at (C1) {$C\'$};\n'
                '\\node[left] at (0.8,-0.9) {$%s$};\n' % latex(m*a) +
                '\\node[above] at (2.2,0) {$%s$};\n' % latex(n*a) +
                '\\node[right] at (0.4,2) {$%s$};\n' % latex(k*a) +
                '\\end{tikzpicture} \\end{center}'
            )

            # Đưa đáp án vào danh sách
            da_d = ('\\True ' + str(da_dung))
            list_ans = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_ans)

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

