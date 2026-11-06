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


def bt_dang38_p1_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random công bội của cấp số nhân (khác 1, -1, 0 để đảm bảo công thức có nghĩa và các phương án nhiễu hợp lý)
                a = random.choice([-4, -3, -2, 2, 3, 4])

                # Tính các số hạng đầu tiên để hiển thị trên đề bài
                term1 = str(a)
                term2 = "+ %s" % (a**2) if a**2 > 0 else "- %s" % abs(a**2)
                term3 = "+ %s" % (a**3) if a**3 > 0 else "- %s" % abs(a**3)
                term4 = "+ %s" % (a**4) if a**4 > 0 else "- %s" % abs(a**4)
                term5 = "+ %s" % (a**5) if a**5 > 0 else "- %s" % abs(a**5)
                term6 = "+ %s" % (a**6) if a**6 > 0 else "- %s" % abs(a**6)

                # Xác định dấu trước dấu ba chấm (...) dựa trên số hạng thứ 7
                sign_ellipsis = "-" if a**7 < 0 else "+"

                # Xử lý chuỗi công bội (nếu âm thì có ngoặc)
                a_str = "(%s)" % a if a < 0 else str(a)

                # Tính mẫu số chuẩn
                d = 1 - a

                # Các giá trị dùng cho phương án nhiễu (sai)
                abs_a = abs(a)
                d_abs = 1 - abs_a

                # Các đáp án trắc nghiệm
                da_val = 'S = %s \\cdot \\frac{1 - %s^n}{%s}' % (a, a_str, d)
                du = ['$%s$' % da_val]
                da = random.choice(du)

                s = [
                    '$%s$' % ('S = %s \\cdot \\frac{1 - %s^n}{%s}' % (abs_a, abs_a, d_abs)),
                    '$%s$' % ('S = %s n' % abs_a),
                    '$%s$' % ('S = %s^n' % abs_a),
                    '$%s$' % ('S = %s \\cdot \\frac{1 + %s^n}{%s}' % (a, a_str, d)),
                    '$%s$' % ('S = %s \\cdot \\frac{%s^n - 1}{%s}' % (a, a_str, d))
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Tổng $S = %s %s %s %s %s %s %s ... + %s^{n-1} + %s^n$ với $n \\ge 1, n \\in \\mathbb{N}$ bằng'''
                                 % (term1, term2, term3, term4, term5, term6, sign_ellipsis, a_str, a_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Các số hạng của tổng $S$ lập thành một cấp số nhân có số hạng đầu $u_1 = %s$ và công bội $q = %s$. \\\\
                             Tổng $S$ là tổng của $n$ số hạng đầu tiên của cấp số nhân này. \\\\
                             Áp dụng công thức tính tổng $n$ số hạng đầu tiên của cấp số nhân: $S_n = u_1 \\cdot \\frac{1 - q^n}{1 - q}$, ta có: \\\\
                             $S = %s \\cdot \\frac{1 - %s^n}{1 - %s} = %s \\cdot \\frac{1 - %s^n}{%s}$.'''
                             % (a, a, a, a_str, a_str, a, a_str, d))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi) + ' \n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

