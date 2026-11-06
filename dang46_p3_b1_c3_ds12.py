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


def bt_dang46_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu cho Sympy
            x = symbols('x')

            # Bước 1 & 3: Thiết lập thông số và Random bài toán
            # Để bài toán có kết quả đẹp, ta chọn a, b, C trước rồi tính f'(1), f(1)...
            a_val = random.randint(2, 9)
            b_val = random.randint(2, 9)
            # Chọn C là một số hữu tỷ để f(1) và f(1/2) không quá phức tạp
            C_val = Rational(random.randint(2, 12), 6)


            f_prime_1 = a_val + b_val
            f_1 = Rational(a_val, 3) - Rational(b_val, 2) + C_val
            f_half = Rational(a_val, 24) - 2 * b_val + C_val

            # Kết quả cần tìm: 2a + b
            kq_val = 2 * a_val + b_val

            # Bước 4: Tạo các phương án sai (đảm bảo không trùng đáp án đúng)
            s = set()
            while len(s) < 3:
                sai = kq_val + random.choice([-3, -2, -1, 1, 2, 3, 4])
                if sai != kq_val and sai > 0:
                    s.add(f'${latex(sai)}$')

            list_s = list(s)
            da_d = f'\\True ${latex(kq_val)}$'
            da_s1 = list_s[0]
            da_s2 = list_s[1]
            da_s3 = list_s[2]

            # Trộn đáp án
            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Nội dung câu hỏi
            noidungcauhoi = (f"Cho hàm số $f(x)$ thỏa mãn $f'(x) = {latex(a_val)}x^2 + \\frac{{{latex(b_val)}}}{{x^3}}$, "
                             f"$f'(1) = {latex(f_prime_1)}$, $f(1) = {latex(f_1)}$, $f\\left(\\frac{{1}}{{2}}\\right) = {latex(f_half)}$. "
                             f"Khi đó $2a+b$ bằng bao nhiêu?")

            # Nội dung lời giải (Viết lại y hệt cấu trúc trong hình)
            loigiai = (f"Ta có $f'(1) = {f_prime_1} \\Rightarrow a + b = {f_prime_1} \\quad (1)$.\\\\ "
                       f"Hàm số có đạo hàm liên tục trên khoảng $(0; +\\infty)$, các điểm $x=1, x=\\frac{{1}}{{2}}$ đều thuộc $(0; +\\infty)$ nên:\\\\ "
                       f"$f(x) = \\int f'(x)dx = \\int \\left( ax^2 + \\frac{{b}}{{x^3}} \\right)dx = \\frac{{ax^3}}{{3}} - \\frac{{b}}{{2x^2}} + C$.\\\\ "
                       f"+ $f(1) = {latex(f_1)} \\Rightarrow \\frac{{a}}{{3}} - \\frac{{b}}{{2}} + C = {latex(f_1)} \\quad (2)$.\\\\ "
                       f"+ $f\\left(\\frac{{1}}{{2}}\\right) = {latex(f_half)} \\Rightarrow \\frac{{a}}{{24}} - 2b + C = {latex(f_half)} \\quad (3)$.\\\\ "
                       f"Từ (1), (2) và (3) ta được hệ phương trình: "
                       f"$\\begin{{cases}} a+b = {f_prime_1} \\\\ \\frac{{a}}{{3}} - \\frac{{b}}{{2}} + C = {latex(f_1)} \\\\ \\frac{{a}}{{24}} - 2b + C = {latex(f_half)} \\end{{cases}} "
                       f"\\Leftrightarrow \\begin{{cases}} a = {a_val} \\\\ b = {b_val} \\\\ C = {latex(C_val)} \\end{{cases}}$.\\\\ "
                       f"Vậy $2a + b = 2 \\cdot {a_val} + {b_val} = {kq_val}$.")
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(kq_val)) 

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

