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


def bt_dang44_p1_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random bài toán
                # Chọn m là số nguyên dương để đáp án đẹp
                m_val = randint(2, 8)
                # Tính diện tích S tương ứng: S = (1/3)*m^2
                S_val = Rational(m_val**2, 3)

                # Đáp án đúng
                kq = m_val

                # Bước 4: Điều chỉnh phương án sai không trùng đáp án đúng
                s = []
                while len(s) < 3:
                    sai = kq + random.choice([-3, -2, -1, 1, 2, 3, 4])
                    if sai > 0 and sai != kq and sai not in s:
                        s.append(sai)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                # Sử dụng latex(S_val) để hiển thị phân số nếu S không nguyên
                noidungcauhoi = (r'''Gọi $S$ là diện tích hình phẳng giới hạn bởi các đường $my = x^2$, $mx = y^2$ ($m > 0$). Giá trị của $m$ để $S = %s$ là'''
                                 % (latex(S_val)))

                # Các đáp án
                da_d = ('\\True $%s$' % (latex(kq)))
                da_s1 = ('$%s$' % (latex(das1)))
                da_s2 = ('$%s$' % (latex(das2)))
                da_s3 = ('$%s$' % (latex(das3)))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết lại y hệt mẫu hình ảnh, thay dx bằng \text{d}x)
                loigiai = (r'''Tọa độ giao điểm của hai đồ thị hàm số là nghiệm của hệ phương trình: $\begin{cases} my = x^2 & (1) \\ mx = y^2 & (2) \end{cases}$ \\
                             Thế (1) vào (2) ta được: $mx = \left( \frac{x^2}{m} \right)^2 \Leftrightarrow m^3x - x^4 = 0 \Leftrightarrow \begin{cases} x = 0 \\ x = m > 0 \end{cases}$ \\
                             Vì $y = \frac{x^2}{m} \ge 0$ nên $mx = y^2 \xrightarrow{y \ge 0} y = \sqrt{mx}$. \\
                             Khi đó diện tích hình phẳng cần tìm là: $S = \int\limits_{0}^{m} \left| \sqrt{mx} - \frac{x^2}{m} \right| \text{d}x = \left| \int\limits_{0}^{m} \left( \sqrt{mx} - \frac{x^2}{m} \right) \text{d}x \right|$ \\
                             $= \left| \left( \frac{2\sqrt{m}}{3} \cdot x^{\frac{3}{2}} - \frac{x^3}{3m} \right) \bigg|_{0}^{m} \right| = \left| \frac{2}{3}m^2 - \frac{1}{3}m^2 \right| = \frac{1}{3}m^2$. \\
                             Yêu cầu bài toán $S = %s \Leftrightarrow \frac{1}{3}m^2 = %s \Leftrightarrow m^2 = %s \Leftrightarrow m = \pm %s$. \\
                             Vì $m > 0$ nên $m = %s$.'''
                           % (latex(S_val), latex(S_val), latex(3*S_val), latex(kq), latex(kq)))

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

