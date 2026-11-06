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


def bt_dang72_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số a cho hàm số y = (sin x + 1) / (2cos^2(ax) - 1)
                # Đưa giá trị 3 của bài gốc vào tập random
                a = random.choice([2, 3, 4, 5, 6])

                # Tính các hệ số liên quan cho đáp án và lời giải
                a2 = 2 * a
                a4 = 4 * a

                # Câu hỏi
                noidungcauhoi = ('Tìm tập xác định của hàm số $y = \\frac{\\sin x + 1}{2\\cos^2 %sx - 1}$.' % (a))

                # Đáp án đúng
                # Điều kiện: 2cos^2(ax) - 1 != 0 <=> cos(2ax) != 0 <=> 2ax != pi/2 + k*pi <=> x != pi/(4a) + k*pi/(2a)
                da_str = 'D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{%s} + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}' % (a4, a2)

                # Các đáp án sai (Distractors)
                # Sai lầm 1: Quên chia chu kỳ k*pi cho 2a
                das1_str = 'D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{%s} + k\\pi, k \\in \\mathbb{Z} \\right\\}' % (a4)

                # Sai lầm 2: Nhầm điều kiện cos(2ax) != 0 thành sin(2ax) != 0 (x != k*pi/(2a))
                das2_str = 'D = \\mathbb{R} \\setminus \\left\\{ \\frac{k\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}' % (a2)

                # Sai lầm 3: Quên nhân đôi góc trong công thức (áp dụng sai thành cos(ax) != 0)
                das3_str = 'D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{%s} + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z} \\right\\}' % (a2, a)

                # Đóng gói các đáp án
                da_d = ('\\True $%s$' % (da_str))
                da_s1 = ('$%s$' % (das1_str))
                da_s2 = ('$%s$' % (das2_str))
                da_s3 = ('$%s$' % (das3_str))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Hàm số xác định khi và chỉ khi mẫu số khác $0$: \\\\
                             $2\\cos^2 %sx - 1 \\neq 0$ \\\\
                             Áp dụng công thức $\\cos 2a = 2\\cos^2 a - 1$, ta có: \\\\
                             $\\Leftrightarrow \\cos %sx \\neq 0$ \\\\
                             $\\Leftrightarrow %sx \\neq \\frac{\\pi}{2} + k\\pi$ \\\\
                             $\\Leftrightarrow x \\neq \\frac{\\pi}{%s} + \\frac{k\\pi}{%s}, k \\in \\mathbb{Z}$.\\\\
                             Vậy tập xác định của hàm số là $%s$.'''
                             % (a, a2, a2, a4, a2, da_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

