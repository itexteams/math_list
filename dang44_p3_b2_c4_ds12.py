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


def bt_dang44_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random các thông số của bài toán
                # p_pct: tỉ lệ dân số mắc bệnh (2% -> random từ 1 đến 5)
                p_pct = randint(1, 5)
                # acc_pct: tỉ lệ chính xác đối với người mắc bệnh (99% -> random từ 95 đến 99)
                acc_pct = randint(95, 99)
                # err_pct: tỉ lệ dương tính giả đối với người không mắc bệnh (1% -> random từ 1 đến 5)
                err_pct = randint(1, 5)

                # Tính toán các xác suất thành phần
                p_a = Rational(p_pct, 100) # P(A)
                p_not_a = 1 - p_a           # P(not A)
                p_b_a = Rational(acc_pct, 100) # P(B|A)
                p_b_not_a = Rational(err_pct, 100) # P(B|not A)

                # Tính xác suất theo công thức Bayes
                tu_so = p_b_a * p_a
                mau_so = tu_so + (p_b_not_a * p_not_a)
                ket_qua_so = float(tu_so / mau_so)

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_dec = Decimal(str(ket_qua_so)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq = str(kq_dec).replace('.', ',')

                # Bước 4: Tạo các phương án sai không trùng với đáp án đúng
                v_kq = float(kq_dec)
                s_list = []
                while len(s_list) < 3:
                    # Tạo sai số ngẫu nhiên khoảng +/- 0.1 hoặc 0.2
                    sai_so = random.choice([-0.15, -0.1, 0.1, 0.15, 0.2])
                    v_sai = round(v_kq + sai_so, 2)
                    # Đảm bảo xác suất trong khoảng (0, 1) và không trùng đáp án đúng
                    if 0 < v_sai < 1 and v_sai != v_kq:
                        val_str = ('$%s$' % (str(v_sai).replace('.', ',')))
                        if val_str not in s_list:
                            s_list.append(val_str)

                # Đáp án đúng
                da_d = ('\\True $%s$' % (kq))

                # Câu hỏi
                noidungcauhoi = ('''Một địa phương có $%s\\%%$ dân số mắc căn bệnh $X$. Một phương pháp chẩn đoán có tỉ lệ chính xác là $%s\\%%$. Nghĩa là, với những người thực sự mắc bệnh, xác suất để xét nghiệm cho kết quả dương tính là $%s\\%%$ số trường hợp mắc bệnh. Tuy nhiên, phương pháp này không hoàn hảo, tức là với những người không mắc bệnh, xác suất để vẫn cho kết quả dương tính (dương tính giả) là $%s\\%%$. Chọn ngẫu nhiên một người dân của địa phương đó đi xét nghiệm. Nếu người được kiểm tra cho kết quả là dương tính thì xác suất để người đó thực sự bị bệnh là bao nhiêu? (Làm tròn kết quả đến hàng phần trăm).'''
                                 %(latex(p_pct), latex(acc_pct), latex(acc_pct), latex(err_pct)))

                # Nội dung lời giải chi tiết
                loigiai=('''Gọi $A$ là biến cố: "Người đó thực sự mắc bệnh".\\\\
                         $\\overline{A}$ là biến cố: "Người đó không mắc bệnh".\\\\
                         $B$ là biến cố: "Kết quả dương tính".\\\\
                         Theo đề bài, ta có: $P(A) = %s; P(\\overline{A}) = %s; P(B|A) = %s; P(B|\\overline{A}) = %s$.\\\\
                         Xác suất để người đó thực sự bị bệnh biết kết quả nhận được là dương tính là:\\\\
                         $P(A|B) = \\frac{P(B|A).P(A)}{P(B|A).P(A) + P(B|\\overline{A}).P(\\overline{A})} = \\frac{%s . %s}{%s . %s + %s . %s} \\approx %s$.'''
                         %(latex(float(p_a)).replace('.',','), 
                           latex(float(p_not_a)).replace('.',','), 
                           latex(float(p_b_a)).replace('.',','), 
                           latex(float(p_b_not_a)).replace('.',','),
                           latex(float(p_b_a)).replace('.',','), 
                           latex(float(p_a)).replace('.',','),
                           latex(float(p_b_a)).replace('.',','), 
                           latex(float(p_a)).replace('.',','),
                           latex(float(p_b_not_a)).replace('.',','), 
                           latex(float(p_not_a)).replace('.',','),
                           kq))
                dapan=' \\shortans[0]{$%s$} '%(kq)
            # Xáo trộn đáp án
            list_all = [da_d, s_list[0], s_list[1], s_list[2]]
            random.shuffle(list_all)

            # Xuất câu trắc nghiệm theo đúng format mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

