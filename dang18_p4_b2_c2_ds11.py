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


def bt_dang18_p4_b2_c2_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random số hạng đầu b1 của CSC thứ hai, suy ra a1 sao cho a1 - b1 = 2
        b1 = random.randint(2, 8)
        a1 = b1 + 2
        N = random.choice([80, 90, 100, 110, 120, 150])

        # 3 số hạng đầu tiên của mỗi cấp số cộng
        ap1_t1 = a1
        ap1_t2 = a1 + 3
        ap1_t3 = a1 + 6

        ap2_t1 = b1
        ap2_t2 = b1 + 4
        ap2_t3 = b1 + 8

        # Biến đổi u_n và v_m
        c1 = a1 - 3
        c2 = b1 - 4

        if c1 > 0:
            str_un = '%s + 3n' % latex(c1)
        elif c1 < 0:
            str_un = '-%s + 3n' % latex(abs(c1))
        else:
            str_un = '3n'

        if c2 > 0:
            str_vm = '%s + 4m' % latex(c2)
        elif c2 < 0:
            str_vm = '-%s + 4m' % latex(abs(c2))
        else:
            str_vm = '4m'

        # Tính các giới hạn cho t
        t1 = N // 3
        t2 = (N + 1) // 4
        t_max = min(t1, t2)

        # Nội dung câu hỏi
        noidungcauhoi = (
            '''Cho hai cấp số cộng có dãy số hạng lần lượt là: $%s; %s; %s; \\dots$ và $%s; %s; %s; \\dots$. Trong $%s$ số hạng đầu tiên của mỗi cấp số, tìm số các số hạng chung.'''
            % (
                latex(ap1_t1),
                latex(ap1_t2),
                latex(ap1_t3),
                latex(ap2_t1),
                latex(ap2_t2),
                latex(ap2_t3),
                latex(N),
            )
        )

        # Nội dung lời giải
        loigiai = (
            '''Giả sử $u_n, v_m$ theo thứ tự là số hạng thứ $n$ và $m$ của mỗi cấp số cộng, ta có:\\\\
            $u_n = %s + 3(n-1)$ và $v_m = %s + 4(m-1)$.\\\\
            Theo giả thiết, số hạng chung thỏa mãn:\\\\
            $u_n = v_m \\Leftrightarrow %s + 3(n-1) = %s + 4(m-1) \\Leftrightarrow %s = %s \\Leftrightarrow n = \\frac{4m-1}{3} = m + \\frac{m-1}{3}$.\\\\
            Vì $n, m \\in \\mathbb{N}^*$ nên $(m - 1) \\vdots 3 \\Rightarrow m = 3t - 2$ (với $t \\in \\mathbb{N}^*$), suy ra $n = 4t - 3$.\\\\
            Trong $%s$ số hạng đầu tiên của mỗi cấp số, ta có hệ điều kiện:\\\\
            $\\begin{cases} 1 \\le m = 3t - 2 \\le %s \\\\ 1 \\le n = 4t - 3 \\le %s \\end{cases} \\Leftrightarrow \\begin{cases} 1 \\le t \\le \\frac{%s}{3} \\\\ 1 \\le t \\le \\frac{%s}{4} \\end{cases} \\Rightarrow 1 \\le t \\le %s$ (do $t \\in \\mathbb{N}^*$).\\\\
            Suy ra $t \\in \\{1; 2; 3; \\dots; %s\\}$. Với mỗi giá trị của $t$, ta có một số hạng chung thuộc về hai dãy $(u_n)$ và $(v_m)$.\\\\
            Vậy có tất cả $%s$ số hạng chung của hai dãy số đã cho trong $%s$ số hạng đầu tiên.'''
            % (
                latex(a1),
                latex(b1),
                latex(a1),
                latex(b1),
                str_un,
                str_vm,
                latex(N),
                latex(N),
                latex(N),
                latex(N + 2),
                latex(N + 3),
                latex(t_max),
                latex(t_max),
                latex(t_max),
                latex(N),
            )
        )

    # Xuất câu hỏi và lời giải
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\loigiai{ \n' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content 

