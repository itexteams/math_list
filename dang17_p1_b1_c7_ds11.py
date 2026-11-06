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


def bt_dang17_p1_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B1: Ngẫu nhiên hóa các tham số của hàm số y = (ax + b) / (cx + d)
            # Để đạo hàm đẹp và không quá phức tạp, ta chọn các số nguyên nhỏ
            a = random.randint(-5, 5)
            while a == 0: a = random.randint(-5, 5)

            b = random.randint(-5, 5)

            c = random.randint(1, 4) # Thường chọn c dương để mẫu số nhìn gọn

            d = random.randint(-5, 5)
            while a*d - b*c == 0: # Đảm bảo hàm số không suy biến thành hàm hằng
                d = random.randint(-5, 5)

            # Chọn x0 sao cho mẫu số cx0 + d != 0
            x0 = random.randint(-3, 3)
            while c * x0 + d == 0:
                x0 = random.randint(-3, 3)

            # B2: Tính toán đạo hàm và hệ số góc
            f = (a*x + b) / (c*x + d)
            f_prime = diff(f, x)
            # Hệ số góc k = f'(x0)
            k_val = f_prime.subs(x, x0)

            # Chuyển đổi sang dạng Latex cho tử và mẫu của đạo hàm (ax+b)/(cx+d) -> (ad-bc)/(cx+d)^2
            tu_dao_ham = a*d - b*c
            mau_dao_ham_str = f"({latex(c)}x + {latex(d)})^2" if d > 0 else f"({latex(c)}x - {latex(abs(d))})^2"
            # Xử lý dấu +- trong chuỗi mẫu số thủ công để đẹp hơn
            mau_dao_ham_str = mau_dao_ham_str.replace("+ -", "- ").replace("- -", "+ ").replace("--", "+ ")

            # Đáp án đúng
            da_dung = f"${latex(k_val)}$"

            # Tạo các đáp án nhiễu
            s = [
                f"${latex(-k_val)}$",
                f"${latex(k_val + 1)}$",
                f"${latex(k_val - 1)}$",
                f"${latex(Rational(1, k_val))}$" if k_val != 0 else "$0$",
                f"${latex(tu_dao_ham)}$",
                f"$-{latex(tu_dao_ham)}$"
            ]
            random.shuffle(s)
            da_s1 = s[0]
            da_s2 = s[1]
            da_s3 = s[2]

            # Nội dung câu hỏi
            noidungcauhoi = (f"Tiếp tuyến của đồ thị hàm số $y = \\frac{{{latex(a)}x + {latex(b)}}}{{{latex(c)}x + {latex(d)}}}$ "
                             f"tại điểm có hoành độ $x_0 = {latex(x0)}$ có hệ số góc bằng")

            # Nội dung lời giải
            loigiai = (f"TXĐ: $D = \\mathbb{{R}} \\setminus \\left\\{{ {latex(Rational(-d, c))} \\right\\}}$.\\\\ "
                       f"Ta có $f'(x) = \\frac{{{latex(tu_dao_ham)}}}{{({latex(c)}x + {latex(d)})^2}}$.\\\\ "
                       f"Hệ số góc của tiếp tuyến của đồ thị hàm số tại điểm có hoành độ $x_0 = {latex(x0)}$ là:\\\\ "
                       f"$f'({latex(x0)}) = \\frac{{{latex(tu_dao_ham)}}}{{({latex(c)} \\cdot ({latex(x0)}) + {latex(d)})^2}} = {latex(k_val)}$.")

            # Xử lý hiển thị dấu +- và --
            noidungcauhoi = noidungcauhoi.replace("+ -", "- ").replace("- -", "+ ").replace("--", "+ ")
            loigiai = loigiai.replace("+ -", "- ").replace("- -", "+ ").replace("--", "+ ")

            # Các đáp án trắc nghiệm
            da_d = '\\True ' + da_dung
            list_1 = [da_d, da_s1, da_s2, da_s3]
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
                       '\\end{ex}\n \\end{minipage} \n\n').replace('1x','x')
            return content

