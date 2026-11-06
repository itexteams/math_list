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


def bt_dang16_p4_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập tham số ngẫu nhiên logic
                # Biểu thức gốc dựa trên hệ thức: sin(beta)cos(alpha) + cos(beta)sin(alpha) = sin(beta + alpha)
                # Hoặc dạng tương đương biến đổi góc: sin(beta - alpha)
                # Trong đề bài gốc: alpha = -53, beta = 23. Hiệu: 23 - 53 = -30 độ.
                # Ta chọn ngẫu nhiên góc đặc biệt kết quả mong muốn là -30, -45 hoặc -60 độ
                goc_kq = random.choice([-30, -45, -60])

                # Chọn góc beta ngẫu nhiên (góc nhọn dương)
                beta = randint(15, 40)
                # Tính alpha dựa trên góc kết quả: beta + alpha = goc_kq (với alpha âm)
                alpha = goc_kq - beta

                # Tính các góc biến đổi lớn hơn 360 độ hoặc phụ/bù để làm đề bài giống mẫu gốc
                # sin(-337) tương ứng với sin(beta - 360)
                goc_sin1 = beta - 360
                # sin(307) tương ứng với sin(alpha + 360)
                goc_sin2 = alpha + 360
                # sin(113) tương ứng với sin(90 + beta) -> biến đổi thành cos(beta)
                goc_sin3 = 90 + beta

                # Tính toán giá trị chính xác của biểu thức bằng SymPy: sin(goc_kq)
                val_sin = sin(goc_kq * pi / 180)
                da_dung_str = latex(val_sin).replace('.', ',')

                da = '$%s$' % da_dung_str
                du = [da]
                da_chon = random.choice(du)

                # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s_set = set()
                nhiieu_list = [
                    latex(-val_sin).replace('.', ','),
                    '\\frac{1}{2}',
                    '-\\frac{1}{2}',
                    '\\frac{\\sqrt{2}}{2}',
                    '-\\frac{\\sqrt{2}}{2}',
                    '\\frac{\\sqrt{3}}{2}',
                    '-\\frac{\\sqrt{3}}{2}'
                ]

                for item in nhiieu_list:
                    p_an = '$%s$' % item
                    if p_an != da:
                        s_set.add(p_an)

                list_sai = list(s_set)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Tính giá trị biểu thức $M = \\cos (%s^\\circ) \\cdot \\sin (%s^\\circ) + \\sin %s^\\circ \\cdot \\sin %s^\\circ$.'''
                                 % (latex(alpha), latex(goc_sin1), latex(goc_sin2), latex(goc_sin3)))

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Trình bày lời giải chi tiết rõ ràng từng bước như nội dung gốc
                loigiai = ('''$M = \\cos (%s^\\circ) \\cdot \\sin (%s^\\circ) + \\sin %s^\\circ \\cdot \\sin %s^\\circ$ \\\\
            = $\\cos (%s^\\circ) \\cdot \\sin (%s^\\circ - 360^\\circ) + \\sin (%s^\\circ + 360^\\circ) \\cdot \\sin (90^\\circ + %s^\\circ)$ \\\\
            = $\\cos (%s^\\circ) \\cdot \\sin %s^\\circ + \\sin (%s^\\circ) \\cdot \\cos %s^\\circ = \\sin (%s^\\circ + %s^\\circ) = \\sin (%s^\\circ) = %s$.'''
                           % (latex(alpha), latex(goc_sin1), latex(goc_sin2), latex(goc_sin3),
                              latex(alpha), latex(beta), latex(alpha), latex(beta),
                              latex(alpha), latex(beta), latex(alpha), latex(beta), latex(beta), latex(alpha), latex(goc_kq), da_dung_str))

            # Xuất câu trắc nghiệm định dạng minipage TeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

