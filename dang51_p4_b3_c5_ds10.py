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


def bt_dang51_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các giá trị ngẫu nhiên
                # n là số mũ, b là hệ số của x
                n = randint(10, 15)
                b = randint(2, 4)

                # Tính toán k để tìm hệ số lớn nhất
                # a_{k+1} > a_k <=> b(n-k) > k+1 <=> k(b+1) < bn - 1 <=> k < (bn-1)/(b+1)
                limit_num = b * n - 1
                limit_den = b + 1
                limit_val = limit_num / limit_den

                k_limit = math.floor(limit_val)
                k_max = k_limit + 1

                # Tính hệ số lớn nhất
                he_so_max = binomial(n, k_max) * (b**k_max)

                # Tính các giá trị lân cận để làm phương án sai
                h_gan_1 = binomial(n, k_max - 1) * (b**(k_max - 1))
                h_gan_2 = binomial(n, k_max + 1) * (b**(k_max + 1)) if k_max < n else he_so_max - 100

                # Tạo phương án sai bằng cách đảo chữ số hoặc cộng trừ ngẫu nhiên
                def generate_wrong(correct):
                    s_val = str(correct)
                    if len(s_val) > 3:
                        # Đảo vị trí 2 chữ số ngẫu nhiên
                        idx = randint(1, len(s_val) - 2)
                        list_s = list(s_val)
                        list_s[idx], list_s[idx+1] = list_s[idx+1], list_s[idx]
                        wrong = int("".join(list_s))
                        if wrong != correct: return wrong
                    return correct + randint(100, 500)

                da_d = ('\\True $%s$' % (latex(he_so_max)))

                # Tạo danh sách đáp án sai
                s = []
                s.append('$%s$' % (latex(h_gan_1)))
                s.append('$%s$' % (latex(h_gan_2)))
                s.append('$%s$' % (latex(generate_wrong(he_so_max))))

                # Đảm bảo không trùng lặp và không trùng đáp án đúng
                final_s = []
                for item in s:
                    if item != ('$%s$' % (latex(he_so_max))) and item not in final_s:
                        final_s.append(item)

                while len(final_s) < 3:
                    new_w = '$%s$' % (latex(he_so_max + randint(10, 1000)))
                    if new_w not in final_s:
                        final_s.append(new_w)

                da_s1 = final_s[0]
                da_s2 = final_s[1]
                da_s3 = final_s[2]

                # Câu hỏi
                noidungcauhoi = ('''Tìm hệ số có giá trị lớn nhất khi khai triển $P\\left(x\\right)=\\left(1+%sx^2\\right)^{%s}$ thành đa thức.'''
                                 %(latex(b), latex(n)))

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Khai triển: $P\\left(x\\right)=\\sum_{k=0}^{%s} C_{%s}^k %s^k x^{2k}=\\sum_{k=0}^{%s} a_k x^{2k}$ với $a_k = C_{%s}^k %s^k$. \\\\
                             Xét bất đẳng thức $a_{k+1} > a_k$: \\\\
                             $\\Leftrightarrow C_{%s}^{k+1} %s^{k+1} > C_{%s}^k %s^k$ \\\\
                             $\\Leftrightarrow \\frac{%s!}{\\left(k+1\\right)! \\left(%s-k-1\\right)!} \\cdot %s > \\frac{%s!}{k! \\left(%s-k\\right)!}$ \\\\
                             $\\Leftrightarrow \\frac{%s}{k+1} > \\frac{1}{%s-k}$ \\\\
                             $\\Leftrightarrow %s\\left(%s-k\\right) > k+1 \\Leftrightarrow k < \\frac{%s}{%s} \\approx %s$ \\\\
                             $\\Rightarrow k \\le %s$. \\\\
                             Như vậy $a_0 < a_1 < a_2 < \\dots < a_{%s}$. \\\\
                             Xét bất đẳng thức $a_{k+1} < a_k$: \\\\
                             $\\Leftrightarrow k > \\frac{%s}{%s} \\Rightarrow k \\ge %s$. \\\\
                             Như vậy $a_{%s} > a_{%s} > \\dots > a_{%s}$. \\\\
                             Vậy hệ số có giá trị lớn nhất là $a_{%s} = C_{%s}^{%s} %s^{%s} = %s$.'''
                           %(latex(n), latex(n), latex(b), latex(n), latex(n), latex(b),
                             latex(n), latex(b), latex(n), latex(b),
                             latex(n), latex(n), latex(b), latex(n), latex(n),
                             latex(b), latex(n),
                             latex(b), latex(n), latex(limit_num), latex(limit_den), latex(round(limit_val, 2)),
                             latex(k_limit),
                             latex(k_max),
                             latex(limit_num), latex(limit_den), latex(k_max),
                             latex(k_max), latex(k_max + 1), latex(n),
                             latex(k_max), latex(n), latex(k_max), latex(b), latex(k_max), latex(he_so_max)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

