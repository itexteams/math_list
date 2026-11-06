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


def bt_dang29_p3_b2_c5_ds10(self):
            while True:
                # Random số đỉnh n (Giới hạn n <= 99 để n*(n-1) < 9999)
                n = random.randint(5, 50) 

                # Tính kết quả cuối cùng: A_n^2 = n * (n-1)
                kq_val = n * (n - 1)

                if kq_val < 9999:
                    break

            # Từ điển tên gọi đa giác
            dict_ten = {
                5: 'ngũ giác', 6: 'lục giác', 7: 'thất giác', 8: 'bát giác', 
                9: 'cửu giác', 10: 'thập giác', 11: 'thập nhất giác', 12: 'thập nhị giác'
            }
            ten_da_giac = dict_ten.get(n, str(n) + '-giác')

            # Tạo nhãn các đỉnh
            chu_cai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if n <= 26:
                nhan_dinh = chu_cai[:n]
            else:
                nhan_dinh = "A_1A_2...A_{%s}" % (latex(n))

            # Đáp án đúng dạng số tự nhiên
            da_dung = '$%s$' % (latex(kq_val))

            # Tạo các phương án sai dạng số
            s_set = set()
            while len(s_set) < 3:
                # Các lỗi thường gặp: tính nhầm thành C_n^2, n^2, n, hoặc cộng/trừ sai
                sai_cn2 = n * (n - 1) // 2
                sai_n2 = n**2
                sai_pn = n # Chỉ là n
                offset = random.choice([1, -1, 2, n, -n])

                nhieu_val = random.choice([sai_cn2, sai_n2, kq_val + offset])
                if nhieu_val > 0 and nhieu_val != kq_val:
                    s_set.add('$%s$' % (latex(nhieu_val)))

            list_ans = ['\\True ' + da_dung] + list(s_set)
            random.shuffle(list_ans)

            # Câu hỏi
            noidungcauhoi = ('''Số vectơ khác $\\vec{0}$ có điểm đầu, điểm cuối là hai trong $%s$ đỉnh của %s $%s$ bằng bao nhiêu?'''
                             % (latex(n), ten_da_giac, nhan_dinh))

            # Nội dung lời giải
            loigiai = ('''Mỗi vectơ khác $\\vec{0}$ được xác định bởi một cặp điểm đầu và điểm cuối phân biệt.\\\\
                         Để tạo thành một vectơ khác $\\vec{0}$ từ các đỉnh của %s, ta cần chọn ra $2$ đỉnh trong số $%s$ đỉnh và sắp xếp thứ tự của chúng (đỉnh nào là điểm đầu, đỉnh nào là điểm cuối).\\\\
                         Số cách chọn và sắp xếp như vậy là số chỉnh hợp chập $2$ của $%s$ phần tử.\\\\
                         Vậy số vectơ thỏa mãn là $A_{%s}^2 = %s \\times (%s - 1) = %s$.'''
                       % (ten_da_giac, latex(n), latex(n), latex(n), latex(n), latex(n), latex(kq_val)))

            # Đáp án ngắn (Dạng số tự nhiên)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq_val))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

