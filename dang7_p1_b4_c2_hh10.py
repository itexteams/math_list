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


def bt_dang7_p1_b4_c2_hh10(self):
    # Chọn 2 điểm phân biệt để tránh độ dài MN = 0
    while True:
        x1 = randint(-9, 9)
        y1 = randint(-9, 9)
        x2 = randint(-9, 9)
        y2 = randint(-9, 9)
        if (x1, y1) != (x2, y2):
            break

    lis0 = ['A', 'B', 'C', 'D', 'E', 'H', 'P', 'Q']
    d1 = random.choice(lis0)
    lis0.remove(d1)
    d2 = random.choice(lis0)

    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    if dang == '1':
        # Nội dung câu hỏi
        noidungcauhoi = (
            'Trong mặt phẳng tọa độ $(Oxy)$, cho hai điểm $%s(%s;%s)$ và $%s(%s;%s)$, gọi $M, N$ là trung điểm của $O%s$ và $O%s$. Tọa độ vectơ $\\overrightarrow{MN}$ là \n'
            % (str(d1), latex(x1), latex(y1), str(d2), latex(x2), latex(y2), str(d1), str(d2))
        )
        # Đáp án đúng
        u_dung = (Rational(x2 - x1, 2), Rational(y2 - y1, 2))
        da_d = '\\True $\\left( %s; %s \\right)$' % (latex(u_dung[0]), latex(u_dung[1]))

        # Sinh tập các phương án sai phân biệt với đáp án đúng
        sai_set = set()
        # Danh sách các độ lệch khả dĩ
        deltas = [-2, -1, 1, 2, 3, -3]
        for dx in deltas:
            for dy in [0, 1, -1]:
                candi = (Rational(x2 - x1 + dx, 2), Rational(y2 - y1 + dy, 2))
                if candi != u_dung:
                    sai_set.add(candi)
            candi_y = (Rational(x2 - x1, 2), Rational(y2 - y1 + dx, 2))
            if candi_y != u_dung:
                sai_set.add(candi_y)

        # Đảo dấu x, y để tạo nhiễu đánh lừa dấu
        sai_set.add((Rational(x1 - x2, 2), Rational(y1 - y2, 2)))
        sai_set.discard(u_dung)

        ds_sai = random.sample(list(sai_set), 3)
        da_s1 = '$\\left( %s; %s \\right)$' % (latex(ds_sai[0][0]), latex(ds_sai[0][1]))
        da_s2 = '$\\left( %s; %s \\right)$' % (latex(ds_sai[1][0]), latex(ds_sai[1][1]))
        da_s3 = '$\\left( %s; %s \\right)$' % (latex(ds_sai[2][0]), latex(ds_sai[2][1]))

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Lời giải
        loigiai = (
            'Tọa độ điểm $M$ là $\\left( %s; %s \\right)$. \\\\ \n '
            'Tọa độ điểm $N$ là $\\left( %s; %s \\right)$. \\\\ \n '
            'Ta có $\\overrightarrow{MN}=\\left( %s; %s \\right)$. '
            % (
                latex(Rational(x1, 2)), latex(Rational(y1, 2)),
                latex(Rational(x2, 2)), latex(Rational(y2, 2)),
                latex(Rational(x2 - x1, 2)), latex(Rational(y2 - y1, 2)),
            )
        )

    if dang == '2':
        # Nội dung câu hỏi
        noidungcauhoi = (
            'Trong mặt phẳng tọa độ $(Oxy)$, cho hai điểm $%s(%s;%s)$ và $%s(%s;%s)$, gọi $M, N$ là trung điểm của $O%s$ và $O%s$. Độ dài đoạn thẳng $MN$ là \n'
            % (str(d1), latex(x1), latex(y1), str(d2), latex(x2), latex(y2), str(d1), str(d2))
        )

        # MN = AB / 2
        tong_bp = (x2 - x1)**2 + (y2 - y1)**2
        mn = sqrt(tong_bp) / 2
        da_d = '\\True $%s$' % (latex(mn))

        # Sinh tập các giá trị sai phân biệt
        danh_sach_sai_val = set()
        delta_k = [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(delta_k)
        for k in delta_k:
            val = tong_bp + k
            if val > 0 and val != tong_bp:
                sai_val = sqrt(val) / 2
                if sai_val != mn:
                    danh_sach_sai_val.add(sai_val)
            if len(danh_sach_sai_val) >= 5:
                break

        ds_sai = random.sample(list(danh_sach_sai_val), 3)
        da_s1 = '$%s$' % (latex(ds_sai[0]))
        da_s2 = '$%s$' % (latex(ds_sai[1]))
        da_s3 = '$%s$' % (latex(ds_sai[2]))

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Lời giải
        loigiai = (
            'Tọa độ điểm $M$ là $\\left( %s; %s \\right)$. \\\\ \n '
            'Tọa độ điểm $N$ là $\\left( %s; %s \\right)$. \\\\ \n '
            'Ta có $\\overrightarrow{MN}=\\left( %s; %s \\right)$. \\\\ \n'
            'Độ dài đoạn thẳng $MN$ là $\\sqrt{%s+%s}=%s$.'
            % (
                latex(Rational(x1, 2)), latex(Rational(y1, 2)),
                latex(Rational(x2, 2)), latex(Rational(y2, 2)),
                latex(Rational(x2 - x1, 2)), latex(Rational(y2 - y1, 2)),
                latex(Rational((x2 - x1)**2, 4)), latex(Rational((y2 - y1)**2, 4)),
                latex(mn),
            )
        )

    # Xuất câu trắc nghiệm
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) +
        '\\choice \n'
        '{' + str(list_1[1]) + '}\n'
        '{' + str(list_1[2]) + '}\n'
        '{' + str(list_1[3]) + '}\n'
        '{' + str(list_1[0]) + '}\n'
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('--', '+')

    return content

