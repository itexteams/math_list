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


def bt_dang14_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # --- CẤU HÌNH BIẾN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Random hệ số a, b cho đường thẳng d: ax + by + c_d = 0
                # Chọn a dương, b âm để giống định dạng 2x - y trong ảnh
                a = random.randint(1, 5)
                b = random.randint(-5, -1)
                c_d = random.randint(100, 2026) # Số tự do của đường thẳng d (không ảnh hưởng MN)

                # 2. Chọn hằng số c_kq để kết quả MN và phương trình cuối cùng đẹp
                # Công thức: MN = (|c| * sqrt(a^2 + b^2)) / |a*b|
                # Ta chọn c_kq trước để tính ngược ra MN
                c_kq = random.randint(2, 12)

                # Tính giá trị MN dựa trên c_kq đã chọn
                tu_so = c_kq * sqrt(a**2 + b**2)
                mau_so = abs(a * b)
                MN_val = simplify(tu_so / mau_so)

                # Định dạng dấu cho b để hiển thị phương trình: ax + by + c = 0
                dau_b = "+" if b > 0 else "" # b đã âm nên không cần thêm dấu "-"

                # --- NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (r'''Trong mặt phẳng với hệ tọa độ $Oxy$, lập phương trình đường thẳng $\Delta$ song song với đường thẳng $d: %sx %s %sy + %s = 0$ và cắt hai trục tọa độ tại $M$ và $N$ sao cho $MN = %s$.'''
                                 %(latex(a), dau_b, latex(b), latex(c_d), latex(MN_val)))

                # --- TẠO CÁC ĐÁP ÁN ---
                # Đáp án đúng
                da_dung = r'$%sx %s %sy + %s = 0$ và $%sx %s %sy - %s = 0$' % (latex(a), dau_b, latex(b), latex(c_kq), latex(a), dau_b, latex(b), latex(c_kq))

                # Đáp án sai 1: Sai số tự do
                s1 = r'$%sx %s %sy + %s = 0$ và $%sx %s %sy - %s = 0$' % (latex(a), dau_b, latex(b), latex(c_kq + 2), latex(a), dau_b, latex(b), latex(c_kq + 2))

                # Đáp án sai 2: Đảo hệ số x, y (vuông góc thay vì song song)
                s2 = r'$%sx + %sy + %s = 0$' % (latex(-b), latex(a), latex(c_kq))

                # Đáp án sai 3: Thiếu một trường hợp
                s3 = r'$%sx %s %sy + %s = 0$' % (latex(a), dau_b, latex(b), latex(c_kq))

                # Trộn đáp án
                list_1 = ['\\True ' + da_dung, s1, s2, s3]
                random.shuffle(list_1)

                # --- NỘI DUNG LỜI GIẢI ---
                # Tính các thành phần cho lời giải chi tiết
                mau_so_binh_phuong = a**2 * b**2
                tu_so_binh_phuong = a**2 + b**2

                loigiai = (r'''Vì $\Delta \parallel d$ nên phương trình $\Delta$ có dạng: $%sx %s %sy + c = 0$ ($c \neq %s$).\\
                $\Delta$ cắt $Ox$ tại $M \Rightarrow M\left(-\frac{c}{%s}; 0\right)$.\\
                $\Delta$ cắt $Oy$ tại $N \Rightarrow N\left(0; -\frac{c}{%s}\right)$.\\
                Ta có: $MN^2 = OM^2 + ON^2 \Leftrightarrow MN^2 = \left(-\frac{c}{%s}\right)^2 + \left(-\frac{c}{%s}\right)^2$.\\
                $\Leftrightarrow MN^2 = \frac{c^2}{%s} + \frac{c^2}{%s} = c^2 \cdot \frac{%s}{%s}$.\\
                Theo giả thiết: $MN = %s \Rightarrow MN^2 = %s$.\\
                Do đó: $c^2 \cdot \frac{%s}{%s} = %s \Leftrightarrow c^2 = %s \Leftrightarrow c = \pm %s$.\\
                Vậy có hai đường thẳng thỏa mãn: $%sx %s %sy + %s = 0$ và $%sx %s %sy - %s = 0$.'''
                %(latex(a), dau_b, latex(b), latex(c_d), 
                  latex(a), latex(b), 
                  latex(a), latex(b), 
                  latex(a**2), latex(b**2), latex(tu_so_binh_phuong), latex(mau_so_binh_phuong),
                  latex(MN_val), latex(simplify(MN_val**2)),
                  latex(tu_so_binh_phuong), latex(mau_so_binh_phuong), latex(simplify(MN_val**2)),
                  latex(c_kq**2), latex(c_kq),
                  latex(a), dau_b, latex(b), latex(c_kq),
                  latex(a), dau_b, latex(b), latex(c_kq)))

            # --- XUẤT KẾT QUẢ ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

