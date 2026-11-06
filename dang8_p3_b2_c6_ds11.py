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


def bt_dang8_p3_b2_c6_ds11(self):
            # Khai báo biến
            # w thường nhỏ (2-3) để lời giải không quá dài, b random từ 6-10.
            w = random.randint(2, 3)
            b = random.randint(7, 10)
            tong = w + b
            tong_con_lai = tong - 2

            # Tính xác suất các trường hợp
            # Biến cố A: Lần đầu lấy 2 đen, lần sau lấy 1 trắng
            tu_a = binomial(b, 2) * binomial(w, 1)
            mau_a = binomial(tong, 2) * binomial(tong_con_lai, 1)
            p_a = Rational(tu_a, mau_a)

            # Biến cố B: Lần đầu lấy 1 đen 1 trắng, lần sau lấy 1 trắng
            tu_b = binomial(b, 1) * binomial(w, 1) * binomial(w - 1, 1)
            mau_b = binomial(tong, 2) * binomial(tong_con_lai, 1)
            p_b = Rational(tu_b, mau_b)

            # Biến cố C: Lần đầu lấy 2 trắng, lần sau lấy 1 trắng (Chỉ xảy ra nếu w > 2)
            tu_c = binomial(w, 2) * binomial(w - 2, 1)
            mau_c = binomial(tong, 2) * binomial(tong_con_lai, 1)
            p_c = Rational(tu_c, mau_c)

            p_tong = p_a + p_b + p_c
            kq_float = float(p_tong)
            kq_decimal = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq_final = str(kq_decimal).replace('.', ',')

            # B4: Điều chỉnh các phương án sai
            da_dung = '$' + kq_final + '$'
            s_list = []
            while len(s_list) < 3:
                sai_so = random.choice([-0.2, -0.1, 0.1, 0.2, 0.3])
                val_sai = float(kq_decimal) + sai_so
                if val_sai > 0 and val_sai < 1:
                    str_sai = '$' + str(Decimal(str(val_sai)).quantize(Decimal('0.1'))).replace('.', ',') + '$'
                    if str_sai != da_dung and str_sai not in s_list:
                        s_list.append(str_sai)

            da_s1, da_s2, da_s3 = s_list

            # B2: Viết nội dung câu hỏi
            noidungcauhoi = (
                'Trong một bình có $%s$ viên bi trắng và $%s$ viên bi đen. '
                'Người ta bốc $2$ viên bi bỏ ra ngoài rồi bốc tiếp một viên bi thứ ba. '
                'Xác suất để viên bi thứ ba là trắng bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'
                % (latex(w), latex(b))
            )

            # Viết lời giải chi tiết
            loigiai_chi_tiet = []
            loigiai_chi_tiet.append('Gọi $A$ là biến cố "lần đầu lấy $2$ viên bi đen, lần sau lấy $1$ viên bi trắng".')
            loigiai_chi_tiet.append('$P\\left(A\\right) = \\frac{C_{%s}^2 \\cdot C_{%s}^1}{C_{%s}^2 \\cdot C_{%s}^1} = %s$.' 
                                    % (latex(b), latex(w), latex(tong), latex(tong_con_lai), latex(p_a)))

            loigiai_chi_tiet.append('Gọi $B$ là biến cố "lần đầu lấy $1$ viên bi đen và $1$ viên bi trắng, lần sau lấy $1$ viên bi trắng".')
            loigiai_chi_tiet.append('$P\\left(B\\right) = \\frac{C_{%s}^1 \\cdot C_{%s}^1 \\cdot C_{%s}^1}{C_{%s}^2 \\cdot C_{%s}^1} = %s$.' 
                                    % (latex(b), latex(w), latex(w-1), latex(tong), latex(tong_con_lai), latex(p_b)))

            if w > 2:
                loigiai_chi_tiet.append('Gọi $C$ là biến cố "lần đầu lấy $2$ viên bi trắng, lần sau lấy $1$ viên bi trắng".')
                loigiai_chi_tiet.append('$P\\left(C\\right) = \\frac{C_{%s}^2 \\cdot C_{%s}^1}{C_{%s}^2 \\cdot C_{%s}^1} = %s$.' 
                                        % (latex(w), latex(w-2), latex(tong), latex(tong_con_lai), latex(p_c)))
                loigiai_str = '\\\\ '.join(loigiai_chi_tiet) + '\\\\ Ta có xác suất cần tìm là $P = P\\left(A\\right) + P\\left(B\\right) + P\\left(C\\right) = %s \\approx %s$.' % (latex(p_tong), kq_final)
            else:
                loigiai_str = '\\\\ '.join(loigiai_chi_tiet) + '\\\\ Ta có xác suất cần tìm là $P = P\\left(A\\right) + P\\left(B\\right) = %s \\approx %s$.' % (latex(p_tong), kq_final)

            # Đưa vào list chọn ngẫu nhiên
            list_da = ['\\True ' + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_da)
            dapan=' \\shortans[0]{$%s$} '%(kq_final)
            # Xuất câu trắc nghiệm theo mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai_str) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

