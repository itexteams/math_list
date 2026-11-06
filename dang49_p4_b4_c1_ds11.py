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


def bt_dang49_p4_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random vế phải của phương trình: có thể là sqrt(3) hoặc 1 hoặc -sqrt(3) hoặc 0,... 
                # Ở đây cố định cấu trúc mẫu và tạo đáp án nhiễu linh hoạt dựa trên bài toán gốc để đảm bảo độ chính xác.
                # Bài toán gốc: VP = sqrt(3)
                vp_val = sqrt(3)
                vp_latex = latex(vp_val)

                # Đáp án đúng của bài toán gốc
                da = 'x = -\\frac{\\pi}{6} + k2\\pi'
                du = ['$%s$' % da]
                da_choice = random.choice(du)

                # Các phương án nhiễu dựa theo cấu trúc trắc nghiệm của câu hỏi
                s = [
                    '$x = \\pm \\frac{\\pi}{6} + k2\\pi$',
                    '$x = \\frac{\\pi}{6} + k2\\pi$',
                    '$x = -\\frac{\\pi}{6} + k2\\pi, x = -\\frac{\\pi}{2} + k2\\pi$',
                    '$x = -\\frac{\\pi}{3} + k2\\pi$',
                    '$x = \\frac{\\pi}{3} + k2\\pi$'
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Giải phương trình $\\frac{\\cos x (1 - 2\\sin x)}{2\\cos^2 x - \\sin x - 1} = %s$.'''
                                 %(vp_latex))

                # Các đáp án
                da_d = ('\\True ' + str(da_choice))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Điều kiện: \\\\
            $2\\cos^2 x - \\sin x - 1 \\neq 0 \\Leftrightarrow 2\\sin^2 x + \\sin x - 1 \\neq 0 \\Leftrightarrow \\begin{cases} \\sin x \\neq -1 \\\\ \\sin x \\neq \\frac{1}{2} \\end{cases} \\Leftrightarrow \\begin{cases} x \\neq -\\frac{\\pi}{2} + k2\\pi \\\\ x \\neq \\frac{\\pi}{6} + k2\\pi \\\\ x \\neq \\frac{5\\pi}{6} + k2\\pi \\end{cases} \\Leftrightarrow x \\neq -\\frac{\\pi}{6} + \\frac{k2\\pi}{3}$. \\\\
            Ta có $\\frac{\\cos x(1 - 2\\sin x)}{2\\cos^2 x - \\sin x - 1} = %s \\Leftrightarrow \\cos x - \\sin 2x = %s (\\cos 2x - \\sin x)$ \\\\
            $\\Leftrightarrow %s \\sin x + \\cos x = \\sin 2x + %s \\cos x \\Leftrightarrow \\sin\\left(x + \\frac{\\pi}{6}\\right) = \\sin\\left(2x + \\frac{\\pi}{3}\\right)$ \\\\
            $\\Leftrightarrow \\begin{bmatrix} 2x + \\frac{\\pi}{3} = x + \\frac{\\pi}{6} + k2\\pi \\\\ 2x + \\frac{\\pi}{3} = \\pi - \\left(x + \\frac{\\pi}{6}\\right) + k2\\pi \\end{bmatrix} \\Leftrightarrow \\begin{bmatrix} x = -\\frac{\\pi}{6} + k2\\pi \\\\ x = \\frac{\\pi}{6} + \\frac{k2\\pi}{3} \\end{bmatrix}$. \\\\
            Đối chiếu với điều kiện, ta được nghiệm của phương trình là $x = -\\frac{\\pi}{6} + k2\\pi$.'''
                           %(vp_latex, vp_latex, vp_latex, vp_latex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

