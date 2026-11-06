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


def bt_dang41_p4_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B1: Nghiên cứu và ngẫu nhiên hóa các thông số
                # n_tong: Tổng số học sinh (thường từ 25 đến 35)
                n_tong = randint(25, 35)

                # n_nu: Số học sinh nữ (phải đảm bảo n >= 1 và n_nam >= 2 để chọn được 2 nam 1 nữ)
                n_nu = randint(10, n_tong - 5)
                n_nam = n_tong - n_nu

                # B2: Tính toán các giá trị tổ hợp và xác suất
                # Không gian mẫu n(Omega) = C(n_tong, 3)
                n_omega = binomial(n_tong, 3)

                # Số cách chọn 2 nam và 1 nữ: n(A) = C(n_nam, 2) * C(n_nu, 1)
                n_A = binomial(n_nam, 2) * binomial(n_nu, 1)

                # Xác suất theo giả thiết
                p_prob = Rational(n_A, n_omega)

                # Đáp án đúng là số học sinh nữ
                kq = n_nu
                da = '$%s$' % (latex(kq))

                # B3: Tạo các phương án sai không trùng đáp án đúng
                s_list = []
                while len(s_list) < 3:
                    sai = kq + random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
                    if 5 < sai < n_tong - 2 and sai != kq and str(sai) not in s_list:
                        s_list.append(str(sai))

                das1 = '$%s$' % (s_list[0])
                das2 = '$%s$' % (s_list[1])
                das3 = '$%s$' % (s_list[2])

                # B4: Nội dung câu hỏi
                noidungcauhoi = ('''Một lớp học có $%s$ học sinh gồm cả nam và nữ. Chọn ngẫu nhiên 3 học sinh để tham gia hoạt động của Đoàn trường. Xác suất chọn được 2 nam và 1 nữ là $%s$. Tính số học sinh nữ của lớp.'''
                                 % (latex(n_tong), latex(p_prob)))

                # Các đáp án được shuffle
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # B5: Nội dung lời giải chi tiết (Viết y hệt mẫu ảnh, dùng \left \right)
                loigiai = ('''Gọi số học sinh nữ của lớp là $n \\left(n \\in \\mathbb{N}^*, n \\le %s\\right)$. \\\\
            Suy ra số học sinh nam là $%s - n$. \\\\
            Không gian mẫu là chọn bất kì 3 học sinh từ $%s$ học sinh. Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^3$. \\\\
            Gọi $A$ là biến cố "Chọn được 2 học sinh nam và 1 học sinh nữ" \\\\
            - Chọn 2 nam trong $%s - n$ nam, có $C_{%s - n}^2$ cách. \\\\
            - Chọn 1 nữ trong $n$ nữ, có $C_n^1$ cách. \\\\
            Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = C_{%s - n}^2 \\cdot C_n^1$. \\\\
            Do đó xác suất của biến cố $A$ là $P\\left(A\\right) = \\frac{C_{%s - n}^2 \\cdot C_n^1}{C_{%s}^3}$. \\\\
            Theo giả thiết, ta có $P\\left(A\\right) = %s \\Leftrightarrow \\frac{C_{%s - n}^2 \\cdot C_n^1}{C_{%s}^3} = %s \\Leftrightarrow n = %s$. \\\\
            Vậy số học sinh nữ của lớp là $%s$ học sinh.'''
                           % (latex(n_tong - 2), latex(n_tong), latex(n_tong), latex(n_tong), 
                              latex(n_tong), latex(n_tong), latex(n_tong), latex(n_tong), 
                              latex(n_tong), latex(p_prob), latex(n_tong), latex(n_tong), 
                              latex(p_prob), latex(kq), latex(kq)
                             ))

            # Xuất câu trắc nghiệm (Không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

