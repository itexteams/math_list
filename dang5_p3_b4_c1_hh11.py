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


def bt_dang5_p3_b4_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random hệ số k sao cho AA' = k * MA' (k nguyên từ 3 đến 6)
        k = random.choice([3, 4, 5, 6])

        # Theo đề bài: AA' = k * MA' => AM = (k - 1) * MA' hay A'M / AM = 1 / (k - 1)
        val = Decimal(1) / Decimal(k - 1)
        kq = val.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Hình vẽ TikZ vẽ đúng 100% theo mẫu và ảnh cung cấp, bỏ lưới tọa độ, màu black
        hinhve = (
            "\\begin{center}\n"
            "        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "        \\coordinate (Ap) at (2.0, 3.5);\n"
            "        \\coordinate (Bp) at (6.0, 3.5);\n"
            "        \\coordinate (Dp) at (0.6, 1.8);\n"
            "        \\coordinate (Cp) at (4.6, 1.8);\n"
            "        \\coordinate (A) at (2.7, 0.2);\n"
            "        \\coordinate (B) at (6.7, 0.2);\n"
            "        \\coordinate (D) at (1.3, -1.5);\n"
            "        \\coordinate (C) at (5.3, -1.5);\n"
            "        \\coordinate (M) at ($(Ap)!0.25!(A)$);\n"
            "        \\coordinate (N) at ($(Bp)!0.25!(B)$);\n"
            "        \\coordinate (P) at ($(Dp)!0.25!(D)$);\n"
            "        \\coordinate (Q) at ($(Cp)!0.25!(C)$);\n"
            "        \\draw[line width=1pt] (Ap)--(Bp) (Dp)--(Cp)--(Bp) (Dp)--(D)--(C)--(Cp) (C)--(B)--(Bp);\n"
            "        \\draw[line width=1pt] (P)--(Q)--(N);\n"
            "        \\draw[line width=1pt, dashed] (Ap)--(Dp) (Ap)--(A)--(D) (A)--(B);\n"
            "        \\draw[line width=1pt, dashed] (P)--(M)--(N);\n"
            "        \\fill (Ap) circle (1pt) node[above] {$A'$};\n"
            "        \\fill (Bp) circle (1pt) node[above right] {$B'$};\n"
            "        \\fill (Cp) circle (1pt) node[above left] {$C'$};\n"
            "        \\fill (Dp) circle (1pt) node[above left] {$D'$};\n"
            "        \\fill (A) circle (1pt) node[above right] {$A$};\n"
            "        \\fill (B) circle (1pt) node[right] {$B$};\n"
            "        \\fill (C) circle (1pt) node[right] {$C$};\n"
            "        \\fill (D) circle (1pt) node[above left] {$D$};\n"
            "        \\fill (M) circle (1pt) node[above right] {$M$};\n"
            "        \\fill (N) circle (1pt) node[above right] {$N$};\n"
            "        \\fill (P) circle (1pt);\n"
            "        \\fill (Q) circle (1pt);\n"
            "        \\end{tikzpicture}\n"
            "        \\end{center}"
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình hộp $ABCD.A'B'C'D'$. Gọi $M$ nằm trên cạnh $AA'$ sao cho $AA' = %d MA'$. Mặt phẳng qua $M$ và song song $(A'B'C'D')$ cắt $BB'$ tại $N$. Tỉ số $\\frac{B'N}{BN}$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm).'''
                         % (k)
                         )

        # Nội dung lời giải
        loigiai = (hinhve+'''Theo định lí Thales trong không gian, ta có: $\\frac{A'M}{AM} = \\frac{B'N}{BN} = \\frac{1}{%d} \\approx %s$.\\\\
    Vậy tỉ số $\\frac{B'N}{BN} \\approx %s$.'''
                   % (k - 1, kq_str, kq_str)
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

