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


def bt_dang13_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Ngẫu nhiên tổng hai mặt từ 3 đến 11
                tong_s = randint(3, 11)

                # Tính không gian mẫu
                kgm = 36

                # Tìm các cặp số (x, y) có tổng bằng tong_s
                cac_cap = []
                for x_val in range(1, 7):
                    y_val = tong_s - x_val
                    if 1 <= y_val <= 6:
                        cac_cap.append((x_val, y_val))

                so_kq_thuan_loi = len(cac_cap)
                xs_dung = Rational(so_kq_thuan_loi, kgm)

                # SỬA LỖI TẠI ĐÂY: Dùng \\ để tránh SyntaxError
                chuoi_cac_cap = ', '.join(['\\left(' + str(pair[0]) + ';' + str(pair[1]) + '\\right)' for pair in cac_cap])

                # Tạo đáp án đúng
                da = '$%s$' % (latex(xs_dung))

                # Tạo danh sách các đáp án sai (đảm bảo không trùng đáp án đúng)
                tap_da_sai = [
                    Rational(1, 6), Rational(5, 36), Rational(1, 9), Rational(1, 12),
                    Rational(7, 36), Rational(1, 4), Rational(1, 2), Rational(1, 3),
                    Rational(11, 36), Rational(2, 9)
                ]

                s = []
                for item in tap_da_sai:
                    if item != xs_dung:
                        s.append('$%s$' % (latex(item)))

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Câu hỏi
                noidungcauhoi = ('''Gieo một con xúc xắc hai lần. Xác suất để biến cố có tổng hai mặt bằng $%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                 %(latex(tong_s)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)
                h1=xs_dung
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.', ',')
                # Nội dung lời giải (Sử dụng \\ cho tất cả các lệnh LaTeX)
                loigiai = ('''Số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = 6 \\cdot 6 = 36$. \\\\
                             Gọi $A$ là biến cố 'Số chấm trên mặt hai lần gieo có tổng bằng $%s$'. \\\\
                             Gọi số chấm trên mặt khi gieo lần một là $x$, số chấm trên mặt khi gieo lần hai là $y$. \\\\
                             Theo bài ra, ta có $\\begin{cases} 1 \\le x \\le 6 \\\\ 1 \\le y \\le 6 \\\\ x + y = %s \\end{cases} \\Rightarrow (x; y) = \\{%s\\}$. \\\\
                             Khi đó số kết quả thuận lợi cho biến cố là $n\\left(A\\right) = %s$. \\\\
                             Vậy xác suất cần tính $P(A) = \\frac{%s}{36} = %s \\approx %s$.'''
                           %(latex(tong_s), latex(tong_s), chuoi_cac_cap, latex(so_kq_thuan_loi), latex(so_kq_thuan_loi), latex(xs_dung),kqz))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

