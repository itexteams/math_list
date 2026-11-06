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


def bt_dang9_p4_b1_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (Dạng 1: Bài toán chọn sách từ kệ)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random bài toán
                # m: số sách Toán, v: số sách Văn
                m = randint(7, 10) 
                v = randint(5, 8)
                k = 3 # Lấy lần lượt 3 cuốn

                # Tính toán kết quả theo tổ hợp/chỉnh hợp
                # n(A): Lấy được 3 cuốn sách Toán (lần lượt, không hoàn lại -> Chỉnh hợp)
                # n(A) = A_m^3 = m * (m-1) * (m-2)
                nA = m * (m-1) * (m-2)

                # n(B): Lấy được 2 Toán, 1 Văn
                # Chọn 2 vị trí cho sách Toán trong 3 lần lấy: C_3^2
                # Chọn và sắp xếp 2 sách Toán vào 2 vị trí đó: A_m^2
                # Chọn và sắp xếp 1 sách Văn vào vị trí còn lại: A_v^1
                # n(B) = C_3^2 * A_m^2 * A_v^1 = 3 * (m * (m-1)) * v
                nB = 3 * (m * (m-1)) * v

                # Tổng số cách: n(H) = n(A) + n(B)
                kq_dung = nA + nB

                # Tạo các phương án sai (Bước 4: Tránh trùng đáp án đúng)
                # Sai lầm phổ biến 1: Dùng tổ hợp thay vì chỉnh hợp (không tính thứ tự)
                nA_sai = math.comb(m, 3)
                nB_sai = math.comb(m, 2) * math.comb(v, 1)
                kq_sai1 = nA_sai + nB_sai

                # Sai lầm phổ biến 2: Chỉ tính trường hợp 2 Toán 1 Văn
                kq_sai2 = nB

                # Sai lầm phổ biến 3: Tính nhầm n(A) + n(B) với sai số ngẫu nhiên
                kq_sai3 = kq_dung + randint(10, 50)

                # Đảm bảo không trùng
                list_kq_sai = list(set([kq_sai1, kq_sai2, kq_sai3]))
                while len(list_kq_sai) < 3:
                    new_val = kq_dung + randint(-100, 100)
                    if new_val != kq_dung and new_val > 0:
                        list_kq_sai.append(new_val)

                da = "$%s$" % (latex(kq_dung))

                s = [
                    "$%s$" % (latex(list_kq_sai[0])),
                    "$%s$" % (latex(list_kq_sai[1])),
                    "$%s$" % (latex(list_kq_sai[2]))
                ]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (Bước 2: Viết lại đề bài)
                noidungcauhoi = ("Trên kệ sách có $%s$ sách Toán và $%s$ sách Văn. Lấy lần lượt $%s$ cuốn sách mà không để lại trên kệ. Tìm số cách để chọn được ít nhất hai cuốn sách Toán."
                                 % (latex(m), latex(v), latex(k)))

                # Các đáp án
                da_d = ("\\True " + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (Bước 2)
                loigiai = ("Gọi biến cố $A$ \"Lấy được $%s$ cuốn sách Toán\". \\\\ "
                           "Biến cố $B$ \"Lấy được $2$ cuốn sách Toán, $1$ cuốn sách Văn\". \\\\ "
                           "Biến cố $H$ \"Lấy $%s$ cuốn sách có ít nhất hai cuốn sách Toán\". \\\\ "
                           "Khi đó $H = A \\cup B$ và $A \\cap B = \\varnothing$. \\\\ "
                           "Do hai biến cố $A$ và $B$ là xung khắc nên $n\\left(H\\right) = n\\left(A\\right) + n\\left(B\\right)$ \\\\ "
                           "Số các kết quả thuận lợi cho biến cố $A$ là: $n\\left(A\\right) = A_{%s}^{%s} = %s$ \\\\ "
                           "Số các kết quả thuận lợi cho biến cố $B$ là: $n\\left(B\\right) = C_{%s}^{2} \\cdot A_{%s}^{2} \\cdot A_{%s}^{1} = %s$ \\\\ "
                           "Số các kết quả thuận lợi cho biến cố $H$ là: $n\\left(H\\right) = n\\left(A\\right) + n\\left(B\\right) = %s$."
                           % (latex(k), latex(k), 
                              latex(m), latex(k), latex(nA),
                              latex(k), latex(m), latex(v), latex(nB),
                              latex(kq_dung)))

            # Xuất câu trắc nghiệm (Không dùng tiền tố r, dùng \left( \right))
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

