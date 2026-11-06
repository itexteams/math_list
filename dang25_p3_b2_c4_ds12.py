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


def bt_dang25_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến loại câu hỏi
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random dữ liệu cho bài toán
                # Hộp I: w1 bi trắng, r1 bi đỏ
                w1 = randint(4, 6)
                r1 = randint(7, 9)
                total1 = w1 + r1

                # Hộp II: w2 bi trắng, r2 bi đỏ
                w2 = randint(10, 15)
                r2 = randint(15, 20)
                total2_init = w2 + r2
                total2_after = total2_init + 2 # Sau khi chuyển 2 bi từ hộp I sang

                # Bước 2: Tính toán xác suất theo công thức Bayes
                # Các biến cố H1, H2, H3 (Hộp I sang II)
                mau_h = binomial(total1, 2)
                p_h1 = Rational(binomial(w1, 2), mau_h) # 2 trắng
                p_h2 = Rational(binomial(r1, 2), mau_h) # 2 đỏ
                p_h3 = Rational(w1 * r1, mau_h)         # 1 trắng, 1 đỏ

                # Xác suất lấy được bi trắng từ hộp II (Biến cố A)
                p_a_h1 = Rational(w2 + 2, total2_after)
                p_a_h2 = Rational(w2, total2_after)
                p_a_h3 = Rational(w2 + 1, total2_after)

                # Xác suất đầy đủ P(A)
                p_a = p_h1 * p_a_h1 + p_h2 * p_a_h2 + p_h3 * p_a_h3

                # Xác suất Bayes P(H3|A) = a/b
                p_h3_a = (p_h3 * p_a_h3) / p_a

                a = p_h3_a.p # Tử số của phân số tối giản
                b = p_h3_a.q # Mẫu số của phân số tối giản

                # Đáp án đúng
                kq = a + b

                # Các đáp án trắc nghiệm sai (đảm bảo không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    sai = kq + randint(-5, 5)
                    if sai != kq and sai > 0:
                        s.add(sai)

                list_sai = list(s)
                das1 = '$%s$' % (latex(list_sai[0]))
                das2 = '$%s$' % (latex(list_sai[1]))
                das3 = '$%s$' % (latex(list_sai[2]))

                da = '$%s$' % (latex(kq))

                # Câu hỏi
                noidungcauhoi = ('''Có hai hộp bi, hộp I có $%s$ bi trắng và $%s$ bi đỏ, hộp II có $%s$ bi trắng và $%s$ bi đỏ. Lấy ngẫu nhiên hai viên bi từ hộp I chuyển sang hộp II. Sau đó, từ hộp II lấy ngẫu nhiên 1 viên bi thì được bi trắng. Xác suất để 2 bi chuyển từ hộp I sang hộp II không cùng màu là $\\frac{a}{b}$ (là phân số tối giản). Tổng $a+b$ bằng bao nhiêu?'''
                                 %(latex(w1), latex(r1), latex(w2), latex(r2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai=('''Gọi $H_1$ là biến cố: Hai viên bi chuyển từ hộp I sang hộp II là bi trắng. \\\\
                            $H_2$ là biến cố: Hai viên bi chuyển từ hộp I sang hộp II là bi đỏ. \\\\
                            $H_3$ là biến cố: Hai viên bi chuyển từ hộp I sang hộp II có 1 bi trắng và 1 bi đỏ. \\\\
                            Ba biến cố $H_1, H_2, H_3$ tạo thành một hệ đầy đủ. \\\\
                            Ta có: $P(H_1) = \\frac{C_{%s}^2}{C_{%s}^2} = %s$; $P(H_2) = \\frac{C_{%s}^2}{C_{%s}^2} = %s$; $P(H_3) = \\frac{C_{%s}^1C_{%s}^1}{C_{%s}^2} = %s$. \\\\
                            Gọi $A$ là biến cố: Viên bi lấy ra từ hộp II là bi trắng. \\\\
                            Số bi ở hộp II sau khi nhận thêm 2 bi là $%s + 2 = %s$. \\\\
                            Ta có: $P(A|H_1) = \\frac{%s+2}{%s} = %s$; $P(A|H_2) = \\frac{%s}{%s} = %s$; $P(A|H_3) = \\frac{%s+1}{%s} = %s$. \\\\
                            Cần tính xác suất $P(H_3|A)$. Theo công thức xác suất Bayes: \\\\
                            $P(H_3|A) = \\frac{P(H_3).P(A|H_3)}{P(H_1).P(A|H_1) + P(H_2).P(A|H_2) + P(H_3).P(A|H_3)}$ \\\\
                            Thay số: $P(H_3|A) = %s = \\frac{%s}{%s} \\Rightarrow a+b = %s$.'''
                         %(latex(w1), latex(total1), latex(p_h1),
                           latex(r1), latex(total1), latex(p_h2),
                           latex(w1), latex(r1), latex(total1), latex(p_h3),
                           latex(total2_init), latex(total2_after),
                           latex(w2), latex(total2_after), latex(p_a_h1),
                           latex(w2), latex(total2_after), latex(p_a_h2),
                           latex(w2), latex(total2_after), latex(p_a_h3),
                           latex(p_h3_a), latex(a), latex(b), latex(kq)
                          ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

