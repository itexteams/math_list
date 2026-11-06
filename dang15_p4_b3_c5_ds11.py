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


def bt_dang15_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, m = symbols('x m')

            # Danh sách dạng bài (ở đây chỉ có 1 dạng theo hình ảnh)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':


                a = random.randint(1, 4) # Hệ số liên quan đến x
                b = random.randint(1, 5) # Hệ số liên quan đến m
                base = random.choice([2, 3, 5, 10, 2018, 2024, 2025])

                # Tử số ngẫu nhiên (không ảnh hưởng tập xác định)
                n1 = random.randint(2, 5)
                n2 = random.randint(1, 9)
                tu_so = n1*x + n2

                coeff_x = -2 * a
                coeff_m = -2 * b
                constant_val = a**2 + b**2 + 1

                # Biểu thức f(x,m) bên trong log
                expr_log = x**2 + coeff_x*x + m**2 + coeff_m*m + constant_val

                m_min = b - 1
                m_max = b + 1

                da_dung = f'(-\\infty ; {m_min}) \\cup ({m_max} ; +\\infty)'

                # Tạo các phương án sai (đảm bảo không trùng đáp án đúng)
                s = [
                    f'({m_min} ; {m_max})',
                    f'(-\\infty ; {m_min-1}) \\cup ({m_max+1} ; +\\infty)',
                    f'\\mathbb{{R}} \\setminus \\{{{b}\\}}',
                    f'(-\\infty ; {m_min}] \\cup [{m_max} ; +\\infty)',
                    f'\\varnothing'
                ]

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # --- B2: Viết lại nội dung đề bài và lời giải ---
                noidungcauhoi = (
                    f'Tìm tập hợp tất cả các giá trị của tham số $m$ để hàm số '
                    f'$y = \\frac{{{latex(tu_so)}}}{{\\log_{{{base}}}\\left({latex(expr_log)}\\right)}}$ '
                    f'xác định với mọi $x \\in \\mathbb{{R}}$.'
                )

                # Chi tiết lời giải theo từng bước của hình ảnh
                loigiai = (
                    f'Xét hàm số $y = \\frac{{{latex(tu_so)}}}{{\\log_{{{base}}}\\left({latex(expr_log)}\\right)}}$.\\\\ '
                    f'ĐKXĐ: $\\begin{{cases}} {latex(expr_log)} > 0 \\\\ \\log_{{{base}}}\\left({latex(expr_log)}\\right) \\neq 0 \\end{{cases}} '
                    f'\\Leftrightarrow \\begin{{cases}} {latex(expr_log)} > 0 \\\\ {latex(expr_log)} \\neq 1 \\end{{cases}}$.\\\\ '
                    f'Nên điều kiện để hàm số xác định với mọi $x \\in \\mathbb{{R}}$ là '
                    f'$\\begin{{cases}} {latex(expr_log)} > 0 \\\\ x^2 {coeff_x:+d}x + m^2 {coeff_m:+d}m + {constant_val-1} \\neq 0 \\end{{cases}}$ với $\\forall x \\in \\mathbb{{R}}$.\\\\ '
                    f'Điều này xảy ra khi và chỉ khi:\\\\ '
                    f'$\\begin{{cases}} \\Delta\'_1 = {a**2} - (m^2 {coeff_m:+d}m + {constant_val}) < 0 \\\\ '
                    f'\\Delta\'_2 = {a**2} - (m^2 {coeff_m:+d}m + {constant_val - 1}) < 0 \\end{{cases}} '
                    f'\\Leftrightarrow \\begin{{cases}} -(m-{b})^2 < 0 \\\\ -(m-{b})^2 + 1 < 0 \\end{{cases}} '
                    f'\\Leftrightarrow -(m-{b})^2 + 1 < 0 \\Leftrightarrow \\left[\\begin{{matrix}} m < {m_min} \\\\ m > {m_max} \\end{{matrix}}\\right.$.\\\\ '
                    f'Vậy $m \\in {da_dung}$.'
                )

                # Các đáp án trắc nghiệm
                da_d = '\\True $' + da_dung + '$'
                list_1 = [da_d, '$' + das1 + '$', '$' + das2 + '$', '$' + das3 + '$']
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo định dạng LaTeX mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

