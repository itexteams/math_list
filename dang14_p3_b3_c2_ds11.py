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


def bt_dang14_p3_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---

                # Số tầng của tháp (N)
                N = random.randint(8, 12)  # Random số tầng từ 8 đến 12

                # Công bội q = 1/2
                q = Rational(1, 2)

                # Diện tích mặt sàn tầng cuối (u_N) - Kết quả mong muốn là một số nguyên nhỏ
                target_uN = random.choice([8, 12, 16, 20, 24]) # Chọn các số chẵn dễ nhìn

                # u1 = u_N * 2^(N-1). Tính ngược u1 để đảm bảo u_N là số nguyên
                u1_base = int(math.pow(2, N - 1)) # Mẫu số 2^(N-1)
                u1 = target_uN * u1_base

                # Tính kết quả: Diện tích mặt sàn tầng trên cùng (tầng N)
                # u_N = u1 * q^(N-1)
                uN = u1 * q**(N - 1)

                # Kết quả đúng (là một số nguyên)
                kq = uN

                # --- Tạo các đáp án trắc nghiệm ---
                du = ['$%s$'%(latex(kq)),]
                da= random.choice(du)

                # Tạo các đáp án sai: xung quanh kết quả đúng
                da_sai_pool = set()

                # Đảm bảo tạo 3 đáp án sai khác nhau và > 0
                possible_offsets = [-4, -3, -2, -1, 1, 2, 3, 4]
                random.shuffle(possible_offsets)

                for offset in possible_offsets:
                    sai_val = kq + offset
                    if sai_val > 0 and sai_val != kq:
                        da_sai_pool.add(sai_val)
                    if len(da_sai_pool) == 3:
                        break

                # Lấy 3 đáp án sai từ pool
                s = [latex(i) for i in da_sai_pool]

                # Nếu không đủ 3 đáp án sai (ví dụ kq quá nhỏ), thêm đáp án dự phòng
                while len(s) < 3:
                    s.append(latex(kq + len(s) + 1)) # Thêm 1, 2, 3...

                das1 = '$%s$'%(s[0])
                das2 = '$%s$'%(s[1])
                das3 = '$%s$'%(s[2])

                # --- B1, B2: Nội dung câu hỏi và lời giải ---

                # Câu hỏi
                noidungcauhoi = ('''Một cái tháp có $%s$ tầng. Diện tích của mặt sàn tầng $2$ bằng $\\frac{1}{2}$ diện tích của mặt đáy tháp và diện tích của mặt sàn mỗi tầng bằng $\\frac{1}{2}$ diện tích của mặt sàn mỗi tầng ngay bên dưới. Biết mặt đáy tháp có diện tích là $%s\\text{ m}^2$. Diện tích của mặt sàn tầng trên cùng của tháp là bao nhiêu mét vuông?'''
                                  %(latex(N),latex(u1)
                                  ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Gọi diện tích mặt sàn tầng $n$ là $u_n$ với $n\\in \\mathbb{N}^*$. \\\\
                          Theo đề bài, diện tích mặt sàn tầng sau bằng $\\frac{1}{2}$ diện tích mặt sàn tầng ngay bên dưới, nên dãy $(u_n)$ lập thành một cấp số nhân với: \\\\
                          \\[\\text{Số hạng đầu (mặt đáy) } u_1 = %s\\text{ m}^2\\]
                          \\[\\text{Công bội } q = \\frac{1}{2}\\]
                          Diện tích mặt sàn tầng trên cùng chính là mặt tháp tầng $%s$, ta cần tính $u_{%s}$. \\\\
                          Áp dụng công thức số hạng tổng quát của cấp số nhân: $u_n = u_1 \\cdot q^{n-1}$. \\\\
                          \\[u_{%s} = u_1 \\cdot q^{%s-1} = %s \\cdot \\left(\\frac{1}{2}\\right)^{%s}\\]
                          \\[u_{%s} = %s \\cdot \\frac{1}{%s} = %s\\text{ m}^2\\]'''

                        %(latex(u1),
                          latex(N),latex(N),
                          latex(N),latex(N),latex(u1),latex(N-1),
                          latex(N),latex(u1),latex(u1_base),latex(kq),
                        ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))  

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')               
            return content 

