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


def bt_dang50_p1_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- Random dữ liệu đầu vào ---
                # Chọn u1 là một số chẵn ngẫu nhiên từ 100 đến 3000 để kết quả chia 2 ra số nguyên
                u1_val = randint(50, 1500) * 2

                # Kết quả giới hạn (limit = u1 / 2)
                ket_qua = u1_val // 2

                # --- Các đáp án trắc nghiệm ---
                # Đáp án đúng
                da_dung = ket_qua

                # Sinh các đáp án sai (nhiễu)
                # Nhiễu 1: u1 (quên chia 2)
                nhieu1 = u1_val
                # Nhiễu 2: u1 / 4 (tính sai hệ số)
                nhieu2 = u1_val // 4
                # Nhiễu 3: Một số ngẫu nhiên gần đáp án đúng
                nhieu3 = ket_qua + randint(1, 10) * random.choice([-1, 1])
                if nhieu3 == ket_qua: nhieu3 += 1 # Tránh trùng đáp án đúng

                du = ['$%s$' % latex(da_dung)]
                da = random.choice(du)

                s = [
                    '$%s$' % latex(nhieu1),
                    '$%s$' % latex(nhieu2),
                    '$%s$' % latex(nhieu3)
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- Nội dung câu hỏi ---
                noidungcauhoi = (
                    '''Cho dãy số $(u_n)$ được xác định như sau $u_1 = %s; u_{n-1} = n^2(u_{n-1} - u_n)$, với mọi $n \\in \\mathbb{N}^*, n \\ge 2$, giới hạn của dãy số $(u_n)$ bằng'''
                    % (latex(u1_val))
                )

                # --- Các đáp án để hiển thị ---
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải ---
                # Ta chuẩn bị các chuỗi latex cho lời giải
                # Công thức tổng quát: u_n = (n+1)/(2n) * u1
                # Giá trị cuối cùng của u_n khi rút gọn u1: (n+1)/n * ket_qua

                loigiai = ('''Ta có $u_{n-1} = n^2(u_{n-1} - u_n) \\Leftrightarrow u_{n-1}(n^2 - 1) = n^2 u_n \\Leftrightarrow u_n = \\dfrac{n-1}{n} \\cdot \\dfrac{n+1}{n} \\cdot u_{n-1}$. \\\\
                Khi đó ta có: \\\\
                $u_2 = \\dfrac{1}{2} \\cdot \\dfrac{3}{2} \\cdot u_1$ \\\\
                $u_3 = \\dfrac{2}{3} \\cdot \\dfrac{4}{3} \\cdot u_2$ \\\\
                $\\dots$ \\\\
                $u_n = \\dfrac{n-1}{n} \\cdot \\dfrac{n+1}{n} \\cdot u_{n-1}$ \\\\
                Nhân theo vế các đẳng thức trên ta có $u_n = \\dfrac{n+1}{2n} \\cdot u_1 = \\dfrac{n+1}{n} \\cdot %s$. \\\\
                Vậy $\\lim_{n \\to +\\infty} u_n = %s$.'''
                % (latex(ket_qua), latex(ket_qua)))

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +
                '\n\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

