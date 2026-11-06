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


def bt_dang66_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo các hệ số ngẫu nhiên cho đường thẳng d: y = ax + b
                # d: ax - y + b = 0
                a = randint(2, 6)
                b = randint(-9, 9)
                if b == 0: b = 1

                # Tọa độ VTPT của d
                n_vec = (a, -1)

                # Tạo các phương án sai (là các đường thẳng song song hoặc trùng với d)
                # Phương án song song 1: -ax + y = 0 (tương đương ax - y = 0)
                sai1 = "-%sx + y = 0" % (latex(a)) if a > 0 else "%sx + y = 0" % (latex(-a))

                # Phương án song song 2: ax - y + c2 = 0
                c2 = b + randint(2, 5)
                sign2 = "+" if c2 > 0 else ""
                sai2 = "%sx - y %s %s = 0" % (latex(a), sign2, latex(c2))

                # Phương án song song 3: ax - y + c3 = 0
                c3 = b - randint(2, 5)
                sign3 = "+" if c3 > 0 else ""
                sai3 = "%sx - y %s %s = 0" % (latex(a), sign3, latex(c3))

                # Đáp án đúng (Không song song): ax + y + c4 = 0 
                # VTPT là (a, 1), không cùng phương với (a, -1) vì a != 0
                c4 = randint(-9, 9)
                if c4 == 0: c4 = 6
                sign4 = "+" if c4 > 0 else ""
                da_dung_str = "%sx + y %s %s = 0" % (latex(a), sign4, latex(c4))

                # Câu hỏi
                # Chuyển b sang dạng hiển thị y = ax + b
                b_disp = ""
                if b > 0: b_disp = "+ " + str(b)
                elif b < 0: b_disp = "- " + str(abs(b))

                noidungcauhoi = ('''Phương trình nào sau đây là phương trình đường thẳng \\textbf{không} song song với đường thẳng $d: y = %sx %s$?'''
                                 % (latex(a), b_disp))

                # Các đáp án
                da_d = ('\\True $%s$' % (da_dung_str))
                da_s1 = '$%s$' % (sai1)
                da_s2 = '$%s$' % (sai2)
                da_s3 = '$%s$' % (sai3)

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # Chuyển d về dạng tổng quát ax - y + b = 0
                sign_b_lg = "+" if b > 0 else ""
                loigiai = ('''Ta có $d: y = %sx %s \\Leftrightarrow %sx - y %s %s = 0$. \\\\
                             Đường thẳng $(d)$ có VTPT là $\\vec{n} = (%s; -1)$. \\\\
                             Xét đường thẳng $%s$ có VTPT là $\\vec{n}_1 = (%s; 1)$. \\\\
                             Vì $\\vec{n}_1 \\neq k\\vec{n}$ (do tỉ số $\\frac{%s}{%s} \\neq \\frac{1}{-1}$) nên $\\vec{n}$ và $\\vec{n}_1$ không cùng phương. \\\\
                             Do đó đường thẳng $%s$ không song song với đường thẳng $(d)$.'''
                           % (latex(a), b_disp, latex(a), sign_b_lg, latex(b),
                              latex(a), da_dung_str, latex(a), latex(a), latex(a), da_dung_str))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
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

