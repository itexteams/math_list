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


def bt_dang16_p3_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':


                k = random.randint(2, 4)
                m = random.randint(1, k - 1)

                t0 = 2 * k
                a = 2 * m * k
                a2 = a**2
                C = t0 * (t0 - 1)
                x_sol = k**2 + m**2

                # Các giá trị trung gian cho lời giải
                t_neg = -(t0 - 1)
                K = (t0**2) // 2 # K = 2*k^2

                # Đáp án đúng
                kq = x_sol

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu (đảm bảo không trùng đáp án đúng)
                s = []
                while len(s) < 3:
                    sai = x_sol + random.choice([-3, -2, -1, 1, 2, 3, 4])
                    if sai != x_sol and sai > 0 and ('$%s$' % sai) not in s:
                        s.append('$%s$' % sai)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Nghiệm của phương trình $\\sqrt{x+%s} + \\sqrt{x-%s} = 2x - %s + 2\\sqrt{x^2 - %s}$ bằng bao nhiêu?'''
                                 % (latex(a), latex(a), latex(C), latex(a2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo mẫu ảnh
                loigiai = ('''Điều kiện: $x \\ge %s$. Đặt $t = \\sqrt{x+%s} + \\sqrt{x-%s} \\quad (t \\ge 0)$ \\\\
                             $\\Rightarrow t^2 = x+%s + x-%s + 2\\sqrt{(x-%s)(x+%s)} = 2x + 2\\sqrt{x^2 - %s}$. \\\\
                             Phương trình trở thành: $t = t^2 - %s \\Leftrightarrow t^2 - t - %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} & t = %s \\text{ (loại)} \\\\ & t = %s \\text{ (nhận)} \\end{aligned} \\right.$ \\\\
                             Với $t = %s$ thì $%s^2 = 2x + 2\\sqrt{x^2 - %s} \\Leftrightarrow 2\\sqrt{x^2 - %s} = %s - 2x \\Leftrightarrow \\sqrt{x^2 - %s} = %s - x$ \\\\
                             $\\Leftrightarrow \\begin{cases} %s - x \\ge 0 \\\\ x^2 - %s = (%s - x)^2 \\end{cases} \\Leftrightarrow \\begin{cases} x \\le %s \\\\ x^2 - %s = %s - %sx + x^2 \\end{cases} \\Leftrightarrow \\begin{cases} x \\le %s \\\\ %sx = %s \\end{cases} \\Leftrightarrow x = %s$ \\\\
                             Vậy nghiệm phương trình là $x = %s$.'''
                           % (latex(a), latex(a), latex(a), 
                              latex(a), latex(a), latex(a), latex(a), latex(a2),
                              latex(C), latex(C), latex(t_neg), latex(t0),
                              latex(t0), latex(t0), latex(a2), latex(a2), latex(t0**2), latex(a2), latex(K),
                              latex(K), latex(a2), latex(K), latex(K), latex(a2), latex(K**2), latex(2*K), latex(K), latex(2*K), latex(K**2 + a2), latex(x_sol),
                              latex(x_sol)
                             ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(x_sol))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

