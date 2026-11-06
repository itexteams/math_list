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


def bt_dang48_p3_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random các số n (số mũ) và m (số mũ của x cần tìm)
                n = randint(8, 12)
                m = randint(4, 6)

                # Bước 2: Tính toán logic
                # (1+x+x^2+x^3)^n = (1+x)^n * (1+x^2)^n
                # Hệ số của x^m là tổng của C(n, i) * C(n, k) sao cho i + 2k = m

                ket_qua_so = 0
                cac_buoc_giai = []

                # Tìm các cặp (k, i) thỏa mãn 2k + i = m
                # k chạy từ 0 đến m//2
                for k in range(m // 2 + 1):
                    i = m - 2 * k
                    if i <= n:
                        term_val = math.comb(n, k) * math.comb(n, i)
                        ket_qua_so += term_val
                        cac_buoc_giai.append({
                            'k': k,
                            'i': i,
                            'val': term_val
                        })

                kq = ket_qua_so

                # Tạo các đáp án nhiễu
                s = set()
                while len(s) < 3:
                    nhieu = kq + randint(-100, 100)
                    if nhieu != kq and nhieu > 0:
                        s.add("$%s$" % (latex(nhieu)))

                list_s = list(s)
                das1 = list_s[0]
                das2 = list_s[1]
                das3 = list_s[2]

                # Câu hỏi
                noidungcauhoi = ('''Hệ số của số hạng chứa $x^{%s}$ trong khai triển $\\left(1+x+x^2+x^3\\right)^{%s}$ bằng bao nhiêu?'''
                                 % (latex(m), latex(n)))

                # Đáp án đúng
                da_d = ('\\True $%s$' % (latex(kq)))

                # Lời giải chi tiết
                dong_cac_truong_hop = ""
                for idx, step in enumerate(cac_buoc_giai):
                    dong_cac_truong_hop += "Trường hợp %s: $k=%s, i=%s$ nên hệ số chứa $x^{%s}$ là $C_{%s}^{%s} \\cdot C_{%s}^{%s} = %s$. \\\\ \n" % (
                        latex(idx + 1), latex(step['k']), latex(step['i']), latex(m), latex(n), latex(step['k']), latex(n), latex(step['i']), latex(step['val'])
                    )

                tong_hop_phep_tinh = " + ".join(["C_{%s}^{%s} \\cdot C_{%s}^{%s}" % (latex(n), latex(step['k']), latex(n), latex(step['i'])) for step in cac_buoc_giai])

                loigiai = ('''Ta có: $\\left(1+x+x^2+x^3\\right)^{%s} = \\left(\\left(1+x\\right)\\left(1+x^2\\right)\\right)^{%s} = \\left(1+x^2\\right)^{%s} \\left(1+x\\right)^{%s}$ \\\\
                             $= \\sum_{k=0}^{%s} C_{%s}^k \\cdot x^{2k} \\cdot \\sum_{i=0}^{%s} C_{%s}^i \\cdot x^i = \\sum_{k=0}^{%s} \\sum_{i=0}^{%s} C_{%s}^k \\cdot C_{%s}^i \\cdot x^{2k+i}$. \\\\
                             Hệ số của số hạng chứa $x^{%s}$ nên $2k+i=%s$. \\\\
                             %s
                             Vậy hệ số của số hạng chứa $x^{%s}$ là $%s = %s$.'''
                           % (latex(n), latex(n), latex(n), latex(n),
                              latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(n),
                              latex(m), latex(m),
                              dong_cac_truong_hop,
                              latex(m), tong_hop_phep_tinh, latex(kq)
                              ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

                # Trộn đáp án
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

