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


def bt_dang37_p3_b6_c2_hh11(self):
            # Khai báo biến
            # k là độ dài cạnh (thay cho k*a)
            lis_k = [1, 2, 3, 4, 5, 6]
            k = random.choice(lis_k)

            # Tính toán các giá trị số thực
            # Cạnh đáy AB = k
            # SB = k / tan(30) = k * sqrt(3)
            # SA = sqrt(SB^2 - AB^2) = sqrt(3k^2 - k^2) = k * sqrt(2)
            # V = 1/3 * SA * S_day = 1/3 * (k * sqrt(2)) * (k^2) = (k^3 * sqrt(2)) / 3

            canh_day = k
            dien_tich_day = k**2
            sa_real = k * math.sqrt(2)
            sb_real = k * math.sqrt(3)
            vol_real = (k**3 * math.sqrt(2)) / 3

            # Làm tròn kết quả đến hàng phần chục (1 chữ số thập phân)
            kq_dung_val = round(vol_real, 1)

            # Tạo các đáp án sai (cũng làm tròn đến 1 chữ số thập phân)
            # Sai 1: Quên 1/3 (V = SA * S_day)
            kq_sai1_val = round(sa_real * dien_tich_day, 1)
            # Sai 2: Nhầm đường cao (V = 1/3 * SB * S_day)
            kq_sai2_val = round((1/3) * sb_real * dien_tich_day, 1)
            # Sai 3: Nhầm công thức diện tích hoặc hệ số
            kq_sai3_val = round((2/3) * k**3, 1)

            # Đảm bảo các đáp án không trùng nhau do làm tròn
            if kq_sai1_val == kq_dung_val: kq_sai1_val += 1.5
            if kq_sai2_val == kq_dung_val: kq_sai2_val += 2.2
            if kq_sai3_val == kq_dung_val: kq_sai3_val += 0.9

            # Câu hỏi
            noidungcauhoi = (
                f"Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh ${canh_day}$, $SA$ vuông góc với đáy, "
                f"$SC$ tạo với mặt phẳng $(SAB)$ một góc $30^\\circ$. Thể tích khối chóp $S.ABCD$ "
                f"(làm tròn đến hàng phần chục) bằng"
            )

            # TikZ Code
            tikz_code = (
                "\\begin{center}\n"
                "\\begin{tikzpicture}[scale=1, line join=round, line cap=round, line width=1pt]\n"
                "\\coordinate (A) at (0,0);\n"
                "\\coordinate (B) at (-1.2,-1.2);\n"
                "\\coordinate (C) at (2.5,-1.2);\n"
                "\\coordinate (D) at (3.7,0);\n"
                "\\coordinate (S) at (0,3.5);\n"
                "\\draw [dashed] (S)--(A) (A)--(B) (A)--(D);\n"
                "\\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D);\n"
                "\\draw (0.3,2.6) arc (-60:-110:0.5);\n"
                "\\node at (0.4,2.4) {$30^\\circ$};\n"
                "\\node at (A) [left] {$A$};\n"
                "\\node at (B) [below left] {$B$};\n"
                "\\node at (C) [below right] {$C$};\n"
                "\\node at (D) [right] {$D$};\n"
                "\\node at (S) [above] {$S$};\n"
                "\\end{tikzpicture}\n"
                "\\end{center}"
            )

            # Các đáp án
            da_d = f"\\True ${kq_dung_val}$"
            da_s1 = f"${kq_sai1_val}$"
            da_s2 = f"${kq_sai2_val}$"
            da_s3 = f"${kq_sai3_val}$"

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Lời giải chi tiết
            loigiai = (
                f"Do $ABCD$ là hình vuông cạnh ${canh_day}$ nên: $S_{{ABCD}} = {canh_day}^2 = {dien_tich_day}$. \\\\\n"
                f"Chứng minh được $BC \\perp (SAB) \\Rightarrow$ góc giữa $SC$ và $(SAB)$ là $\\widehat{{CSB}} = 30^\\circ$. \\\\\n"
                f"Tam giác $SBC$ vuông tại $B$ nên $SB = \\frac{{BC}}{{\\tan 30^\\circ}} = \\frac{{{canh_day}}}{{\\frac{{1}}{{\\sqrt{{3}}}}}} = {canh_day}\\sqrt{{3}}$. \\\\\n"
                f"Tam giác $SAB$ vuông tại $A$ nên $SA = \\sqrt{{SB^2 - AB^2}} = \\sqrt{{({canh_day}\\sqrt{{3}})^2 - {canh_day}^2}} = {canh_day}\\sqrt{{2}} \\approx {round(sa_real, 2)}$. \\\\\n"
                f"Vậy $V_{{S.ABCD}} = \\frac{{1}}{{3}} \\cdot SA \\cdot S_{{ABCD}} = \\frac{{1}}{{3}} \\cdot {canh_day}\\sqrt{{2}} \\cdot {dien_tich_day} \\approx {kq_dung_val}$."
            )
            dapan='\\shortans[0]{$%s$}\n'%(str(kq_dung_val).replace('.',','))
            # Xuất nội dung
            content = (
                "\\begin{minipage}{\\textwidth}\n"
                "\\begin{ex}\n"
                + str(noidungcauhoi) + str(dapan)+
                "\\loigiai{" + str(tikz_code)+ str(loigiai) + "}\n"
                "\\end{ex}\n"
                "\\end{minipage}\n\n")
            return content

