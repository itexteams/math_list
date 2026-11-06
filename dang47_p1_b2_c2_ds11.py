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


def bt_dang47_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random vị trí p, q và số hạng cần tính tổng N
                p = randint(3, 6)
                q = randint(15, 22)
                N = randint(8, 15)

                # Random u1 và công sai d khác 0
                u1 = randint(-40, 40)
                d = randint(-8, 8)
                while d == 0:
                    d = randint(-8, 8)

                # Tính u_p và u_q
                p_minus_1 = p - 1
                q_minus_1 = q - 1
                up = u1 + p_minus_1 * d
                uq = u1 + q_minus_1 * d

                # Tính tổng S_N = N/2 * (2*u1 + (N-1)*d)
                N_minus_1 = N - 1
                two_u1 = 2 * u1
                sum_inner = two_u1 + N_minus_1 * d
                SN_val = Rational(N * sum_inner, 2)

                # Định dạng đáp án đúng
                da_val = 'S_{%s} = %s' % (latex(N), latex(SN_val))

                # Tạo các đáp án sai không trùng với đáp án đúng
                s_set = set()
                s_set.add('S_{%s} = %s' % (latex(N), latex(-SN_val)))
                s_set.add('S_{%s} = %s' % (latex(N), latex(SN_val * 2)))
                s_set.add('S_{%s} = %s' % (latex(N), latex(SN_val + 75)))
                s_set.add('S_{%s} = %s' % (latex(N), latex(SN_val - 75)))
                s_set.add('S_{%s} = %s' % (latex(N), latex(SN_val + 100)))
                s_set.add('S_{%s} = %s' % (latex(N), latex(SN_val - 100)))

                s_set.discard(da_val)

                s_list = list(s_set)
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho cấp số cộng $(u_n)$ có $u_{%s} = %s, u_{%s} = %s$. Tổng của $%s$ số hạng đầu tiên của cấp số cộng này là'''
                                 % (latex(p), latex(up), latex(q), latex(uq), latex(N)))

                # Các đáp án
                da_d = ('\\True $%s$' % (da_val))
                da_s1 = '$%s$' % (das1)
                da_s2 = '$%s$' % (das2)
                da_s3 = '$%s$' % (das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Các giá trị tính toán trung gian phục vụ trình bày lời giải
                q_minus_p = q - p
                uq_minus_up = uq - up

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi $u_1$ là số hạng đầu và $d$ là công sai của cấp số cộng $(u_n)$. \\\\
            Mặt khác, ta có $\\begin{cases} u_{%s} = u_1 + %sd = %s \\\\ u_{%s} = u_1 + %sd = %s \\end{cases}$. \\\\
            Trừ hai vế của phương trình thứ hai cho phương trình thứ nhất, ta được: \\\\
            $%sd = %s \\Leftrightarrow d = %s$. \\\\
            Thay $d = %s$ vào phương trình $u_1 + %sd = %s$, ta được: \\\\
            $u_1 + %s \\cdot (%s) = %s \\Leftrightarrow u_1 = %s$. \\\\
            Tổng của $%s$ số hạng đầu tiên của cấp số cộng là: \\\\
            $S_{%s} = \\frac{%s}{2} \\left[ 2u_1 + (%s - 1)d \\right] = \\frac{%s}{2} \\left[ 2 \\cdot (%s) + %s \\cdot (%s) \\right] = %s$.'''
                           % (latex(p), latex(p_minus_1), latex(up),
                              latex(q), latex(q_minus_1), latex(uq),
                              latex(q_minus_p), latex(uq_minus_up), latex(d),
                              latex(d), latex(p_minus_1), latex(up),
                              latex(p_minus_1), latex(d), latex(up), latex(u1),
                              latex(N),
                              latex(N), latex(N), latex(N), latex(N), latex(u1), latex(N_minus_1), latex(d), latex(SN_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

