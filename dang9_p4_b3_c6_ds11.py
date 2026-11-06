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


def bt_dang9_p4_b3_c6_ds11(self):
            # Khai báo biến
            # B3-Suy nghĩ tìm cách random bài toán
            # Random xác suất sinh con trai từ 0.48 đến 0.52
            p_trai_val = Decimal(str(random.randint(48, 52) / 100))
            # Random số lần sinh từ 3 đến 5 lần
            n_lan_val = random.randint(3, 5)

            # Tính toán các giá trị liên quan
            p_gai_val = 1 - p_trai_val
            kq_chinh_xac = 1 - (p_gai_val ** n_lan_val)
            # Làm tròn đến 2 chữ số thập phân
            kq_final = kq_chinh_xac.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            # Định dạng số với dấu phẩy cho tiếng Việt
            p_trai_str = str(p_trai_val).replace('.', ',')
            p_gai_str = str(p_gai_val).replace('.', ',')
            kq_str = str(kq_final).replace('.', ',')

            # B4-Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            da_dung = '$%s$' % kq_str
            s = []
            while len(s) < 3:
                # Tạo các phương án sai quanh đáp án đúng
                sai_val = kq_final + Decimal(str(random.choice([-0.2, -0.1, 0.1, 0.2, -0.15, 0.05])))
                sai_str = '$%s$' % (str(sai_val).replace('.', ','))
                if sai_str != da_dung and sai_str not in s:
                    s.append(sai_str)

            da_s1, da_s2, da_s3 = s

            # B2-Viết lại bài toán theo mẫu code python
            # Câu hỏi
            noidungcauhoi = ('''Xác suất sinh con trai trong mỗi lần sinh là $%s$. Tính xác suất sao cho trong $%s$ lần sinh có ít nhất $1$ lần là con trai (mỗi lần sinh $1$ con).'''
                              % (p_trai_str, n_lan_val))

            # Đáp án
            da_d = ('\\True ' + da_dung)
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            loigiai = ('''Gọi $A$ là biến cố: "Trong $%s$ lần sinh có ít nhất $1$ lần là con trai". \\\\
                         Khi đó biến cố đối $\\overline{A}$ là biến cố: "Cả $%s$ lần sinh đều là con gái". \\\\
                         Vì xác suất sinh con trai trong mỗi lần sinh là $%s$ nên xác suất sinh con gái trong mỗi lần sinh là $1 - %s = %s$. \\\\
                         Xác suất của biến cố đối là: $P\\left(\\overline{A}\\right) = \\left(%s\\right)^{%s}$. \\\\
                         Vậy xác suất của biến cố $A$ là: \\\\
                         $P\\left(A\\right) = 1 - P\\left(\\overline{A}\\right) = 1 - \\left(%s\\right)^{%s} \\approx %s$.'''
                       % (n_lan_val, n_lan_val, p_trai_str, p_trai_str, p_gai_str, p_gai_str, n_lan_val, p_gai_str, n_lan_val, kq_str))

            # Xuất câu trắc nghiệm (không dùng raw string r, dùng \\ để thay thế)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

