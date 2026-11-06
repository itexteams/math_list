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


def bt_dang45_p3_b1_c5_ds10(self):
            # Chọn ngẫu nhiên 5 chữ số khác nhau từ 1 đến 9
            all_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            chosen_digits = random.sample(all_digits, 5)
            chosen_digits.sort()

            d1, d2, d3, d4, d5 = chosen_digits
            sum_d = sum(chosen_digits)

            # SỐ CÁCH CHỌN: Chỉnh hợp chập 2 của 5 phần tử: A(5,2) = 20
            so_cac_so = 20 
            # SỐ LẦN XUẤT HIỆN: Mỗi chữ số xuất hiện ở hàng chục/đơn vị là: 20 / 5 = 4 lần
            so_lan = 4
            # TỔNG GIÁ TRỊ: S = 4 * (d1+d2+d3+d4+d5) * (10 + 1)
            tong_gia_tri = so_lan * sum_d * 11

            da_dung = tong_gia_tri

            # Tạo các phương án sai
            s = set()
            while len(s) < 3:
                # Nhiễu dựa trên sai lệch đơn vị 11 hoặc số ngẫu nhiên
                sai = da_dung + random.choice([-11, 11, -22, 22, -110, 110, -5, 5])
                if sai != da_dung and sai > 0:
                    s.add(sai)

            list_sai = list(s)
            das1, das2, das3 = list_sai

            # Nội dung câu hỏi
            str_digits = ", ".join(map(str, chosen_digits))
            noidungcauhoi = ('''Cho 5 chữ số $%s$. Lập các số tự nhiên có 2 chữ số đôi một khác nhau từ 5 chữ số đã cho. Tổng của các số lập được bằng bao nhiêu?'''
                             %(str_digits))

            # Nội dung lời giải chi tiết
            loigiai = ('''Mỗi số tự nhiên có 2 chữ số đôi một khác nhau từ 5 chữ số $%s$ là một chỉnh hợp chập 2 của các chữ số này. Do đó, ta lập được $A_5^2 = %s$ số. \\\\
            Do vai trò các chữ số như nhau, nên số lần xuất hiện của mỗi chữ số trong các chữ số này ở hàng chục và hàng đơn vị là như nhau và bằng $%s : 5 = %s$ lần. \\\\
            Vậy, tổng các số lập được là: \\\\
            $S = %s \\cdot \\left( %s + %s + %s + %s + %s \\right) \\cdot \\left( 10 + 1 \\right) = %s$.'''
                       %(str_digits, latex(so_cac_so), latex(so_cac_so), latex(so_lan),
                         latex(so_lan), latex(d1), latex(d2), latex(d3), latex(d4), latex(d5), 
                         latex(da_dung)))

            # Đáp án
            dapan = '\\shortans[0]{$%s$}\n'%(latex(da_dung))

            # Thiết lập các đáp án trắc nghiệm
            da_d = ('\\True $%s$' % (latex(da_dung)))
            da_s1 = ('$%s$' % (latex(das1)))
            da_s2 = ('$%s$' % (latex(das2)))
            da_s3 = ('$%s$' % (latex(das3)))

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

