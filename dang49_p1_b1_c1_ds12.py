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


def bt_dang49_p1_b1_c1_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        tu_so = random.choice([1, 2, 3, 4, 5])
        mau_so = tu_so + random.choice([1, 2, 3])
        co_so = Rational(tu_so, mau_so) # 0 < co_so < 1

        x0 = random.randint(-4, 4)
        if x0 == 0:
            x0 = 1
        b_hs = -2 * x0
        c_hs = x0**2 + random.randint(1, 3)

        u_expr = x**2 + b_hs * x + c_hs
        u_dao_ham = 2 * x + b_hs

        # Giá trị cực đại tại x = x0: u(x0) = c_hs - x0^2
        u_max = c_hs - x0**2

        # Do 0 < a < 1, u(x) đạt cực tiểu tại x = x0, nên y = a^(u(x)) đạt cực đại tại x = x0
        da_dung_str = 'Hàm số đạt cực đại tại $x = %s$' % latex(x0)

        # Tập hợp các phương án nhiễu
        s = [
            'Hàm số đạt cực tiểu tại $x = %s$' % latex(x0),
            'Hàm số đạt cực tiểu tại $x = %s$' % latex(-x0),
            'Hàm số đạt cực đại tại $x = %s$' % latex(-x0),
            'Hàm số đạt cực tiểu tại $x = %s$' % latex(x0 + 1),
            'Hàm số đạt cực đại tại $x = %s$' % latex(x0 + 1),
            'Hàm số không có cực trị',
            'Hàm số có 2 cực trị',
            'Hàm số có 3 cực trị'
        ]

        # Lấy ngẫu nhiên 3 phương án sai khác nhau
        random.shuffle(s)
        das1 = s.pop()
        das2 = s.pop()
        das3 = s.pop()

        # Câu hỏi
        noidungcauhoi = ('''Cho hàm số $y=\\left(%s\\right)^{%s}$. Khẳng định nào sau đây đúng?'''
                         % (latex(co_so), latex(u_expr)))

        # Các đáp án
        da_d = ('\\True ' + str(da_dung_str))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách và xáo trộn
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải chi tiết có bảng biến thiên và xét dấu
        loigiai = ('''Tập xác định của hàm số là $D = \\mathbb{R}$.\\\\
    Ta có:
    $y' = \\left( \\left(%s\\right)^{%s} \\right)' \\\\
       = \\left(%s\\right)' \\cdot \\left(%s\\right)^{%s} \\cdot \\ln\\left(%s\\right) \\\\
       = \\left(%s\\right) \\cdot \\left(%s\\right)^{%s} \\cdot \\ln\\left(%s\\right).$ \\\\
    Phương trình đạo hàm $y' = 0$:
    $y' = 0 \\Leftrightarrow %s = 0 \\quad \\left(\\text{do } \\left(%s\\right)^{%s} > 0 \\text{ và } \\ln\\left(%s\\right) \\neq 0\\right) \\\\
           \\Leftrightarrow x = %s.$\\\\
    Vì $0 < %s < 1$ nên $\\ln\\left(%s\\right) < 0$.\\\\
    Bảng biến thiên và xét dấu của đạo hàm $y'$:
    \\begin{center}
    \\begin{tikzpicture}
    \\tkzTabInit[lgt=1.5,espcl=3]{$x$/0.8,$y'$/0.8,$y$/1.5}{$-\\infty$,$%s$,$+\\infty$}
    \\tkzTabLine{,+,$0$,-,}
    \\tkzTabVar{-/$0$,+/$\\left(%s\\right)^{%s}$,-/$0$}
    \\end{tikzpicture}
    \\end{center}
    Từ bảng biến thiên, ta thấy đạo hàm $y'$ đổi dấu từ dương sang âm khi qua điểm $x = %s$.\\\\
    Vậy hàm số đạt cực đại tại $x = %s$.'''
                   % (latex(co_so), latex(u_expr),
                      latex(u_expr), latex(co_so), latex(u_expr), latex(co_so),
                      latex(u_dao_ham), latex(co_so), latex(u_expr), latex(co_so),
                      latex(u_dao_ham), latex(co_so), latex(u_expr), latex(co_so),
                      latex(x0),
                      latex(co_so), latex(co_so),
                      latex(x0),
                      latex(co_so), latex(u_max),
                      latex(x0),
                      latex(x0)))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\choice\n'
               '{' + str(list_1[1]) + '}\n'
               '{' + str(list_1[2]) + '}\n'
               '{' + str(list_1[3]) + '}\n'
               '{' + str(list_1[0]) + '}\n'
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n\\end{minipage}\n\n')
    return content

