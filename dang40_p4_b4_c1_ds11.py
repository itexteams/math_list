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


def bt_dang40_p4_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số độ beta trong cụm (2x - beta) của đề bài
                # Bài mẫu: beta = 15
                beta = random.choice([15, 30, 45])

                # Biến đổi phương trình: tan(2x - beta) = 1 <=> 2x - beta = 45 + k*180
                # => 2x = (45 + beta) + k*180 <=> x = alpha_base + k*90
                alpha_base = Rational(45 + beta, 2)

                # Chặn nghiệm x trong khoảng (-90; 90) để tìm các giá trị k nguyên
                # -90 < alpha_base + k*90 < 90 <=> (-90 - alpha_base)/90 < k < (90 - alpha_base)/90
                k_min_val = Rational(-90 - alpha_base, 90)
                k_max_val = Rational(90 - alpha_base, 90)

                # Lấy các giá trị k nguyên nằm trong khoảng
                list_k = []
                # Quét k trong khoảng thực tế an toàn từ -5 đến 5
                for k_test in range(-5, 6):
                    if k_min_val < k_test < k_max_val:
                        list_k.append(k_test)

                # Sắp xếp k giảm dần hoặc giữ nguyên theo cấu trúc bài toán gốc
                list_k = sorted(list_k, reverse=True)

                # Tính các nghiệm x tương ứng và tổng các nghiệm
                list_x = [alpha_base + k*90 for k in list_k]
                tong_nghiem = sum(list_x)

                kq = '%s^\\circ' % latex(tong_nghiem)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai không trùng đáp án đúng
                s = []
                for sai_val in [0, 30, -30, -60, 45, -45, 60, 90]:
                    sai_str = '$%s^\\circ$' % latex(sai_val)
                    if sai_str != da:
                        s.append(sai_str)

                s = list(set(s))
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Tính tổng các nghiệm của phương trình $\\tan \\left( 2x-%s^\\circ \\right)=1$ trên khoảng $\\left( -90^\\circ;90^\\circ \\right)$.'''
                                 % (latex(beta)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tạo chuỗi hệ ngoặc vuông liệt kê các giá trị k ứng với x cho lời giải
                str_he_k = '\\left[ \\begin{aligned} '
                for k_val in list_k:
                    x_val = alpha_base + k_val*90
                    str_he_k += '& k = %s \\rightarrow x = %s^\\circ \\\\ ' % (latex(k_val), latex(x_val))
                str_he_k += '\\end{aligned} \\right.'

                # Tạo chuỗi phép cộng tổng các nghiệm thỏa mãn
                str_phep_cong = ' + '.join(['%s^\\circ' % latex(x_val) for x_val in reversed(list_x)])
                # Thay thế dấu '+ -' thành '-' nếu có nghiệm âm để biểu thức toán chuẩn đẹp
                str_phep_cong = str_phep_cong.replace('+ -', '- ')

                # Lời giải chi tiết bám sát tuyệt đối từng bước như ảnh mẫu
                loigiai = ('''Ta có $\\tan \\left( 2x-%s^\\circ \\right)=1 \\Leftrightarrow 2x-%s^\\circ=45^\\circ+k180^\\circ \\Leftrightarrow x=%s^\\circ+k90^\\circ\\,\\left( k\\in \\mathbb{Z} \\right)$. \\\\
                           Do $x\\in \\left( -90^\\circ;90^\\circ \\right) \\rightarrow -90^\\circ <%s^\\circ+k90^\\circ <90^\\circ \\Leftrightarrow %s < k < %s$. \\\\
                           $\\xrightarrow{k\\in \\mathbb{Z}} %s \\rightarrow %s = %s^\\circ$.'''
                           % (latex(beta), latex(beta), latex(alpha_base), latex(alpha_base),
                              latex(k_min_val), latex(k_max_val), str_he_k, str_phep_cong, latex(tong_nghiem)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

