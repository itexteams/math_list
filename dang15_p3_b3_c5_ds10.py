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


def bt_dang15_p3_b3_c5_ds10(self):
            # Vòng lặp để đảm bảo kết quả nằm trong khoảng (-999, 9999)
            while True:
                a = randint(1, 10)
                b = randint(-10, 10)
                if b == 0: continue
                n = randint(3, 15)

                # Tổng các hệ số của P(x) = (a + bx)^n là P(1) = (a + b)^n
                kq_val = (a + b)**n

                if -999 < kq_val < 9999:
                    break

            # Định dạng hiển thị nhị thức (a + bx)
            b_sign = "+" if b > 0 else "-"
            b_abs = abs(b)
            if b_abs == 1:
                nhithuc_str = "%s %s x" % (a, b_sign)
            else:
                nhithuc_str = "%s %s %sx" % (a, b_sign, b_abs)

            # Câu hỏi
            noidungcauhoi = ('''Tổng các hệ số trong khai triển nhị thức Niu-tơn của biểu thức $P(x) = \\left( %s \\right)^{%s}$ bằng bao nhiêu?'''
                             % (nhithuc_str, latex(n)))

            # Đáp án đúng dạng số nguyên
            da_d = '\\True $%d$' % kq_val

            # Tạo các phương án nhiễu
            s_set = set()
            # Các sai lầm: tính (a-b)^n, tính nhầm n, hoặc cộng/trừ đơn vị
            wrong_list = [
                (a - b)**n,
                (a + b)**(n - 1) if n > 3 else kq_val + 10,
                kq_val + randint(1, 5),
                kq_val - randint(1, 5),
                a**n # Quên hệ số b
            ]
            for w in wrong_list:
                if w != kq_val and -2000 < w < 20000:
                    s_set.add('$%d$' % w)

            while len(s_set) < 3:
                s_set.add('$%d$' % (kq_val + randint(-20, 20)))

            list_ans = list(s_set)
            list_ans.append(da_d)
            random.shuffle(list_ans)

            # Nội dung lời giải
            loigiai = ('''Tổng các hệ số trong khai triển nhị thức Niu-tơn của đa thức $P(x)$ được tính bằng giá trị của đa thức đó tại $x = 1$.\\\\
                         Thay $x = 1$ vào biểu thức $P(x) = \\left( %s \\right)^{%s}$, ta được:\\\\
                         $S = P(1) = \\left( %s %s %s \\cdot 1 \\right)^{%s} = \\left( %s \\right)^{%s} = %d$.'''
                       % (nhithuc_str, latex(n),
                          a, b_sign, b_abs, latex(n),
                          a + b, latex(n), kq_val))

            # Đáp án ngắn: Ghi kết quả số nguyên vào phần dapan
            dapan = '\\shortans[0]{$%d$}\n' % kq_val

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('--', '+')

            return content

