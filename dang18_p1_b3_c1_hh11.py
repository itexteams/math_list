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


def bt_dang18_p1_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    # Random tên đường thẳng và mặt phẳng
    cac_cap_duong = [('a', 'd'), ('d_1', 'd_2'), ('d', '\\Delta'), ('b', 'd')]
    cac_cap_mp = [('\\alpha', '\\beta'), ('P', 'Q'), ('\\alpha', 'P'), ('P', '\\beta')]

    duong_thang = random.choice(cac_cap_duong)
    mat_phang = random.choice(cac_cap_mp)

    duong_a, duong_d = duong_thang[0], duong_thang[1]
    mp_alpha, mp_beta = mat_phang[0], mat_phang[1]

    if dang == '1':
        # Dạng 1: Giống bài gốc - Tìm kết luận ĐÚNG
        noidungcauhoi = ('''Cho đường thẳng $%s$ song song với mặt phẳng $(%s)$. Mặt phẳng $(%s)$ chứa $%s$ và cắt mặt phẳng $(%s)$ theo giao tuyến $%s$. Kết luận nào sau đây đúng?'''
                         % (duong_a, mp_alpha, mp_beta, duong_a, mp_alpha, duong_d))

        da = '$%s$ và $%s$ song song' % (duong_a, duong_d)

        s = [
            '$%s$ và $%s$ cắt nhau' % (duong_a, duong_d),
            '$%s$ và $%s$ trùng nhau' % (duong_a, duong_d),
            '$%s$ và $%s$ chéo nhau' % (duong_a, duong_d),
            '$%s$ và $%s$ vuông góc nhau' % (duong_a, duong_d)
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        loigiai = ('''Ta có: \\\\
    $\\left\\{\\begin{array}{l} %s = (%s) \\cap (%s) \\\\ %s \\subset (%s) \\\\ %s // (%s) \\end{array}\\right. \\Rightarrow %s // %s$. \\\\
    Vậy hai đường thẳng $%s$ và $%s$ song song với nhau.'''
                   % (duong_d, mp_alpha, mp_beta, duong_a, mp_beta, duong_a, mp_alpha, duong_d, duong_a, duong_a, duong_d))

    elif dang == '2':
        # Dạng 2: Tìm khẳng định SAI
        noidungcauhoi = ('''Cho đường thẳng $%s$ song song với mặt phẳng $(%s)$. Mặt phẳng $(%s)$ chứa $%s$ và cắt mặt phẳng $(%s)$ theo giao tuyến $%s$. Khẳng định nào sau đây \\textbf{sai}?'''
                         % (duong_a, mp_alpha, mp_beta, duong_a, mp_alpha, duong_d))

        # Khẳng định sai được chọn làm đáp án đúng của câu hỏi
        ds_sai = [
            '$%s$ và $%s$ cắt nhau' % (duong_a, duong_d),
            '$%s$ và $%s$ chéo nhau' % (duong_a, duong_d),
            '$%s$ và $%s$ trùng nhau' % (duong_a, duong_d)
        ]
        da = random.choice(ds_sai)

        s = [
            '$%s$ và $%s$ song song' % (duong_a, duong_d),
            '$%s // %s$' % (duong_d, duong_a),
            '$%s$ và $%s$ cùng nằm trong mặt phẳng $(%s)$' % (duong_a, duong_d, mp_beta),
            '$%s$ và $%s$ không có điểm chung' % (duong_a, duong_d)
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        loigiai = ('''Theo định lý về giao tuyến của hai mặt phẳng: \\\\
    Nếu đường thẳng $%s$ song song với mặt phẳng $(%s)$ thì mọi mặt phẳng $(%s)$ chứa $%s$ và cắt $(%s)$ theo giao tuyến $%s$ thì $%s // %s$. \\\\
    Ta có: \\\\
    $\\left\\{\\begin{array}{l} %s = (%s) \\cap (%s) \\\\ %s \\subset (%s) \\\\ %s // (%s) \\end{array}\\right. \\Rightarrow %s // %s$. \\\\
    Do đó hai đường thẳng $%s$ và $%s$ song song, chúng cùng thuộc mặt phẳng $(%s)$ và không có điểm chung. \\\\
    Vậy khẳng định "%s" là khẳng định sai.'''
                   % (duong_a, mp_alpha, mp_beta, duong_a, mp_alpha, duong_d, duong_d, duong_a,
                      duong_d, mp_alpha, mp_beta, duong_a, mp_beta, duong_a, mp_alpha, duong_d, duong_a,
                      duong_a, duong_d, mp_beta, da))

    # Các đáp án trắc nghiệm
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\choice \n'
        '{' + str(list_1[1]) + '}\n'
        '{' + str(list_1[2]) + '}\n'
        '{' + str(list_1[3]) + '}\n'
        '{' + str(list_1[0]) + '}\n'
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

