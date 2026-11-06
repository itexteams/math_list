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


def bt_dang30_p1_b2_c3_ds11(self):
            # Khai báo biến
            # Giá trị đại diện tương ứng: 5, 7, 9, 11, 13
            def generate_data():
                while True:
                    n1 = random.randint(4, 8)
                    n2 = random.randint(10, 14)
                    n3 = random.randint(15, 20)
                    n4 = random.randint(8, 12)
                    n5 = 50 - (n1 + n2 + n3 + n4)
                    if n5 > 2:
                        return [n1, n2, n3, n4, n5]

            counts = generate_data()
            n1, n2, n3, n4, n5 = counts
            mids = [5, 7, 9, 11, 13]

            # Tính trung bình cộng
            mean_val = (5*n1 + 7*n2 + 9*n3 + 11*n4 + 13*n5) / 50
            mean_str = ("%.2f" % mean_val).replace('.', ',')

            # Tạo các đáp án nhiễu
            def get_distractors(correct_val):
                s = set()
                while len(s) < 3:
                    # Tạo nhiễu quanh giá trị đúng
                    noise = random.uniform(-0.5, 0.5)
                    val = correct_val + noise
                    val_str = ("%.2f" % val).replace('.', ',')
                    if val_str != str(correct_val).replace('.', ','):
                        s.add(val_str)
                return list(s)

            distractors = get_distractors(mean_val)

            # Định dạng đáp án
            da_d = '\\True $' + mean_str + '$'
            da_s1 = '$' + distractors[0] + '$'
            da_s2 = '$' + distractors[1] + '$'
            da_s3 = '$' + distractors[2] + '$'

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Bảng câu hỏi (LaTeX)
            table_q = ('''\\begin{center}
            \\begin{tabular}{|c|c|c|c|c|c|}
            \\hline
            Cân nặng (kg) & [4; 6) & [6; 8) & [8; 10) & [10; 12) & [12; 14) \\\\
            \\hline
            Số con lợn & %s & %s & %s & %s & %s \\\\
            \\hline
            \\end{tabular}
            \\end{center}''' %(n1, n2, n3, n4, n5))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cân nặng (kg) của 50 con lợn của một gia đình nông dân chăn nuôi được thống kê trong bảng dưới đây:
            %s
            Khối lượng trung bình của 50 con lợn ở bảng thống kê trên bằng''' % table_q)

            # Lời giải
            # Bảng lời giải
            table_sol = ('''\\begin{center}
            \\begin{tabular}{|c|c|c|c|c|c|}
            \\hline
            Cân nặng (kg) & [4; 6) & [6; 8) & [8; 10) & [10; 12) & [12; 14) \\\\
            \\hline
            Giá trị đại diện & 5 & 7 & 9 & 11 & 13 \\\\
            \\hline
            Số con lợn & %s & %s & %s & %s & %s \\\\
            \\hline
            \\end{tabular}
            \\end{center}''' %(n1, n2, n3, n4, n5))

            loigiai = ('''Ta có bảng giá trị đại diện:
            %s
            Khối lượng trung bình của 50 con lợn là:
            $\\bar{x} = \\frac{5 \\cdot %s + 7 \\cdot %s + 9 \\cdot %s + 11 \\cdot %s + 13 \\cdot %s}{50} = \\frac{%s}{50} = %s$ (kg).'''
            %(table_sol, n1, n2, n3, n4, n5, (5*n1 + 7*n2 + 9*n3 + 11*n4 + 13*n5), mean_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+list_1[0]+'}\n'
                '{'+list_1[1]+'}\n'
                '{'+list_1[2]+'}\n'
                '{'+list_1[3]+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

