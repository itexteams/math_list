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


def bt_dang40_p1_b3_c1_hh12(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            xA, yA, zA = randint(-4, 4), randint(-4, 4), randint(-4, 4)
            xB, yB, zB = randint(-4, 4), randint(-4, 4), randint(-4, 4)
            cA = xA**2 + yA**2 + zA**2
            cB = xB**2 + yB**2 + zB**2
            tu_so = cB - cA
            mau_so = 2 * (xB - xA)
            # Đảm bảo mẫu số khác 0 và m khác 0 để các điểm không bị trùng gốc tọa độ
            if mau_so != 0 and tu_so != 0:
                m_val = sp.Rational(tu_so, mau_so)
                break

        m_latex = latex(m_val)
        da = f"$M\\left({m_latex};0;0\\right)$"

        # Tập hợp các đáp án nhiễu phong phú, tránh thiếu phần tử
        s_set = set()
        s_set.add(f"$M\\left(0;{m_latex};0\\right)$")
        s_set.add(f"$M\\left(0;0;{m_latex}\\right)$")
        s_set.add(f"$M\\left({latex(-m_val)};0;0\\right)$")
        s_set.add(f"$M\\left({latex(m_val + 1)};0;0\\right)$")
        s_set.add(f"$M\\left({latex(m_val - 1)};0;0\\right)$")
        s_set.add(f"$M\\left({latex(2 * m_val)};0;0\\right)$")
        s_set.add(f"$M\\left(0;{latex(-m_val)};0\\right)$")

        # Loại bỏ đáp án đúng nếu trùng
        s_set.discard(da)

        s = list(s_set)
        random.shuffle(s)
        das1, das2, das3 = s[0], s[1], s[2]

        # Biểu thức tính toán chuẩn LaTeX
        m_sym = symbols('m')
        am2_expr = expand((m_sym - xA)**2 + yA**2 + zA**2)
        bm2_expr = expand((m_sym - xB)**2 + yB**2 + zB**2)

        noidungcauhoi = f"Trong không gian $Oxyz$, cho hai điểm $A({xA};{yA};{zA})$ và $B({xB};{yB};{zB})$. Tìm tọa độ điểm $M$ thuộc trục $Ox$ sao cho $M$ cách đều hai điểm $A, B$."

        da_d = '\\True ' + str(da)
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = (
            f"Vì điểm $M$ thuộc trục $Ox$ nên tọa độ của $M$ có dạng $M(m;0;0)$.\\\\\n"
            f"Ta có:\\\\\n"
            f"$\\overrightarrow{{AM}} = (m - {xA}; {-yA}; {-zA}) \\Rightarrow AM^2 = (m - {xA})^2 + ({-yA})^2 + ({-zA})^2 = {latex(am2_expr)}$.\\\\\n"
            f"$\\overrightarrow{{BM}} = (m - {xB}; {-yB}; {-zB}) \\Rightarrow BM^2 = (m - {xB})^2 + ({-yB})^2 + ({-zB})^2 = {latex(bm2_expr)}$.\\\\\n"
            f"Điểm $M$ cách đều hai điểm $A, B \\Leftrightarrow AM = BM \\Leftrightarrow AM^2 = BM^2$\\\\\n"
            f"$\\Leftrightarrow {latex(am2_expr)} = {latex(bm2_expr)} \\Leftrightarrow {2 * (xB - xA)}m = {cB - cA} \\Leftrightarrow m = {m_latex}$.\\\\\n"
            f"Vậy tọa độ điểm cần tìm là $M\\left({m_latex};0;0\\right)$."
        )

    # Xuất câu trắc nghiệm
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\choice \n'
        '{' + str(list_1[0]) + '}\n'
        '{' + str(list_1[1]) + '}\n'
        '{' + str(list_1[2]) + '}\n'
        '{' + str(list_1[3]) + '}\n'
        '\\loigiai{\n' + str(loigiai) + '\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n'  ) 
    content = content.replace("+-", "-").replace("- -", "+").replace("--", "+").replace("+ -", "-")
    return content

