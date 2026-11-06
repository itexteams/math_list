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


def bt_dang23_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random các thông số (đảm bảo tính hợp lý của đề bài)
                # Tổng số thẻ n (thường là số chẵn)
                n_total = random.choice([20, 30]) 
                # Số thẻ chọn ra k
                n_pick = 8
                # Số thẻ lẻ x và số thẻ chẵn y (x + y = k)
                n_odd_pick = 3
                n_even_pick = 5
                # Số thẻ chia hết cho 10 trong nhóm thẻ chẵn
                n_div_10_pick = 1

                # Bước 2: Tính toán các giá trị thành phần
                n_odd_total = n_total // 2
                n_even_total = n_total // 2
                n_div_10_total = n_total // 10
                n_even_not_div_10 = n_even_total - n_div_10_total

                # Không gian mẫu
                n_omega = binomial(n_total, n_pick)

                # Số cách chọn thỏa mãn biến cố A
                # 1. Chọn n_odd_pick thẻ lẻ từ n_odd_total thẻ lẻ
                ways_odd = binomial(n_odd_total, n_odd_pick)
                # 2. Chọn n_div_10_pick thẻ chia hết cho 10 từ n_div_10_total thẻ
                ways_div_10 = binomial(n_div_10_total, n_div_10_pick)
                # 3. Chọn số thẻ chẵn còn lại từ nhóm thẻ chẵn không chia hết cho 10
                ways_even_remain = binomial(n_even_not_div_10, n_even_pick - n_div_10_pick)

                n_a = ways_odd * ways_div_10 * ways_even_remain
                prob = Rational(n_a, n_omega)

                # Đáp án đúng
                da = "$%s$" % (latex(prob))

                # Tạo các đáp án nhiễu (đảm bảo không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Tạo ngẫu nhiên bằng cách thay đổi tử số hoặc mẫu số một chút
                    sai_tu = n_a + random.randint(-50, 50)
                    if sai_tu <= 0 or sai_tu == n_a: continue
                    sai_prob = Rational(sai_tu, n_omega)
                    if sai_prob != prob:
                        s.add("$%s$" % (latex(sai_prob)))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Có $%s$ tấm thẻ được đánh số từ $1$ đến $%s$. Chọn ngẫu nhiên ra $%s$ tấm thẻ, xác suất để có $%s$ thẻ mang tấm số lẻ, $%s$ thẻ mang tấm số chẵn trong đó chỉ có đúng $%s$ tấm thẻ mang số chia hết cho $10$ bằng'''
                                 % (latex(n_total), latex(n_total), latex(n_pick), latex(n_odd_pick), latex(n_even_pick), latex(n_div_10_pick)))

                # Các đáp án
                da_d = ("\\True " + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Không gian mẫu là cách chọn $%s$ tấm thẻ trong $%s$ tấm thẻ.\\\\
                             Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^{%s}$.\\\\
                             Gọi $A$ là biến cố "$%s$ tấm thẻ mang số lẻ, $%s$ tấm thẻ mang số chẵn trong đó chỉ có đúng $%s$ tấm thẻ mang số chia hết cho $10$". Để tìm số phần tử của $A$ ta làm như sau:\\\\
                             + Đầu tiên chọn $%s$ tấm thẻ trong $%s$ tấm thẻ mang số lẻ, có $C_{%s}^{%s}$ cách.\\\\
                             + Tiếp theo chọn $%s$ tấm thẻ trong $%s$ tấm thẻ mang số chẵn (không chia hết cho $10$), có $C_{%s}^{%s}$ cách.\\\\
                             + Sau cùng ta chọn $%s$ trong $%s$ tấm thẻ mang số chia hết cho $10$, có $C_{%s}^{%s}$ cách.\\\\
                             Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = C_{%s}^{%s} \\cdot C_{%s}^{%s} \\cdot C_{%s}^{%s} = %s$.\\\\
                             Vậy xác suất cần tính $P\\left(A\\right) = \\frac{C_{%s}^{%s} \\cdot C_{%s}^{%s} \\cdot C_{%s}^{%s}}{C_{%s}^{%s}} = %s$.'''
                           % (latex(n_pick), latex(n_total),
                              latex(n_total), latex(n_pick),
                              latex(n_odd_pick), latex(n_even_pick), latex(n_div_10_pick),
                              latex(n_odd_pick), latex(n_odd_total), latex(n_odd_total), latex(n_odd_pick),
                              latex(n_even_pick - n_div_10_pick), latex(n_even_not_div_10), latex(n_even_not_div_10), latex(n_even_pick - n_div_10_pick),
                              latex(n_div_10_pick), latex(n_div_10_total), latex(n_div_10_total), latex(n_div_10_pick),
                              latex(n_odd_total), latex(n_odd_pick), latex(n_even_not_div_10), latex(n_even_pick - n_div_10_pick), latex(n_div_10_total), latex(n_div_10_pick), latex(n_a),
                              latex(n_odd_total), latex(n_odd_pick), latex(n_even_not_div_10), latex(n_even_pick - n_div_10_pick), latex(n_div_10_total), latex(n_div_10_pick), latex(n_total), latex(n_pick), latex(prob)
                              ))

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

