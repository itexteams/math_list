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


def bt_dang20_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo danh sách dạng (ở đây chỉ có 1 dạng)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Random các thông số
                x0 = random.randint(1, 5)      # Hoành độ điểm I
                y0 = random.randint(1, 5)      # Tung độ điểm I
                k = random.randint(100,500) # Số mũ của a

                # 2. Tính toán các giá trị hiển thị trong đề
                hai_x0 = 2 * x0

                # 3. Tính đáp án đúng
                # Công thức: f(2x0 - a^k) = 2y0 - k
                kq_dung = 2 * y0 - k

                # 4. Tạo các phương án nhiễu (sai)
                # Đảm bảo các phương án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    # Nhiễu quanh giá trị k, y0 hoặc kết quả
                    sai = random.choice([
                        2 * y0 + k, 
                        k - 2 * y0, 
                        -kq_dung, 
                        y0 - k, 
                        2 * x0 - k,
                        -(2 * y0 + k)
                    ])
                    if sai != kq_dung:
                        s.add(sai)

                list_sai = list(s)

                # 5. Thiết lập nội dung câu hỏi (sử dụng LaTeX)
                noidungcauhoi = (
                    r"Đồ thị hàm số $y=f(x)$ đối xứng với đồ thị hàm số $y=\log_a x$, ($0 < a \neq 1$) "
                    r"qua điểm $I(%s; %s)$. Tính giá trị của biểu thức $f(%s - a^{%s})$."
                    % (latex(x0), latex(y0), latex(hai_x0), latex(k))
                )

                # 6. Các đáp án trắc nghiệm
                da_d = r'\True $%s$' % latex(kq_dung)
                da_s1 = r'$%s$' % latex(list_sai[0])
                da_s2 = r'$%s$' % latex(list_sai[1])
                da_s3 = r'$%s$' % latex(list_sai[2])

                # Đưa vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # 7. Nội dung lời giải chi tiết
                loigiai = (
                    r"Lấy điểm $A(%s - a^{%s}; f(%s - a^{%s}))$ thuộc đồ thị hàm số $y = f(x)$ "
                    r" và điểm $B(x; \log_a x)$ thuộc đồ thị hàm số $y = \log_a x$. \\ "
                    r"Hai điểm $A$ và $B$ đối xứng nhau qua điểm $I$ khi và chỉ khi: \\ "
                    r"$\begin{cases} %s - a^{%s} + x = 2 \cdot %s \\ f(%s - a^{%s}) + \log_a x = 2 \cdot %s \end{cases} "
                    r"\Leftrightarrow \begin{cases} x = a^{%s} \\ f(%s - a^{%s}) + \log_a a^{%s} = %s \end{cases}$ \\ "
                    r"$\Rightarrow f(%s - a^{%s}) + %s = %s \Rightarrow f(%s - a^{%s}) = %s$."
                    % (hai_x0, k, hai_x0, k, 
                       hai_x0, k, x0, hai_x0, k, y0, 
                       k, hai_x0, k, k, 2*y0, 
                       hai_x0, k, k, 2*y0, hai_x0, k, kq_dung)
                )

            # Xuất nội dung theo mẫu LaTeX
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

