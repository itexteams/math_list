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


def bt_dang16_p3_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo các giá trị ngẫu nhiên cho khai triển (x + by)^n
                # Tìm hệ số của x^(n-k) * y^k
                n = random.randint(4, 6)
                b = random.randint(2, 4)
                k = random.randint(2, n - 1)
                p_x = n - k
                p_y = k

                # Tính toán hệ số đúng
                # C(n, k) * (1^(n-k)) * (b^k)
                he_so_to_hop = math.comb(n, k)
                luy_thua_b = b**k
                ket_qua = he_so_to_hop * luy_thua_b

                # Đáp án đúng
                da = ket_qua

                # Tạo các đáp án sai (đảm bảo không trùng với đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Một số lỗi phổ biến: quên lũy thừa của b, quên tổ hợp, hoặc nhầm k
                    sai1 = he_so_to_hop * b
                    sai2 = luy_thua_b
                    sai3 = he_so_to_hop
                    sai4 = math.comb(n, k-1) * (b**(k-1))
                    sai5 = ket_qua + random.choice([-2, 2, 5, 10])

                    candidates = [sai1, sai2, sai3, sai4, sai5]
                    val = random.choice(candidates)
                    if val != da and val > 0:
                        s.add(val)

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                # Định dạng (x + by)^n
                bieu_thuc = "\\left( x + %s y \\right)^{%s}" % (latex(b), latex(n))
                term_find = "x^{%s} y^{%s}" % (latex(p_x), latex(p_y))

                noidungcauhoi = ("Hệ số của $%s$ trong khai triển nhị thức Niu-tơn của $%s$ bằng bao nhiêu?"
                                 % (term_find, bieu_thuc))

                # Các đáp án
                da_d = ('\\True $%s$' % (latex(da)))
                da_s1 = '$%s$' % (latex(das1))
                da_s2 = '$%s$' % (latex(das2))
                da_s3 = '$%s$' % (latex(das3))

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $%s = \\sum_{k=0}^{%s} C_{%s}^k x^{%s-k} \\left( %s y \\right)^k = \\sum_{k=0}^{%s} C_{%s}^k \\cdot %s^k \\cdot x^{%s-k} y^k$. \\\\
                           Số hạng chứa $%s$ trong khai triển trên ứng với $k = %s$. \\\\
                           Vậy hệ số của $%s$ trong khai triển của $%s$ là $C_{%s}^{%s} \\cdot %s^{%s} = %s$.'''
                           % (bieu_thuc, latex(n), latex(n), latex(n), latex(b), 
                              latex(n), latex(n), latex(b), latex(n),
                              term_find, latex(k),
                              term_find, bieu_thuc, latex(n), latex(k), latex(b), latex(k), latex(da)
                             ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(da))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

