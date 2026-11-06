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


def bt_dang29_p1_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random biến số a (với cos a = 1/a)
                a = random.choice([2, 3, 4, 5])
                k = a**3 - a

                # Tính toán đáp án
                ans_val = Rational(2 - a**2, a**2)
                da = '$%s$' % latex(ans_val)

                # Tạo các phương án nhiễu
                pool = [
                    Rational(2 + a**2, a**2),
                    Rational(a**2 - 2, a**2),
                    Rational(1, a**2),
                    Rational(-1, a**2),
                    Rational(1, a),
                    Rational(-1, a)
                ]
                # Bổ sung các phương án nhiễu đặc trưng khi a = 2 giống bài mẫu
                if a == 2:
                    pool.extend([sqrt(3)/2, -sqrt(3)/2, Rational(1, 2)])

                # Lọc các phương án trùng với đáp án đúng
                pool_unique = []
                for val in pool:
                    if val != ans_val and val not in pool_unique:
                        pool_unique.append(val)

                random.shuffle(pool_unique)
                das1 = '$%s$' % latex(pool_unique[0])
                das2 = '$%s$' % latex(pool_unique[1])
                das3 = '$%s$' % latex(pool_unique[2])

                # Câu hỏi
                noidungcauhoi = ('''Giả sử $\\frac{\\sin \\alpha}{%s}$, $\\cos \\alpha$, $\\tan \\alpha$ theo thứ tự đó là một cấp số nhân. Giá trị $\\cos 2\\alpha$ bằng''' % k)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Theo giả thiết $\\frac{\\sin \\alpha}{%s}$, $\\cos \\alpha$, $\\tan \\alpha$ theo thứ tự đó là một cấp số nhân nên ta có: \\\\
                             $\\cos^2 \\alpha = \\frac{\\sin \\alpha}{%s} \\cdot \\tan \\alpha \\Leftrightarrow \\cos^2 \\alpha = \\frac{\\sin^2 \\alpha}{%s \\cos \\alpha}$ \\\\
                             $\\Leftrightarrow %s \\cos^3 \\alpha = \\sin^2 \\alpha = 1 - \\cos^2 \\alpha \\Leftrightarrow %s \\cos^3 \\alpha + \\cos^2 \\alpha - 1 = 0$ \\\\
                             $\\Leftrightarrow \\left( \\cos \\alpha - \\frac{1}{%s} \\right) \\left( %s \\cos^2 \\alpha + %s \\cos \\alpha + 1 \\right) = 0$. \\\\
                             Vì phương trình $%s t^2 + %s t + 1 = 0$ vô nghiệm nên ta có $\\cos \\alpha = \\frac{1}{%s}$. \\\\
                             Vậy $\\cos 2\\alpha = 2\\cos^2 \\alpha - 1 = 2 \\left( \\frac{1}{%s} \\right)^2 - 1 = %s$.'''
                             % (k, k, k, k, k, a, a**2 - 1, a, a**2 - 1, a, a, a, latex(ans_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

