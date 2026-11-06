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


def bt_dang6_p4_b2_c6_ds11(self):
            # Khai báo biến
            # nx: số quả cầu xanh, nd: số quả cầu đỏ
            nx = random.randint(4, 9)
            nd = random.randint(3, 8)
            total = nx + nd

            # Tính toán các giá trị không gian mẫu và biến cố
            n_omega = math.comb(total, 2)
            n_a = math.comb(nx, 2)
            n_b = math.comb(nd, 2)

            # Xác suất thành phần và xác suất cuối cùng
            p_a = Rational(n_a, n_omega)
            p_b = Rational(n_b, n_omega)
            kq_final = p_a + p_b

            # B4: Tạo các phương án sai và đảm bảo không trùng với đáp án đúng
            da_dung = '$%s$' % latex(kq_final)
            da_sai_list = []

            # Các ứng viên cho phương án sai: P(A), P(B), hoặc các phân số ngẫu nhiên
            candidates = [p_a, p_b, Rational(random.randint(1, n_omega-1), n_omega)]

            for c in candidates:
                val = '$%s$' % latex(c)
                if c != kq_final and val not in da_sai_list:
                    da_sai_list.append(val)

            # Bổ sung phương án sai nếu chưa đủ 3 cái
            while len(da_sai_list) < 3:
                temp_val = Rational(random.randint(1, n_omega-1), n_omega)
                val_str = '$%s$' % latex(temp_val)
                if temp_val != kq_final and val_str not in da_sai_list:
                    da_sai_list.append(val_str)

            # Trộn đáp án
            da_d = '\\True ' + da_dung
            list_da = [da_d] + da_sai_list
            random.shuffle(list_da)

            # B2: Viết lại nội dung câu hỏi và lời giải chi tiết theo mẫu
            noidungcauhoi = ('Một hộp đựng $%s$ quả cầu màu xanh và $%s$ quả cầu màu đỏ có cùng kích thước và khối lượng. Chọn ngẫu nhiên hai quả cầu trong hộp. Tính xác suất để chọn được hai quả cầu có cùng màu.'
                             % (latex(nx), latex(nd)))

            loigiai = ('''Xét các biến cố A: "Chọn được cả hai quả cầu màu xanh",\\\\
                         B: "Chọn được cả hai quả cầu màu đỏ".\\\\
                         Biến cố C: "Hai quả cầu có cùng màu" là biến cố hợp của A và B.\\\\
                         Hai biến cố A và B là xung khắc nên $P\\left(C\\right) = P\\left(A\\right) + P\\left(B\\right)$.\\\\
                         $n\\left(\\Omega\\right) = C_{%s}^{2} = %s, n\\left(A\\right) = C_{%s}^{2} = %s$.\\\\
                         Do đó $P\\left(A\\right) = \\frac{%s}{%s}$.\\\\
                         $n\\left(B\\right) = C_{%s}^{2} = %s$. Do đó $P\\left(B\\right) = \\frac{%s}{%s}$.\\\\
                         Vậy $P\\left(C\\right) = P\\left(A\\right) + P\\left(B\\right) = \\frac{%s}{%s} + \\frac{%s}{%s} = %s$.'''
                       % (latex(total), latex(n_omega), latex(nx), latex(n_a),
                          latex(n_a), latex(n_omega),
                          latex(nd), latex(n_b), latex(n_b), latex(n_omega),
                          latex(n_a), latex(n_omega), latex(n_b), latex(n_omega), latex(kq_final)))

            # Xuất nội dung theo cấu trúc yêu cầu (không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

