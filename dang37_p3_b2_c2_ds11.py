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


def bt_dang37_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số hạng đầu b1 của CSC thứ hai, suy ra a1 sao cho a1 - b1 = 2
                b1 = random.randint(2, 8)
                a1 = b1 + 2
                N = random.choice([80, 90, 100, 110, 120, 150])

                # 3 số hạng đầu tiên của mỗi cấp số cộng
                ap1_t1 = a1
                ap1_t2 = a1 + 3
                ap1_t3 = a1 + 6

                ap2_t1 = b1
                ap2_t2 = b1 + 4
                ap2_t3 = b1 + 8

                # Biến đổi u_n và v_m
                c1 = a1 - 3
                c2 = b1 - 4

                if c1 > 0:
                    str_un = '%s + 3n' % latex(c1)
                elif c1 < 0:
                    str_un = '-%s + 3n' % latex(abs(c1))
                else:
                    str_un = '3n'

                if c2 > 0:
                    str_vm = '%s + 4m' % latex(c2)
                elif c2 < 0:
                    str_vm = '-%s + 4m' % latex(abs(c2))
                else:
                    str_vm = '4m'

                # Tính các giới hạn cho t
                t1 = N // 3
                t2 = (N + 1) // 4
                t_max = min(t1, t2)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % latex(t_max)]
                da = random.choice(du)

                # Sinh các phương án sai không trùng nhau và không trùng đáp án đúng
                s_set = set()
                for delta in [1, 2, 3, -1, -2, -3, 4, -4, 5]:
                    w = t_max + delta
                    if w > 0 and w != t_max:
                        s_set.add('$%s$' % latex(w))
                if t1 != t_max:
                    s_set.add('$%s$' % latex(t1))

                s = list(s_set)
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Nội dung câu hỏi
                noidungcauhoi = (
                    '''Cho hai cấp số cộng có dãy số hạng lần lượt là: $%s; %s; %s; \\dots$ và $%s; %s; %s; \\dots$. Hỏi trong $%s$ số hạng đầu tiên của mỗi cấp số, có bao nhiêu số hạng chung?'''
                    % (
                        latex(ap1_t1),
                        latex(ap1_t2),
                        latex(ap1_t3),
                        latex(ap2_t1),
                        latex(ap2_t2),
                        latex(ap2_t3),
                        latex(N),
                    )
                )

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (
                    '''Giả sử $u_n, v_m$ theo thứ tự là số hạng thứ $n$ và $m$ của mỗi cấp số cộng, ta có:\\\\
            $u_n = %s + 3(n-1); v_m = %s + 4(m-1)$. Ta có:\\\\
            $u_n = v_m \\Leftrightarrow %s + 3(n-1) = %s + 4(m-1) \\Leftrightarrow %s = %s \\Leftrightarrow n = \\frac{4m}{3} - 1$.\\\\
            Đặt $t = \\frac{m}{3}$, vì $n \\in \\mathbb{N}^* \\Rightarrow t \\in \\mathbb{N}^*$. Ta có: $\\begin{cases} m = 3t \\le %s \\\\ n = 4t - 1 \\le %s \\end{cases} \\Rightarrow \\begin{cases} t \\le %s \\\\ t \\le %s \\end{cases}$.\\\\
            Suy ra $t \\in \\{1; 2; 3; \\dots; %s\\}$. Với mỗi giá trị của $t$, ta có một số hạng chung thuộc về hai dãy $(u_n), (v_m)$. Vậy có tất cả %s số hạng chung của hai dãy số đã cho trong %s số hạng đầu tiên.'''
                    % (
                        latex(a1),
                        latex(b1),
                        latex(a1),
                        latex(b1),
                        str_un,
                        str_vm,
                        latex(N),
                        latex(N),
                        latex(t1),
                        latex(t2),
                        latex(t_max),
                        latex(t_max),
                        latex(N),
                    )
                )
            dapan='\\shortans[0]{$%s$}\n'%(latex(N))
            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

