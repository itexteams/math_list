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


def bt_dang33_p1_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Câu hỏi
        noidungcauhoi = "Cho hình chóp tứ giác $S.ABCD$ có đáy không là hình thang. Giao tuyến của hai mặt phẳng $(SAC)$ và $(SBD)$ là"

        # Random tên các điểm giao cắt để tạo phương án nhiễu
        points = ['I', 'K', 'E', 'F', 'M', 'N', 'P', 'Q']
        random.shuffle(points)

        # Chọn 2 tên điểm cho các giao điểm giả định
        p1 = points[0]
        p2 = points[1]
        # Điểm giao của hai đường chéo (luôn là O như truyền thống hoặc có thể đổi nếu muốn)
        p_O = 'O'

        # Đáp án đúng
        kq = "$S%s$ ($%s$ là giao điểm của $AC$ và $BD$)" % (p_O, p_O)
        da_d = '\\True ' + kq

        # Các đáp án nhiễu
        s = [
            "$S%s$ ($%s$ là giao điểm của $AB$ và $CD$)" % (p1, p1),
            "$S%s$ ($%s$ là giao điểm của $AD$ và $BC$)" % (p2, p2),
            "$SA$",
            "$SB$",
            "$SC$",
            "$SD$"
        ]

        # Chọn 3 đáp án nhiễu ngẫu nhiên
        das1 = random.choice(s[:2]) # Ưu tiên lấy ít nhất 1 đáp án giao điểm các cạnh đối
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Gán vào biến đáp án
        da_s1 = das1
        da_s2 = das2
        da_s3 = das3

        # Đưa các đáp án vào danh sách và xáo trộn
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Lời giải chi tiết
        loigiai = ("\\begin{center}\n"
        "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
        "\\coordinate (A) at (0,0);\n"
        "\\coordinate (D) at (4.5,0);\n"
        "\\coordinate (B) at (1,-1.5);\n"
        "\\coordinate (C) at (4,-2);\n"
        "\\coordinate (S) at (2.5,3.5);\n"
        "\\coordinate (O) at (intersection of A--C and B--D);\n"
        "\\draw[line width=1pt] (S)--(A) (S)--(B) (S)--(C) (S)--(D) (A)--(B)--(C)--(D);\n"
        "\\draw[line width=1pt, dashed] (A)--(D) (A)--(C) (B)--(D) (S)--(O);\n"
        "\\fill (A) circle (1pt) node[left] {$A$};\n"
        "\\fill (B) circle (1pt) node[below left] {$B$};\n"
        "\\fill (C) circle (1pt) node[below right] {$C$};\n"
        "\\fill (D) circle (1pt) node[right] {$D$};\n"
        "\\fill (S) circle (1pt) node[above] {$S$};\n"
        "\\fill (O) circle (1pt) node[below] {$%s$};\n"
        "\\end{tikzpicture}\n"
        "\\end{center}"
            "Trong mặt phẳng $(ABCD)$, gọi $%s$ là giao điểm của $AC$ và $BD$. \\\\ "
                   "Ta có: $S \\in (SAC) \\cap (SBD) \\quad (1)$ \\\\ "
                   "Lại có: $\\begin{cases} %s \\in AC \\subset (SAC) \\\\ %s \\in BD \\subset (SBD) \\end{cases} \\Rightarrow %s \\in (SAC) \\cap (SBD) \\quad (2)$ \\\\ "
                   "Từ $(1)$ và $(2)$ suy ra $(SAC) \\cap (SBD) = S%s$. \\\\ "
                   ) % (p_O, p_O, p_O, p_O, p_O, p_O)

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content

