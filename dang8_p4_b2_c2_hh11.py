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


def bt_dang8_p4_b2_c2_hh11(self):
            # Khai báo biến
            # Khai báo các bộ tên điểm để random
            danh_sach_ten = [
                ('S', 'A', 'B', 'C', 'D', 'O'),
                ('S', 'M', 'N', 'P', 'Q', 'I'),
                ('S', 'E', 'F', 'G', 'H', 'K')
            ]

            ten = random.choice(danh_sach_ten)
            S, A, B, C, D, O = ten

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho hình chóp $' + S + '.' + A + B + C + D + '$ có đáy là hình bình hành tâm $' + O + '$, '
                '$' + S + A + '=' + S + C + '$, $' + S + B + '=' + S + D + '$. Chứng minh $' + S + O + '\\perp \\left(' + A + B + C + D + '\\right)$'
            )

            # Tạo các đáp án
            da_dung = '\\True $' + S + O + '\\perp \\left(' + A + B + C + D + '\\right)$'
            sai_1 = '$' + S + A + '\\perp \\left(' + A + B + C + D + '\\right)$'
            sai_2 = '$' + S + B + '\\perp \\left(' + A + B + C + D + '\\right)$'
            sai_3 = '$' + S + C + '\\perp \\left(' + A + B + C + D + '\\right)$'
            sai_4 = '$' + S + D + '\\perp \\left(' + A + B + C + D + '\\right)$'

            # Lấy ngẫu nhiên 3 đáp án sai và đảm bảo không trùng đáp án đúng
            ds_sai = [sai_1, sai_2, sai_3, sai_4]
            random.shuffle(ds_sai)
            list_1 = [da_dung, ds_sai[0], ds_sai[1], ds_sai[2]]
            random.shuffle(list_1)

            # Vẽ hình bằng TikZ (độ dày nét 1pt)

            # Nội dung lời giải chi tiết
            loigiai = (    '\\begin{center} \\begin{tikzpicture}[scale=0.8, line join=round, line cap=round, line width=1pt]\n'
                '  \\coordinate (A) at (1.5,1.5);\n'
                '  \\coordinate (B) at (5,1.5);\n'
                '  \\coordinate (C) at (3.5,0);\n'
                '  \\coordinate (D) at (0,0);\n'
                '  \\coordinate (O) at (2.5,0.75);\n'
                '  \\coordinate (S) at (2.5,4);\n'
                '  \\draw[dashed] (A)--(B) (A)--(D) (S)--(A) (A)--(C) (B)--(D) (S)--(O);\n'
                '  \\draw (S)--(D) (S)--(C) (S)--(B) (D)--(C) (C)--(B);\n'
                '  \\node at (S) [above] {$' + S + '$};\n'
                '  \\node at (A) [left] {$' + A + '$};\n'
                '  \\node at (B) [right] {$' + B + '$};\n'
                '  \\node at (C) [below right] {$' + C + '$};\n'
                '  \\node at (D) [below left] {$' + D + '$};\n'
                '  \\node at (O) [below] {$' + O + '$};\n'
                '\\end{tikzpicture} \\end{center}'
                'Ta có $' + O + '$ là trung điểm của $' + A + C + '$ và $' + B + D + '$ (tính chất hình bình hành).\\\\\n'
                'Vì tam giác $' + S + A + C + '$ có $' + S + A + '=' + S + C + '$ nên tam giác $' + S + A + C + '$ cân tại $' + S + '$.\\\\\n'
                'Mà $' + O + '$ là trung điểm của $' + A + C + '$ nên $' + S + O + '\\perp ' + A + C + '$.\\\\\n'
                'Tương tự, vì tam giác $' + S + B + D + '$ có $' + S + B + '=' + S + D + '$ nên tam giác $' + S + B + D + '$ cân tại $' + S + '$.\\\\\n'
                'Mà $' + O + '$ là trung điểm của $' + B + D + '$ nên $' + S + O + '\\perp ' + B + D + '$.\\\\\n'
                'Ta có: $\\begin{cases} ' + S + O + '\\perp ' + A + C + ' \\\\ ' + S + O + '\\perp ' + B + D + ' \\end{cases}$ mà $' + A + C + '$ và $' + B + D + '$ cắt nhau tại $' + O + '$ trong mặt phẳng $\\left(' + A + B + C + D + '\\right)$.\\\\\n'
                'Suy ra $' + S + O + '\\perp \\left(' + A + B + C + D + '\\right)$.'
            )

            # Xuất nội dung theo cấu trúc mẫu (Không dùng tiền tố r)
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'  + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

