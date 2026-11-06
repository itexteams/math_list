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


def bt_dang14_p4_b1_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC NGẪU NHIÊN HÓA ---
                # k là bậc của căn thức (mẫu số của số mũ phân số)
                k = random.randint(2, 6) 
                # m là số mũ của tích ab sau khi rút gọn
                m = random.randint(1, 3) 

                # Tính toán số mũ ở tử số: m + 1/k = (m*k + 1)/k
                tu_so_mu = Rational(m * k + 1, k)
                mau_so_mu = Rational(1, k)

                # Biểu diễn LaTeX cho căn thức ở mẫu
                if k == 2:
                    latex_mau = r"\sqrt{a} + \sqrt{b}"
                else:
                    latex_mau = r"\sqrt[%s]{a} + \sqrt[%s]{b}" % (k, k)

                # --- ĐÁP ÁN ---
                # Đáp án đúng: (ab)^m
                if m == 1:
                    kq_dung = "ab"
                else:
                    kq_dung = "a^{%s}b^{%s}" % (m, m)

                da_d = r'\True $%s$' % kq_dung

                # Tạo các đáp án nhiễu
                s = [
                    r'$a + b$',
                    r'$a^{%s} + b^{%s}$' % (m, m),
                    r'$ab^{%s}$' % (m + 1),
                    r'$(ab)^{1/%s}$' % k,
                    r'$a^{1/%s} + b^{1/%s}$' % (k, k),
                    r'$1$'
                ]

                # Lấy ngẫu nhiên 3 đáp án sai từ danh sách s
                random.shuffle(s)
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Trộn các đáp án
                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # --- NỘI DUNG CÂU HỎI ---
                # Sử dụng định dạng LaTeX cho biểu thức P
                bieu_thuc_P = r"P = \frac{a^{%s}b^{%s} + a^{%s}b^{%s}}{%s}" % (
                    latex(tu_so_mu), m, m, latex(tu_so_mu), latex_mau
                )

                noidungcauhoi = r"Cho $a, b$ là các số thực dương. Rút gọn biểu thức $%s$." % bieu_thuc_P

                # --- NỘI DUNG LỜI GIẢI ---
                loigiai = r'''Ta có: \\
                $P = \frac{a^{%s} \cdot a^{\frac{1}{%s}} \cdot b^{%s} + a^{%s} \cdot b^{%s} \cdot b^{\frac{1}{%s}}}{a^{\frac{1}{%s}} + b^{\frac{1}{%s}}}$ \\
                $P = \frac{a^{%s}b^{%s} \left( a^{\frac{1}{%s}} + b^{\frac{1}{%s}} \right)}{a^{\frac{1}{%s}} + b^{\frac{1}{%s}}}$ \\
                $P = %s$.''' % (
                    m, k, m, m, m, k, k, k,
                    m, m, k, k, k, k,
                    kq_dung
                )

            # --- XUẤT KẾT QUẢ ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

