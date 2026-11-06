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


def bt_dang12_p3_b4_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random giá trị a nguyên từ 2 đến 6
        val_a = random.choice([2, 3, 4, 5, 6])

        ans_val = 8 * (val_a ** 2)
        kq_str = str(ans_val)

        # Hình vẽ TikZ vẽ đúng 100% như ảnh mẫu, nét vẽ 1pt, điểm 1pt, màu black
        hinhve = (
            "\\begin{center}\n"
            "        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "        % Toa do cac dinh cua hinh chop S.ABCD\n"
            "        \\coordinate (A) at (0.0, 0.0);\n"
            "        \\coordinate (B) at (4.5, -0.2);\n"
            "        \\coordinate (D) at (1.8, 1.4);\n"
            "        \\coordinate (C) at (6.3, 1.2);\n"
            "        \\coordinate (S) at (0.2, 4.6);\n"
            "        \\coordinate (O) at ($(A)!0.5!(C)$);\n"
            "        \\coordinate (M) at ($(S)!0.667!(B)$);\n"
            "        \\coordinate (N) at ($(S)!0.667!(D)$);\n"
            "        \\coordinate (K) at ($(S)!0.667!(O)$);\n"
            "        \\coordinate (I) at ($(S)!0.5!(C)$);\n"
            "        \\draw[line width=1pt] (S)--(A)--(B)--(C)--(S) (S)--(B) (M)--(I);\n"
            "        \\draw[line width=1pt, dashed] (A)--(D)--(C) (S)--(D) (A)--(C) (B)--(D) (S)--(O) (M)--(N) (A)--(M) (A)--(N) (N)--(I) (A)--(I);\n"
            "        \\fill (S) circle (1pt) node[above left] {$S$};\n"
            "        \\fill (A) circle (1pt) node[below left] {$A$};\n"
            "        \\fill (B) circle (1pt) node[below] {$B$};\n"
            "        \\fill (C) circle (1pt) node[right] {$C$};\n"
            "        \\fill (D) circle (1pt) node[above right] {$D$};\n"
            "        \\fill (O) circle (1pt) node[below] {$O$};\n"
            "        \\fill (M) circle (1pt) node[right] {$M$};\n"
            "        \\fill (N) circle (1pt) node[left] {$N$};\n"
            "        \\fill (K) circle (1pt) node[left] {$K$};\n"
            "        \\fill (I) circle (1pt) node[above] {$I$};\n"
            "        \\end{tikzpicture}\n"
            "        \\end{center}"
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$. Có đáy $ABCD$ là hình vuông cạnh $3a\\sqrt{2}$. $SA \\perp (ABCD)$, $SA = 2a\\sqrt{7}$. Gọi $M, N$ lần lượt thuộc các cạnh $SB, SD$ sao cho $SM = 2MB$, $SN = 2ND$. Mặt phẳng $(AMN)$ cắt cạnh $SC$ tại $I$. Diện tích tứ giác $AMIN$ khi $a = %d$ bằng bao nhiêu?'''
                         % (val_a)
                         )

        # Nội dung lời giải
        loigiai = ('''Ta có $AC = BD = AB\\sqrt{2} = 3a\\sqrt{2} \\cdot \\sqrt{2} = 6a$, $SC = \\sqrt{SA^2 + AC^2} = \\sqrt{(2a\\sqrt{7})^2 + (6a)^2} = 8a$.\\\\
    Gọi $O$ là tâm của hình vuông $ABCD$.\\\\
    Trong mặt phẳng $(SBD)$, gọi giao điểm của $MN$ và $SO$ là $K$.\\\\
    Trong mặt phẳng $(SAC)$, gọi giao điểm của $AK$ và $SC$ là $I$.\\\\
    Thiết diện tạo bởi mặt phẳng $(AMN)$ với hình chóp $S.ABCD$ là tứ giác $AMIN$.\\\\
    Vì $SM = 2MB, SN = 2ND \\Rightarrow MN = \\frac{2}{3} BD = \\frac{2}{3} \\cdot 6a = 4a$.\\\\
    Đồng thời $SM = 2MB, SN = 2ND \\Rightarrow SK = \\frac{2}{3} SO$.\\\\
    Vì $SO$ là trung tuyến của tam giác $\\Delta SAC$ và $SK = \\frac{2}{3} SO$ nên $K$ là trọng tâm tam giác $\\Delta SAC$.\\\\
    Suy ra $AI$ là trung tuyến của tam giác $\\Delta SAC$, do đó $I$ là trung điểm của $SC$.\\\\
    Vì tam giác $\\Delta SAC$ vuông tại $A$ có trung tuyến $AI$ nên $AI = \\frac{1}{2} SC = \\frac{1}{2} \\cdot 8a = 4a$.\\\\
    Ta có:\\\\
    $\\begin{cases} MN // BD \\\\ BD \\perp (SAC) \\Rightarrow BD \\perp AI \\end{cases} \\Rightarrow AI \\perp MN$.\\\\
    Tứ giác $AMIN$ có hai đường chéo vuông góc nên diện tích của nó là:\\\\
    $S_{AMIN} = \\frac{1}{2} AI \\cdot MN = \\frac{1}{2} \\cdot 4a \\cdot 4a = 8a^2$.\\\\
    Với $a = %d$, ta có diện tích là $S_{AMIN} = 8 \\cdot %d^2 = %s$.\\\\
    Vậy diện tích tứ giác $AMIN$ là %s.'''
                   % (val_a, val_a, kq_str, kq_str)
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

