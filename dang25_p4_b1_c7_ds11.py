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


def bt_dang25_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo danh sách dạng
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Hàm số có dạng: y = x^3 - m*x^2 + (Am + B)x + C
                # Ở đề bài gốc: A = 2, B = -3, C = -1
                m=symbols('m')
                A = random.randint(1, 5)
                # Để có thể ra trường hợp (m-k)^2 < 0 như đề bài (m rỗng)
                # Ta cần Delta' = m^2 - 3(Am + B) là một bình phương đầy đủ và có dạng (m-k)^2
                # m^2 - 3Am - 3B = (m - 3A/2)^2 => Cần 3A chia hết cho 2 và -3B = (3A/2)^2

                mode = random.choice(['empty', 'range']) # Chọn ngẫu nhiên kiểu đáp án

                if mode == 'empty':
                    # Tạo trường hợp vô nghiệm (giống đề gốc)
                    k = random.randint(1, 5) * 2 # k chẵn để A = 2*k/3 đẹp hơn, hoặc chọn A trực tiếp
                    # Delta' = (m - k)^2 = m^2 - 2km + k^2
                    # So sánh với m^2 - 3Am - 3B: 3A = 2k => A = 2k/3, -3B = k^2 => B = -k^2/3
                    # Để số đẹp, chọn k là bội của 3
                    k = random.choice([3, 6, 9])
                    A_val = int(2*k/3)
                    B_val = int(-k**2/3)
                else:
                    # Tạo trường hợp có khoảng nghiệm
                    A_val = random.randint(1, 4)
                    B_val = random.randint(1, 5)

                C_val = random.randint(-10, 10)

                # Thiết lập biểu thức
                y = x**3 - m*x**2 + (A_val*m + B_val)*x + C_val
                y_prime = 3*x**2 - 2*m*x + (A_val*m + B_val)

                # Tính Delta' của y' theo biến x
                # Delta' = (-m)^2 - 3*(A_val*m + B_val)
                delta_p = m**2 - 3*A_val*m - 3*B_val
                delta_p_simplified = simplify(delta_p)

                # Giải bất phương trình delta_p < 0
                sol = solve_univariate_inequality(delta_p_simplified < 0, m, relational=False)

                # --- Xử lý nội dung câu hỏi ---
                # Chú ý hiển thị dấu +- thành -
                expr_x = latex(A_val*m + B_val).replace('+-', '-')
                noidungcauhoi = (r'Tìm $m$ để mọi tiếp tuyến của đồ thị hàm số $y = x^3 - mx^2 + (%s)x %s$ đều có hệ số góc dương.'
                                 % (expr_x, latex(C_val) if C_val < 0 else '+ ' + str(C_val)))

                # --- Xử lý đáp án ---
                if sol == EmptySet:
                    da_dung = r'$m \in \varnothing$'
                    s = [r'$m \neq %s$' % random.randint(1, 5), 
                         r'$m > %s$' % random.randint(0, 3), 
                         r'$m < %s$' % random.randint(1, 4),
                         r'$m \in \mathbb{R}$']
                else:
                    da_dung = '$%s$' % latex(sol)
                    s = [r'$m \in \varnothing$', 
                         r'$m \neq 1$', 
                         r'$m > 0$', 
                         r'$m < 5$']

                da_d = '\\True ' + da_dung
                random.shuffle(s)
                da_s1, da_s2, da_s3 = s[0], s[1], s[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Xử lý lời giải ---
                loigiai = (r'''Hệ số góc tiếp tuyến của đồ thị hàm số $y = %s$ tại tiếp điểm $M(x_0; y_0)$ là: \\
                           $y'(x_0) = %s$. \\
                           Hệ số góc luôn dương $\Leftrightarrow y'(x_0) > 0, \forall x_0 \in \mathbb{R} \Leftrightarrow \begin{cases} 3 > 0 \\ \Delta' < 0 \end{cases}$ \\
                           $\Leftrightarrow %s < 0$. \\
                           Kết quả: %s.'''
                           % (latex(y), latex(y_prime).replace('x', 'x_0'), latex(delta_p_simplified), da_dung))

            # B2: Xuất câu trắc nghiệm đúng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

