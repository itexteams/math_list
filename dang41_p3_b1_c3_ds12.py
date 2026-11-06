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


def bt_dang41_p3_b1_c3_ds12(self):
            # Khai báo biến
            # --- BƯỚC 1: NGHIÊN CỨU VÀ KHỞI TẠO BIẾN NGẪU NHIÊN ---

            m = random.randint(-3, 3) 
            N = random.randint(8, 15)

            # Tính toán các hằng số C_k:
            # F(pi/4 + k*pi) = tan(pi/4) + C_k = 1 + C_k
            # Theo đề bài: 1 + C_k = k + m  => C_k = k + m - 1

            # Tính giá trị từng số hạng F(n*pi):
            # F(n*pi) = tan(n*pi) + C_n = 0 + (n + m - 1) = n + m - 1

            # Tính tổng: S = sum_{n=0}^{N} (n + m - 1)
            def calculate_sum(n_val, m_val):
                total = 0
                for n in range(n_val + 1):
                    total += (n + m_val - 1)
                return total

            kq_dung = calculate_sum(N, m)

            # --- BƯỚC 2: TẠO CÁC PHƯƠNG ÁN SAI (KHÔNG TRÙNG ĐÁP ÁN ĐÚNG) ---
            s = set()
            while len(s) < 3:
                sai = kq_dung + random.choice([-2, -1, 1, 2, 5, 10, -5]) + random.randint(-3, 3)
                if sai != kq_dung:
                    s.add(f'${sai}$')

            list_sai = list(s)

            # --- BƯỚC 3: NỘI DUNG CÂU HỎI ---
            # Tạo chuỗi k + m để hiển thị
            if m == 0:
                bieu_thuc_k = "k"
            elif m > 0:
                bieu_thuc_k = f"k + {m}"
            else:
                bieu_thuc_k = f"k - {abs(m)}"

            noidungcauhoi = (
                f"Cho $F(x)$ là một nguyên hàm của hàm số $f(x) = \\frac{{1}}{{\\cos^2 x}}$. "
                f"Biết $F\\left( \\frac{{\\pi}}{{4}} + k\\pi \\right) = {bieu_thuc_k}$ với mọi $k \\in \\mathbb{{Z}}$. "
                f"Giá trị $F(0) + F(\\pi) + F(2\\pi) + \\dots + F({N}\\pi)$ bằng bao nhiêu?"
            )

            # --- BƯỚC 4: NỘI DUNG LỜI GIẢI CHI TIẾT ---
            # Chuẩn bị các bước tính toán cho lời giải
            c0 = 0 + m - 1
            c1 = 1 + m - 1
            cN = N + m - 1

            loigiai = (
                f"Ta có $\\int f(x) \\, \\text{{d}}x = \\int \\frac{{\\text{{d}}x}}{{\\cos^2 x}} = \\tan x + C.$\\\\ \n"
                f"Trên mỗi khoảng $\\left( \\frac{{(2k-1)\\pi}}{{2}}; \\frac{{(2k+1)\\pi}}{{2}} \\right)$, "
                f"hàm số $F(x)$ có dạng $F(x) = \\tan x + C_k$.\\\\ \n"
                f"Theo giả thiết: $F\\left( \\frac{{\\pi}}{{4}} + k\\pi \\right) = \\tan\\left( \\frac{{\\pi}}{{4}} + k\\pi \\right) + C_k = 1 + C_k = {bieu_thuc_k} \\Rightarrow C_k = k + {m-1 if m-1 !=0 else ''}$.\\\\ \n"
                f"Khi đó $F(n\\pi) = \\tan(n\\pi) + C_n = 0 + n + {m-1 if m-1 !=0 else ''} = n + {m-1 if m-1 !=0 else ''}$.\\\\ \n"
                f"Vậy tổng cần tính là:\\\\ \n"
                f"$F(0) + F(\\pi) + \\dots + F({N}\\pi) = ({c0}) + ({c1}) + \\dots + ({cN}) = {kq_dung}$."
            ).replace("+ -", "- ").replace("(0)", "0")

            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(kq_dung)) 

            # --- BƯỚC 5: XUẤT NỘI DUNG THEO MẪU ---
            da_d = '\\True $' + str(kq_dung) + '$'
            list_ans = [da_d] + list_sai
            random.shuffle(list_ans)

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

