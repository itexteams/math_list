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


def bt_dang20_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các tham số: n là số mũ, a là bậc căn thứ nhất, b là bậc căn thứ hai
                # Để k là số nguyên: k = (b*n) / (a+b). Ta chọn a, b trước rồi tính n.
                a = random.randint(2, 4)
                b = random.randint(2, 5)
                # Để k nguyên, n phải là bội số của (a+b) / gcd(b, a+b)
                step = (a + b) // math.gcd(b, a + b)
                m = random.randint(1, 2) # Hệ số nhân để n không quá lớn
                n = m * step

                # Tính toán các giá trị
                k = (b * n) // (a + b)
                kq_val = binomial(n, k)

                # Tạo các phương án sai
                s_list = set()
                while len(s_list) < 3:
                    # Phương án sai dựa trên các tổ hợp k lân cận hoặc số ngẫu nhiên
                    sai1 = binomial(n, abs(k-1)) if k > 0 else kq_val + 5
                    sai2 = binomial(n, k+1) if k < n else kq_val + 10
                    sai3 = kq_val + random.randint(5, 15)

                    for v in [sai1, sai2, sai3]:
                        if v != kq_val and v > 0:
                            s_list.add(str(v))
                    if len(s_list) < 3:
                        s_list.add(str(kq_val + random.randint(16, 30)))

                s = list(s_list)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                # Cấu trúc: (\sqrt[a]{x} + 1/\sqrt[b]{x})^n
                bieuthuc = "\\left(\\sqrt[%s]{x} + \\frac{1}{\\sqrt[%s]{x}}\\right)^{%s}" % (latex(a), latex(b), latex(n))
                noidungcauhoi = ("Tìm hệ số không chứa $x$ của khai triển nhị thức Newton của $%s$ với $x > 0$."
                                 % (bieuthuc))

                # Đáp án đúng
                da = "$%s$" % (latex(kq_val))
                da_d = ("\\True " + str(da))
                da_s1 = "$%s$" % (das1)
                da_s2 = "$%s$" % (das2)
                da_s3 = "$%s$" % (das3)

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tính toán các hệ số cho phần lời giải
                mau_so = a * b
                # Số mũ của x: (n-k)/a - k/b = [b(n-k) - ak] / ab = [bn - (a+b)k] / ab
                tu_so_1 = b * n
                tu_so_2 = a + b

                # Nội dung lời giải
                loigiai = ("Ta có: $%s = \\sum_{k=0}^{%s} C_{%s}^k \\left(\\sqrt[%s]{x}\\right)^{%s-k} \\left(\\frac{1}{\\sqrt[%s]{x}}\\right)^k = \\sum_{k=0}^{%s} C_{%s}^k x^{\\frac{%s-k}{%s}} \\cdot \\frac{1}{x^{\\frac{k}{%s}}} = \\sum_{k=0}^{%s} C_{%s}^k x^{\\frac{%s-%sk}{%s}}$. \\\\"
                           "Số hạng tổng quát trong khai triển là: $C_{%s}^k x^{\\frac{%s-%sk}{%s}}$. \\\\"
                           "Để có số hạng không chứa $x$ thì $\\frac{%s-%sk}{%s} = 0 \\Leftrightarrow %s - %sk = 0 \\Leftrightarrow k = %s$. \\\\"
                           "Vậy hệ số không chứa $x$ trong khai triển là: $C_{%s}^{%s} = %s$."
                           % (bieuthuc, latex(n), latex(n), latex(a), latex(n), latex(b), latex(n), latex(n), latex(n), latex(a), latex(b), latex(n), latex(n), latex(tu_so_1), latex(tu_so_2), latex(mau_so),
                              latex(n), latex(tu_so_1), latex(tu_so_2), latex(mau_so),
                              latex(tu_so_1), latex(tu_so_2), latex(mau_so), latex(tu_so_1), latex(tu_so_2), latex(k),
                              latex(n), latex(k), latex(kq_val)
                           ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

