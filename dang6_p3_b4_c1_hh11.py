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


def bt_dang6_p3_b4_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random tỷ số CQ = k * QD với k nguyên từ 2 đến 6
        k = random.choice([2, 3, 4, 5, 6])

        # Theo định lý Menelaus: SA = k * SD => AD = SA + SD = (k + 1) * DS
        ans_val = k + 1
        kq_str = str(ans_val)

        # Hình vẽ TikZ 100% như ảnh, nét 1pt, điểm 1pt, màu black
        hinhve = (
            "\\begin{center}\n"
            "        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "        \\coordinate (B) at (0,0);\n"
            "        \\coordinate (C) at (1.8,-1.7);\n"
            "        \\coordinate (A) at (2.0,2.3);\n"
            "        \\coordinate (D) at (3.8,0);\n"
            "        \\coordinate (I) at (4.9,0);\n"
            "        \\coordinate (P) at ($(B)!0.6!(A)$);\n"
            "        \\coordinate (R) at ($(B)!0.6!(C)$);\n"
            "        \\coordinate (Q) at (intersection of R--I and C--D);\n"
            "        \\coordinate (S) at (intersection of I--P and A--D);\n"
            "        \\draw[line width=1pt] (A)--(B)--(C)--(A) (A)--(D)--(I) (C)--(D) (P)--(R)  (Q)--(I) (A)--(C) (S)--(I);\n"
            "        \\draw[line width=1pt, dashed] (B)--(D) (R)--(Q) (S)--(D) (P)--(S);\n"
            "        \\fill (A) circle (1pt) node[above] {$A$};\n"
            "        \\fill (B) circle (1pt) node[left] {$B$};\n"
            "        \\fill (C) circle (1pt) node[below] {$C$};\n"
            "        \\fill (D) circle (1pt) node[above right] {$D$};\n"
            "        \\fill (I) circle (1pt) node[right] {$I$};\n"
            "        \\fill (P) circle (1pt) node[above left] {$P$};\n"
            "        \\fill (R) circle (1pt) node[below left] {$R$};\n"
            "        \\fill (Q) circle (1pt) node[below right] {$Q$};\n"
            "        \\fill (S) circle (1pt) node[above right] {$S$};\n"
            "        \\end{tikzpicture}\n"
            "        \\end{center}"
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tứ diện $ABCD$ và ba điểm $P,Q,R$ lần lượt trên ba cạnh $AB,CD,BC$ sao cho $PR // AC$ và $CQ = %d QD$. Gọi giao điểm của $AD$ và $(PQR)$ là $S$. Khi đó, $AD = x \\cdot DS$. Giá trị $x$ bằng bao nhiêu?'''
                         % (k)
                         )

        # Nội dung lời giải
        loigiai = (hinhve+'''Gọi $I$ là giao điểm của $BD$ và $RQ$. Gọi $S = IP \\cap AD$.\\\\
    Áp dụng định lí Menelaus trong tam giác $BCD$ với cát tuyến $R, Q, I$, ta có:\\\\
    $\\frac{DI}{IB} \\cdot \\frac{BR}{RC} \\cdot \\frac{CQ}{QD} = 1$ và $\\frac{CQ}{QD} = %d$ suy ra $\\frac{DI}{IB} \\cdot \\frac{BR}{RC} = \\frac{1}{%d} \\Leftrightarrow \\frac{DI}{IB} = \\frac{1}{%d} \\cdot \\frac{RC}{BR}$.\\\\
    Vì $PR // AC$ nên theo định lí Thales, ta có $\\frac{RC}{BR} = \\frac{AP}{PB} \\Rightarrow \\frac{DI}{IB} = \\frac{1}{%d} \\cdot \\frac{AP}{PB}$.\\\\
    Áp dụng định lí Menelaus trong tam giác $ABD$ với cát tuyến $P, S, I$, ta có:\\\\
    $\\frac{SA}{SD} \\cdot \\frac{DI}{IB} \\cdot \\frac{BP}{PA} = 1 \\Rightarrow \\frac{SA}{SD} \\cdot \\frac{1}{%d} \\cdot \\frac{AP}{PB} \\cdot \\frac{BP}{PA} = 1 \\Leftrightarrow \\frac{SA}{SD} = %d \\Rightarrow SA = %d SD$.\\\\
    Suy ra $AD = SA + SD = %d DS + DS = %s DS$.\\\\
    Vậy $x = %s$.'''
                   % (k, k, k, k, k, k, k, k, kq_str, kq_str)
                   )

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

