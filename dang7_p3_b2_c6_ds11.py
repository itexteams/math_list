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


def bt_dang7_p3_b2_c6_ds11(self):
            # Khai báo biến
            # Khai báo danh sách các dạng (ở đây có 1 dạng)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Tìm cách random bài toán
                # Chọn mẫu số cho xác suất màu xanh (a) và màu vàng (b)
                # Đảm bảo tổng xác suất < 1 và các mẫu số khác nhau để bài toán hay hơn
                a = random.randint(3, 6)
                b = random.randint(2, 5)
                while a == b or (1/a + 1/b >= 1):
                    a = random.randint(4, 8)
                    b = random.randint(2, 4)

                # Tính toán các giá trị phân số
                p_xanh = Rational(1, a)
                p_vang = Rational(1, b)
                tong_p = p_xanh + p_vang

                # Bán kính/mẫu số để dùng trong lời giải latex
                mau_so_chung = a * b
                tu_so_tong = a + b

                # Tính toán giá trị thập phân và làm tròn đến hàng phần trăm (0,01)
                val_float = float(tong_p)
                kq_decimal = Decimal(str(val_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
                da_dung = '$' + kq_str + '$'

                s_wrong = set()
                while len(s_wrong) < 3:
                    # Tạo các phương án sai bằng cách cộng/trừ các giá trị nhỏ
                    sai_so = random.choice([0.1, -0.1, 0.05, -0.05, 0.12, -0.08])
                    val_sai = kq_decimal + Decimal(str(sai_so))
                    if 0 < val_sai < 1 and val_sai != kq_decimal:
                        s_wrong.add('$' + str(val_sai).replace('.', ',') + '$')

                list_wrong = list(s_wrong)
                das1 = list_wrong[0]
                das2 = list_wrong[1]
                das3 = list_wrong[2]

                # B2: Viết lại nội dung câu hỏi (Không dùng raw string r, thay ( ) bằng \left( \right))
                noidungcauhoi = ("Một hộp có chứa một số quả cầu gồm bốn màu xanh, vàng, đỏ, trắng (các quả cầu cùng màu thì khác nhau về bán kính). Lấy ngẫu nhiên một quả cầu từ hộp, biết xác suất để lấy được một quả cầu màu xanh bằng $\\frac{1}{" + str(a) + "}$, xác suất để lấy được một quả cầu màu vàng bằng $\\frac{1}{" + str(b) + "}$. Xác suất để lấy được một quả cầu xanh hoặc một quả cầu vàng bằng bao nhiêu? (Kết quả làm tròn đến hàng phần trăm).")

                # Nội dung đáp án
                da_d = '\\True ' + da_dung
                da_s1 = das1
                da_s2 = das2
                da_s3 = das3

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # B2: Viết lại nội dung lời giải chi tiết (không viết tắt)
                loigiai = ("Gọi biến cố $A$: \"Lấy được một quả cầu màu xanh\" và $B$: \"Lấy được một quả cầu màu vàng\". Ta có $A, B$ là hai biến cố xung khắc.\\\\ "
                           "Xác suất để lấy được một quả cầu màu xanh hoặc một quả cầu màu vàng là: \\\\ "
                           "$P\\left(A \\cup B\\right) = P\\left(A\\right) + P\\left(B\\right) = \\frac{1}{" + str(a) + "} + \\frac{1}{" + str(b) + "} = \\frac{" + str(tu_so_tong) + "}{" + str(mau_so_chung) + "} \\approx " + kq_str + "$.")
                dapan=' \\shortans[0]{$%s$} '%(kq_str)
            # Xuất câu trắc nghiệm theo cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

