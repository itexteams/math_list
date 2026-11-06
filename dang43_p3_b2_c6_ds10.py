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


def bt_dang43_p3_b2_c6_ds10(self):
            #Khai báo biến
            # B2 & B3 - Viết lại và tìm cách random bài toán
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # n là tổng số phiếu, k là số phiếu trúng, m là vị trí người lấy
                n = randint(10, 20)
                k = randint(2, 5)
                m = randint(2, n-1)

                # Tính xác suất đúng
                prob = Rational(k, n)
                da = '$%s$'%(latex(prob))

                # B4-Điều chỉnh các phương án sai không được trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    # Tạo các phân số khác nhau có mẫu là n
                    sai_num = randint(1, n-1)
                    if sai_num != k:
                        phuong_an_sai = Rational(sai_num, n)
                        s_latex = '$%s$'%(latex(phuong_an_sai))
                        if s_latex != da:
                            s.add(s_latex)

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('Một hộp có $%s$ phiếu, trong đó có $%s$ phiếu trúng thưởng. Có $%s$ người lần lượt lấy ngẫu nhiên mỗi người một phiếu. Xác suất người thứ $%s$ lấy được phiếu trúng thưởng bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'
                                 %(latex(n), latex(k), latex(n), latex(m)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                h1=prob
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')
                # Nội dung lời giải chi tiết theo mẫu ảnh
                # n(Omega) = n!
                # n(A) = C(k,1) * (n-1)!
                loigiai = ('''Không gian mẫu là mỗi người lấy ngẫu nhiên một phiếu. Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = %s!$.\\\\
            Gồm $A$ là biến cố "người thứ %s lấy được phiếu trúng thưởng". Ta mô tả khả năng thuận lợi của biến cố $A$ như sau:\\\\
            Người thứ %s có $C_{%s}^{1} = %s$ khả năng lấy được phiếu trúng thưởng.\\\\
            $%s$ người còn lại có số cách lấy phiếu là $%s!$.\\\\
            Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = %s \\cdot %s!$.\\\\
            Vậy xác suất cần tính là $P\\left(A\\right) = \\frac{%s \\cdot %s!}{%s!} = %s \\approx %s$.'''
                           %(latex(n), latex(m), 
                             latex(m), latex(k), latex(k),
                             latex(n-1), latex(n-1),
                             latex(k), latex(n-1),
                             latex(k), latex(n-1), latex(n), latex(prob),kqz
                            ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            # Xuất câu trắc nghiệm - Không dùng raw string, dùng double backslash
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

