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


def bt_dang16_p4_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # K_val tương ứng với số hạng tự do trong nghiệm x2 = K - m^2. Trong ảnh gốc K = 1.
                # Chọn K_val sao cho K_val - 1/2 > 0 để có nghiệm thực
                K_val = random.choice([Rational(1), Rational(2), Rational(3), Rational(5, 2)])

                # Tính toán các hệ số dựa trên logic: 
                # Khi bình phương 2 vế và chuyển vế, ta được PT: 2x^2 + (2m^2 + c_idx - 4)x + 1 - c_const - m^2 = 0
                # Để có nghiệm x = 1/2 và x = K_val - m^2:
                c_idx = 3 - 2 * K_val
                c_const = 1 - K_val

                # Điều kiện nghiệm: K_val - m^2 > 1/2 <=> m^2 < K_val - 1/2
                limit_val = K_val - Rational(1, 2)
                val_a = -sqrt(limit_val)
                val_b = sqrt(limit_val)
                diff = val_b - val_a # Giá trị b - a

                # Chuyển sang LaTeX (chỉ gọi hàm latex() MỘT LẦN duy nhất cho mỗi giá trị)
                c_idx_lx = latex(c_idx)
                c_const_lx = latex(c_const)
                K_val_lx = latex(K_val)
                limit_val_lx = latex(limit_val)
                val_a_lx = latex(val_a)
                val_b_lx = latex(val_b)
                kq_final_lx = latex(simplify(diff))

                # Câu hỏi
                noidungcauhoi = ('''Phương trình $\\sqrt{2x^2 - (2m^2 + %s)x + m^2 + %s} = 2x - 1$ có hai nghiệm phân biệt thì $m \\in (a, b)$. Tính giá trị $b - a$.'''
                                 % (c_idx_lx, c_const_lx))

                # Đáp án
                da_dung = '$%s$' % kq_final_lx
                s = [
                    '$%s$' % latex(simplify(diff / 2)),
                    '$%s$' % latex(simplify(diff * 2)),
                    '$%s$' % latex(simplify(diff + 1)),
                    '$1$', '$2$', '$\\sqrt{3}$', '$\\frac{\\sqrt{2}}{2}$'
                ]
                if da_dung in s:
                    s.remove(da_dung)
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                da_d = '\\True ' + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Lời giải chi tiết - dùng trực tiếp các biến đã latex hóa
                loigiai = ('''Phương trình ban đầu có hai nghiệm phân biệt tương đương với phương trình: \\\\
                             $2x^2 - (2m^2 + %s)x + m^2 + %s = (2x - 1)^2$ (1) có hai nghiệm phân biệt thuộc $[\\frac{1}{2}; +\\infty)$. \\\\
                             Mà (1) $\\Leftrightarrow 2x^2 - (2m^2 + %s)x + m^2 + %s = 4x^2 - 4x + 1$ \\\\
                             $\\Leftrightarrow 2x^2 + (2m^2 + %s)x + %s - m^2 = 0$ \\\\
                             $\\Leftrightarrow \\left[\\begin{aligned} & x = \\frac{1}{2} \\\\ & x = %s - m^2 \\end{aligned}\\right.$. \\\\
                             Để phương trình có hai nghiệm phân biệt thuộc $[\\frac{1}{2}; +\\infty)$, ta cần: \\\\
                             $%s - m^2 > \\frac{1}{2} \\Leftrightarrow m^2 < %s$ \\\\
                             $\\Leftrightarrow %s < m < %s$. \\\\
                             Suy ra $m \\in (%s; %s)$, do đó $a = %s$ và $b = %s$. \\\\
                             Vậy $b - a = %s - (%s) = %s$.'''
                           % (c_idx_lx, c_const_lx, 
                              c_idx_lx, c_const_lx, 
                              latex(c_idx - 4), latex(1 - c_const), 
                              K_val_lx, K_val_lx, limit_val_lx,
                              val_a_lx, val_b_lx,
                              val_a_lx, val_b_lx,
                              val_a_lx, val_b_lx,
                              val_b_lx, val_a_lx, kq_final_lx))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + 
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-')
            return content

