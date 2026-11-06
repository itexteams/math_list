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


def bt_dang14_p1_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập tham số ngẫu nhiên logic
                bo_ba_list = [(5, 12, 13), (3, 4, 5), (8, 15, 17)]

                bo_alpha = random.choice(bo_ba_list)
                bo_beta = random.choice(bo_ba_list)

                # Đảm bảo hai bộ ba không bị trùng lặp hoàn toàn để bài toán phong phú hơn
                while bo_alpha == bo_beta:
                    bo_beta = random.choice(bo_ba_list)

                # Thiết lập cho góc alpha: pi/2 < alpha < pi (sin dương, cos âm)
                sin_alpha = Rational(bo_alpha[0], bo_alpha[2])
                cos_alpha = -Rational(bo_alpha[1], bo_alpha[2])

                # Thiết lập cho góc beta: 0 < beta < pi/2 (sin dương, cos dương)
                cos_beta = Rational(bo_beta[1], bo_beta[2])
                sin_beta = Rational(bo_beta[0], bo_beta[2])

                # Tính giá trị biểu thức: cos(alpha - beta) = cos_alpha * cos_beta + sin_alpha * sin_beta
                kq_chinh_xac = cos_alpha * cos_beta + sin_alpha * sin_beta

                # Định dạng chuỗi LaTeX cho đáp án đúng
                da_dung_str = latex(kq_chinh_xac)
                da = '$%s$' % da_dung_str
                du = [da]
                da_chon = random.choice(du)

                # B4: Tạo các phương án sai (nhiễu) không trùng đáp án đúng
                s_set = set()
                nhiieu_list = [
                    -kq_chinh_xac, 
                    cos_alpha * cos_beta - sin_alpha * sin_beta, 
                    -(cos_alpha * cos_beta - sin_alpha * sin_beta),
                    Rational(bo_alpha[1] * bo_beta[1] + bo_alpha[0] * bo_beta[0], bo_alpha[2] * bo_beta[2])
                ]

                for item in nhiieu_list:
                    p_an = '$%s$' % latex(item)
                    if p_an != da:
                        s_set.add(p_an)

                list_sai = list(s_set)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hai góc $\\alpha, \\beta$ thỏa mãn $\\sin \\alpha = %s, \\left( \\frac{\\pi}{2} < \\alpha < \\pi \\right)$ và $\\cos \\beta = %s, \\left( 0 < \\beta < \\frac{\\pi}{2} \\right)$. Giá trị đúng của $\\cos (\\alpha - \\beta)$ bằng'''
                                 % (latex(sin_alpha), latex(cos_beta)))

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # KHU VỰC ĐÃ FIX LỖI CÚ PHÁP: Thêm dấu nháy đơn bao quanh chuỗi định dạng
                sin_alpha_binh = '\\frac{%s}{%s}' % (latex(bo_alpha[0]**2), latex(bo_alpha[2]**2))
                cos_beta_binh = '\\frac{%s}{%s}' % (latex(bo_beta[1]**2), latex(bo_beta[2]**2))

                # Trình bày lời giải chi tiết từng bước
                loigiai = ('''$\\sin \\alpha = %s, \\left( \\frac{\\pi}{2} < \\alpha < \\pi \\right)$ nên $\\cos \\alpha = -\\sqrt{1 - \\left( %s \\right)^2} = -%s$. \\\\
            $\\cos \\beta = %s, \\left( 0 < \\beta < \\frac{\\pi}{2} \\right)$ nên $\\sin \\beta = \\sqrt{1 - \\left( %s \\right)^2} = %s$. \\\\
            $\\cos (\\alpha - \\beta) = \\cos \\alpha \\cos \\beta + \\sin \\alpha \\sin \\beta = \\left( -%s \\right) \\cdot %s + %s \\cdot %s = %s$.'''
                           % (latex(sin_alpha), latex(sin_alpha), latex(-cos_alpha),
                              latex(cos_beta), latex(cos_beta), latex(sin_beta),
                              latex(-cos_alpha), latex(cos_beta), latex(sin_alpha), latex(sin_beta), da_dung_str))

            # Xuất câu trắc nghiệm định dạng minipage TeX
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

