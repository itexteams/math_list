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


def bt_dang43_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random u1, d, và giá trị đúng n
                u1 = randint(2, 7)
                d = randint(2, 6)
                n = randint(8, 16)

                # Tính tổng Sn
                Sn = (n * (2 * u1 + (n - 1) * d)) // 2

                # Các hệ số của phương trình bậc 2: a*n^2 + b*n + c = 0
                a = d
                b = 2 * u1 - d
                c = -2 * Sn

                # Nghiệm thứ hai của phương trình
                n2_val = Rational(-b - sqrt(b**2 - 4*a*c), 2*a)

                # Xử lý chuỗi hệ số b cho lời giải
                if b == 1:
                    b_str = '+ n'
                elif b == -1:
                    b_str = '- n'
                elif b > 0:
                    b_str = '+ %sn' % (b)
                elif b < 0:
                    b_str = '- %sn' % (-b)
                else:
                    b_str = ''

                # Tạo các đáp án sai không trùng với đáp án đúng
                s_set = set()
                while len(s_set) < 3:
                    fake_n = n + randint(-3, 4)
                    if fake_n != n and fake_n > 0:
                        s_set.add(fake_n)

                s_list = list(s_set)
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho dãy số $(u_n)$ là một cấp số cộng có $u_1 = %s$ và công sai $d = %s$. Biết tổng $n$ số hạng đầu của dãy số $(u_n)$ là $S_n = %s$. Giá trị $n$ bằng'''
                                 % (latex(u1), latex(d), latex(Sn)))

                # Định dạng phương án trắc nghiệm
                da_d = ('\\True $%s$' % (latex(n)))
                da_s1_str = ('$%s$' % (latex(das1)))
                da_s2_str = ('$%s$' % (latex(das2)))
                da_s3_str = ('$%s$' % (latex(das3)))

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1_str, da_s2_str, da_s3_str]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Ta có công thức tổng $n$ số hạng đầu tiên của cấp số cộng: $S_n = \\frac{n}{2}[2u_1 + (n-1)d]$. \\\\
            Thay $u_1 = %s$, $d = %s$ và $S_n = %s$ vào công thức, ta được: \\\\
            $%s = \\frac{n}{2}[2 \\cdot %s + (n-1) \\cdot %s] \\Leftrightarrow %s = n(%s + %sn - %s) \\Leftrightarrow %s = %sn^2 %s \\Leftrightarrow %sn^2 %s - %s = 0$. \\\\
            Giải phương trình trên (với điều kiện $n \\in \\mathbb{N}^*$), ta thu được $n = %s$ (thỏa mãn) hoặc $n = %s$ (loại). \\\\
            Vậy $n = %s$.'''
                           % (latex(u1), latex(d), latex(Sn),
                              latex(Sn), latex(u1), latex(d), latex(2*Sn), latex(2*u1), latex(d), latex(d), latex(2*Sn), latex(d), b_str, latex(d), b_str, latex(2*Sn),
                              latex(n), latex(n2_val),
                              latex(n)))

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

