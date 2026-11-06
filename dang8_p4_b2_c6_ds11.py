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


def bt_dang8_p4_b2_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random bài toán
                # n_do: số bi đỏ, n_xanh: số bi xanh
                n_do = random.randint(4, 7)
                n_xanh = random.randint(4, 7)
                tong_bi = n_do + n_xanh
                so_bi_lay = 2

                # Tính toán không gian mẫu
                n_omega = int(math.comb(tong_bi, so_bi_lay))

                # Tính số cách lấy 2 bi cùng màu
                # Trường hợp 1: 2 bi đỏ
                n_A = int(math.comb(n_do, so_bi_lay))
                # Trường hợp 2: 2 bi xanh
                n_B = int(math.comb(n_xanh, so_bi_lay))

                n_bien_co = n_A + n_B

                # Tính xác suất rút gọn
                tu_so = n_bien_co
                mau_so = n_omega
                pg = math.gcd(tu_so, mau_so)

                kq_tu = tu_so // pg
                kq_mau = mau_so // pg

                # Đáp án đúng
                da = Rational(kq_tu, kq_mau)

                # Bước 4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s_list = []
                while len(s_list) < 3:
                    # Tạo ngẫu nhiên các phân số sai khác nhau
                    sai_tu = random.randint(1, kq_mau - 1)
                    # Rút gọn phân số sai
                    pg_sai = math.gcd(sai_tu, kq_mau)
                    sai_tu //= pg_sai
                    sai_mau = kq_mau // pg_sai

                    phan_so_sai = Rational(sai_tu, sai_mau)
                    if phan_so_sai != da and phan_so_sai not in s_list:
                        s_list.append(phan_so_sai)

                # Gán các đáp án
                da_d = '\\True $%s$' % (latex(da))
                da_s1 = '$%s$' % (latex(s_list[0]))
                da_s2 = '$%s$' % (latex(s_list[1]))
                da_s3 = '$%s$' % (latex(s_list[2]))

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Câu hỏi
                noidungcauhoi = ('''Một chiếc hộp chứa $%s$ viên bi cùng kích thước và khối lượng, trong đó có $%s$ viên bi màu đỏ, $%s$ viên bi màu xanh. Lấy ngẫu nhiên từ hộp $%s$ viên bi. Tính xác suất của biến cố "lấy được $%s$ viên bi cùng màu".'''
                                 %(latex(tong_bi), latex(n_do), latex(n_xanh), latex(so_bi_lay), latex(so_bi_lay)))

                # Lời giải chi tiết theo mẫu trong ảnh
                loigiai = ('''Không gian mẫu $n\\left(\\Omega\\right) = C_{%s}^{%s} = %s$. \\\\
                            Gọi biến cố $A$: "Lấy được $%s$ viên bi màu đỏ": $n\\left(A\\right) = C_{%s}^{%s} = %s \\Rightarrow P\\left(A\\right) = \\frac{%s}{%s}$. \\\\
                            Biến cố $B$: "Lấy được $%s$ viên bi màu xanh": $n\\left(B\\right) = C_{%s}^{%s} = %s \\Rightarrow P\\left(B\\right) = \\frac{%s}{%s}$. \\\\
                            Vì $A, B$ là hai biến cố xung khắc nên: $P\\left(A \\cup B\\right) = P\\left(A\\right) + P\\left(B\\right) = %s$.'''
                           %(latex(tong_bi), latex(so_bi_lay), latex(n_omega),
                             latex(so_bi_lay), latex(n_do), latex(so_bi_lay), latex(n_A), latex(n_A), latex(n_omega),
                             latex(so_bi_lay), latex(n_xanh), latex(so_bi_lay), latex(n_B), latex(n_B), latex(n_omega),
                             latex(da)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

