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


def bt_dang28_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thông số cố định của kì thi THPT Quốc gia 2016
                N = 50
                diem_cong = 0.2
                diem_tru = 0.1

                # Bước 3: Random hóa điểm số bằng cách chọn số câu đúng ngẫu nhiên
                # Điểm = 0.2*x - 0.1*(50-x) = 0.3*x - 5
                # Các giá trị x sao cho điểm là số đẹp: 20, 25, 30, 35, 40
                x_dung = random.choice([20, 25, 30, 35, 40])
                x_sai = N - x_dung

                diem_so_val = 0.3 * x_dung - 5
                diem_so_str = str(Decimal(str(diem_so_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

                # Công thức đáp án đúng
                da_dung_tex = '\\frac{C_{' + latex(N) + '}^{' + latex(x_dung) + '}3^{' + latex(x_sai) + '}}{4^{' + latex(N) + '}}'

                # Bước 4: Tạo các phương án sai không trùng với đáp án đúng
                s = [
                    '\\frac{A_{' + latex(N) + '}^{' + latex(x_sai) + '}3^{' + latex(x_dung) + '}}{4^{' + latex(N) + '}}',
                    '\\frac{C_{' + latex(N) + '}^{' + latex(x_dung) + '}3^{' + latex(x_sai) + '}}{' + latex(N) + '}',
                    '\\frac{A_{' + latex(N) + '}^{' + latex(x_sai) + '}3^{' + latex(x_dung) + '}}{' + latex(N) + '}',
                    '\\frac{C_{' + latex(N) + '}^{' + latex(x_sai) + '}3^{' + latex(x_dung) + '}}{4^{' + latex(N) + '}}'
                ]

                # Lọc bỏ nếu phương án sai vô tình giống đáp án đúng (trong trường hợp x_dung = x_sai)
                s = [item for item in s if item != da_dung_tex]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (B2: Viết lại y hệt nội dung và cấu trúc)
                noidungcauhoi = ('''Trong kì thi THPT Quốc Gia năm 2016 có môn thi bắt buộc là môn Tiếng Anh. Môn thi này thi dưới hình thức trắc nghiệm với 4 phương án trả lời $A, B, C, D$. Mỗi câu trả lời đúng được cộng $%s$ điểm và mỗi câu trả lời bị sai bị trừ đi $%s$. Bạn Hòa vì học rất kém môn Tiếng Anh nên chọn ngẫu nhiên cả $%s$ câu trả lời. Xác suất để bạn Hòa được $%s$ điểm môn Tiếng Anh trong kì thi trên bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                 %(str(diem_cong).replace('.',','), str(diem_tru).replace('.',','), latex(N), diem_so_str))

                # Các đáp án
                da_d = ('\\True $' + da_dung_tex + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$' 
                da_s3 = '$' + str(das3) + '$' 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                h1=math.comb(N, x_dung)*3**x_sai/4**N
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')

                # Nội dung lời giải (Viết chi tiết, không viết tắt, dùng \left và \right)
                loigiai = ('''Gọi $x$ là số câu trả lời đúng, suy ra $%s - x$ là số câu trả lời sai. \\\\
                            Ta có số điểm của Hòa là $%s x - %s \\left( %s - x \\right) = %s \\Leftrightarrow x = %s$. \\\\
                            Do đó bạn Hòa trả lời đúng $%s$ câu và sai $%s$ câu. \\\\
                            Không gian mẫu là số phương án trả lời $%s$ câu hỏi mà bạn Hòa chọn ngẫu nhiên. Mỗi câu có $4$ phương án trả lời nên có $4^{%s}$ khả năng. \\\\
                            Suy ra số phần tử của không gian mẫu là $n \\left( \\Omega \\right) = 4^{%s}$. \\\\
                            Gọi $X$ là biến cố "bạn Hòa trả lời đúng $%s$ câu và sai $%s$ câu". Vì mỗi câu đúng có $1$ phương án trả lời, mỗi câu sai có $3$ phương án trả lời. Vì vậy có $C_{%s}^{%s} 3^{%s}$ khả năng thuận lợi cho biến cố $X$. \\\\
                            Suy ra số phần tử của biến cố $X$ là $n \\left( X \\right) = C_{%s}^{%s} 3^{%s}$. \\\\
                            Vậy xác suất cần tính $P \\left( X \\right) =$ %s $\\approx %s$.'''
                           %(latex(N), str(diem_cong).replace('.',','), str(diem_tru).replace('.',','), latex(N), diem_so_str, latex(x_dung),
                             latex(x_dung), latex(x_sai), latex(N), latex(N), latex(N), latex(x_dung), latex(x_sai), latex(N), latex(x_dung), latex(x_sai),
                             latex(N), latex(x_dung), latex(x_sai), '$' + da_dung_tex + '$', kqz))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            # Xuất câu trắc nghiệm (B2: Không dùng tiền tố r trong phần content)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

