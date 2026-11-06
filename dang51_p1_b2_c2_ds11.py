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


def bt_dang51_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random u1, uN, và số lượng số hạng chèn thêm k
                u1 = randint(1, 15)
                uN = randint(1500, 3000)
                # k được chọn là số lẻ để số hạng cần tìm rơi vào chính giữa
                k = random.choice([199, 399, 499, 799, 999, 1999])
                N = k + 2
                m = (N + 1) // 2 # Vị trí của số hạng chính giữa

                # Tính u_m
                um = Rational(u1 + uN, 2)

                # Tính toán các biến phụ cho lời giải
                k_plus_1 = N - 1
                uN_minus_u1 = uN - u1
                m_minus_1 = m - 1

                # Đáp án đúng
                da_val = um

                # Tạo phương án sai không trùng với đáp án đúng
                s_set = set()
                s_set.add(Rational(u1 + uN - 1, 2))
                s_set.add(Rational(u1 + uN + 1, 2))
                s_set.add(Rational(u1 + uN + 2, 2))
                s_set.add(Rational(u1 + uN - 2, 2))
                s_set.add(da_val + 1)
                s_set.add(da_val - 1)

                s_set.discard(da_val)

                s_list = list(s_set)
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Người ta viết thêm $%s$ số thực vào giữa số $%s$ và số $%s$ để được cấp số cộng có $%s$ số hạng. Số hạng thứ $%s$ là'''
                                 % (latex(k), latex(u1), latex(uN), latex(N), latex(m)))

                # Định dạng đáp án
                da_d = ('\\True $%s$' % (latex(da_val)))
                da_s1 = ('$%s$' % (latex(das1)))
                da_s2 = ('$%s$' % (latex(das2)))
                da_s3 = ('$%s$' % (latex(das3)))

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Cấp số cộng $(u_n)$ có $u_1 = %s$ và $u_{%s} = %s$. \\\\
            Ta có $u_{%s} = u_1 + %sd \\Leftrightarrow %s = %s + %sd \\Leftrightarrow %sd = %s \\Leftrightarrow d = \\frac{%s}{%s}$. \\\\
            Số hạng thứ $%s$ là: \\\\
            $u_{%s} = u_1 + %sd = %s + %s \\cdot \\frac{%s}{%s} = %s$. \\\\
            \\textit{Cách khác:} Ta nhận thấy $1 + %s = 2 \\cdot %s$, nên theo tính chất của cấp số cộng: \\\\
            $u_{%s} = \\frac{u_1 + u_{%s}}{2} = \\frac{%s + %s}{2} = %s$.'''
                           % (latex(u1), latex(N), latex(uN),
                              latex(N), latex(k_plus_1), latex(uN), latex(u1), latex(k_plus_1), latex(k_plus_1), latex(uN_minus_u1), latex(uN_minus_u1), latex(k_plus_1),
                              latex(m),
                              latex(m), latex(m_minus_1), latex(u1), latex(m_minus_1), latex(uN_minus_u1), latex(k_plus_1), latex(da_val),
                              latex(N), latex(m),
                              latex(m), latex(N), latex(u1), latex(uN), latex(da_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

