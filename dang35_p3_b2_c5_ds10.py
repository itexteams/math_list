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


def bt_dang35_p3_b2_c5_ds10(self):
            # Chọn n sao cho C_n^3 < 9999 (n tối đa khoảng 40)
            n = random.randint(10, 40)

            # Tính giá trị số tự nhiên của C_n^3
            # kq_val = n! / (3! * (n-3)!) = n*(n-1)*(n-2) / 6
            kq_val = n * (n - 1) * (n - 2) // 6

            # Đáp án đúng dạng số
            da_dung = '$%s$' % (latex(kq_val))

            # Tạo các phương án nhiễu (dạng số tự nhiên)
            s_set = set()
            while len(s_set) < 3:
                # Các lỗi thường gặp: tính nhầm thành A_n^3, C_n^2, hoặc n*3
                sai_an3 = n * (n - 1) * (n - 2)
                sai_cn2 = n * (n - 1) // 2
                sai_nhan3 = n * 3
                offset = random.choice([1, -1, 10, -10, 5, 2])

                # Chọn ngẫu nhiên một giá trị sai để thêm vào set
                nhieu_val = random.choice([sai_an3, sai_cn2, sai_nhan3, kq_val + offset])

                if 0 < nhieu_val < 20000 and nhieu_val != kq_val:
                    s_set.add('$%s$' % (latex(nhieu_val)))

            list_ans = ['\\True ' + da_dung] + list(s_set)
            random.shuffle(list_ans)

            # Câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng cho $%s$ điểm phân biệt trong đó không có $3$ điểm nào thẳng hàng. Số tam giác có đỉnh là $3$ trong số $%s$ điểm đã cho bằng bao nhiêu?'''
                             %(latex(n), latex(n)))

            # Nội dung lời giải chi tiết
            loigiai = ('''Để tạo thành một tam giác, ta cần chọn $3$ điểm từ $%s$ điểm đã cho. \\\\
                         Vì trong $%s$ điểm không có $3$ điểm nào thẳng hàng, nên cứ mỗi cách chọn $3$ điểm bất kì ta luôn lập được một tam giác. \\\\
                         Số cách chọn $3$ điểm từ $%s$ điểm phân biệt là số tổ hợp chập $3$ của $%s$ phần tử: 
                         $C_{%s}^3 = \\dfrac{%s \\cdot %s \\cdot %s}{6} = %s$. \\\\
                         Vậy số tam giác có thể tạo thành là $%s$.'''
                       %(latex(n), latex(n), latex(n), latex(n), latex(n), 
                         latex(n), latex(n-1), latex(n-2), latex(kq_val), latex(kq_val)))

            # Đáp án ngắn (hiển thị số tự nhiên)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq_val))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

