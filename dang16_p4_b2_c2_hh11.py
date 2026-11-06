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


def bt_dang16_p4_b2_c2_hh11(self):
            # Khai báo biến
            # Chúng ta sẽ random bộ tên các đỉnh của hình chóp
            danh_sach_bo_chu = [
                {'S': 'S', 'A': 'A', 'B': 'B', 'C': 'C', 'H': 'H'},
                {'S': 'P', 'A': 'O', 'B': 'M', 'C': 'N', 'H': 'K'},
                {'S': 'D', 'A': 'E', 'B': 'F', 'C': 'G', 'H': 'I'},
                {'S': 'S', 'A': 'H', 'B': 'A', 'C': 'B', 'H': 'M'}
            ]

            bo_chon = random.choice(danh_sach_bo_chu)
            S = bo_chon['S']
            A = bo_chon['S'] # Đỉnh chóp
            A = bo_chon['A'] # Hình chiếu của S lên đáy
            B = bo_chon['B']
            C = bo_chon['C']
            H = bo_chon['H'] # Hình chiếu của S lên BC

            # Bước 4: Điều chỉnh các phương án sai
            # Đáp án đúng: BC vuông góc AH
            da_dung = '$' + C + B + ' \\perp ' + A + H + '$'

            # Các phương án sai ngẫu nhiên
            cac_phuong_an_sai = [
                '$' + C + B + ' \\perp ' + S + C + '$',
                '$' + C + B + ' \\perp ' + A + B + '$',
                '$' + C + B + ' \\perp ' + A + C + '$',
                '$' + S + A + ' \\perp ' + S + B + '$',
                '$' + S + H + ' \\perp ' + A + C + '$'
            ]
            random.shuffle(cac_phuong_an_sai)
            da_s1, da_s2, da_s3 = cac_phuong_an_sai[:3]

            # Câu hỏi
            noidungcauhoi = (
                'Cho hình chóp $' + S + '.' + A + B + C + '$ có $' + S + A + ' \\perp \\left( ' + A + B + C + ' \\right)$ '
                'và $' + H + '$ là hình chiếu vuông góc của $' + S + '$ lên $' + B + C + '$. Chứng minh $' + C + B + ' \\perp ' + A + H + '$.'
            )

            # Các đáp án
            da_d = ('\\True ' + da_dung)
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            loigiai = (    '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1, line width=1pt, >=stealth]\n'
                '  \\coordinate (A) at (0,0);\n'
                '  \\coordinate (S) at (0,3);\n'
                '  \\coordinate (B) at (1.5,-1.2);\n'
                '  \\coordinate (C) at (5,-0.5);\n'
                '  % Tính toán chân đường vuông góc H trên BC\n'
                '  \\coordinate (H) at (2.81,-0.94);\n'
                '  \\draw [dashed] (A)--(C) (A)--(H);\n'
                '  \\draw (S)--(A) (A)--(B);'
                '  \\draw (S)--(B) (S)--(C) (B)--(C) (S)--(H);\n'
                '  \\node at (A) [left] {$' + A + '$};\n'
                '  \\node at (S) [above] {$' + S + '$};\n'
                '  \\node at (B) [below left] {$' + B + '$};\n'
                '  \\node at (C) [right] {$' + C + '$};\n'
                '  \\node at (H) [below right] {$' + H + '$};\n'
                '  % Ký hiệu vuông góc\n'
                '  \\draw (0,0.3)--(0.3,0.3)--(0.3,0);\n'
                '  \\draw (2.65,-0.65)--(2.9,-0.58)--(3.05,-0.87);\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
                'Ta có $' + S + A + ' \\perp \\left( ' + A + B + C + ' \\right)$ nên $' + S + A + ' \\perp ' + B + C + '$ (vì $' + B + C + '$ nằm trong mặt phẳng đáy).\\\\ \n'
                'Theo giả thiết, $' + H + '$ là hình chiếu vuông góc của $' + S + '$ lên $' + B + C + '$, suy ra $' + S + H + ' \\perp ' + B + C + '$.\\\\ \n'
                'Trong mặt phẳng $\\left( ' + S + A + H + ' \\right)$, ta có:\\\\ \n'
                '$\\begin{cases} ' + B + C + ' \\perp ' + S + A + ' \\\\ ' + B + C + ' \\perp ' + S + H + ' \\end{cases} '
                '\\Rightarrow ' + B + C + ' \\perp \\left( ' + S + A + H + ' \\right)$.\\\\ \n'
                'Vì $' + A + H + '$ nằm trong mặt phẳng $\\left( ' + S + A + H + ' \\right)$, nên $' + B + C + ' \\perp ' + A + H + '$.'
            )

            # Xuất câu trắc nghiệm theo mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


