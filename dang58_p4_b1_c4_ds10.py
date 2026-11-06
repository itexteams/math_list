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


def bt_dang58_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến loại câu hỏi
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các tham số ngẫu nhiên
                # Để đảm bảo x-2 và x-1 giống mẫu, ta chọn a là số chẵn, b = a/2
                a = randint(2, 5) * 2  # a sẽ là 4, 6, 8, 10...
                b = a // 2            # b sẽ là 2, 3, 4, 5...
                k = randint(2, 5)     # Hệ số k đứng trước trị tuyệt đối thứ 2

                # Giá trị lớn nhất (kq) theo logic bài toán là y(b) = (a-b) - k|b-b| = a-b
                kq_val = a - b
                kq = latex(kq_val)

                # Tạo các phương án sai (đảm bảo không trùng đáp án đúng)
                s = []
                candidates = [kq_val + 1, kq_val + 2, kq_val - 1, kq_val - 2, 0, a, b]
                for c in candidates:
                    if c != kq_val and c not in s:
                        s.append(c)

                random.shuffle(s)
                das1 = '$%s$' % latex(s[0])
                das2 = '$%s$' % latex(s[1])
                das3 = '$%s$' % latex(s[2])

                # Đáp án đúng
                da = '$%s$' % kq

                # Nội dung câu hỏi
                # y = |x - a| - k|x - b| trên đoạn [0; a]
                noidungcauhoi = ('''Tìm giá trị lớn nhất của hàm số $y=|x-%s|-%s|x-%s|$ trên đoạn $[0;%s]$.'''
                                 %(latex(a), latex(k), latex(b), latex(a)))

                # Các đáp án trắc nghiệm
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (viết y hệt logic trong ảnh)
                # k_minus_1 dùng cho phần tách -2|x-1| trong ảnh (ở đây là -(k-1)|x-b|)
                k_m_1 = k - 1
                loigiai = ('''Có $x \\in [0;%s] \\Rightarrow |x-%s|=%s-x \\Rightarrow y=%s-x-%s|x-%s|=%s+(%s-x)-|x-%s|-%s|x-%s|$. \\\\
                             Do $|x-%s| \\ge 0 \\Rightarrow -%s|x-%s| \\le 0$ và $(%s-x)-|x-%s| \\le 0$ nên $y \\le %s$. \\\\
                             Dấu "$=$" xảy ra khi $\\begin{cases} |x-%s|=0 \\\\ %s-x=|x-%s| \\end{cases} \\Leftrightarrow x=%s$. \\\\
                             Vậy giá trị lớn nhất của hàm số $y=|x-%s|-%s|x-%s|$ trên đoạn $[0;%s]$ là $%s$.'''
                           %(latex(a), latex(a), latex(a), latex(a), latex(k), latex(b), latex(kq_val), latex(b), latex(b), latex(k_m_1), latex(b),
                             latex(b), latex(k_m_1), latex(b), latex(b), latex(b), latex(kq_val),
                             latex(b), latex(b), latex(b), latex(b),
                             latex(a), latex(k), latex(b), latex(a), latex(kq_val)
                            ))

            # Xuất câu trắc nghiệm theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

