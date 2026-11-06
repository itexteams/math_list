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


def bt_dang37_p4_b6_c2_hh11(self):
            # Khai báo biến
            # k là hệ số của cạnh a (ví dụ: a, 2a, 3a...)
            lis_k = [1, 2, 3, 4, 5]
            k = random.choice(lis_k)

            # Tính toán các giá trị theo k
            # Cạnh đáy AB = k*a
            # SB = k*a / tan(30) = k*a * sqrt(3)
            # SA = sqrt(SB^2 - AB^2) = sqrt(3k^2*a^2 - k^2*a^2) = k*a*sqrt(2)
            # V = 1/3 * SA * S_day = 1/3 * (k*a*sqrt(2)) * (k^2*a^2) = (k^3*sqrt(2)/3)*a^3

            # Thiết lập các biểu thức latex
            if k == 1:
                canh_day = "a"
                dien_tich_day = "a^2"
                sa_val = "\\sqrt{2}a"
                sb_val = "\\sqrt{3}a"
                kq_dung = "\\frac{\\sqrt{2}a^3}{3}"
                kq_sai1 = "\\frac{2a^3}{3}"
                kq_sai2 = "\\frac{\\sqrt{6}a^3}{3}"
                kq_sai3 = "\\sqrt{2}a^3"
            else:
                canh_day = f"{k}a"
                dien_tich_day = f"{k**2}a^2"
                sa_val = f"{k}\\sqrt{{2}}a"
                sb_val = f"{k}\\sqrt{{3}}a"
                # Tính tử số cho thể tích
                kq_dung = f"\\frac{{{k**3}\\sqrt{{2}}a^3}}{{3}}"
                kq_sai1 = f"\\frac{{{2*k**3}a^3}}{{3}}"
                kq_sai2 = f"\\frac{{{k**3}\\sqrt{{6}}a^3}}{{3}}"
                kq_sai3 = f"{k**3}\\sqrt{{2}}a^3"

            # Câu hỏi
            noidungcauhoi = (
                "Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh $" + canh_day + "$, $SA$ vuông góc với đáy, $SC$ tạo với mặt phẳng $(SAB)$ một góc $30^\\circ$. Tính thể tích khối chóp $S.ABCD$."
            )

            # TikZ Code (Nét vẽ 1pt, giống hình ảnh 100%)
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
            da_d = "\\True $" + kq_dung + "$"
            da_s1 = "$" + kq_sai1 + "$"
            da_s2 = "$" + kq_sai2 + "$"
            da_s3 = "$" + kq_sai3 + "$"

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Lời giải chi tiết
            loigiai = (
                "Do $ABCD$ là hình vuông cạnh $" + canh_day + "$ nên: $S_{ABCD} = " + dien_tich_day + "$. \\\\\n"
                "Chứng minh được $BC \\perp \\left( SAB \\right) \\Rightarrow$ góc giữa $SC$ và $\\left( SAB \\right)$ là $\\widehat{CSB} = 30^\\circ$. \\\\\n"
                "Đặt $SA = x$. Tam giác $SAB$ vuông tại $A$ nên $SB = \\sqrt{SA^2 + AB^2} = \\sqrt{x^2 + \\left( " + canh_day + " \\right)^2}$. \\\\\n"
                "Tam giác $SBC$ vuông tại $B$ nên $\\tan \\widehat{CSB} = \\tan 30^\\circ = \\frac{1}{\\sqrt{3}} = \\frac{BC}{SB}$. \\\\\n"
                "Ta được: $SB = BC\\sqrt{3} \\Leftrightarrow \\sqrt{x^2 + " + str(k**2) + "a^2} = " + canh_day + "\\sqrt{3} \\Rightarrow x = " + sa_val + "$. \\\\\n"
                "Vậy $V_{S.ABCD} = \\frac{1}{3} \\cdot SA \\cdot S_{ABCD} = \\frac{1}{3} \\cdot " + sa_val + " \\cdot " + dien_tich_day + " = " + kq_dung + "$."
            )

            # Xuất nội dung
            content = (
                "\\begin{minipage}{\\textwidth}\n"
                "\\begin{ex}\n"
                + str(noidungcauhoi) + "\n"
                "\\loigiai{" + str(tikz_code)+ str(loigiai) + "}\n"
                "\\end{ex}\n"
                "\\end{minipage}\n\n")
            return content

