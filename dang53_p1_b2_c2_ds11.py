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


def bt_dang53_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số lượng cạnh n, công sai d và số hạng đầu u1
                while True:
                    n = randint(4, 9)
                    d = randint(2, 6)
                    u1 = randint(10, 30)
                    # Điều kiện để phương trình bậc 2 chỉ có 1 nghiệm nguyên dương
                    if (2 * u1) % d != 0:
                        un = u1 + (n - 1) * d
                        Sn = n * (u1 + un) // 2
                        break

                # Tính toán các biến phục vụ lời giải
                u1_const = un + d
                sum_const = u1_const + un
                c_quad = 2 * Sn
                n2_frac = Rational(c_quad, d * n)

                # Đáp án đúng
                da_val = n

                # Tạo danh sách các phương án sai (distractors)
                s_set = set()
                s_set.add(n + 1)
                s_set.add(n + 2)
                s_set.add(n - 1)
                if n - 2 >= 3:
                    s_set.add(n - 2)
                s_set.add(n + 3)

                s_set.discard(da_val)

                s_list = list(s_set)
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Chu vi một đa giác là $%s$ cm, số đo các cạnh của nó lập thành một cấp số cộng với công sai $d = %s$ cm. Biết cạnh lớn nhất là $%s$ cm. Số cạnh của đa giác đó là'''
                                 % (latex(Sn), latex(d), latex(un)))

                # Định dạng các phương án trả lời
                da_d = ('\\True $%s$' % (latex(da_val)))
                da_s1 = ('$%s$' % (latex(das1)))
                da_s2 = ('$%s$' % (latex(das2)))
                da_s3 = ('$%s$' % (latex(das3)))

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Gọi số cạnh của đa giác là $n$ ($n \\in \\mathbb{N}, n \\ge 3$). \\\\
            Các cạnh của đa giác lập thành cấp số cộng có công sai $d = %s$ cm, cạnh lớn nhất là $u_n = %s$ cm. \\\\
            Theo công thức số hạng tổng quát: \\\\
            $u_n = u_1 + (n-1)d \\Leftrightarrow %s = u_1 + (n-1) \\cdot %s \\Leftrightarrow u_1 = %s - %sn + %s = %s - %sn$. \\\\
            Tổng các cạnh của đa giác là chu vi: \\\\
            $S_n = \\frac{n(u_1 + u_n)}{2} \\Leftrightarrow %s = \\frac{n(%s - %sn + %s)}{2} = \\frac{n(%s - %sn)}{2}$ \\\\
            $\\Leftrightarrow %s = %sn - %sn^2 \\Leftrightarrow %sn^2 - %sn + %s = 0$ \\\\
            $\\Leftrightarrow \\left[ \\begin{array}{l} n = %s \\text{ (thỏa mãn)} \\\\ n = %s \\text{ (loại)} \\end{array} \\right.$. \\\\
            Vậy đa giác đó có $%s$ cạnh.'''
                           % (latex(d), latex(un),
                              latex(un), latex(d), latex(un), latex(d), latex(d), latex(u1_const), latex(d),
                              latex(Sn), latex(u1_const), latex(d), latex(un), latex(sum_const), latex(d),
                              latex(c_quad), latex(sum_const), latex(d), latex(d), latex(sum_const), latex(c_quad),
                              latex(n), latex(n2_frac),
                              latex(n)))

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

