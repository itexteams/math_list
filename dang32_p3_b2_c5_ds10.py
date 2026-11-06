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


def bt_dang32_p3_b2_c5_ds10(self):
            while True:
                # Giới hạn n và k nhỏ để kết quả A_n^k < 9999
                # k thường là 2, 3 hoặc 5 quả luân lưu tùy giải đấu
                k = random.choice([2, 3, 5]) 
                n = random.randint(k + 1, 15)

                # Tính kết quả chỉnh hợp A_n^k
                kq_val = math.perm(n, k)

                # Kiểm tra điều kiện kết quả < 9999
                if kq_val < 9999:
                    break

            # Đáp án đúng dạng số tự nhiên
            da_dung_val = '$%s$' % (latex(kq_val))

            # Tạo các phương án sai dạng số
            s_set = set()
            while len(s_set) < 3:
                # Các lỗi thường gặp: tính nhầm sang Tổ hợp C_n^k hoặc nhầm n, k
                sai_to_hop = math.comb(n, k)
                sai_hoan_vi = math.factorial(k)
                offset = random.choice([1, 10, -10, 5, 100])

                # Chọn ngẫu nhiên một kiểu sai
                nhieu_val = random.choice([sai_to_hop, sai_hoan_vi, kq_val + offset])

                if nhieu_val > 0 and nhieu_val != kq_val:
                    s_set.add('$%s$' % (latex(nhieu_val)))

            list_ans = ['\\True ' + da_dung_val] + list(s_set)
            random.shuffle(list_ans)

            # Câu hỏi
            noidungcauhoi = ('''Có bao nhiêu cách chọn $%s$ cầu thủ từ một đội bóng gồm $%s$ cầu thủ để thực hiện đá $%s$ quả luân lưu $11$ m, biết các quả đá được thực hiện theo thứ tự từ quả thứ nhất đến quả thứ $%s$?'''
                             %(latex(k), latex(n), latex(k), latex(k)))

            # Nội dung lời giải chi tiết
            loigiai = ('''Mỗi cách chọn $%s$ cầu thủ và sắp xếp thứ tự đá luân lưu là một chỉnh hợp chập $%s$ của $%s$ phần tử.\\\\
                         Số cách chọn thỏa mãn yêu cầu bài toán là: $A_{%s}^{%s} = \\frac{%s!}{(%s - %s)!} = %s$ (cách).'''
                       %(latex(k), latex(k), latex(n), latex(n), latex(k), latex(n), latex(n), latex(k), latex(kq_val)))

            # Đáp án ngắn (Số tự nhiên)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq_val))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

