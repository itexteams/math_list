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


def bt_dang15_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Bước 3: Suy nghĩ tìm cách random bài toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khai báo số lượng (Random số lượng nam từ 4-6, nữ từ 7-9 để bài toán đa dạng)
                nu = randint(7, 9)
                nam = randint(4, 6)
                tong = nu + nam
                chon = 4

                # Tính không gian mẫu n(Omega) = C(tong, chon)
                omega = math.comb(tong, chon)

                # Biến cố A: Ít nhất 3 nữ trong 4 người
                # TH1: 3 nữ, 1 nam
                th1_cach = math.comb(nu, 3) * math.comb(nam, 1)
                # TH2: 4 nữ, 0 nam
                th2_cach = math.comb(nu, 4)

                na = th1_cach + th2_cach

                # Tính xác suất dạng phân số tối giản
                pa = Rational(na, omega)
                tu_so = pa.p
                mau_so = pa.q

                # Đáp án đúng
                da = '$%s$' % (latex(pa))

                # Bước 4: Điều chỉnh các phương án sai không được trùng với đáp án đúng
                s = []
                while len(s) < 3:
                    # Tạo các phương án sai bằng cách thay đổi tử số
                    sai_tu = na + randint(-15, 15)
                    if sai_tu > 0 and sai_tu != na:
                        pa_sai = Rational(sai_tu, omega)
                        da_sai = '$%s$' % (latex(pa_sai))
                        if da_sai not in s and da_sai != da:
                            s.append(da_sai)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một đội gồm $%s$ nam và $%s$ nữ. Lập một nhóm gồm $%s$ người hát tố ca, xác suất để trong $%s$ người được chọn ít nhất $%s$ nữ là'''
                                 % (latex(nam), latex(nu), latex(chon), latex(chon), latex(3)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (B2: Viết lại y hệt logic trong ảnh)
                loigiai = ('''Không gian mẫu là chọn tùy ý $%s$ người từ $%s$ người. \\\\
                             Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^{%s} = %s$. \\\\
                             Gọi $A$ là biến cố '$\\,%s$ người được chọn ít nhất $3$ nữ'. Ta có hai trường hợp thuận lợi cho biến cố $A$ như sau: \\\\
                             \\textbf{TH1:} Chọn $3$ nữ và $1$ nam, có $C_{%s}^{3}C_{%s}^{1} = %s$ cách. \\\\
                             \\textbf{TH2:} Chọn cả $4$ nữ, có $C_{%s}^{4} = %s$ cách. \\\\
                             Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = C_{%s}^{3}C_{%s}^{1} + C_{%s}^{4} = %s$. \\\\
                             Vậy xác suất cần tính $P\\left(A\\right) = \\frac{%s}{%s} = %s$.'''
                           % (latex(chon), latex(tong), latex(tong), latex(chon), latex(omega),
                              latex(chon), latex(nu), latex(nam), latex(th1_cach),
                              latex(nu), latex(th2_cach),
                              latex(nu), latex(nam), latex(nu), latex(na),
                              latex(na), latex(omega), latex(pa)
                              ))

            # Xuất câu trắc nghiệm (B2: Đúng cấu trúc content, không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

