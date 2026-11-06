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


def bt_dang25_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # T'(x) = -Ax + B
                # T(x) = -(A/2)x^2 + Bx + C
                # Đỉnh parabol (doanh thu max) tại x_max = B/A

                # Chọn A là số chẵn để A/2 nguyên (e.g. 10, 20, 30)
                A = random.choice([10, 20, 30])
                # Chọn x_max để B = A * x_max là số đẹp (e.g. 12, 15, 18, 20)
                x_max = random.choice([12, 15, 18, 20])
                B = A * x_max

                # Điều kiện ban đầu: Tại x_0, doanh thu là T_0
                x0 = random.choice([5, 8, 10])
                T0 = random.choice([8000, 10000, 12000, 15000])

                # Tính toán hằng số C
                # T0 = -(A/2)*x0^2 + B*x0 + C => C = T0 + (A/2)*x0^2 - B*x0
                C = T0 + (A//2)*(x0**2) - B*x0

                # Doanh thu cực đại T_max tại x_max
                T_max = -(A//2)*(x_max**2) + B*x_max + C

                # Kết quả cần tìm là x_max
                da_val = x_max
                da = '$%s$' % da_val

                # Bước 4: Các phương án sai xoay quanh x_max
                s_wrong = set()
                while len(s_wrong) < 3:
                    sai_offset = random.choice([-5, -3, -2, 2, 3, 5, 10])
                    sai_val = x_max + sai_offset
                    if sai_val > 0 and sai_val != x_max:
                        s_wrong.add('$%s$' % sai_val)

                list_wrong = list(s_wrong)
                das1, das2, das3 = list_wrong[0], list_wrong[1], list_wrong[2]

                # Tạo mã TikZ vẽ đồ thị Parabol doanh thu
                # Tính toán tọa độ hiển thị cho TikZ
                x_end = x_max * 1.8
                y_top = T_max * 1.2
                # Scale tỉ lệ để hình vẽ cân đối trong LaTeX
                x_scale = 4.0 / x_max
                y_scale = 3.0 / T_max



                # Câu hỏi (B2: Viết lại y hệt bài toán theo mẫu)
                noidungcauhoi = (r'''Chủ một trung tâm thương mại muốn cho thuê một số gian hàng như nhau. Người đó muốn tăng giá cho thuê của mỗi gian hàng thêm $x$ (triệu đồng) ($x \ge 0$). Tốc độ thay đổi doanh thu từ các gian hàng đó được biểu diễn bởi hàm số $T'(x) = -%sx + %s$, trong đó $T'(x)$ tính bằng triệu đồng. Biết rằng nếu người đó tăng giá thuê cho mỗi gian hàng thêm $%s$ triệu đồng thì doanh thu là $%s$ triệu đồng. Tìm giá trị của $x$ để người đó có doanh thu là cao nhất?
                ''' % (A, B, x0, T0))

                # Nội dung lời giải (Bám sát logic Câu 1 trong ảnh)
                loigiai = (r'''Ta có: $T(x) = \int T'(x) \text{d}x = \int (-%sx + %s) \text{d} x = -%sx^2 + %sx + C, C \in \mathbb{R}$. \\
                             Khi người đó tăng giá cho thuê mỗi gian hàng thêm $%s$ triệu đồng thì doanh thu là $%s$ triệu đồng. Nên ứng với $x = %s$ ta có $T(%s) = %s$, suy ra: \\
                             $%s = -%s \cdot %s^2 + %s \cdot %s + C \Rightarrow C = %s$. \\
                             Vậy $T(x) = -%sx^2 + %sx + %s$. \\
                             Ta có $T(x)$ là một hàm số bậc hai với hệ số $a = -%s < 0$ và đồ thị hàm số có đỉnh là $I(%s;%s)$. \\
                             Dựa vào tính chất của hàm số bậc hai, doanh thu cao nhất đạt được khi $x = %s$. \\
                             Khi đó doanh thu cao nhất là $%s$ triệu đồng và mỗi gian hàng đã tăng giá cho thuê thêm $%s$ triệu đồng.'''
                           % (A, B, A//2, B, 
                              x0, T0, x0, x0, T0,
                              T0, A//2, x0, B, x0, C,
                              A//2, B, C,
                              A//2, x_max, T_max,
                              x_max, T_max, x_max))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(x_max))

                # Đưa các đáp án vào danh sách
                da_d = '\\True ' + str(da)
                list_ans = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_ans)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

