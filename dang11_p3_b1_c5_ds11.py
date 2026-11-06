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


def bt_dang11_p3_b1_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            a = symbols('a')

            # B3: Random số liệu để kết quả m, n nhỏ
            # Mục tiêu: A = a^(m/n), đáp án là giá trị m + n (tối đa 4 ký tự)
            n1 = random.choice([2, 3, 5]) 
            m1 = random.randint(1, 4)
            m2_val = random.randint(1, 5)
            n2_val = n1 

            k1 = random.randint(1, 3)
            n3 = random.choice([2, 3, 7])
            m3 = random.randint(-5, -1)

            # Tính toán
            mu_tu = Rational(m1, n1) + Rational(m2_val, n2_val)
            mu_mau = k1 + Rational(m3, n3)
            mu_tong = mu_tu - mu_mau

            m = abs(mu_tong.p) # Tử số
            n = abs(mu_tong.q) # Mẫu số

            # Giá trị cần hỏi (Ví dụ: Tổng m + n)
            kq_dung = m + n 

            # Tạo danh sách đáp án nhiễu (đảm bảo tối đa 4 ký tự)
            da_dung_str = str(kq_dung)
            s = set()
            while len(s) < 3:
                fake = kq_dung + random.randint(-5, 5)
                if fake > 0 and fake != kq_dung and len(str(fake)) <= 4:
                    s.add(str(fake))

            list_wrong = list(s)

            # Câu hỏi
            noidungcauhoi = (r'''Cho biểu thức $A = \frac{\sqrt[%s]{a^{%s}} \cdot a^{\frac{%s}{%s}}}{a^{%s} \cdot \sqrt[%s]{a^{%s}}}$ với $a > 0$. Viết $A$ dưới dạng $a^{\frac{m}{n}}$ (với $\frac{m}{n}$ là phân số tối giản). Khi đó giá trị $S = m + n$ bằng bao nhiêu?''' 
                             % (latex(n1), latex(m1), latex(m2_val), latex(n2_val), latex(k1), latex(n3), latex(m3)))

            # Lời giải
            loigiai = (r'''Ta có: $A = \frac{a^{\frac{%s}{%s}} \cdot a^{\frac{%s}{%s}}}{a^{%s} \cdot a^{\frac{%s}{%s}}} = a^{\left(\frac{%s}{%s} + \frac{%s}{%s}\right) - \left(%s + \frac{%s}{%s}\right)} = a^{\frac{%s}{%s}}$. \\
                         Phân số tối giản có $m = %s, n = %s$. \\
                         Vậy $S = m + n = %s + %s = %s$.'''
                         % (m1, n1, m2_val, n2_val, k1, m3, n3, m1, n1, m2_val, n2_val, k1, m3, n3, m, n, m, n, m, n, kq_dung))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_dung))

            # Trộn đáp án
            da_d = '\\True ' + da_dung_str
            list_1 = [da_d, list_wrong[0], list_wrong[1], list_wrong[2]]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

