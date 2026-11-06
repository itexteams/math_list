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


def bt_dang38_p3_b2_c5_ds10(self):
            while True:
                # Thiết lập dải số ngẫu nhiên
                n1 = randint(5, 10)  # Số học sinh nam
                n2 = randint(5, 12)  # Số học sinh nữ
                k_tong = randint(3, 5) # Tổng số chọn ra
                k1 = randint(1, k_tong - 1) # Số nam chọn ra (ít nhất 1 nam, 1 nữ)
                k2 = k_tong - k1 # Số nữ chọn ra

                # Kiểm tra tính hợp lệ của k so với n
                if k1 > n1 or k2 > n2:
                    continue

                # Tính toán giá trị trung gian và kết quả cuối
                val_c1 = math.comb(n1, k1)
                val_c2 = math.comb(n2, k2)
                kq_val = val_c1 * val_c2

                # Khống chế kết quả < 9999
                if 0 < kq_val < 9999:
                    break

            # Đáp án đúng dạng số tự nhiên
            da_dung = '$%s$' % (latex(kq_val))

            # Tạo các phương án sai (nhiễu số học)
            s_set = set()
            while len(s_set) < 3:
                # Các bẫy: Quy tắc cộng, dùng Chỉnh hợp, hoặc tính nhầm n, k
                sai_quy_tac_cong = val_c1 + val_c2
                sai_chinh_hop = math.perm(n1, k1) * math.perm(n2, k2)
                offset = random.choice([1, 10, -10, 50, -50, 100])

                nhieu_val = random.choice([sai_quy_tac_cong, sai_chinh_hop, kq_val + offset])

                if nhieu_val > 0 and nhieu_val != kq_val and nhieu_val < 20000:
                    s_set.add('$%s$' % (latex(nhieu_val)))

            list_ans = ['\\True ' + da_dung] + list(s_set)
            random.shuffle(list_ans)

            # Câu hỏi
            noidungcauhoi = ('''Một tổ có $%s$ học sinh nam và $%s$ học sinh nữ. Hỏi có bao nhiêu cách chọn $%s$ học sinh đi lao động trong đó có đúng $%s$ học sinh nam?'''
                             %(latex(n1), latex(n2), latex(k_tong), latex(k1)))

            # Nội dung lời giải chi tiết
            loigiai = ('''Để chọn ra $%s$ học sinh gồm $%s$ nam và $%s$ nữ, ta thực hiện hai bước: \\\\
                         - Bước 1: Chọn $%s$ nam từ $%s$ nam. Số cách chọn là $C_{%s}^{%s} = %s$ (cách). \\\\
                         - Bước 2: Chọn $%s$ nữ từ $%s$ nữ. Số cách chọn là $C_{%s}^{%s} = %s$ (cách). \\\\
                         Theo quy tắc nhân, tổng số cách chọn thỏa mãn yêu cầu là: $%s \\times %s = %s$ (cách).'''
                       %(latex(k_tong), latex(k1), latex(k2),
                         latex(k1), latex(n1), latex(n1), latex(k1), latex(val_c1),
                         latex(k2), latex(n2), latex(n2), latex(k2), latex(val_c2),
                         latex(val_c1), latex(val_c2), latex(kq_val)))

            # Đáp án ngắn (Số tự nhiên)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq_val))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

