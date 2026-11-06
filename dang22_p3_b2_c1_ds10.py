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


def bt_dang22_p3_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Sinh ngẫu nhiên số lượng học sinh ở các phần giao nhau rời rạc trước để đảm bảo bài toán luôn có nghĩa
                x_HMN = randint(3, 6)   # Cả 3 tiết mục
                x_HM = randint(2, 6)    # Chỉ hát và múa
                x_HN = randint(2, 6)    # Chỉ hát và nhảy
                x_MN = randint(6, 12)   # Chỉ múa và nhảy
                x_H = randint(2, 8)     # Chỉ hát
                x_M = randint(4, 12)    # Chỉ múa
                x_N = randint(5, 15)    # Chỉ nhảy

                # Tính toán tổng số lượng theo từng điều kiện của đề bài
                c_H = x_H + x_HM + x_HN + x_HMN    # Tham gia hát
                c_M = x_M + x_HM + x_MN + x_HMN    # Tham gia múa
                c_N = x_N + x_HN + x_MN + x_HMN    # Tham gia nhảy

                c_HM = x_HM + x_HMN   # Tham gia hát và múa
                c_HN = x_HN + x_HMN   # Tham gia hát và nhảy
                c_MN = x_MN + x_HMN   # Tham gia múa và nhảy

                c_HMN = x_HMN         # Tham gia cả 3

                # Kết quả đúng theo công thức bao hàm - loại trừ
                kq = c_H + c_M + c_N - (c_HM + c_HN + c_MN) + c_HMN

                da = '$%s$' % latex(kq)

                # Tạo các phương án sai không trùng với đáp án đúng
                s = []
                for diff in [4, 6, 8, -4, -6, -8]:
                    wrong_ans = kq + diff
                    if wrong_ans > 0 and wrong_ans != kq:
                        s.append('$%s$' % latex(wrong_ans))

                s = list(set(s))  # Đảm bảo các phương án sai là duy nhất
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Để chuẩn bị cho đêm văn nghệ, trường THPT Lý Tự Trọng đã chọn các em học sinh có năng khiếu về múa, hát, nhảy để tham gia văn nghệ. Nhà trường đã chọn được $%s$ học sinh tham gia hát, $%s$ học sinh tham gia múa, $%s$ học sinh tham gia nhảy. Trong đó có $%s$ học sinh tham gia hát và múa, $%s$ học sinh tham gia hát và nhảy, $%s$ học sinh tham gia múa và nhảy và $%s$ học sinh tham gia cả 3 tiết mục múa, hát, nhảy. Số học sinh được chọn tham gia trong đêm văn nghệ bằng bao nhiêu?'''
                                 %(latex(c_H), latex(c_M), latex(c_N), latex(c_HM), latex(c_HN), latex(c_MN), latex(c_HMN)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $H, M, N$ lần lượt là tập hợp các học sinh tham gia hát, múa và nhảy. \\\\
                             Theo giả thiết bài ra, ta có: \\\\
                             $|H| = %s$, $|M| = %s$, $|N| = %s$. \\\\
                             $|H \\cap M| = %s$, $|H \\cap N| = %s$, $|M \\cap N| = %s$. \\\\
                             $|H \\cap M \\cap N| = %s$. \\\\
                             Số học sinh tham gia trong đêm văn nghệ chính là số phần tử của tập hợp $H \\cup M \\cup N$. \\\\
                             Áp dụng công thức bao hàm - loại trừ cho ba tập hợp, ta có: \\\\
                             $|H \\cup M \\cup N| = |H| + |M| + |N| - (|H \\cap M| + |H \\cap N| + |M \\cap N|) + |H \\cap M \\cap N|$ \\\\
                             $= %s + %s + %s - (%s + %s + %s) + %s = %s$. \\\\
                             Vậy nhà trường đã chọn được $%s$ học sinh tham gia trong đêm văn nghệ.'''
                           %(latex(c_H), latex(c_M), latex(c_N),
                             latex(c_HM), latex(c_HN), latex(c_MN),
                             latex(c_HMN),
                             latex(c_H), latex(c_M), latex(c_N), latex(c_HM), latex(c_HN), latex(c_MN), latex(c_HMN), latex(kq),
                             latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

