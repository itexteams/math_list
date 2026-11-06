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


def bt_dang4_p3_b3_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Randomize the constants A and B for the production function f(x) = (A*x) / (x + B)
                # A: The theoretical maximum output (the limit) - must be a nice integer (e.g., 80, 90, 110, 120)
                A = random.choice([80, 90, 110, 120])
                # B: The experience factor (positive integer)
                B = random.choice([5, 8, 12, 15])

                # The Production Function f(x)
                fx = (A * x) / (x + B)

                # The limit as x approaches infinity
                limit_fx = limit(fx, x, oo) # This is the theoretical limit: A

                # The actual maximum integer product (the correct answer)
                kq_value = limit_fx - 1
                kq = latex(kq_value)

                # Set up the distractors for the multiple-choice question

                du = ['$%s$'%(kq), # Correct answer (A-1)
                      ]
                da = random.choice(du)

                s = ['$%s$'%(latex(limit_fx)), # Distractor: The theoretical limit (A)
                     '$%s$'%(latex(limit_fx+1)), # Distractor: A+1
                     '$%s$'%(latex(limit_fx-2)) if limit_fx > 2 else '$%s$'%(latex(limit_fx+2)), # Distractor: A-2
                     '$%s$'%(latex(limit_fx/2)), # Distractor: A/2
                     '$%s$'%(latex(B)), # Distractor: The factor B
                    ]

                # Select three unique incorrect answers
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Calculate the x value needed to reach the max actual product (for the solution)
                # f(x) = A - 1  => (A*x) / (x + B) = A - 1
                # => A*x = (A-1)*(x + B) = (A-1)*x + (A-1)*B
                # => x = (A-1)*B
                x_for_max = (A-1) * B

                # Câu hỏi
                noidungcauhoi = ('''Một cơ sở sản xuất tính toán rằng số sản phẩm trung bình mà một nhân viên làm được mỗi ngày là $f(x) = \\frac{%s x}{x + %s}$, với $x$ là số ngày kinh nghiệm làm việc $(x \\geq 0)$. Khi số ngày kinh nghiệm làm việc tăng lên thì số sản phẩm trung bình tối đa mà một nhân viên có thể làm được trong một ngày là bao nhiêu?'''
                                  %(latex(A), latex(B)
                                  ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Ta có: $$f(x) = \\frac{%s x}{x + %s} = \\frac{%s (x + %s) - %s \\cdot %s}{x + %s} = %s - \\frac{%s}{x + %s} < %s$$
                         và $$\\lim_{x \\to \\infty} f(x) = \\lim_{x \\to \\infty} \\frac{%s x}{x + %s} = %s$$
                         Vì $f(x)$ luôn nhỏ hơn $%s$ và tiến dần tới $%s$, nên số sản phẩm trung bình tối đa mà một nhân viên có thể làm được trong một ngày là $\\mathbf{%s}$ sản phẩm.\\\\
                         Ta có $f(x) = %s \\Rightarrow \\frac{%s x}{x + %s} = %s \\Rightarrow %s x = %s (x + %s) \\Rightarrow %s x = %s x + %s \\Rightarrow x = %s.$'''
                         # Đã sửa lại thứ tự và thêm đủ các đối số
                         %(latex(A), latex(B), # 1, 2
                           latex(A), latex(B), # 3, 4
                           latex(A), latex(B), # 5, 6
                           latex(B), latex(A), # 7, 8
                           latex(A*B), latex(B), latex(A), # 9, 10, 11
                           latex(A), latex(B), latex(A), # 12, 13, 14
                           latex(A), latex(A), latex(kq_value), # 15, 16, 17
                           latex(kq_value), # 18
                           latex(A), latex(B), latex(kq_value), # 19, 20, 21
                           latex(A), latex(kq_value), latex(B), # 22, 23, 24
                           latex(A), latex(kq_value), latex(A*B - kq_value*B), # 25, 26, 27. Lưu ý: A*B - (A-1)*B = A*B - A*B + B = B. Cần thay đổi biểu thức cuối để dễ hiểu hơn.
                           latex(x_for_max) # 28
                         ))
                         # THAY ĐỔI LẠI CÁC BIỂU THỨC TRONG LỜI GIẢI ĐỂ SỐ LƯỢNG ĐỐI SỐ KHỚP NHAU

                # Nội dung lời giải (Phiên bản đã sửa)
                loigiai=('''Bởi vì $f(x)$ là hàm sản lượng trung bình, ta tìm giới hạn của hàm số khi số ngày kinh nghiệm $x$ tăng vô hạn:\\\\
                         $$\\lim_{x \\to \\infty} f(x) = \\lim_{x \\to \\infty} \\frac{%s x}{x + %s} = \\lim_{x \\to \\infty} \\frac{%s}{1 + \\frac{%s}{x}} = %s.$$
                         Ta cũng có thể biến đổi hàm số: $$f(x) = \\frac{%s x}{x + %s} = \\frac{%s (x + %s) - %s}{x + %s} = %s - \\frac{%s}{x + %s}.$$
                         Vì %s > 0 và $x$ là số dương, nên $f(x)$ luôn nhỏ hơn $%s$ và tiến dần tới $%s$ khi $x \\to \\infty$.
                         Do sản phẩm phải là số nguyên, số sản phẩm trung bình tối đa mà một nhân viên có thể làm được là $\\mathbf{%s}$ sản phẩm (tức là $%s - 1$).\\\\
                         Để đạt được sản lượng tối đa này, số ngày kinh nghiệm cần thiết là:\\\\
                         $f(x) = %s \\Rightarrow \\frac{%s x}{x + %s} = %s \\Rightarrow %s x = %s (x + %s) \\Rightarrow x = %s.$'''
                         %(latex(A), latex(B), latex(A), latex(B), latex(A), # 1-5
                           latex(A), latex(B), latex(A), latex(B), latex(A*B), latex(B), latex(A), latex(A*B), latex(B), # 6-14
                           latex(A*B), latex(A), latex(A), latex(kq_value), latex(A), # 15-19
                           latex(kq_value), latex(A), latex(B), latex(kq_value), latex(A), latex(kq_value), latex(B), latex(x_for_max) # 20-27
                         )) # TỔNG CỘNG 27 ĐỐI SỐ. BẤY GIỜ MỚI ĐỦ.

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content       

