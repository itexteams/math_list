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


def bt_dang9_p3_b4_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Trọng tâm G chia đoạn trung tuyến IA theo tỉ lệ IG/IA = 1/3
        # Làm tròn đến hàng phần trăm theo yêu cầu đề bài
        val = Decimal(1) / Decimal(3)
        kq = val.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Hình vẽ TikZ vẽ đúng 100% như ảnh, nét 1pt, điểm 1pt, màu black
        hinhve = (
            "\\begin{center}\n"
            "        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "        \\coordinate (S) at (2.2, 4.0);\n"
            "        \\coordinate (C) at (0.0, 0.7);\n"
            "        \\coordinate (B) at (1.2, -0.6);\n"
            "        \\coordinate (A) at (5.2, 0.5);\n"
            "        \\coordinate (I) at ($(B)!0.5!(C)$);\n"
            "        \\coordinate (G) at ($(I)!0.333!(A)$);\n"
            "        \\coordinate (MidAB) at ($(A)!0.5!(B)$);\n"
            "        \\coordinate (M) at ($(S)!0.333!(A)$);\n"
            "        \\coordinate (N) at ($(B)!0.333!(A)$);\n"
            "        \\coordinate (P) at ($(C)!0.333!(A)$);\n"
            "        \\draw[line width=1pt] (S)--(C)--(B)--(S) (S)--(A)--(B) (S)--(I) (M)--(N);\n"
            "        \\draw[line width=1pt, dashed] (A)--(C) (A)--(I) (C)--(MidAB) (M)--(G) (M)--(P)--(N);\n"
            "        \\fill (S) circle (1pt) node[above] {$S$};\n"
            "        \\fill (C) circle (1pt) node[left] {$C$};\n"
            "        \\fill (B) circle (1pt) node[below] {$B$};\n"
            "        \\fill (A) circle (1pt) node[right] {$A$};\n"
            "        \\fill (I) circle (1pt) node[below left] {$I$};\n"
            "        \\fill (G) circle (1pt) node[below] {$G$};\n"
            "        \\fill (M) circle (1pt) node[above right] {$M$};\n"
            "        \\fill (N) circle (1pt) node[below] {$N$};\n"
            "        \\fill (P) circle (1pt) node[above] {$P$};\n"
            "        \\fill (MidAB) circle (1pt);\n"
            "        \\end{tikzpicture}\n"
            "        \\end{center}"
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABC$ có $G$ là trọng tâm tam giác $ABC$. Gọi $(\\alpha)$ là mặt phẳng qua $G$ và song song với mặt phẳng $(SBC)$. Gọi thiết diện của hình chóp $S.ABC$ cắt bởi mặt phẳng $(\\alpha)$ là tam giác $MNP$ với $M \\in SA, N \\in AB, P \\in AC$. Giá trị của biểu thức $\\frac{SM}{SA}$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm).'''  )

        # Nội dung lời giải
        loigiai = (hinhve+'''Gọi $I$ là trung điểm $BC$.\\\\
    Ta có $(\\alpha) // (SBC)$ và mặt phẳng $(SAI)$ cắt hai mặt phẳng $(\\alpha)$, $(SBC)$ lần lượt theo các giao tuyến $MG$ và $SI$, suy ra $SI // MG$.\\\\
    Áp dụng định lí Thales trong tam giác $SAI$, ta có $\\frac{SM}{SA} = \\frac{IG}{IA}$.\\\\
    Vì $G$ là trọng tâm tam giác $ABC$ nên $\\frac{IG}{IA} = \\frac{1}{3}$.\\\\
    Do đó $\\frac{SM}{SA} = \\frac{1}{3} \\approx %s$.\\\\
    Vậy giá trị của $\\frac{SM}{SA}$ bằng $%s$.'''
                   % (kq_str, kq_str)
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

