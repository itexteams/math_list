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


def bt_dang22_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến và chọn dạng
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng thẻ (N) từ 10 đến 15 để tạo biến thể cho bài toán
                N = randint(10, 15)
                k = 3 # Số thẻ lấy ra

                # Tính không gian mẫu n(Omega) = C(N, k) sử dụng hàm binomial của sympy
                omega = binomial(N, k)

                # Để ghép thành số chia hết cho 5, trong 3 thẻ lấy ra phải có ít nhất một thẻ là số 0 hoặc số 5
                # Tập hợp các thẻ không chứa 0 và 5 có N - 2 phần tử
                so_the_con_lai = N - 2
                n_not_A = binomial(so_the_con_lai, k)

                # Số phần tử của biến cố A: n(A) = n(Omega) - n(not A)
                n_A = omega - n_not_A

                # Xác suất P(A) = n(A) / n(Omega)
                phan_so_kq = Rational(n_A, omega)
                da = latex(phan_so_kq)

                # Tạo các phương án sai (nhiễu)
                s = []
                # Nhiễu 1: Tính nhầm n(A) là n(not A)
                s.append('$%s$' % (latex(Rational(n_not_A, omega))))
                # Nhiễu 2: Giả sử chỉ có 1 thẻ đặc biệt (ví dụ chỉ tính số 0)
                n_A_sai = omega - binomial(N - 1, k)
                s.append('$%s$' % (latex(Rational(n_A_sai, omega))))
                # Nhiễu 3: Một phân số ngẫu nhiên khác
                s.append('$%s$' % (latex(Rational(randint(1, 5), 15 if N==10 else N+2))))

                # Đảm bảo các phương án sai không trùng đáp án đúng và không trùng nhau
                da_check = '$%s$' % da
                final_s = []
                for item in s:
                    if item != da_check and item not in final_s:
                        final_s.append(item)

                # Nếu thiếu phương án sai thì bổ sung
                count = 1
                while len(final_s) < 3:
                    fake_val = '$%s$' % (latex(Rational(phan_so_kq.p + count, phan_so_kq.q + count if phan_so_kq.q > 10 else 15)))
                    if fake_val != da_check and fake_val not in final_s:
                        final_s.append(fake_val)
                    count += 1

                das1 = final_s[0]
                das2 = final_s[1]
                das3 = final_s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một hộp đựng $%s$ chiếc thẻ được đánh số từ $0$ đến $%s$. Lấy ngẫu nhiên $%s$ chiếc thẻ, xác suất để $%s$ chữ số trên $%s$ chiếc thẻ được lấy ra có thể ghép thành một số chia hết cho $5$ bằng'''
                                 %(latex(N), latex(N-1), latex(k), latex(k), latex(k)))

                # Các đáp án
                da_d = ('\\True $%s$' % (da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách và trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Không gian mẫu là số cách chọn ngẫu nhiên $%s$ chiếc thẻ từ $%s$ chiếc thẻ. \\\\
                             Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^{%s} = %s$. \\\\
                             Gọi $A$ là biến cố "$%s$ chữ trên $%s$ chiếc thẻ được lấy ra có thể ghép thành một số chia hết cho $5$". \\\\
                             Để cho biến cố $A$ xảy ra thì trong $%s$ thẻ được lấy phải có thẻ mang chữ số $0$ hoặc chữ số $5$. \\\\
                             Ta đi tìm số phần tử của biến cố đối $\\overline{A}$, tức là $%s$ thẻ lấy ra không có thẻ mang chữ số $0$ và cũng không có thẻ mang chữ số $5$. \\\\
                             Số cách chọn $%s$ thẻ từ $%s$ thẻ còn lại (bỏ đi thẻ số $0$ và thẻ số $5$) là $C_{%s}^{%s} = %s$ cách. \\\\
                             Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = C_{%s}^{%s} - C_{%s}^{%s} = %s - %s = %s$. \\\\
                             Vậy xác suất cần tính $P\\left(A\\right) = \\frac{n\\left(A\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{%s} = %s$.'''
                           %(latex(k), latex(N), 
                             latex(N), latex(k), latex(omega),
                             latex(k), latex(k),
                             latex(k),
                             latex(k),
                             latex(k), latex(so_the_con_lai), latex(so_the_con_lai), latex(k), latex(n_not_A),
                             latex(N), latex(k), latex(so_the_con_lai), latex(k), latex(omega), latex(n_not_A), latex(n_A),
                             latex(n_A), latex(omega), da))

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

