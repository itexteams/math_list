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


def bt_dang18_p4_b3_c1_hh12(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        k = random.randint(2, 6)
        t2 = random.choice([2, 3, 4, 5, 10, 12, 15])
        t1 = k * t2
        x_M = random.randint(10, 60) * 10
        y_M = random.randint(10, 50) * 10
        z_M = random.randint(1, 10) * 10
        dx = random.randint(2, 15) * 10
        dy = random.randint(2, 15) * 10
        dz = random.randint(0, 5) * 10
        x_N = x_M + k * dx
        y_N = y_M + k * dy
        z_N = z_M + k * dz
        a = x_N + dx
        b = y_N + dy
        c = z_N + dz
        ans = a + b + c
        vec_MN_x = k * dx
        vec_MN_y = k * dy
        vec_MN_z = k * dz
        noidungcauhoi = f"Trong không gian chọn hệ trục tọa độ cho trước, đơn vị đo lấy kilômét, ra đa phát hiện một máy bay chiến đấu di chuyển với vận tốc và hướng không đổi từ điểm $M({x_M};{y_M};{z_M})$ đến điểm $N({x_N};{y_N};{z_N})$ trong {t1} phút. Nếu máy bay tiếp tục giữ nguyên vận tốc và hướng bay thì tọa độ của máy bay sau {t2} phút tiếp là $Q(a;b;c)$. Khi đó $a+b+c$ bằng bao nhiêu?"
        loigiai = f'''Gọi $Q(x;y;z)$ là tọa độ của máy bay sau {t2} phút tiếp theo.\\\\
    Ta có: $\\overrightarrow{{MN}} = ({vec_MN_x};{vec_MN_y};{vec_MN_z}); \\overrightarrow{{NQ}} = (x - {x_N}; y - {y_N}; z - {z_N})$\\\\
    Vì máy bay giữ nguyên hướng bay nên $\\overrightarrow{{MN}}$ và $\\overrightarrow{{NQ}}$ cùng hướng.\\\\
    Do máy bay tiếp tục giữ nguyên vận tốc và thời gian bay từ $M \\rightarrow N$ gấp {k} lần thời gian bay từ $N \\rightarrow Q$ nên $MN = {k}NQ$\\\\
    Suy ra $\\overrightarrow{{MN}} = {k}\\overrightarrow{{NQ}} \\Leftrightarrow \\begin{{cases}} {vec_MN_x} = {k}(x - {x_N}) \\\\ {vec_MN_y} = {k}(y - {y_N}) \\\\ {vec_MN_z} = {k}(z - {z_N}) \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x = {a} \\\\ y = {b} \\\\ z = {c} \\end{{cases}} \\Rightarrow Q({a};{b};{c})$.\\\\
    Tọa độ của máy bay sau {t2} phút tiếp theo là $Q({a};{b};{c})$.\\\\
    Vậy $a+b+c = {a} + {b} + {c} = {ans}$.'''
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\n\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

