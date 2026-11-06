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


def bt_dang23_p1_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số liệu: 
                # a: số người bị bệnh và dương tính
                # b: số người bị bệnh và âm tính
                # c: số người không bệnh và dương tính
                # d: số người không bệnh và âm tính

                a = random.randint(100, 200)
                b = random.randint(20, 50)
                c = random.randint(30, 60)
                d = random.randint(800, 1000)

                # Tính toán xác suất
                # P(B) = (a + c) / tổng
                # P(A giao B) = a / tổng
                # P(A|B) = a / (a + c)

                tu_so = a
                mau_so = a + c
                xac_suat = float(tu_so) / mau_so
                kq_percent = round(xac_suat * 100, 2)

                # Định dạng kết quả hiển thị (thay dấu chấm bằng dấu phẩy theo chuẩn VN nếu cần)
                kq_str = str(kq_percent).replace('.', ',')

                # Đáp án đúng
                da = '$%s$' % kq_str
                da_d = ('\\True ' + str(da))

                # Tạo các đáp án sai (nhiễu)
                s = []
                while len(s) < 3:
                    nhieu = round(kq_percent + random.choice([-5.5, -10.2, 4.3, 8.7, 12.1, -3.4]), 2)
                    if nhieu > 0 and nhieu != kq_percent:
                        val = '$%s$' % (str(nhieu).replace('.', ','))
                        if val not in s:
                            s.append(val)

                da_s1, da_s2, da_s3 = s[0], s[1], s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho bảng dữ liệu sau về kết quả xét nghiệm một loại bệnh:
            \\begin{center}
            \\begin{tabular}{|c|c|c|}
            \\hline
             & Dương tính & Âm tính \\\\
            \\hline
            Bệnh & $%s$ & $%s$ \\\\
            \\hline
            Không bệnh & $%s$ & $%s$ \\\\
            \\hline
            \\end{tabular}
            \\end{center}
            Nếu một người có kết quả xét nghiệm dương tính, xác suất người đó thực sự bị bệnh là:'''
                                 %(latex(a), latex(b), latex(c), latex(d)))

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $A$ là biến cố người thực sự bị bệnh. $B$ là biến cố người đó có kết quả xét nghiệm dương tính. \\\\
                             Theo bảng số liệu, ta có: \\\\
                             Số người có kết quả xét nghiệm dương tính là: $%s + %s = %s$. \\\\
                             Trong đó, số người thực sự bị bệnh và có kết quả dương tính là: $%s$. \\\\
                             Nếu một người có kết quả xét nghiệm dương tính, xác suất người đó thực sự bị bệnh là: \\\\
                             $$P(A|B) = \\frac{P(AB)}{P(B)} = \\frac{%s}{%s + %s} = \\frac{%s}{%s} \\approx %s.$$'''
                           %(latex(a), latex(c), latex(a+c), 
                             latex(a), 
                             latex(a), latex(a), latex(c), latex(a), latex(a+c), str(kq_str)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

