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


def bt_dang11_p1_b3_c1_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        lis = [1, -1, 2, 3, 4, 5, -2, -3, -4, -5]
        xa = random.choice(lis)
        ya = random.choice(lis)
        za = random.choice(lis)

        xb = random.choice(lis)
        yb = random.choice(lis)
        zb = random.choice(lis)

        xc = random.choice(lis)
        yc = random.choice(lis)
        zc = random.choice(lis)

        # Đảm bảo B và C không trùng tọa độ thành phần để tránh chia cho 0
        while xc == xb or yc == yb or zc == zb:
            xc = random.choice(lis)
            yc = random.choice(lis)
            zc = random.choice(lis)

        x = symbols('x')
        y = symbols('y')
        z = symbols('z')

        u1, u2, u3 = xc - xb, yc - yb, zc - zb

        bt1 = u1 * (x - xa) + u2 * (y - ya) + u3 * (z - za)

        bien_y = ((x - xb) / u1) * u2 + yb
        bien_z = ((x - xb) / u1) * u3 + zb

        pt_x = Eq(u1 * (x - xa) + u2 * (bien_y - ya) + u3 * (bien_z - za), 0)

        # Sửa lỗi: dùng sp.solve để tránh bị ghi đè hàm solve
        xh_res = sp.solve(pt_x, x)
        if isinstance(xh_res, list) and len(xh_res) > 0:
            xh = xh_res[0]
        elif isinstance(xh_res, dict):
            xh = xh_res[x]
        else:
            xh = xh_res

        yh = (xh - xb) * u2 / u1 + yb
        zh = (xh - xb) * u3 / u1 + zb

        # Rút gọn nghiệm dưới dạng số hữu tỉ
        xh = Rational(xh)
        yh = Rational(yh)
        zh = Rational(zh)

        du = ['$\\left(%s; %s; %s \\right)$' % (latex(xh), latex(yh), latex(zh))]
        da = random.choice(du)
        s = [
            '$\\left(%s; %s; %s \\right)$' % (latex(xh), latex(yh), latex(zh + 1)),
            '$\\left(%s; %s; %s \\right)$' % (latex(xh), latex(yh + 1), latex(zh)),
            '$\\left(%s; %s; %s \\right)$' % (latex(xh), latex(yh), latex(zh - 1)),
            '$\\left(%s; %s; %s \\right)$' % (latex(xh - 1), latex(yh - 1), latex(zh)),
            '$\\left(%s; %s; %s \\right)$' % (latex(xh - 1), latex(yh), latex(zh + 2)),
            '$\\left(%s; %s; %s \\right)$' % (latex(xh - 1), latex(yh + 2), latex(zh)),
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = (
            'Trong không gian $Oxyz$, cho ba điểm $A(%s;%s;%s), B(%s;%s;%s)$ và $C(%s;%s;%s)$. '
            'Gọi $H$ là hình chiếu vuông góc của $A$ trên $BC$. Tọa độ điểm $H$ là \n'
            % (latex(xa), latex(ya), latex(za), latex(xb), latex(yb), latex(zb), latex(xc), latex(yc), latex(zc))
        )

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = (
            'Gọi $H(x;y;z)$, ta có \\\\ \n'
            '\\hspace*{1cm} $\\vec{AH}=(x+%s; y+%s; z+%s)$. \\\\ \n'
            '\\hspace*{1cm} $\\vec{BC}=(%s; %s; %s)$. \\\\ \n'
            '$H$ là hình chiếu vuông góc của $A$ trên $BC$ nên $AH$ vuông góc với $BC$.  \\\\ \n'
            'Do đó \\\\ \n'
            '\\hspace*{1cm} $\\vec{BC} \\cdot \\vec{AH}=0 \\Leftrightarrow %s(x+%s)+%s(y+%s)+%s(z+%s)=0$. \\\\ \n'
            '\\hspace*{3.55cm} $\\Leftrightarrow %s=0$ \\hspace*{1cm} (1). \\\\ \n'
            'Mặt khác \\\\ \n'
            '\\hspace*{1cm} $\\vec{BH}=(x+%s; y+%s; z+%s)$. \\\\ \n'
            'Ba điểm $B, C$ và $H$ thẳng hàng nên hai vectơ $\\vec{BH}$ và $\\vec{BC}$ cùng phương. \\\\ \n'
            'Ta có \\\\ \n'
            '\\hspace*{1cm} $\\dfrac{x+%s}{%s}=\\dfrac{y+%s}{%s}=\\dfrac{z+%s}{%s} '
            '\\Leftrightarrow \\heva{& \\dfrac{x+%s}{%s}=\\dfrac{y+%s}{%s} \\\\& \\dfrac{x+%s}{%s}=\\dfrac{z+%s}{%s}} '
            '\\Leftrightarrow \\heva{& y=%s\\\\& z=%s}$ \\hspace*{1cm} (2). \\\\ \n'
            'Thay (2) vào (1) ta được $%s \\Leftrightarrow x=%s$. \\\\ \n'
            'Suy ra $y=%s$ và $z=%s$. \\\\ \n'
            'Vậy điểm cần tìm là $H \\left(%s; %s; %s \\right)$. \\\\ \n'
            % (
                latex(-xa), latex(-ya), latex(-za),
                latex(u1), latex(u2), latex(u3),
                latex(u1), latex(-xa), latex(u2), latex(-ya), latex(u3), latex(-za),
                latex(bt1),
                latex(-xb), latex(-yb), latex(-zb),
                latex(-xb), latex(u1), latex(-yb), latex(u2), latex(-zb), latex(u3),
                latex(-xb), latex(u1), latex(-yb), latex(u2),
                latex(-xb), latex(u1), latex(-zb), latex(u3),
                latex(bien_y), latex(bien_z),
                latex(pt_x), latex(xh),
                latex(yh), latex(zh),
                latex(xh), latex(yh), latex(zh)
            )
        )

    # Xuất câu trắc nghiệm
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + 
        '\\choice[2] \n'
        '{' + str(list_1[1]) + '}\n'
        '{' + str(list_1[2]) + '}\n'
        '{' + str(list_1[3]) + '}\n'
        '{' + str(list_1[0]) + '}\n'
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')        
    return content

