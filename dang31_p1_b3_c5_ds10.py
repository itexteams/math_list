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


def bt_dang31_p1_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                # Dạng 1: Tổng các số hạng lẻ (C_n^1 + C_n^3 + ...)
                n_val = random.choice(['n', '2n', 'n+1']) # Random biến số để tăng tính đa dạng

                noidungcauhoi = ('''Với $%s \\geq 4$, tổng $T = C_{%s}^1 + C_{%s}^3 + C_{%s}^5 + \\dots$ bằng'''
                                 %(n_val, n_val, n_val, n_val))

                # Đáp án đúng
                da_d = ('\\True $2^{%s-1}$' % (n_val))

                # Các đáp án sai
                s = [
                    '$2^{2%s-1}$' % (n_val),
                    '$2^{%s}$' % (n_val),
                    '$2^{%s}-1$' % (n_val),
                    '$2^{%s-2}$' % (n_val),
                    '$2^{%s+1}$' % (n_val)
                ]
                random.shuffle(s)
                da_s1, da_s2, da_s3 = s[0], s[1], s[2]

                # Lời giải chi tiết
                loigiai = ('''Theo khai triển nhị thức Niuton: \\\\
                             $\\left(a+b\\right)^{%s} = \\sum_{k=0}^{%s} C_{%s}^k a^{%s-k}b^k$ (*) \\\\
                             Với $a=1, b=1$, ta có (*) $\\Rightarrow 2^{%s} = C_{%s}^0 + C_{%s}^1 + C_{%s}^2 + \\dots + C_{%s}^{%s}$. (1) \\\\
                             Với $a=1, b=-1$, ta có (*) $\\Rightarrow 0 = C_{%s}^0 - C_{%s}^1 + C_{%s}^2 - \\dots + \\left(-1\\right)^{%s} C_{%s}^{%s}$. (2) \\\\
                             Lấy (1) trừ (2) vế theo vế, ta được: \\\\
                             $2^{%s} - 0 = \\left(C_{%s}^0 + C_{%s}^1 + \\dots + C_{%s}^{%s}\\right) - \\left(C_{%s}^0 - C_{%s}^1 + \\dots + \\left(-1\\right)^{%s} C_{%s}^{%s}\\right)$ \\\\
                             $\\Rightarrow 2^{%s} = 2\\left(C_{%s}^1 + C_{%s}^3 + C_{%s}^5 + \\dots\\right) = 2T$. \\\\
                             Vậy $T = \\frac{2^{%s}}{2} = 2^{%s-1}$.'''
                           %(n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val,
                             n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val, 
                             n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val, 
                             n_val, n_val))

            elif dang == '2':
                # Dạng 2: Tổng các số hạng chẵn (C_n^0 + C_n^2 + ...)
                n_val = random.choice(['n', 'm', 'k'])

                noidungcauhoi = ('''Với $%s \\geq 4$, tổng $T = C_{%s}^0 + C_{%s}^2 + C_{%s}^4 + \\dots$ bằng'''
                                 %(n_val, n_val, n_val, n_val))

                da_d = ('\\True $2^{%s-1}$' % (n_val))

                s = [
                    '$2^{%s}$' % (n_val),
                    '$2^{%s}+1$' % (n_val),
                    '$2^{2%s}$' % (n_val),
                    '$2^{%s-2}$' % (n_val)
                ]
                random.shuffle(s)
                da_s1, da_s2, da_s3 = s[0], s[1], s[2]

                # Lời giải chi tiết - Đã sửa lại số lượng n_val thành 22
                loigiai = ('''Theo khai triển nhị thức Niuton: \\\\
                             $\\left(a+b\\right)^{%s} = \\sum_{k=0}^{%s} C_{%s}^k a^{%s-k}b^k$ (*) \\\\
                             Với $a=1, b=1$, ta có (*) $\\Rightarrow 2^{%s} = C_{%s}^0 + C_{%s}^1 + C_{%s}^2 + \\dots + C_{%s}^{%s}$. (1) \\\\
                             Với $a=1, b=-1$, ta có (*) $\\Rightarrow 0 = C_{%s}^0 - C_{%s}^1 + C_{%s}^2 - \\dots + \\left(-1\\right)^{%s} C_{%s}^{%s}$. (2) \\\\
                             Lấy (1) cộng (2) vế theo vế, ta được: \\\\
                             $2^{%s} + 0 = 2\\left(C_{%s}^0 + C_{%s}^2 + C_{%s}^4 + \\dots\\right) = 2T$. \\\\
                             Vậy $T = \\frac{2^{%s}}{2} = 2^{%s-1}$.'''
                           %(n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val,
                             n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val, n_val, 
                             n_val, n_val))

            # Đưa các đáp án vào danh sách và xáo trộn
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

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

