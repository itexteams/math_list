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


def bt_dang50_p3_b3_c5_ds10(self):
            while True:
                # Random các thông số cơ bản
                # n1, n2 nhỏ để tổ hợp không quá lớn
                n1 = random.randint(5, 12)
                n2 = random.randint(5, 12)
                # p là bậc của x cần tìm (ví dụ bậc 4 hoặc 5)
                p = random.randint(4, 5)
                # a1, a2 nhỏ để lũy thừa không vượt ngưỡng
                a1 = random.choice([-2, -1, 1, 2])
                a2 = random.choice([-2, -1, 1, 2])

                # k = p - 1 (do nhân thêm x)
                # m = p - 2 (do nhân thêm x^2)
                k = p - 1
                m = p - 2

                # Tính toán hệ số thành phần
                # Kiểm tra n >= k và n >= m để math.comb không lỗi
                if n1 < k or n2 < m:
                    continue

                h1 = (a1**k) * math.comb(n1, k)
                h2 = (a2**m) * math.comb(n2, m)
                kq_val = h1 + h2

                # Điều kiện kết quả: -999 < kq_val < 9999
                if -999 < kq_val < 9999:
                    break

            # Định dạng hiển thị dấu cho a1, a2
            str_a1 = f"{a1:+}x" if a1 != 1 else "+x"
            if a1 == -1: str_a1 = "-x"

            str_a2 = f"{a2:+}x" if a2 != 1 else "+x"
            if a2 == -1: str_a2 = "-x"

            # Câu hỏi
            noidungcauhoi = (r'''Hệ số của $x^{%s}$ trong khai triển $P\left(x\right) = x\left(1 %sx\right)^{%s} + x^2\left(1 %sx\right)^{%s}$ bằng bao nhiêu?'''
                             % (latex(p), latex(str_a1), latex(n1), latex(str_a2), latex(n2)))

            # Đáp án đúng
            da_d = '\\True $%d$' % kq_val

            # Tạo các phương án nhiễu
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 10, -10, 2, -2, 5, -5])
                nhieu = kq_val + offset
                if nhieu != kq_val:
                    s_set.add('$%d$' % nhieu)

            list_ans = [da_d] + list(s_set)
            random.shuffle(list_ans)

            # Nội dung lời giải
            loigiai = (r'''Khai triển $P\left(x\right)$ có số hạng tổng quát là:\\
                         $T = x \cdot C_{%s}^{k} (1)^{%s-k} (%sx)^k + x^2 \cdot C_{%s}^{m} (1)^{%s-m} (%sx)^m$\\
                         $T = (%d)^k C_{%s}^k x^{k+1} + (%d)^m C_{%s}^m x^{m+2}$.\\
                         Số hạng chứa $x^{%s}$ ứng với:\\
                         $\begin{cases} k+1 = %s \\ m+2 = %s \end{cases} \Leftrightarrow \begin{cases} k = %s \\ m = %s \end{cases}$.\\
                         Vậy hệ số cần tìm là: $(%d)^{%s} C_{%s}^{%s} + (%d)^{%s} C_{%s}^{%s} = %d$.'''
                       % (latex(n1), latex(n1), latex(a1), latex(n2), latex(n2), latex(a2),
                          a1, latex(n1), a2, latex(n2),
                          latex(p), latex(p), latex(p), latex(k), latex(m),
                          a1, k, latex(n1), k, a2, m, latex(n2), m, kq_val))

            # Đáp án ngắn (Ghi kết quả số nguyên vào ô dapan)
            dapan = '\\shortans[0]{$%d$}\n' % kq_val

            # Xuất câu trắc nghiệm và dọn dẹp ký tự thừa
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + dapan +
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('++', '+').replace('(+', '(')

            return content

