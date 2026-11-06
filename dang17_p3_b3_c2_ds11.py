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


def bt_dang17_p3_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # P là tổng tiền vay (triệu đồng), chọn các số chia hết cho 12 để tiền gốc hàng tháng là số nguyên
                P = random.choice([120, 240, 300, 360, 480, 600])
                # r_year là lãi suất năm (%), chọn các số chia hết cho 1,2 để lãi tháng đẹp
                r_year = random.choice([6.0, 7.2, 8.4, 9.6, 10.8, 12.0])
                n = 12 # Số tháng

                # Tính toán các thông số
                tien_goc_thang = P // n
                lai_thang_he_so = r_year / 12 / 100

                # Tính tổng tiền lãi L = (P + (P-goc) + (P-2*goc) + ... + goc) * lai_thang_he_so
                # Đây là tổng cấp số cộng: n/2 * (P + goc)
                tong_du_no = (n * (P + tien_goc_thang)) / 2
                tong_lai_thuan = tong_du_no * lai_thang_he_so

                # Làm tròn đến hàng phần mười
                kq_decimal = Decimal(str(tong_lai_thuan)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Tạo các phương án sai (Bước 4: Tránh trùng đáp án đúng)
                s = []
                offsets = [-2.1, -1.5, 0.8, 1.2, 2.5, 3.3]
                for offset in offsets:
                    wrong_val = float(kq_decimal) + offset
                    if wrong_val > 0:
                        val_str = str(Decimal(str(wrong_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                        if val_str != kq_str:
                            s.append('$%s$' % val_str)

                random.shuffle(s)
                da_d = '\\True $%s$' % kq_str
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2: Viết lại nội dung và lời giải (không dùng raw string, dùng \left( \right))
                r_year_str = str(r_year).replace('.', ',')
                lai_thang_he_so_str = str(lai_thang_he_so).replace('.', ',')

                noidungcauhoi = ('Anh Tú vay ngân hàng ' + str(P) + ' triệu đồng để mua xe ô tô với lãi suất cố định $' + r_year_str + '$ \\%/năm theo hình thức trả góp hằng tháng, trong thời hạn ' + str(n) + ' tháng (ứng với ' + str(n) + ' kì trả nợ). Trong thời hạn đó, cuối mỗi kì trả nợ, anh Tú phải trả ' + str(tien_goc_thang) + ' triệu đồng tiền gốc (ứng với ' + str(P) + ' triệu đồng chia đều cho ' + str(n) + ' tháng) và một khoản tiền lãi được tính theo số tiền dư nợ còn lại. Sau ' + str(n) + ' tháng, tổng số tiền lãi anh Tú phải trả ngân hàng là bao nhiêu triệu đồng? (kết quả làm tròn đến hàng phần mười).')

                # Lời giải chi tiết
                du_no_1 = P - tien_goc_thang
                du_no_2 = du_no_1 - tien_goc_thang

                loigiai = ('Tháng 1: Lãi = $' + str(P) + ' \\times ' + lai_thang_he_so_str + '$. Dư nợ còn lại = $' + str(P) + ' - ' + str(tien_goc_thang) + ' = ' + str(du_no_1) + '$ triệu. \\\\ ' +
                           'Tháng 2: Lãi = $' + str(du_no_1) + ' \\times ' + lai_thang_he_so_str + '$. Dư nợ còn lại = $' + str(du_no_1) + ' - ' + str(tien_goc_thang) + ' = ' + str(du_no_2) + '$ triệu. \\\\ ' +
                           '... \\\\ ' +
                           'Tháng ' + str(n) + ': Lãi = $' + str(tien_goc_thang) + ' \\times ' + lai_thang_he_so_str + '$. Dư nợ còn lại = $0$ triệu. \\\\ ' +
                           'Vậy tổng tiền lãi $L = \\left(' + str(P) + ' + ' + str(du_no_1) + ' + ' + str(du_no_2) + ' + \\dots + ' + str(tien_goc_thang) + '\\right) \\times ' + lai_thang_he_so_str + ' = ' + kq_str + '$ triệu đồng.')
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_str))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')     
            return content 

