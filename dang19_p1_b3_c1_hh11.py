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


def bt_dang19_p1_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2', '3']
    dang = random.choice(lisdang)

    # Random tên hai đường thẳng
    cap_duong_thang = random.choice([('a', 'b'), ('d_1', 'd_2'), ('d', '\\Delta'), ('p', 'q')])
    d1 = cap_duong_thang[0]
    d2 = cap_duong_thang[1]

    if dang == '1':
        # Dạng 1: Giống hệt bài gốc trong ảnh
        # Random chọn đường chứa và đường song song
        if random.choice([True, False]):
            duong_chua = d1
            duong_ss = d2
        else:
            duong_chua = d2
            duong_ss = d1

        noidungcauhoi = ('''Cho hai đường thẳng chéo nhau $%s$ và $%s$. Có bao nhiêu mặt phẳng chứa đường thẳng $%s$ và song song với đường thẳng $%s$?'''
                         % (d1, d2, duong_chua, duong_ss))

        da = '$1$'

        s = [
            '$2$',
            '$3$',
            'Vô số',
            '$0$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        loigiai = ('''Theo định lý về sự xác định mặt phẳng song song với một đường thẳng: \\\\
    Lấy một điểm $M$ tùy ý trên đường thẳng $%s$. Qua $M$ dựng đường thẳng $%s\' // %s$. \\\\
    Vì $%s$ và $%s$ chéo nhau nên điểm $M$ không thuộc $%s$, do đó hai đường thẳng cắt nhau $%s$ và $%s\'$ xác định duy nhất một mặt phẳng $(\\alpha)$. \\\\
    Mặt phẳng $(\\alpha)$ này chứa $%s$ và song song với $%s$. \\\\
    Vậy có duy nhất $1$ mặt phẳng chứa đường thẳng $%s$ và song song với đường thẳng $%s$.'''
                   % (duong_chua, duong_ss, duong_ss, duong_chua, duong_ss, duong_ss, duong_chua, duong_ss, duong_chua, duong_ss, duong_chua, duong_ss))

    elif dang == '2':
        # Dạng 2: Hỏi về số cặp mặt phẳng song song lần lượt chứa hai đường thẳng chéo nhau
        noidungcauhoi = ('''Cho hai đường thẳng chéo nhau $%s$ và $%s$. Có bao nhiêu cặp mặt phẳng song song với nhau lần lượt chứa hai đường thẳng $%s$ và $%s$?'''
                         % (d1, d2, d1, d2))

        da = '$1$'

        s = [
            '$0$',
            '$2$',
            '$3$',
            'Vô số'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        loigiai = ('''Theo tính chất: Qua hai đường thẳng chéo nhau $%s$ và $%s$, có duy nhất một mặt phẳng $(\\alpha)$ chứa $%s$ và song song với $%s$, đồng thời có duy nhất một mặt phẳng $(\\beta)$ chứa $%s$ và song song với $%s$. \\\\
    Khi đó, $(\\alpha) // (\\beta)$. \\\\
    Vậy có duy nhất $1$ cặp mặt phẳng song song với nhau lần lượt chứa hai đường thẳng $%s$ và $%s$.'''
                   % (d1, d2, d1, d2, d2, d1, d1, d2))

    elif dang == '3':
        # Dạng 3: Số mặt phẳng song song với CẢ HAI đường thẳng chéo nhau
        noidungcauhoi = ('''Cho hai đường thẳng chéo nhau $%s$ và $%s$. Có bao nhiêu mặt phẳng song song với cả hai đường thẳng $%s$ và $%s$?'''
                         % (d1, d2, d1, d2))

        da = 'Vô số'

        s = [
            '$0$',
            '$1$',
            '$2$',
            '$3$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        loigiai = ('''Lấy một điểm $O$ bất kì không thuộc cả $%s$ và $%s$. \\\\
    Qua $O$, kẻ hai đường thẳng $%s\' // %s$ và $%s\' // %s$. \\\\
    Mặt phẳng xác định bởi hai đường thẳng cắt nhau $%s\'$ và $%s\'$ sẽ song song với cả $%s$ và $%s$. \\\\
    Vì có vô số điểm $O$ thỏa mãn trong không gian nên có vô số mặt phẳng song song với cả hai đường thẳng $%s$ và $%s$.'''
                   % (d1, d2, d1, d1, d2, d2, d1, d2, d1, d2, d1, d2))

    # Gán các phương án
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

