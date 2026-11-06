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


def bt_dang15_p1_b2_c3_ds12(self):
            # Khai báo biến
            # 1. Random số hạng tự do trong tích phân: a + f(x)
            a = randint(2, 9) 

            # 2. Random cận tích phân (để đáp án đẹp, giữ cận dưới = 0)
            can_duoi = 0
            can_tren = randint(1, 3) # Random cận trên là 1, 2 hoặc 3

            # 3. Tính toán giá trị đúng
            # I = int_{u}^{v} (a + f(x)) dx
            # I = a*(v - u) + F(v) - F(u)
            # Với F(x) = e^x và u=0 => F(u) = 1
            phan_hang_so = a * (can_tren - can_duoi) - 1  # -1 vì trừ đi F(0) = e^0 = 1

            # Hàm hỗ trợ hiển thị e^k trong LaTeX
            def format_e(n):
                if n == 1: return "e"
                return f"e^{n}"

            str_e = format_e(can_tren)

            # Đáp án đúng
            kq_dung = f"{phan_hang_so} + {str_e}"

            # 4. Tạo các đáp án nhiễu
            # Nhiễu 1: Quên trừ F(0) (tức là quên trừ 1)
            kq_nhieu1 = f"{phan_hang_so + 1} + {str_e}"

            # Nhiễu 2: Cộng nhầm hằng số a (tăng a lên 1 đơn vị)
            kq_nhieu2 = f"{phan_hang_so -1} + {str_e}"

            # Nhiễu 3: Sai dấu (trừ e thay vì cộng e, hoặc sai số hạng đầu)
            kq_nhieu3 = f"{phan_hang_so + 3} + {str_e}"

            # Danh sách đáp án
            du = [f'${kq_dung}$', f'${kq_nhieu1}$', f'${kq_nhieu2}$', f'${kq_nhieu3}$']

            # Đảo vị trí đáp án để tạo list_1
            list_1 = du.copy()
            random.shuffle(list_1)

            # Tìm vị trí đáp án đúng sau khi đảo để set \True
            # (Trong tool thi trắc nghiệm thường dùng \True trước đáp án đúng)
            # Ở code mẫu của bạn dùng cơ chế list_1[0] là đúng rồi shuffle,
            # nhưng ở đây tôi làm tường minh string để bạn dễ kiểm soát.
            # Để khớp với mẫu của bạn:
            da_d = '\\True ' + du[0] # Cái đầu tiên trong du là đúng
            da_s1 = du[1]
            da_s2 = du[2]
            da_s3 = du[3]

            final_choices = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(final_choices)

            # --- NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---

            noidungcauhoi = (
                'Biết $F(x)=e^x$ là một nguyên hàm của hàm số $f(x)$ trên $\\mathbb{R}$. '
                'Giá trị của $\\displaystyle\\int\\limits_{%s}^{%s}{\\left[ %s + f(x) \\right]\\text{d}x}$ bằng'
                % (can_duoi, can_tren, a)
            )

            loigiai = (
                'Ta có: $\\displaystyle\\int\\limits_{%s}^{%s}{\\left[ %s + f(x) \\right]\\text{d}x} '
                '= \\displaystyle\\int\\limits_{%s}^{%s}{%s \\text{d}x} + \\displaystyle\\int\\limits_{%s}^{%s}{f(x)\\text{d}x}$ \\\\\n'
                '$= %s x \\Big|_{%s}^{%s} + F(x) \\Big|_{%s}^{%s} $ \\\\\n'
                '$= %s(%s - %s) + F(%s) - F(%s) $ \\\\\n'
                '$= %s + e^{%s} - e^{%s} = %s + %s - 1 = %s$.'
                % (
                    can_duoi, can_tren, a,
                    can_duoi, can_tren, a, can_duoi, can_tren,
                    a, can_duoi, can_tren, can_duoi, can_tren,
                    a, can_tren, can_duoi, can_tren, can_duoi,
                    a * (can_tren - can_duoi), can_tren, can_duoi,
                    a * (can_tren - can_duoi), str_e, kq_dung
                )
            )

            # --- XUẤT RA ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(final_choices[0]) + '}\n'
                       '{' + str(final_choices[1]) + '}\n'
                       '{' + str(final_choices[2]) + '}\n'
                       '{' + str(final_choices[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

