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


def bt_dang22_p1_b2_c2_hh10(self):
            # Khai báo biến
            # Random góc giữa hai lực (các góc đẹp để có giá trị lượng giác chính xác)
            alpha_deg = random.choice([30, 45, 60])
            beta_deg = 180 - alpha_deg

            # Ánh xạ giá trị lượng giác của góc bù beta (để hiển thị lời giải đẹp)
            if beta_deg == 150:
                cos_str = "-\\frac{\\sqrt{3}}{2}"
                cos_val = -math.sqrt(3) / 2
            elif beta_deg == 135:
                cos_str = "-\\frac{\\sqrt{2}}{2}"
                cos_val = -math.sqrt(2) / 2
            else: # 120 độ
                cos_str = "-\\frac{1}{2}"
                cos_val = -0.5

            # Random cường độ lực F1, F2 (bội số của 10)
            f1 = random.randint(3, 10) * 10
            f2 = random.randint(3, 10) * 10
            while f1 == f2: # Tránh trường hợp bằng nhau để hình vẽ minh hoạ tổng quát hơn
                f2 = random.randint(3, 10) * 10

            # Tính toán bình phương độ dài AC (định lí cosin)
            # AC^2 = F1^2 + F2^2 - 2*F1*F2*cos(beta)
            ac2_val = f1**2 + f2**2 - 2 * f1 * f2 * cos_val
            ac2_round = round(ac2_val, 2)
            ac2_str = str(ac2_round).replace('.', ',') if not ac2_round.is_integer() else str(int(ac2_round))

            # Tính kết quả cuối cùng (làm tròn đến hàng đơn vị)
            kq_val = math.sqrt(ac2_val)
            kq = int(kq_val + 0.5) # Quy tắc làm tròn lên truyền thống
            kq_str = str(kq)

            # Tạo các đáp án nhiễu
            s = [kq + 1, kq - 1, kq + 2, kq - 2, kq + 5, kq - 5]
            s = list(set([x for x in s if x > 0])) # Đảm bảo không trùng và luôn dương
            random.shuffle(s)

            # Khởi tạo danh sách đáp án
            dapan_dung = f'${kq_str}$'
            dapan_sai = [f'${str(x)}$' for x in s[:3]]

            list_1 = ['\\True ' + dapan_dung] + dapan_sai
            random.shuffle(list_1) # Trộn ngẫu nhiên

            # ==========================================
            # Tạo nội dung Câu hỏi và Lời giải
            # ==========================================

            noidungcauhoi = (f"Cho hai lực $\\overrightarrow{{F_1}}, \\overrightarrow{{F_2}}$ có điểm đặt $A$ tạo với nhau góc ${alpha_deg}^\\circ$, "
                             f"biết rằng cường độ của hai lực $\\overrightarrow{{F_1}}$ và $\\overrightarrow{{F_2}}$ lần lượt bằng ${f1}\\text{{ N}}, {f2}\\text{{ N}}$. "
                             f"Tính cường độ tổng hợp của hai lực trên? Kết quả làm tròn đến hàng đơn vị.")

            # Code vẽ hình bằng TikZ tự động chèn vào lời giải (ĐÃ FIX LỖI F-STRING CỦA TIKZ)
            tikz_code = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                '\\coordinate (A) at (0,2);\n'
                '\\coordinate (B) at (4,2);\n'
                '\\coordinate (D) at (2.5,0.5);\n'
                '\\coordinate (C) at (6.5,0.5);\n'
                '\\draw[->, thick] (A)--(B) node[ above] {$\\overrightarrow{F_1}$};\n'
                '\\draw[->, thick] (A)--(D) node[ below left] {$\\overrightarrow{F_2}$};\n'
                '\\draw[->, thick] (A)--(C);\n'
                '\\draw[dashed] (B)--(C)--(D);\n'
                f'\\draw (0.6,2) arc (0:-35:0.6) node[midway, right, xshift=-2pt, yshift=-1pt] {{${alpha_deg}^\\circ$}};\n'
                f'\\draw (3.6,2) arc (180:215:0.4) node[midway, left, xshift=1pt, yshift=-4pt] {{${beta_deg}^\\circ$}};\n'
                '\\foreach \\p/\\pos in {A/above left, B/above right, C/below right, D/below right}\n'
                '\\fill (\\p) circle (1.5pt) node[\\pos] {$\\p$};\n'
                f'\\node at (2,2.3) {{${f1} \\text{{ N}}$}};\n'
                f'\\node at (1.2,0.6) {{${f2} \\text{{ N}}$}};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
            )

            # Lời giải chi tiết
            loigiai = (
                f"{tikz_code}"
                f"Đặt $\\overrightarrow{{F_1}} = \\overrightarrow{{AB}}, \\overrightarrow{{F_2}} = \\overrightarrow{{AD}}$. \\\\\n"
                f"Vẽ hình bình hành $ABCD$. \\\\\n"
                f"Ta có: $\\overrightarrow{{F_1}} + \\overrightarrow{{F_2}} = \\overrightarrow{{AB}} + \\overrightarrow{{AD}} = \\overrightarrow{{AC}}$. \\\\\n"
                f"Vì $\\widehat{{BAD}} = {alpha_deg}^\\circ \\Rightarrow \\widehat{{ABC}} = {beta_deg}^\\circ; AD = {f2} = BC$. \\\\\n"
                f"Theo định lí cosin ta có: \\\\\n"
                f"$\\begin{{aligned}} AC^2 &= AB^2 + BC^2 - 2AB \\cdot BC \\cdot \\cos {beta_deg}^\\circ \\\\ &= {f1}^2 + {f2}^2 - 2 \\cdot {f1} \\cdot {f2} \\cdot \\left( {cos_str} \\right) \\approx {ac2_str} \\Rightarrow AC \\approx {kq_str}. \\end{{aligned}}$ \\\\\n"
                f"Vậy vectơ hợp lực của $\\overrightarrow{{F_1}}, \\overrightarrow{{F_2}}$ có độ lớn là: $|\\overrightarrow{{F_1}} + \\overrightarrow{{F_2}}| \\approx {kq_str}\\text{{ N}}.$"
            )

            # ==========================================
            # Xuất câu trắc nghiệm theo đúng form yêu cầu
            # ==========================================

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{\n' + str(loigiai) + '\n}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

