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


def bt_dang42_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random vị trí n, u1 và công sai d
                n = randint(6, 10)
                u1_den = randint(2, 4)
                u1_num = randint(1, 5)
                u1 = Rational(u1_num, u1_den)

                d_num = randint(2, 12)
                while d_num % u1_den == 0:
                    d_num = randint(2, 12)

                d_exact = Rational(d_num, u1_den)

                # Tính u_n theo công thức u_n = u1 + (n - 1)*d
                un = u1 + (n - 1) * d_exact

                # Các giá trị tính toán cho lời giải
                n_minus_1 = n - 1
                un_minus_u1 = un - u1

                # Đáp án đúng
                da_val = d_exact

                # Tạo các đáp án sai không trùng với đáp án đúng
                s_set = set()
                if da_val.p != 0:
                    s_set.add(Rational(da_val.q, da_val.p)) # Đảo ngược tử và mẫu
                s_set.add(Rational(un_minus_u1, n)) # Nhầm chia cho n thay vì (n-1)
                s_set.add(da_val + Rational(1, u1_den))
                s_set.add(da_val - Rational(1, u1_den))
                s_set.add(da_val + 1)
                s_set.add(da_val - 1)

                s_set.discard(da_val)

                s_list = list(s_set)
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Biểu diễn LaTeX của các phương án
                da = 'd = %s' % (latex(da_val))
                da_s1 = 'd = %s' % (latex(das1))
                da_s2 = 'd = %s' % (latex(das2))
                da_s3 = 'd = %s' % (latex(das3))

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho một cấp số cộng $(u_n)$ có $u_1 = %s$, $u_{%s} = %s$. Công sai $d$ là'''
                                 % (latex(u1), latex(n), latex(un)))

                # Định dạng phương án trắc nghiệm
                da_d = ('\\True $' + str(da) + '$')
                da_s1_str = ('$' + str(da_s1) + '$')
                da_s2_str = ('$' + str(da_s2) + '$')
                da_s3_str = ('$' + str(da_s3) + '$')

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1_str, da_s2_str, da_s3_str]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Ta có công thức số hạng tổng quát của cấp số cộng: $u_n = u_1 + (n - 1)d$. \\\\
            Thay $n = %s$, $u_1 = %s$ và $u_{%s} = %s$ vào công thức, ta được: \\\\
            $%s = %s + (%s - 1)d \\Leftrightarrow %s \\cdot d = %s - %s \\Leftrightarrow %s \\cdot d = %s \\Leftrightarrow d = %s$.'''
                           % (latex(n), latex(u1), latex(n), latex(un),
                              latex(un), latex(u1), latex(n), latex(n_minus_1), latex(un), latex(u1), latex(n_minus_1), latex(un_minus_u1), latex(da_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

