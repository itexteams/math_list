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


def bt_dang20_p3_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Random các thông số b (cơ số log) và k (cơ số mẫu số)
                # Trong đề gốc b=3, k=9
                b = random.choice([2, 3, 5])
                k = random.randint(4, 10)

                # Đáp án đúng luôn là 2
                kq = 2

                # B4: Tạo các phương án sai không trùng với đáp án đúng
                s = [1, 3, 4, 5, 0]
                random.shuffle(s)

                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Câu hỏi
                noidungcauhoi = (r'''Gọi $a$ là giá trị nhỏ nhất của $f(n)=\frac{\log_{%s} 2 \cdot \log_{%s} 3 \dots \log_{%s} n}{%s^n}$ với $n \in \mathbb{N}$ và $n \ge 2$. Số giá trị của $n$ để $f(n)=a$ bằng bao nhiêu?'''
                                 % (latex(b), latex(b), latex(b), latex(k)))

                # Các đáp án
                da_d = r'\True $%s$' % (latex(kq))
                da_s1 = '$%s$' % (latex(das1))
                da_s2 = '$%s$' % (latex(das2))
                da_s3 = '$%s$' % (latex(das3))

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Sử dụng logarit cơ số b^k để giải thích giống mẫu
                bk = b**k
                loigiai = (r'''Ta xét tỷ số giữa hai số hạng liên tiếp: $\frac{f(n+1)}{f(n)} = \frac{\log_{%s}(n+1)}{%s}$. \\
                           - Nếu $\frac{\log_{%s}(n+1)}{%s} < 1 \Leftrightarrow n+1 < %s^{%s} \Leftrightarrow n < %s - 1$, khi đó $f(n+1) < f(n)$ (hàm giảm). \\
                           - Nếu $\frac{\log_{%s}(n+1)}{%s} = 1 \Leftrightarrow n+1 = %s^{%s} \Leftrightarrow n = %s - 1$, khi đó $f(n+1) = f(n)$. \\
                           - Nếu $\frac{\log_{%s}(n+1)}{%s} > 1 \Leftrightarrow n+1 > %s^{%s} \Leftrightarrow n > %s - 1$, khi đó $f(n+1) > f(n)$ (hàm tăng). \\
                           Do đó, $f(n)$ đạt giá trị nhỏ nhất tại $n = %s - 1$ và $n = %s$. \\
                           Vậy có $2$ giá trị của $n$ thỏa mãn.'''
                           % (latex(b), latex(k), 
                              latex(b), latex(k), latex(b), latex(k), latex(bk),
                              latex(b), latex(k), latex(b), latex(k), latex(bk),
                              latex(b), latex(k), latex(b), latex(k), latex(bk),
                              latex(bk), latex(bk)
                             ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(bk))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

