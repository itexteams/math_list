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


def bt_dang47_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Tìm cách random bài toán
                # Trong bài gốc, hệ số của x^2 là -6 (tức 2k = 6 => k = 3)
                # Ta chọn k ngẫu nhiên để bài toán luôn có nghiệm đẹp
                k = random.randint(2, 8) 
                he_so_x2 = 2 * k

                # Theo tính chất hàm trùng phương, diện tích trên = diện tích dưới khi:
                # m = 5/9 * k^2
                m_val = Rational(5 * k**2, 9)
                a = m_val.p
                b = m_val.q

                # Kết quả S = a + b
                kq_S = a + b

                # Các đáp án trắc nghiệm
                da = '$%s$' % (kq_S)

                # Bước 4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = kq_S + random.choice([-3, -2, -1, 1, 2, 3, 5, 10])
                    if sai != kq_S and sai > 0:
                        s.add('$%s$' % (sai))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Bước 2: Viết lại nội dung câu hỏi
                noidungcauhoi = (r'''Cho hàm số $y=x^4 - %sx^2 + m$ có đồ thị $(C_m)$. Giả sử $(C_m)$ cắt trục hoành tại bốn điểm phân biệt sao cho hình phẳng giới hạn bởi $(C_m)$ và trục hoành có phần phía trên trục hoành và phần phía dưới trục hoành có diện tích bằng nhau. Khi đó $m=\frac{a}{b}$ (với $a, b$ là các số nguyên, $b>0, \frac{a}{b}$ là phân số tối giản). Tính giá trị của biểu thức $S=a+b$.'''
                                 % (latex(he_so_x2)))

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Sử dụng \text{d}x theo yêu cầu)
                # Tính toán các giá trị trung gian cho lời giải
                k_sq = k**2
                he_so_loigiai_1 = 2 * k
                he_so_loigiai_2 = Rational(10 * k, 3) # Từ phương trình tích phân

                loigiai = (r'''Phương trình hoành độ giao điểm: $x^4 - %sx^2 + m = 0$ (1). \\
                             Đặt $t=x^2$ ($t \ge 0$), (1) trở thành $t^2 - %st + m = 0$ (2). \\
                             $(C_m)$ cắt trục hoành tại bốn điểm phân biệt thì phương trình (2) có hai nghiệm dương phân biệt $\Leftrightarrow \begin{cases} \Delta' = %s - m > 0 \\ P = m > 0 \\ S = %s > 0 \end{cases} \Leftrightarrow 0 < m < %s$ (*). \\
                             Gọi $t_1, t_2$ ($0 < t_1 < t_2$) là hai nghiệm của (2). Lúc đó (1) có 4 nghiệm: $x_1=-\sqrt{t_2}; x_2=-\sqrt{t_1}; x_3=\sqrt{t_1}; x_4=\sqrt{t_2}$. \\
                             Do tính đối xứng của đồ thị $(C_m)$ nên ta có: $\int_{0}^{x_3} (x^4 - %sx^2 + m) \text{d}x = \int_{x_3}^{x_4} (-x^4 + %sx^2 - m) \text{d}x$ \\
                             $\Rightarrow \int_{0}^{x_4} (x^4 - %sx^2 + m) \text{d}x = 0 \Leftrightarrow \frac{x_4^5}{5} - \frac{%s x_4^3}{3} + m x_4 = 0 \Leftrightarrow x_4^4 - %s x_4^2 + 5m = 0$. \\
                             Từ đó có $x_4$ là nghiệm của hệ: $\begin{cases} x_4^4 - %s x_4^2 + m = 0 \quad (3) \\ x_4^4 - %s x_4^2 + 5m = 0 \quad (4) \end{cases}$ \\
                             Lấy $(4) - (3) \Rightarrow %s x_4^2 = 4m \Rightarrow x_4^2 = \frac{%s}{3}m$. \\
                             Thay ngược vào (3) ta được phương trình theo $m$, giải ra ta được $m = \frac{%s}{%s}$. \\
                             Đối chiếu điều kiện (*) ta có $m = \frac{%s}{%s} \Rightarrow a = %s, b = %s$. \\
                             Vậy $S = %s$.'''
                           % (latex(he_so_x2), latex(he_so_x2), latex(k_sq), latex(he_so_x2), latex(k_sq),
                              latex(he_so_x2), latex(he_so_x2), latex(he_so_x2), latex(2*k), latex(he_so_loigiai_2),
                              latex(he_so_x2), latex(he_so_loigiai_2), latex(Rational(4*k, 3)), latex(k),
                              latex(a), latex(b), latex(a), latex(b), latex(a), latex(b), latex(kq_S)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

