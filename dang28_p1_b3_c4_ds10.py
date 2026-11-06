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


def bt_dang28_p1_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            m = symbols('m')

            # --- BƯỚC 1: NGHIÊN CỨU ĐỀ BÀI ---
            # Cấu trúc tổng quát từ các ảnh: (m - k)x^2 - 2(m - k - 1)x + (m - k - 2) = 0
            # Ảnh 1: k=1 | Ảnh 2: k=4 | Ảnh 3: k=10

            # --- BƯỚC 3: RANDOM BÀI TOÁN ---
            k = random.randint(1, 15)

            # Thiết lập hệ số
            a = m - k
            b = -2 * (m - (k + 1))
            c = m - (k + 2)

            # --- BƯỚC 2: TÍNH TOÁN VÀ VIẾT LỜI GIẢI ---

            # 1. Điều kiện có 2 nghiệm
            dieu_kien_a = f"{latex(a)} \\neq 0 \\Leftrightarrow m \\neq {k}"
            # Delta' = (m-k-1)^2 - (m-k)(m-k-2) = 1
            delta_p_expr = f"({latex(m-(k+1))})^2 - ({latex(m-k)})({latex(m-(k+2))})"

            # 2. Vi-et
            tong_v = f"\\frac{{{latex(-b)}}}{{{latex(a)}}}"  # 2m - 2k - 2 / m - k
            tich_v = f"\\frac{{{latex(c)}}}{{{latex(a)}}}"   # m - k - 2 / m - k

            # 3. Rút gọn dòng cuối (Sửa lỗi logic phân thức)
            # Vế trái: (2m-2k-2 + m-k-2)/(m-k) = (3m-3k-4)/(m-k)
            tu_so_1 = 3*m - (3*k + 4)
            # Bất phương trình: (3m-3k-4)/(m-k) < 1 
            # <=> (3m-3k-4 - (m-k))/(m-k) < 0
            # <=> (2m-2k-4)/(m-k) < 0
            tu_so_cuoi = 2*m - (2*k + 4)

            m_min = k
            m_max = k + 2

            # Nội dung câu hỏi
            noidungcauhoi = (f"Tất cả các giá trị của $m$ thì phương trình $({latex(a)})x^2 +({latex(b)})x + {latex(c)} = 0$ "
                             f"có hai nghiệm $x_1, x_2$ thỏa mãn $x_1 + x_2 + x_1x_2 < 1$ là")

            # Đáp án
            da_dung = f"${m_min} < m < {m_max}$"
            list_ans = ["\\True " + da_dung, f"$m > {m_max}$", f"$m < {m_min}$", f"$0 < m < {m_max}$"]
            random.shuffle(list_ans)

            # Lời giải chi tiết (Đã fix dòng cuối)
            loigiai = (f"Phương trình $({latex(a)})x^2 +({latex(b)})x + {latex(c)} = 0$ có hai nghiệm $x_1, x_2$ khi và chỉ khi: \\\\\n"
                       f"$\\begin{{cases}} {latex(a)} \\neq 0 \\\\ \\Delta' \\geq 0 \\end{{cases}} \\Leftrightarrow "
                       f"\\begin{{cases}} m \\neq {k} \\\\ {delta_p_expr} \\geq 0 \\end{{cases}} "
                       f"\\Leftrightarrow m \\neq {k}$ (vì $\\Delta' = 1 > 0$). \\\\\n"
                       f"Theo định lí Vi-et ta có: $x_1 + x_2 = {tong_v}, x_1x_2 = {tich_v}$. \\\\\n"
                       f"Theo đề ta có: $x_1 + x_2 + x_1x_2 < 1 \\Leftrightarrow {tong_v} + {tich_v} < 1 \\\\\n"
                       f"\\Leftrightarrow \\frac{{{latex(tu_so_1)}}}{{{latex(a)}}} < 1 "
                       f"\\Leftrightarrow \\frac{{{latex(tu_so_cuoi)}}}{{{latex(a)}}} < 0 \\\\\n"
                       f"\\Leftrightarrow {m_min} < m < {m_max}$.")

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_ans[0])+'}\n'
                '{'+str(list_ans[1])+'}\n'
                '{'+str(list_ans[2])+'}\n'
                '{'+str(list_ans[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

