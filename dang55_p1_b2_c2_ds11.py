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


def bt_dang55_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random x_val và d_val sao cho các số hạng dương
                x_val = randint(4, 9)
                d_val = randint(1, 2)

                # Bốn số hạng
                t1 = x_val - 3 * d_val
                t2 = x_val - d_val
                t3 = x_val + d_val
                t4 = x_val + 3 * d_val

                # Tính S và S2
                S = 4 * x_val
                S2 = 4 * (x_val**2) + 20 * (d_val**2)

                val_20d2 = 20 * (d_val**2)
                val_d2 = d_val**2

                # Đáp án đúng
                da_val = '%s, %s, %s, %s' % (t1, t2, t3, t4)

                # Tạo danh sách các phương án sai (giữ tổng bằng S nhưng không phải cấp số cộng)
                s_set = set()
                s_set.add('%s, %s, %s, %s' % tuple(sorted([t1 - 1, t2 + 1, t3, t4])))
                s_set.add('%s, %s, %s, %s' % tuple(sorted([t1 - 1, t2, t3, t4 + 1])))
                s_set.add('%s, %s, %s, %s' % tuple(sorted([t1 - 1, t2, t3 + 1, t4])))
                s_set.add('%s, %s, %s, %s' % tuple(sorted([t1, t2 - 1, t3 + 1, t4])))

                s_set.discard(da_val)

                s_list = list(s_set)
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Bốn số hạng liên tiếp của một cấp số cộng biết tổng của chúng bằng $%s$ và tổng các bình phương của chúng bằng $%s$ là'''
                                 % (latex(S), latex(S2)))

                # Định dạng các phương án trả lời
                da_d = ('\\True $%s$' % (da_val))
                da_s1 = ('$%s$' % (das1))
                da_s2 = ('$%s$' % (das2))
                da_s3 = ('$%s$' % (das3))

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Gọi $4$ số hạng liên tiếp của cấp số cộng là $x-3d, x-d, x+d, x+3d$ với công sai là $2d$ ($d > 0$). \\\\
            Theo giả thiết, ta có hệ phương trình: \\\\
            $\\begin{cases} (x-3d) + (x-d) + (x+d) + (x+3d) = %s \\\\ (x-3d)^2 + (x-d)^2 + (x+d)^2 + (x+3d)^2 = %s \\end{cases}$ \\\\
            $\\Leftrightarrow \\begin{cases} 4x = %s \\\\ 4x^2 + 20d^2 = %s \\end{cases}$ \\\\
            $\\Leftrightarrow \\begin{cases} x = %s \\\\ 4 \\cdot (%s)^2 + 20d^2 = %s \\end{cases}$ \\\\
            $\\Leftrightarrow \\begin{cases} x = %s \\\\ 20d^2 = %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ d^2 = %s \\end{cases}$ \\\\
            $\\Rightarrow d = %s$ (do $d > 0$). \\\\
            Vậy $4$ số hạng cần tìm là: $%s, %s, %s, %s$.'''
                           % (latex(S), latex(S2),
                              latex(S), latex(S2),
                              latex(x_val), latex(x_val), latex(S2),
                              latex(x_val), latex(val_20d2), latex(x_val), latex(val_d2),
                              latex(d_val),
                              latex(t1), latex(t2), latex(t3), latex(t4)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{\n' + str(loigiai) + '\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

