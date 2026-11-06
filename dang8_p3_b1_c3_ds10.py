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


def bt_dang8_p3_b1_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                while True:
                    # Random chiều dài cầu a (từ 500m đến 2000m)
                    a = random.randint(500, 2000)

                    # Random độ chính xác d
                    d = random.choice([0.1, 0.2, 0.4, 0.5, 0.8, 1.0])

                    # Tính sai số tương đối (%)
                    rel_error = (d / a) * 100

                    # Làm tròn kết quả đúng (2 chữ số thập phân, tự động bỏ số 0 vô nghĩa)
                    kq_dec = Decimal(str(round(rel_error, 5))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP).normalize()

                    # Đảm bảo kết quả dương và không bị làm tròn thành 0.00
                    if kq_dec > Decimal('0.00'):
                        break

                def to_str_vi(val):
                    # Hàm định dạng số: loại bỏ số 0 thừa ở đuôi và đổi dấu chấm thành phẩy
                    s = f"{float(val):.5f}".rstrip('0').rstrip('.')
                    if s == '': 
                        s = '0'
                    return s.replace('.', ',')

                kq = to_str_vi(kq_dec)

                # Các phương án nhiễu bám sát logic của ảnh (gấp 10 lần, gấp 5 lần, bằng một nửa)
                dist1_val = kq_dec * Decimal('10')
                dist2_val = kq_dec * Decimal('5')
                dist3_val = kq_dec * Decimal('0.5')

                options_list = [to_str_vi(dist1_val), to_str_vi(dist2_val), to_str_vi(dist3_val)]

                # Format các giá trị đầu vào
                a_str = to_str_vi(a)
                d_str = to_str_vi(d)

                # Câu hỏi
                noidungcauhoi = ('''Độ dài của một cây cầu người ta đo được là $%sm \\pm %sm$ . Sai số tương đối tối đa trong phép đo bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                 % (a_str, d_str))

                # Các đáp án
                da_d = ('\\True $%s\\%%$' % (kq))
                da_s1 = ('$%s\\%%$' % (options_list[0]))
                da_s2 = ('$%s\\%%$' % (options_list[1])) 
                da_s3 = ('$%s\\%%$' % (options_list[2])) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Ta có độ dài gần đúng của cầu là $a = %s$ với độ chính xác $d = %s$.\\\\
            Vì sai số tuyệt đối $\\Delta_a \\le d = %s$ nên sai số tương đối $\\delta_a = \\frac{\\Delta_a}{|a|} \\le \\frac{d}{|a|} = \\frac{%s}{%s} \\approx %s\\%%$.\\\\
            Vậy sai số tương đối tối đa trong phép đo trên là $%s\\%%$.'''
                         % (a_str, d_str, d_str, d_str, a_str, kq, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

