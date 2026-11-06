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


def bt_dang32_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Chọn ngẫu nhiên bề lõm: 1 là quay xuống (a < 0), 2 là quay lên (a > 0)
            dang_be_lom = random.choice(['a_am', 'a_duong'])

            if dang_be_lom == 'a_am':
                a_val = -1
                a_str = "a < 0"
                huong_lom = "xuống dưới"
                # Chọn vị trí đỉnh x_I = -b/2a. Để giống hình mẫu, chọn x_I dương
                # Vì a < 0, để -b/2a > 0 thì b phải > 0
                b_val = 1
                b_str = "b > 0"
                hoanh_do_dinh = "dương"
                # Chọn giao điểm với Oy (c). Để giống hình mẫu, chọn c > 0
                c_val = 1
                c_str = "c > 0"
                tung_do_giao = "dương"
                # Đồ thị Tikz tương ứng
                tikz_code = r"""
                \begin{tikzpicture}[>=stealth, scale=0.6]
                    \draw[->] (-1,0) -- (4,0) node[below] {$x$};
                    \draw[->] (0,-1) -- (0,4) node[left] {$y$};
                    \draw[thick,blue,samples=100,domain=-0.5:3.5] plot (\x, {-0.8*(\x-1.5)*(\x-1.5) + 3});
                    \node[below left] at (0,0) {$O$};
                \end{tikzpicture}"""
            else:
                a_val = 1
                a_str = "a > 0"
                huong_lom = "lên trên"
                b_val = -1
                b_str = "b < 0"
                hoanh_do_dinh = "dương"
                c_val = -1
                c_str = "c < 0"
                tung_do_giao = "âm"
                tikz_code = r"""
                \begin{tikzpicture}[>=stealth, scale=0.6]
                    \draw[->] (-1,0) -- (4,0) node[below] {$x$};
                    \draw[->] (0,-2) -- (0,3) node[left] {$y$};
                    \draw[thick,blue,samples=100,domain=-0.5:3.5] plot (\x, {0.8*(\x-1.5)*(\x-1.5) - 2.5});
                    \node[above left] at (0,0) {$O$};
                \end{tikzpicture}"""

            # Bước 4: Điều chỉnh các phương án không trùng lặp
            dap_an_dung = f"${a_str}, {b_str}, {c_str}$"

            # Tạo danh sách các khả năng dấu (trừ đáp án đúng)
            options = [
                "$a < 0, b > 0, c < 0$",
                "$a < 0, b < 0, c < 0$",
                "$a < 0, b < 0, c > 0$",
                "$a > 0, b > 0, c > 0$",
                "$a > 0, b < 0, c > 0$",
                "$a > 0, b > 0, c < 0$"
            ]
            if dap_an_dung in options:
                options.remove(dap_an_dung)

            random.shuffle(options)
            da_s1, da_s2, da_s3 = options[:3]

            # Nội dung câu hỏi
            noidungcauhoi = f"Cho parabol $y = ax^2 + bx + c$ có đồ thị như hình vẽ dưới đây. Khẳng định nào dưới đây đúng?\n\\begin{{center}} {tikz_code} \\end{{center}}"

            # Nội dung lời giải (B2: Viết y hệt logic hình ảnh)
            loigiai = f"""Parabol quay bề lõm {huong_lom} $\\Rightarrow {a_str}$. \\\\
            Parabol cắt $Oy$ tại điểm có tung độ {tung_do_giao} $\\Rightarrow {c_str}$. \\\\
            Đỉnh của parabol có hoành độ {hoanh_do_dinh} $\\Rightarrow \\frac{{-b}}{{2a}} > 0 \\Rightarrow \\frac{{b}}{{a}} < 0$, mà ${a_str}$ nên suy ra ${b_str}$. \\\\
            Vậy ${a_str}, {b_str}, {c_str}$."""

            # Xuất nội dung theo cấu trúc mẫu
            list_1 = ['\\True ' + dap_an_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

