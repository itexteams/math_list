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


def bt_dang12_p3_b1_c4_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- BƯỚC 1: RANDOM SỐ LIỆU ---
                # Chọn 2 nghiệm nguyên dương phân biệt (để tập S có 2 phần tử và dễ tính toán)
                nghiem1 = randint(1, 4) 
                nghiem2 = randint(nghiem1 + 1, 6) # Đảm bảo khác nghiệm 1

                # Tính toán các tham số cho phương trình a^2 - Sa + P = 0
                # Trong đó P là giới hạn của phân thức, S là hệ số của a
                tong_nghiem = nghiem1 + nghiem2
                tich_nghiem = nghiem1 * nghiem2

                # Random các số trong phân thức (không ảnh hưởng kết quả giới hạn)
                # Phân thức dạng: (tich_nghiem * n + b) / (n + c) -> Lim = tich_nghiem
                so_hang_tu = randint(1, 9)
                so_hang_mau = randint(1, 9)

                # Kết quả đúng (Tổng các phần tử của S)
                kq = tong_nghiem

                # --- BƯỚC 2: TẠO ĐÁP ÁN TRẮC NGHIỆM ---
                # Tạo danh sách đáp án sai
                list_da = set()
                list_da.add(kq)

                while len(list_da) < 4:
                    # Tạo nhiễu: sai lệch +1, -1, hoặc là tích các nghiệm, hoặc hiệu...
                    wrong_val = randint(kq - 3, kq + 3)
                    if wrong_val != kq and wrong_val > 0:
                        list_da.add(wrong_val)
                    elif len(list_da) < 4:
                        # Nếu vẫn thiếu, thêm các giá trị đặc biệt
                        list_da.add(tich_nghiem)
                        list_da.add(abs(nghiem1 - nghiem2))

                list_da = list(list_da)
                if kq in list_da:
                    list_da.remove(kq)

                # Gán vào biến
                da = kq
                das1 = list_da[0]
                das2 = list_da[1]
                das3 = list_da[2]

                # --- BƯỚC 3: SOẠN THẢO NỘI DUNG ---

                # Nội dung câu hỏi
                # Dạng: lim ( (An + B)/(n + C) + a^2 - Da ) = 0
                # A = tich_nghiem, D = tong_nghiem
                noidungcauhoi = ('''Gọi $S$ là tập hợp các tham số nguyên $a$ thỏa mãn $\\lim_{n \\to +\\infty} \\left( \\frac{%sn + %s}{n + %s} + a^2 - %sa \\right) = 0$. Tổng các phần tử của $S$ bằng bao nhiêu?'''
                                 %(latex(tich_nghiem), latex(so_hang_tu), latex(so_hang_mau), latex(tong_nghiem))
                                )

                # Nội dung lời giải
                loigiai = ('''Ta có: $\\lim_{n \\to +\\infty} \\left( \\frac{%sn + %s}{n + %s} + a^2 - %sa \\right)$ \\\\
                $= \\lim_{n \\to +\\infty} \\left( \\frac{n(%s + \\frac{%s}{n})}{n(1 + \\frac{%s}{n})} + a^2 - %sa \\right)$ \\\\
                $= \\lim_{n \\to +\\infty} \\frac{%s + \\frac{%s}{n}}{1 + \\frac{%s}{n}} + a^2 - %sa = %s + a^2 - %sa$. \\\\
                Theo giả thiết: $%s + a^2 - %sa = 0 \\Leftrightarrow a^2 - %sa + %s = 0 \\Leftrightarrow \\left[\\begin{aligned} a& = %s \\\\ a &= %s \\end{aligned}\\right.$.\\\\
                Vậy $S = \\{%s; %s\\} \\Rightarrow %s + %s = %s$.'''
                %(
                    # Dòng 1: Đề bài
                    latex(tich_nghiem), latex(so_hang_tu), latex(so_hang_mau), latex(tong_nghiem),
                    # Dòng 2: Rút n
                    latex(tich_nghiem), latex(so_hang_tu), latex(so_hang_mau), latex(tong_nghiem),
                    # Dòng 3: Khử n -> Kết quả lim
                    latex(tich_nghiem), latex(so_hang_tu), latex(so_hang_mau), latex(tong_nghiem), latex(tich_nghiem), latex(tong_nghiem),
                    # Dòng 4: Giải phương trình bậc 2
                    latex(tich_nghiem), latex(tong_nghiem), latex(tong_nghiem), latex(tich_nghiem), latex(nghiem1), latex(nghiem2),
                    # Dòng 5: Kết luận
                    latex(nghiem1), latex(nghiem2), latex(nghiem1), latex(nghiem2), latex(kq)
                ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

