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


def bt_dang84_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Để đảm bảo a, b dương (thuộc tia Ox, Oy)
            list_data = [
                {'a': 2, 'b': 4, 'xm': -1},
                {'a': 4, 'b': 2, 'xm': -2},
                {'a': 3, 'b': 6, 'xm': -1},
                {'a': 6, 'b': 3, 'xm': -2},
                {'a': 2, 'b': 8, 'xm': -1},
                {'a': 4, 'b': 4, 'xm': -2},
                {'a': 5, 'b': 10, 'xm': -1},
                {'a': 2, 'b': 6, 'xm': -1},
            ]

            data = random.choice(list_data)
            a_val = data['a']
            b_val = data['b']
            xm_val = data['xm']

            # Tính diện tích tam giác OAB: S = 1/2 * a * b
            dt_val = Rational(a_val * b_val, 2)

            # Tính tung độ điểm M thuộc đường thẳng: xm/a + ym/b = 1 => ym = b*(1 - xm/a)
            ym_val = int(b_val * (1 - Rational(xm_val, a_val)))

            # Tính giá trị biểu thức S = a + 2b
            S_correct = a_val + 2 * b_val

            # Tạo các phương án sai
            s = [
                '$S = %s$' % (latex(S_correct + 2)),
                '$S = %s$' % (latex(S_correct - 4)),
                '$S = %s$' % (latex(S_correct + 5)),
                '$S = %s$' % (latex(S_correct + randint(1, 3))),
                '$S = \\frac{%s}{3}$' % (latex(randint(20, 40))),
                '$S = %s$' % (latex(S_correct - 2)),
            ]

            # Loại bỏ giá trị trùng với đáp án đúng nếu có
            s = [item for item in s if item != '$S = %s$' % (latex(S_correct))]
            random.shuffle(s)

            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Câu hỏi
            noidungcauhoi = ('''Đường thẳng $d: \\frac{x}{a} + \\frac{y}{b} = 1, (a \\neq 0; b \\neq 0)$ đi qua $M(%s;%s)$ tạo với tia $Ox, Oy$ một tam giác có diện tích bằng $%s$. Giá trị $S = a + 2b$ bằng'''
                             % (latex(xm_val), latex(ym_val), latex(dt_val)))

            # Các đáp án
            da_d = ('\\True $S = %s$' % (latex(S_correct)))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            loigiai = ('''$d$ đi qua $M(%s; %s) \\Leftrightarrow \\frac{%s}{a} + \\frac{%s}{b} = 1$ (1).\\\\
                         Đường thẳng $d$ cắt tia $Ox$ tại $A(a;0)$ với $a > 0 \\Rightarrow OA = a$.\\\\
                         Đường thẳng $d$ cắt tia $Oy$ tại $B(0;b)$ với $b > 0 \\Rightarrow OB = b$.\\\\
                         $\\triangle OAB$ vuông tại $O$ nên có diện tích là $\\frac{1}{2}OA \\cdot OB = \\frac{1}{2}ab$.\\\\
                         Theo đề bài ta có $\\frac{1}{2}ab = %s \\Leftrightarrow ab = %s \\Leftrightarrow b = \\frac{%s}{a}$ (2).\\\\
                         Thay (2) vào (1) ta được: $\\frac{%s}{a} + \\frac{%s}{\\frac{%s}{a}} = 1 \\Leftrightarrow \\frac{%s}{a} + \\frac{%s a}{%s} = 1$.\\\\
                         Nhân cả hai vế với $%s a$ ta có phương án: $%s a^2 - %s a - %s = 0$.\\\\
                         Giải phương trình bậc hai trên với điều kiện $a > 0$, ta được $a = %s$.\\\\
                         Với $a = %s$, thay vào (2) ta được $b = \\frac{%s}{%s} = %s$.\\\\
                         Vậy $S = a + 2b = %s + 2 \\cdot %s = %s$.'''
                       % (latex(xm_val), latex(ym_val), latex(xm_val), latex(ym_val),
                          latex(dt_val), latex(2 * dt_val), latex(2 * dt_val),
                          latex(xm_val), latex(ym_val), latex(2 * dt_val), latex(xm_val), latex(ym_val), latex(2 * dt_val),
                          latex(2 * dt_val),
                          latex(ym_val), latex(2 * dt_val), latex(abs(xm_val * 2 * dt_val)),
                          latex(a_val),
                          latex(a_val), latex(2 * dt_val), latex(a_val), latex(b_val),
                          latex(a_val), latex(b_val), latex(S_correct)
                          ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

