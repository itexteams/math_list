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


def bt_dang56_p3_b2_c5_ds10(self):
            while True:
                # Giới hạn n1, n2, n3 nhỏ để tích giai thừa < 9999
                # n=4 giai thừa là 24, n=3 là 6, n=2 là 2.
                # Ví dụ: 4! * 3! * 2! * 3! = 24 * 6 * 2 * 6 = 1728 (Thỏa mãn)
                n1 = randint(2, 4)
                n2 = randint(2, 3)
                n3 = randint(2, 3)

                # Tính toán giá trị số tự nhiên
                f1 = math.factorial(n1)
                f2 = math.factorial(n2)
                f3 = math.factorial(n3)
                f_groups = 6 # 3! = 6

                kq_val = f1 * f2 * f3 * f_groups

                # Khống chế kết quả < 9999
                if 0 < kq_val < 9999:
                    break

            # Đáp án đúng dạng số tự nhiên
            da_dung_str = '$%s$' % (latex(kq_val))

            # Tạo các phương án nhiễu dạng số tự nhiên
            s_set = set()
            while len(s_set) < 3:
                # Các sai lầm thường gặp: quên hoán vị nhóm (f_groups=1), 
                # hoặc nhầm 3! thành 3, hoặc cộng các giai thừa.
                sai_1 = f1 * f2 * f3
                sai_2 = f1 * f2 * f3 * 3
                offset = random.choice([10, 20, 50, 100, -10, -20])

                nhieu_val = random.choice([sai_1, sai_2, kq_val + offset])

                if nhieu_val > 0 and nhieu_val != kq_val:
                    s_set.add('$%s$' % (latex(nhieu_val)))

            list_ans = ['\\True ' + da_dung_str] + list(s_set)
            random.shuffle(list_ans)

            # Câu hỏi
            noidungcauhoi = ('''Có $%s$ viên bi đen khác nhau, $%s$ viên bi đỏ khác nhau và $%s$ viên bi xanh khác nhau. Có bao nhiêu cách xếp các viên bi trên thành một dãy sao cho các viên bi cùng màu luôn ở cạnh nhau?'''
                             %(latex(n1), latex(n2), latex(n3)))

            # Nội dung lời giải chi tiết
            loigiai = ('''Để các viên bi cùng màu ở cạnh nhau, ta thực hiện các bước sau:\\\\
                         - Xếp $%s$ viên bi đen khác nhau: có $%s! = %s$ cách.\\\\
                         - Xếp $%s$ viên bi đỏ khác nhau: có $%s! = %s$ cách.\\\\
                         - Xếp $%s$ viên bi xanh khác nhau: có $%s! = %s$ cách.\\\\
                         - Xếp $3$ nhóm màu bi với nhau: có $3! = 6$ cách.\\\\
                         Theo quy tắc nhân, tổng số cách xếp thỏa mãn là: $%s \\times %s \\times %s \\times 6 = %s$ (cách).'''
                       %(latex(n1), latex(n1), latex(f1),
                         latex(n2), latex(n2), latex(f2),
                         latex(n3), latex(n3), latex(f3),
                         latex(f1), latex(f2), latex(f3), latex(kq_val)))

            # Đáp án ngắn (Số tự nhiên)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq_val))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

