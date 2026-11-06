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


def bt_dang19_p4_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các hệ số M, N để tạo ra nhiều câu hỏi khác nhau
                # Biểu thức gốc: M = 3, N = 2
                M = randint(2, 6)
                N = randint(1, 5)

                # Từ phép biến đổi toán học:
                # Tử số luôn là 3*(sqrt(2) - 1) -> a = 3
                # Mẫu số là ((N + 1)*2*sqrt(2) + N*sqrt(2) + M) = (3N + 2)*sqrt(2) + M -> b = 3N + 2
                a = 3
                b = 3 * N + 2

                # Kết quả cần tính là tổng a + b
                kq_dung = a + b

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq_dung))]
                da = random.choice(du)

                # Tạo các phương án nhiễu (không trùng với đáp án đúng và phải lớn hơn 0)
                s = set()
                while len(s) < 3:
                    sai = kq_dung + randint(-5, 5)
                    if sai != kq_dung and sai > 0:
                        s.add('$%s$' % (latex(sai)))

                s = list(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Thiết lập chuỗi hệ số hiển thị trực quan (nếu hệ số bằng 1 thì ẩn đi)
                M_str = '' if M == 1 else latex(M)
                N_str = '' if N == 1 else latex(N)

                # Câu hỏi
                noidungcauhoi = ('''Cho $\\tan \\alpha = \\sqrt{2}$. Tính giá trị của biểu thức $C = \\frac{\\sin \\alpha - \\cos \\alpha}{\\sin^3 \\alpha + %s\\cos^3 \\alpha + %s\\sin \\alpha}$ ta được $C = \\frac{a(\\sqrt{2} - 1)}{b\\sqrt{2} + %s}$ ($\\frac{a}{b}$ tối giản và $b > 0$). Tính giá trị $a + b$.'''
                                 % (M_str, N_str, latex(M)))



                # Nội dung lời giải chi tiết từng bước
                loigiai = ('''Chia cả tử và mẫu của biểu thức $C$ cho $\\cos^3 \\alpha$, ta được: \\\\
                           $C = \\frac{\\frac{\\sin \\alpha}{\\cos^3 \\alpha} - \\frac{\\cos \\alpha}{\\cos^3 \\alpha}}{\\frac{\\sin^3 \\alpha}{\\cos^3 \\alpha} + %s + %s\\frac{\\sin \\alpha}{\\cos^3 \\alpha}} = \\frac{\\tan \\alpha \\cdot \\frac{1}{\\cos^2 \\alpha} - \\frac{1}{\\cos^2 \\alpha}}{\\tan^3 \\alpha + %s + %s\\tan \\alpha \\cdot \\frac{1}{\\cos^2 \\alpha}}$. \\\\
                           Thay $\\frac{1}{\\cos^2 \\alpha} = 1 + \\tan^2 \\alpha$ vào biểu thức, ta được: \\\\
                           $C = \\frac{\\tan \\alpha(1 + \\tan^2 \\alpha) - (1 + \\tan^2 \\alpha)}{\\tan^3 \\alpha + %s + %s\\tan \\alpha(1 + \\tan^2 \\alpha)} = \\frac{(\\tan \\alpha - 1)(1 + \\tan^2 \\alpha)}{(%s)\\tan^3 \\alpha + %s\\tan \\alpha + %s}$. \\\\
                           Thay giả thiết $\\tan \\alpha = \\sqrt{2}$ vào biểu thức trên, ta được: \\\\
                           $C = \\frac{(\\sqrt{2} - 1)(1 + 2)}{(%s) \\cdot (\\sqrt{2})^3 + %s\\sqrt{2} + %s} = \\frac{3(\\sqrt{2} - 1)}{%s\\sqrt{2} + %s\\sqrt{2} + %s} = \\frac{3(\\sqrt{2} - 1)}{%s\\sqrt{2} + %s}$. \\\\
                           Đối chiếu với dạng bài cho $C = \\frac{a(\\sqrt{2} - 1)}{b\\sqrt{2} + %s}$, vì $\\frac{3}{%s}$ là phân số tối giản và $%s > 0$ nên ta chọn $a = 3$ và $b = %s$. \\\\
                           Vậy giá trị $a + b = 3 + %s = %s$.'''
                           % (M_str, N_str, M_str, N_str,
                              M_str, N_str, latex(N + 1), N_str, M_str,
                              latex(N + 1), N_str, M_str, latex(2 * (N + 1)), N_str, M_str, latex(3 * N + 2), M_str,
                              M_str, latex(b), latex(b), latex(b), latex(b), latex(kq_dung)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

