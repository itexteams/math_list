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


def bt_dang12_p1_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập tham số ngẫu nhiên logic
                # Sử dụng bộ ba Pythagore (3,4,5) hoặc (5,12,13) hoặc (8,15,17) để toán đẹp số nguyên
                bo_ba = random.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17)])
                doi = bo_ba[0]   # Cạnh đối (tử số của sin x)
                ke = bo_ba[1]    # Cạnh kề
                huyen = bo_ba[2] # Cạnh huyền (mẫu số)

                # Cho góc x nằm ở góc phần tư thứ hai: pi/2 < x < pi (sin dương, cos âm, tan âm)
                sin_x = Rational(doi, huyen)
                cos_x = -Rational(ke, huyen)
                tan_x = -Rational(doi, ke)

                # Tính giá trị tan(x + pi/4) = (tan_x + 1) / (1 - tan_x)
                tan_pi_4 = 1
                tu_so_kq = tan_x + 1
                mau_so_kq = 1 - tan_x
                kq_chinh_xac = Rational(tu_so_kq, mau_so_kq)

                # Định dạng chuỗi LaTeX cho đáp án đúng
                da_dung_str = latex(kq_chinh_xac).replace('.', ',')
                da = '$%s$' % da_dung_str
                du = [da]
                da_chon = random.choice(du)

                # B4: Điều chỉnh các phương án sai không được trùng với đáp án đúng
                s_set = set()
                # Tạo các phương án nhiễu từ các lỗi sai dấu hoặc sai công thức thông thường
                nhiieu_list = [
                    -kq_chinh_xac,
                    Rational(ke - doi, ke + doi),
                    Rational(doi - ke, ke + doi),
                    Rational(doi + ke, ke - doi),
                    Rational(ke, huyen),
                    -Rational(doi, huyen)
                ]

                for item in nhiieu_list:
                    p_an = '$%s$' % latex(item).replace('.', ',')
                    if p_an != da:
                        s_set.add(p_an)

                list_sai = list(s_set)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho $\\sin x = %s$ với $\\frac{\\pi}{2} < x < \\pi$ khi đó $\\tan \\left( x + \\frac{\\pi}{4} \\right)$ bằng'''
                                 % latex(sin_x))

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuỗi hiển thị phân số bình phương cho lời giải
                sin_binh_str = '\\frac{%s}{%s}' % (latex(doi**2), latex(huyen**2))
                cos_binh_str = '\\frac{%s}{%s}' % (latex(ke**2), latex(huyen**2))
                cos_tuyet_doi_str = '\\frac{%s}{%s}' % (latex(ke), latex(huyen))

                # Nội dung lời giải chi tiết, rõ ràng từng bước như nội dung gốc
                loigiai = ('''Từ $\\sin^2 x + \\cos^2 x = 1 \\Rightarrow \\cos x = \\pm\\sqrt{1 - \\sin^2 x} = \\pm\\sqrt{1 - %s} = \\pm %s$. \\\\
            Vì $\\frac{\\pi}{2} < x < \\pi$ nên $\\cos x = -%s$ do đó $\\tan x = \\frac{\\sin x}{\\cos x} = \\frac{%s}{-%s} = %s$. \\\\
            Ta có: $\\tan \\left( x + \\frac{\\pi}{4} \\right) = \\frac{\\tan x + \\tan \\frac{\\pi}{4}}{1 - \\tan x \\cdot \\tan \\frac{\\pi}{4}} = \\frac{%s + 1}{1 - \\left(%s\\right)} = %s$.'''
                           % (sin_binh_str, cos_tuyet_doi_str, cos_tuyet_doi_str, latex(sin_x), cos_tuyet_doi_str, latex(tan_x),
                              latex(tan_x), latex(tan_x), da_dung_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

