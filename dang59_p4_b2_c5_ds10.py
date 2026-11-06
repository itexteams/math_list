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


def bt_dang59_p4_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng bi mỗi màu, đảm bảo bi trắng > đỏ > xanh > vàng để giữ logic tương tự mẫu
                nw = randint(5, 6)  # Bi trắng
                nr = randint(4, 5)  # Bi đỏ
                nx = randint(3, 4)  # Bi xanh
                nv = randint(2, 3)  # Bi vàng

                total_bi = nw + nr + nx + nv

                # Tính số lượng bi cho mỗi con số
                # Số i xuất hiện nếu màu đó có ít nhất i viên
                max_num = nw
                counts = []
                for i in range(1, max_num + 1):
                    c = 0
                    if nw >= i: c += 1
                    if nr >= i: c += 1
                    if nx >= i: c += 1
                    if nv >= i: c += 1
                    counts.append(c)

                # Tính tổng số cách chọn 3 viên tùy ý
                total_ways = math.comb(total_bi, 3)

                # Tính các trường hợp vi phạm (có ít nhất 2 viên cùng số)
                # 1. Chọn 3 viên cùng số
                same3_steps = []
                sum_same3 = 0
                for i, count in enumerate(counts):
                    if count >= 3:
                        ways = math.comb(count, 3)
                        same3_steps.append('''Chọn $3$ viên bi cùng số $%s$ có $C_{%s}^3 = %s$ cách chọn.''' % (latex(i+1), latex(count), latex(ways)))
                        sum_same3 += ways

                # 2. Chọn 2 viên cùng số và 1 viên khác số
                same2_steps = []
                sum_same2 = 0
                for i, count in enumerate(counts):
                    if count >= 2:
                        ways = math.comb(count, 2) * (total_bi - count)
                        same2_steps.append('''Chọn $2$ viên số $%s$ và $1$ viên khác số $%s$ có $C_{%s}^2 \\cdot C_{%s}^1 = %s$.''' 
                                           % (latex(i+1), latex(i+1), latex(count), latex(total_bi - count), latex(ways)))
                        sum_same2 += ways

                # Kết quả cuối cùng
                kq_val = total_ways - sum_same3 - sum_same2
                kq = latex(kq_val)

                # Các đáp án trắc nghiệm
                da = '$%s$' % (kq)

                s = []
                while len(s) < 3:
                    sai = kq_val + random.choice([-10, -5, 5, 10, 15, 20, -15, -20, 4, 6])
                    sai_str = '$%s$' % (latex(sai))
                    if sai_str != da and sai_str not in s and sai > 0:
                        s.append(sai_str)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một túi có $%s$ viên bi gồm $%s$ viên bi màu trắng được đánh số từ $1$ đến $%s$; $%s$ viên bi màu đỏ được đánh số từ $1$ đến $%s$; $%s$ viên bi màu xanh được đánh số từ $1$ đến $%s$ và $%s$ viên bi màu vàng được đánh số từ $1$ đến $%s$. Tìm số cách chọn $3$ viên bi từng đôi khác số.'''
                                 %(latex(total_bi), latex(nw), latex(nw), latex(nr), latex(nr), latex(nx), latex(nx), latex(nv), latex(nv)
                                 ))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai_same3 = '\\\\ \n'.join(same3_steps)
                loigiai_same2 = '\\\\ \n'.join(same2_steps)

                # Tạo chuỗi phép trừ cho dòng cuối
                tru_same3 = ' - '.join([str(math.comb(c, 3)) for c in counts if c >= 3])
                tru_same2 = ' - '.join([str(math.comb(c, 2) * (total_bi - c)) for c in counts if c >= 2])

                loigiai = ('''Có $C_{%s}^3$ cách chọn $3$ viên bi tùy ý. \\\\
            %s \\\\
            %s \\\\
            Như vậy số cách chọn theo yêu cầu là $C_{%s}^3 - %s - %s = %s$.'''
                           %(latex(total_bi), loigiai_same3, loigiai_same2, latex(total_bi), tru_same3, tru_same2, latex(kq_val)
                           ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

