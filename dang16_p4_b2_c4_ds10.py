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


def bt_dang16_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Trong đề gốc: (4; 2018), m+1 <= 4 => m <= 3. 
                # Ta sẽ random cận dưới 'a' của khoảng (a; b)
                # Hàm số y = x^2 - 2(m+k)x - 3. Trục đối xứng x = m+k.

                a_val = random.randint(2, 10) # Cận dưới của khoảng đồng biến
                b_val = random.randint(2000, 3000) # Cận trên của khoảng đồng biến
                k_val = random.randint(1, 5) # Hệ số k trong (m + k)

                # Hàm số: y = x^2 - 2(m + k)x - 3
                # Trục đối xứng: x_0 = m + k
                # Hàm đồng biến trên (m + k; +inf)
                # Để đồng biến trên (a_val; b_val) thì (a_val; b_val) con (m + k; +inf)
                # <=> m + k <= a_val <=> m <= a_val - k

                limit_m = a_val - k_val

                # Đảm bảo limit_m >= 1 để có ít nhất 1 giá trị nguyên dương
                if limit_m < 1:
                    limit_m = 1
                    a_val = limit_m + k_val

                # Đáp án đúng: số các giá trị nguyên dương m là limit_m (từ 1 đến limit_m)
                kq = limit_m

                # --- B4: Điều chỉnh các phương án sai ---
                du = [f'${kq}$']
                da = random.choice(du)

                # Tạo danh sách các phương án nhiễu không trùng đáp án đúng
                s = []
                candidates = [kq + 1, kq + 2, kq + 3, kq - 1, kq + 4, 0]
                for c in candidates:
                    if c >= 0 and c != kq:
                        s.append(f'${c}$')

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # --- B2: Viết lại nội dung câu hỏi (giống ảnh) ---
                noidungcauhoi = (f'Tìm số giá trị nguyên dương của tham số $m$ để hàm số '
                                 f'$y = x^2 - 2(m + {k_val})x - 3$ đồng biến trên khoảng $({a_val}; {b_val})$.')

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- B2: Nội dung lời giải (giống cấu trúc trong ảnh) ---
                # Liệt kê các giá trị m nếu số lượng ít, nếu nhiều thì ghi khoảng
                if kq <= 5:
                    ds_m = ", ".join([str(i) for i in range(1, kq + 1)])
                else:
                    ds_m = f"1, 2, ..., {kq}"

                loigiai = (f'Hàm số có $a = 1 > 0, \\frac{{-b}}{{2a}} = m + {k_val}$ nên đồng biến trên khoảng $(m + {k_val}; +\\infty)$. \\\\'
                           f'Do đó để hàm số đồng biến trên khoảng $({a_val}; {b_val})$ thì ta phải có \\\\'
                           f'$$({a_val}; {b_val}) \\subset (m + {k_val}; +\\infty) \\Leftrightarrow m + {k_val} \\le {a_val} \\Leftrightarrow m \\le {limit_m}.$$ \\\\'
                           f'Vậy có {kq} giá trị nguyên dương của $m$ thỏa mãn yêu cầu bài toán là {ds_m}.')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

