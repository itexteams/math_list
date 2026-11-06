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


def bt_dang18_p4_b3_c5_ds10(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các tham số m, p, n sao cho tồn tại số hạng không chứa x
                # Biểu thức: (1/x^m + x^p)^n
                # Số hạng tổng quát: C(n, k) * (x^-m)^(n-k) * (x^p)^k = C(n, k) * x^(-m*n + m*k + p*k)
                # Để không chứa x: k(m+p) - mn = 0 => k = (m*n) / (m+p)

                while True:
                    m = randint(1, 2)
                    p = randint(1, 4)
                    n = randint(4, 12)
                    if (m * n) % (m + p) == 0:
                        k_val = (m * n) // (m + p)
                        if 0 < k_val < n: # Đảm bảo không phải số hạng đầu hoặc cuối để bài toán hay hơn
                            break

                # Tính đáp án đúng
                kq_val = math.comb(n, k_val)
                da = '$%s$' % kq_val

                # Tạo các đáp án nhiễu (sai) - ĐÃ SỬA LỖI TREO PHẦN MỀM
                s = set()
                loop_count = 0
                while len(s) < 3:
                    loop_count += 1
                    # Nếu lặp chưa quá 15 lần, ưu tiên lấy nhiễu bằng giá trị tổ hợp lân cận
                    if loop_count < 15:
                        temp_k = random.choice([k_val - 1, k_val + 1, randint(0, n)])
                        if 0 <= temp_k <= n:
                            val = math.comb(n, temp_k)
                            if val != kq_val:
                                s.add('$%s$' % val)
                    else:
                        # Nếu lấy tổ hợp bị trùng quá nhiều (do n nhỏ), sinh số ngẫu nhiên lân cận đáp án
                        val = kq_val + random.choice([-3, -2, -1, 1, 2, 3, 4, 5, 6])
                        if val != kq_val and val > 0:
                            s.add('$%s$' % val)

                list_s = list(s)
                das1 = list_s[0]
                das2 = list_s[1]
                das3 = list_s[2]

                # Thiết lập hiển thị số mũ
                mu_m = '' if m == 1 else '^{%s}' % m
                mu_p = 'x' if p == 1 else 'x^{%s}' % p

                # Câu hỏi
                noidungcauhoi = ('''Tìm số hạng không chứa $x$ trong khai triển nhị thức Niu-tơn của $\\left( \\frac{1}{x%s} + %s \\right)^{%s}$.'''
                                 % (mu_m, mu_p, latex(n)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Biểu thức số hạng tổng quát để trình bày
                exp_text = '%sk - %s' % (m + p, m * n) if m * n > 0 else '%sk' % (m + p)

                loigiai = ('''Ta có $\\left( \\frac{1}{x%s} + %s \\right)^{%s} = \\sum_{k=0}^{%s} C_{%s}^k \\left( \\frac{1}{x%s} \\right)^{%s-k} \\left( %s \\right)^k = \\sum_{k=0}^{%s} C_{%s}^k x^{%sk-%s}$.\\\\
                         Số hạng không chứa $x$ trong khai triển trên ứng với $%s = 0 \\Leftrightarrow k = %s$.\\\\
                         Vậy số hạng không chứa $x$ trong khai triển $\\left( \\frac{1}{x%s} + %s \\right)^{%s}$ là $C_{%s}^{%s} = %s$.'''
                         % (mu_m, mu_p, latex(n), latex(n), latex(n), mu_m, latex(n), mu_p, latex(n), latex(n), latex(m+p), latex(m*n),
                           exp_text, latex(k_val),
                           mu_m, mu_p, latex(n), latex(n), latex(k_val), latex(kq_val)
                          ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')

            return content

