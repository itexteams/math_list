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


def bt_dang12_p1_b2_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random k (hệ số tỉ lệ), u1, u2, u3 (tọa độ vector AB)
                # Chọn sao cho zA = -k * u3 để zM = zA + k*u3 = 0
                k = random.choice([-3, -2, -1, 1, 2, 3])
                u1 = random.choice([i for i in range(-4, 5) if i != 0])
                u2 = random.choice([i for i in range(-4, 5) if i != 0 and i != u1])
                u3 = random.choice([i for i in range(-3, 4) if i != 0])

                xA = random.randint(-4, 4)
                yA = random.randint(-4, 4)
                zA = -k * u3

                xB = xA + u1
                yB = yA + u2
                zB = zA + u3

                xM = xA + k * u1
                yM = yA + k * u2
                zM = 0

                # Hàm hỗ trợ định dạng chuỗi x - x_A, y - y_A đẹp mắt
                def get_num(var, val):
                    if val == 0: 
                        return var
                    elif val > 0: 
                        return "%s - %s" % (var, val)
                    else: 
                        return "%s + %s" % (var, -val)

                num_x = get_num('x', xA)
                num_y = get_num('y', yA)

                # Đáp án đúng
                ans_correct = "M(%s; %s; 0)" % (xM, yM)

                # Tạo danh sách các phương án nhiễu
                opts = set()
                opts.add("M(%s; %s; 0)" % (xM, -yM))
                opts.add("M(%s; %s; 0)" % (-xM, yM))
                opts.add("M(%s; %s; 0)" % (-xM, -yM))
                opts.add("M(%s; %s; 0)" % (yM, xM))
                opts.add("M(%s; %s; 1)" % (xM, yM))
                opts.add("M(%s; %s; 0)" % (xM + 1, yM - 1))

                if ans_correct in opts:
                    opts.remove(ans_correct)

                wrong_opts = random.sample(list(opts), 3)

                da_d = '\\True $%s$' % ans_correct
                da_s1 = '$%s$' % wrong_opts[0]
                da_s2 = '$%s$' % wrong_opts[1]
                da_s3 = '$%s$' % wrong_opts[2]

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Trong không gian với hệ trục tọa độ $Oxyz$, cho hai điểm $A(%s; %s; %s)$ và $B(%s; %s; %s)$. Tọa độ điểm $M$ thuộc mặt phẳng $(Oxy)$ sao cho ba điểm $A$, $B$, $M$ thẳng hàng là''' % 
                                 (xA, yA, zA, xB, yB, zB))

                # Lời giải chi tiết
                loigiai = ('''Gọi $M(x; y; 0) \\in (Oxy)$; $\\overrightarrow{AB} = (%s; %s; %s)$; $\\overrightarrow{AM} = (%s; %s; %s)$. \\\\
            Ba điểm $A$, $B$, $M$ thẳng hàng $\\Leftrightarrow \\overrightarrow{AB}$ và $\\overrightarrow{AM}$ cùng phương $\\Leftrightarrow \\frac{%s}{%s} = \\frac{%s}{%s} = \\frac{%s}{%s}$ \\\\
            $\\Leftrightarrow \\begin{cases} \\frac{%s}{%s} = %s \\\\ \\frac{%s}{%s} = %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$. Vậy $%s$.''' % 
                (u1, u2, u3, num_x, num_y, -zA, 
                 num_x, u1, num_y, u2, -zA, u3,
                 num_x, u1, k, num_y, u2, k, xM, yM, ans_correct))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

