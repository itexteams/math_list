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


def bt_dang32_p1_b2_c1_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Hàm biểu diễn vectơ theo các vectơ đơn vị i, j, k
        def format_vector(vx, vy, vz):
            terms = []
            # Hệ số i
            if vx == 1:
                terms.append('\\vec{i}')
            elif vx == -1:
                terms.append('-\\vec{i}')
            elif vx != 0:
                terms.append('%s\\vec{i}' % vx)
    
            # Hệ số j
            if vy == 1:
                if len(terms) > 0:
                    terms.append('+ \\vec{j}')
                else:
                    terms.append('\\vec{j}')
            elif vy == -1:
                if len(terms) > 0:
                    terms.append('- \\vec{j}')
                else:
                    terms.append('-\\vec{j}')
            elif vy > 0:
                if len(terms) > 0:
                    terms.append('+ %s\\vec{j}' % vy)
                else:
                    terms.append('%s\\vec{j}' % vy)
            elif vy < 0:
                if len(terms) > 0:
                    terms.append('- %s\\vec{j}' % (-vy))
                else:
                    terms.append('-%s\\vec{j}' % (-vy))
    
            # Hệ số k
            if vz == 1:
                if len(terms) > 0:
                    terms.append('+ \\vec{k}')
                else:
                    terms.append('\\vec{k}')
            elif vz == -1:
                if len(terms) > 0:
                    terms.append('- \\vec{k}')
                else:
                    terms.append('-\\vec{k}')
            elif vz > 0:
                if len(terms) > 0:
                    terms.append('+ %s\\vec{k}' % vz)
                else:
                    terms.append('%s\\vec{k}' % vz)
            elif vz < 0:
                if len(terms) > 0:
                    terms.append('- %s\\vec{k}' % (-vz))
                else:
                    terms.append('-%s\\vec{k}' % (-vz))
    
            if len(terms) == 0:
                return '\\vec{0}'
            return ' '.join(terms)
    
        # Random tọa độ điểm M, N sao cho trung điểm I có tọa độ nguyên và không triệt tiêu hết
        while True:
            xM = random.randint(-5, 5)
            yM = random.randint(-5, 5)
            zM = random.randint(-5, 5)
    
            xN = random.randint(-5, 5)
            yN = random.randint(-5, 5)
            zN = random.randint(-5, 5)
    
            # Điều kiện tổng cùng tính chẵn lẻ để trung điểm I có tọa độ nguyên
            if (xM + xN) % 2 == 0 and (yM + yN) % 2 == 0 and (zM + zN) % 2 == 0:
                xI = (xM + xN) // 2
                yI = (yM + yN) // 2
                zI = (zM + zN) // 2
                # Tránh trường hợp trùng điểm hoặc trung điểm là gốc tọa độ
                if (xM, yM, zM) != (xN, yN, zN) and (xI, yI, zI) != (0, 0, 0):
                    break
    
        # Vectơ tổng M + N (lỗi học sinh quên chia 2)
        x_sum = xM + xN
        y_sum = yM + yN
        z_sum = zM + zN
    
        # Đáp án đúng: OI = xI*i + yI*j + zI*k
        da = '$\\vec{OI} = %s$' % format_vector(xI, yI, zI)
    
        # Các đáp án nhiễu theo các lỗi sai phổ biến
        candidates = [
            format_vector(x_sum, y_sum, zI),
            format_vector(xI, yI, z_sum),
            format_vector(x_sum, y_sum, z_sum),
            format_vector(xI, -yI, zI),
            format_vector(xI, yI, -zI),
            format_vector(-xI, yI, zI),
            format_vector(xN - xM, yN - yM, zN - zM)
        ]
    
        s = []
        for cand in candidates:
            ans_str = '$\\vec{OI} = %s$' % cand
            if ans_str != da and ans_str not in s:
                s.append(ans_str)
    
        # Bổ sung đáp án sai nếu danh sách chưa đủ 3 phần tử
        offset = 1
        while len(s) < 3:
            cand_alt = format_vector(xI + offset, yI, zI)
            ans_str = '$\\vec{OI} = %s$' % cand_alt
            if ans_str != da and ans_str not in s:
                s.append(ans_str)
            offset += 1
    
        random.shuffle(s)
        das1 = s.pop()
        das2 = s.pop()
        das3 = s.pop()
    
        # Định dạng dấu số cho phép cộng trong lời giải
        sign_xN = '+ (%s)' % xN if xN < 0 else '+ %s' % xN
        sign_yN = '+ (%s)' % yN if yN < 0 else '+ %s' % yN
        sign_zN = '+ (%s)' % zN if zN < 0 else '+ %s' % zN
    
        bieu_thuc_oi = format_vector(xI, yI, zI)
    
        # Câu hỏi[cite: 5]
        noidungcauhoi = ('''Trong không gian với hệ tọa độ $Oxyz$, cho các điểm $M(%s;%s;%s)$, $N(%s;%s;%s)$ và điểm $I$ là trung điểm của $MN$. Mệnh đề nào sau đây đúng?'''
                         % (xM, yM, zM, xN, yN, zN)
                         )
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải chi tiết[cite: 5]
        loigiai = ('''Vì $I$ là trung điểm của đoạn thẳng $MN$ nên tọa độ của điểm $I$ thỏa mãn:\\\\
    $\\begin{cases} x_I = \\dfrac{x_M + x_N}{2} = \\dfrac{%s %s}{2} = %s \\\\ y_I = \\dfrac{y_M + y_N}{2} = \\dfrac{%s %s}{2} = %s \\\\ z_I = \\dfrac{z_M + z_N}{2} = \\dfrac{%s %s}{2} = %s \\end{cases} \\Rightarrow I(%s;%s;%s)$.\\\\
    Do đó $\\vec{OI} = %s$.'''
                   % (xM, sign_xN, xI, yM, sign_yN, yI, zM, sign_zN, zI, xI, yI, zI, bieu_thuc_oi)
                   )
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
    