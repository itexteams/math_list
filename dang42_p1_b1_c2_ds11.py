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


def bt_dang42_p1_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số
                a = random.randint(2, 4)

                # Tính các số hạng đúng
                u1 = sp.Rational(1, a**1 - 1)
                u2 = sp.Rational(2, a**2 - 1)
                u3 = sp.Rational(3, a**3 - 1)

                # Tính các số hạng sai để tạo nhiễu
                u3_sai1 = sp.Rational(1, a**3 - 1)
                if u3_sai1 == u3:
                     u3_sai1 = sp.Rational(1, a**3)

                u3_sai2 = sp.Rational(3, a**3)
                if u3_sai2 == u3:
                     u3_sai2 = sp.Rational(1, a**3 + 1)

                u2_sai = sp.Rational(2, a**2)
                u3_sai3 = sp.Rational(3, a**3 + 1)

                # Đảm bảo các đáp án sai khác nhau
                s_list = [
                    '\\frac{%s}{%s}; \\frac{%s}{%s}; \\frac{%s}{%s}' % (u1.p, u1.q, u2.p, u2.q, u3_sai1.p, u3_sai1.q),
                    '\\frac{%s}{%s}; \\frac{%s}{%s}; \\frac{%s}{%s}' % (u1.p, u1.q, u2.p, u2.q, u3_sai2.p, u3_sai2.q),
                    '\\frac{%s}{%s}; \\frac{%s}{%s}; \\frac{%s}{%s}' % (u1.p, u1.q, u2_sai.p, u2_sai.q, u3_sai3.p, u3_sai3.q)
                ]

                s = []
                for val in s_list:
                    if val not in s:
                        s.append(val)

                # Nếu chưa đủ 3 đáp án sai khác nhau
                if len(s) < 3:
                     s.append('\\frac{%s}{%s}; \\frac{%s}{%s}; \\frac{%s}{%s}' % (u1.p, u1.q, 1, a**2, 1, a**3))
                if len(s) < 3:
                     s.append('\\frac{%s}{%s}; \\frac{%s}{%s}; \\frac{%s}{%s}' % (u1.p, u1.q, u2.p, u2.q, 1, a**3 - 2))

                # Câu hỏi
                noidungcauhoi = ('Cho dãy số $(u_n)$, biết $u_n = \\frac{n}{%s^n - 1}$. Ba số hạng đầu tiên của dãy số đó là' % (a))

                # Các đáp án
                da_d = ('\\True $\\frac{%s}{%s}; \\frac{%s}{%s}; \\frac{%s}{%s}$' % (u1.p, u1.q, u2.p, u2.q, u3.p, u3.q))
                da_s1 = ('$%s$' % (s[0]))
                da_s2 = ('$%s$' % (s[1]))
                da_s3 = ('$%s$' % (s[2]))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Lần lượt thay $n = 1, 2, 3$ vào công thức của dãy số, ta được: \\\\ '
                           '$u_1 = \\frac{1}{%s^1 - 1} = \\frac{%s}{%s}$. \\\\ '
                           '$u_2 = \\frac{2}{%s^2 - 1} = \\frac{%s}{%s}$. \\\\ '
                           '$u_3 = \\frac{3}{%s^3 - 1} = \\frac{%s}{%s}$. \\\\ '
                           'Vậy ba số hạng đầu tiên là $\\frac{%s}{%s}; \\frac{%s}{%s}; \\frac{%s}{%s}$.' 
                           % (a, u1.p, u1.q, a, u2.p, u2.q, a, u3.p, u3.q, u1.p, u1.q, u2.p, u2.q, u3.p, u3.q))

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

