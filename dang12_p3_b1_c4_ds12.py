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


def bt_dang12_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random số liệu bài toán
                # Hộp I: r1 quả đỏ, v1 quả vàng
                r1 = randint(5, 8)
                v1 = randint(3, 6)
                # Hộp II: r2 quả đỏ, v2 quả vàng
                r2 = randint(6, 9)
                v2 = randint(2, 5)

                tong1 = r1 + v1
                tong2_bandau = r2 + v2
                tong2_saubochay = tong2_bandau + 1

                # Bước 2: Tính toán theo logic bài toán
                # Không gian mẫu n(Omega) = Lấy 1 ở hộp I bỏ vào hộp II (tong1 cách) * Lấy 1 ở hộp II (tong2_saubochay cách)
                n_omega = tong1 * tong2_saubochay

                # Biến cố A: "Lấy quả màu đỏ ở hộp II"
                # TH1: Hộp I lấy đỏ (r1), hộp II lúc này có (r2 + 1) đỏ -> n1 = r1 * (r2 + 1)
                # TH2: Hộp I lấy vàng (v1), hộp II lúc này có (r2) đỏ -> n2 = v1 * r2
                n_a = r1 * (r2 + 1) + v1 * r2
                p_a_tu = n_a
                p_a_mau = n_omega

                # Biến cố B: "Quả lấy ra từ hộp II là quả được chuyển từ hộp I sang"
                # Để quả đó màu đỏ (giao với A) thì bắt buộc từ hộp I phải lấy quả đỏ chuyển sang
                # Sau đó lấy đúng quả đó ở hộp II (chỉ có 1 cách chọn quả đó)
                # n(A giao B) = r1 (cách chọn đỏ từ hộp I) * 1 (cách chọn đúng quả đó ở hộp II)
                n_ab = r1
                p_ab_tu = n_ab
                p_ab_mau = n_omega

                # Tính xác suất có điều kiện P(B|A) = n(A giao B) / n(A)
                ketqua_huu_ty = Rational(n_ab, n_a)
                kq_decimal = Decimal(n_ab) / Decimal(n_a)
                kq_rounded = kq_decimal.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                # Định dạng kết quả số thập phân dùng dấu phẩy
                kq_str = str(kq_rounded).replace('.', ',')

                # Bước 3: Tạo các phương án sai (không trùng đáp án đúng)
                da = kq_str

                s = []
                # Các giá trị sai phổ biến: P(A), n(AB)/n(Omega), hoặc sai lệch số thập phân
                sai1 = Decimal(n_a) / Decimal(n_omega)
                sai2 = Decimal(n_ab) / Decimal(n_omega)

                list_sai = [
                    sai1.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
                    sai2.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
                    (kq_rounded + Decimal('0.05')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
                    (kq_rounded - Decimal('0.03')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
                    (kq_rounded + Decimal('0.12')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                ]

                for item in list_sai:
                    val_str = str(item).replace('.', ',')
                    if val_str != da and val_str not in s:
                        s.append('$%s$' % val_str)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Có hai chiếc hộp, hộp I có $%s$ quả bóng màu đỏ và $%s$ quả bóng màu vàng, hộp II có $%s$ quả bóng màu đỏ và $%s$ quả bóng màu vàng, các quả bóng có cùng kích thước và khối lượng. Lấy ngẫu nhiên một quả bóng từ hộp I bỏ vào hộp II. Sau đó, lấy ra ngẫu nhiên một quả bóng từ hộp II. Tính xác suất để quả bóng được lấy ra từ hộp II là quả bóng được chuyển từ hộp I sang, biết rằng quả bóng đó có màu đỏ (làm tròn kết quả đến hàng phần trăm).'''
                                 % (latex(r1), latex(v1), latex(r2), latex(v2)))

                # Nội dung lời giải chi tiết
                loigiai = ('''Công việc được hoàn thành bởi $2$ hành động liên tiếp, lấy $1$ quả ở hộp I bỏ vào hộp II, sau đó lấy $1$ quả ở hộp II. Nên $n(\\Omega) = %s \\cdot %s = %s$. \\\\
                           Gọi $A$: "Lấy quả màu đỏ ở hộp II". \\\\
                           Trường hợp 1: Lấy quả đỏ từ hộp I bỏ vào hộp II, sau đó lấy quả đỏ từ hộp II. Có $%s \\cdot %s$ cách. \\\\
                           Trường hợp 2: Lấy quả vàng từ hộp I bỏ vào hộp II, sau đó lấy quả đỏ từ hộp II. Có $%s \\cdot %s$ cách. \\\\
                           Suy ra $n(A) = %s \\cdot %s + %s \\cdot %s = %s \\Rightarrow P(A) = \\frac{%s}{%s}$. \\\\
                           Gọi $B$: "Lấy $1$ quả ở hộp II được quả ở hộp I chuyển sang". \\\\
                           Để quả bóng lấy ra màu đỏ và là quả từ hộp I chuyển sang thì quả chuyển sang phải là màu đỏ. \\\\
                           Do đó $n(A \\cap B) = %s \\cdot 1 = %s \\Rightarrow P(A \\cap B) = \\frac{%s}{%s}$. \\\\
                           Ta có xác suất cần tìm là: $P(B|A) = \\frac{P(A \\cap B)}{P(A)} = \\frac{%s}{%s} \\approx %s$.'''
                           % (latex(tong1), latex(tong2_saubochay), latex(n_omega),
                              latex(r1), latex(r2 + 1),
                              latex(v1), latex(r2),
                              latex(r1), latex(r2 + 1), latex(v1), latex(r2), latex(n_a), latex(n_a), latex(n_omega),
                              latex(r1), latex(r1), latex(r1), latex(n_omega),
                              latex(n_ab), latex(n_a), kq_str))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(kq_str)

                # Các đáp án
                da_d = ('\\True $%s$' % da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

