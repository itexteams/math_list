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


def bt_dang27_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số của cạnh bên (cạnh bên = k*a)
                # Trong đề bài gốc k = 2
                k = random.randint(2, 5)
                a = symbols('a')

                # Tính toán các thông số
                # AI = a*sqrt(3)/2
                # AO = a*sqrt(3)/3
                # SO = sqrt((k*a)**2 - (a*sqrt(3)/3)**2) = sqrt(k^2 - 1/3) * a = sqrt((3k^2-1)/3) * a
                # V = 1/3 * Diện tích đáy * Chiều cao
                # S_day = a^2 * sqrt(3) / 4
                # V = 1/3 * (a^2 * sqrt(3) / 4) * (sqrt(3*k**2 - 1) / sqrt(3)) * a = (sqrt(3*k**2 - 1) * a^3) / 12

                inner_val = 3 * k**2 - 1
                tu_so = sqrt(inner_val)

                # Đáp án đúng
                kq_dung = "$" + "\\frac{\\sqrt{" + str(inner_val) + "}a^3}{12}" + "$"

                # Các đáp án sai (thay đổi mẫu số hoặc biểu thức trong căn)
                s1 = "$" + "\\frac{\\sqrt{" + str(inner_val) + "}a^3}{6}" + "$"
                s2 = "$" + "\\frac{\\sqrt{" + str(inner_val) + "}a^3}{4}" + "$"
                s3 = "$" + "\\frac{\\sqrt{" + str(3 * k**2 + 1) + "}a^3}{12}" + "$"
                s4 = "$" + "\\frac{\\sqrt{" + str(k**2 + 2) + "}a^3}{12}" + "$"

                da_d = "\\True " + kq_dung

                # Chọn ngẫu nhiên 3 đáp án sai từ danh sách
                s_list = [s1, s2, s3, s4]
                random.shuffle(s_list)
                da_s1 = s_list[0]
                da_s2 = s_list[1]
                da_s3 = s_list[2]

                # Trộn các đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung câu hỏi
                noidungcauhoi = (
                    "Cho khối chóp tam giác đều $S.ABC$ có cạnh đáy bằng $a$ và cạnh bên bằng $%sa$. Thể tích $V$ của khối chóp $S.ABC$ bằng"
                    % (latex(k) if k != 1 else "")
                )

                # TikZ code cho hình vẽ giống 100%
                tikz_code = (
                    "\\begin{center}\n"
                    "\\begin{tikzpicture}[scale=1, line join=round, line cap=round, line width=1pt]\n"
                    "\\coordinate (A) at (-1.5,-1);\n"
                    "\\coordinate (B) at (0,-2);\n"
                    "\\coordinate (C) at (2.5,-1);\n"
                    "\\coordinate (I) at ($(B)!0.5!(C)$);\n"
                    "\\coordinate (O) at ($(A)!2/3!(I)$);\n"
                    "\\coordinate (S) at ($(O)+(0,3.5)$);\n"
                    "\\draw (S)--(A)--(B)--(C)--(S)--(B);\n"
                    "\\draw [dashed] (A)--(C) (S)--(O) (A)--(I) (O)--(B) (O)--(C);\n"
                    "\\node [left] at (A) {$A$};\n"
                    "\\node [below] at (B) {$B$};\n"
                    "\\node [right] at (C) {$C$};\n"
                    "\\node [above] at (S) {$S$};\n"
                    "\\node [below] at (O) {$O$};\n"
                    "\\node [below right] at (I) {$I$};\n"
                    "\\end{tikzpicture}\n"
                    "\\end{center}"
                )

                # Lời giải chi tiết
                loigiai = (
                    "Do đáy là tam giác đều nên gọi $I$ là trung điểm cạnh $BC$, khi đó $AI$ là đường cao của tam giác đáy. "
                    "Theo định lý Pitago ta có $AI = \\sqrt{a^2 - \\left(\\frac{a}{2}\\right)^2} = \\frac{a\\sqrt{3}}{2}$, và $AO = \\frac{2}{3}AI = \\frac{2a\\sqrt{3}}{3 \\cdot 2} = \\frac{a\\sqrt{3}}{3}$.\\\\ \n"
                    "Trong tam giác $SOA$ vuông tại $O$ ta có $SO = \\sqrt{\\left(%sa\\right)^2 - \\left(\\frac{a\\sqrt{3}}{3}\\right)^2} = \\sqrt{%sa^2 - \\frac{a^2}{3}} = \\frac{\\sqrt{%s}a}{\\sqrt{3}}$.\\\\ \n"
                    "Diện tích tam giác đáy $ABC$ là $S_{ABC} = \\frac{1}{2} a \\cdot \\frac{a\\sqrt{3}}{2} = \\frac{a^2\\sqrt{3}}{4}$.\\\\ \n"
                    "Vậy thể tích khối chóp $S.ABC$ là $V = \\frac{1}{3} S_{ABC} \\cdot SO = \\frac{1}{3} \\cdot \\frac{a^2\\sqrt{3}}{4} \\cdot \\frac{\\sqrt{%s}a}{\\sqrt{3}} = \\frac{\\sqrt{%s}a^3}{12}$."
                    % (latex(k), latex(k**2), latex(3*k**2-1), latex(3*k**2-1), latex(3*k**2-1))
                )

            # Xuất câu trắc nghiệm
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n"
                + str(noidungcauhoi) + "\n"
                "\\choice \n"
                "{" + str(list_1[0]) + "}\n"
                "{" + str(list_1[1]) + "}\n"
                "{" + str(list_1[2]) + "}\n"
                "{" + str(list_1[3]) + "}\n"
                "\\loigiai{" + str(tikz_code)+ str(loigiai) + "}\n"
                "\\end{ex}\n"
                "\\end{minipage} \n\n")
            return content

