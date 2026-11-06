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


def bt_dang28_p4_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo các thành phần cơ bản
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random
                # Chọn cặp (cơ số c, số mũ n) để k + 2 = c^n -> k = c^n - 2
                # Ví dụ: (2, 3) -> k = 6; (2, 4) -> k = 14; (3, 2) -> k = 7; (5, 2) -> k = 23
                params = [
                    {'c': 2, 'n': 3, 'k': 6},   # Giống bài mẫu
                    {'c': 2, 'n': 4, 'k': 14},
                    {'c': 2, 'n': 5, 'k': 30},
                    {'c': 3, 'n': 2, 'k': 7},
                    {'c': 3, 'n': 3, 'k': 25},
                    {'c': 5, 'n': 2, 'k': 23}
                ]

                selected = random.choice(params)
                c = selected['c']
                n = selected['n']
                k = selected['k']

                # Biểu diễn LaTeX cho log_c(a) + log_c(b)
                log_part = f"\\log_{{{c}}} a + \\log_{{{c}}} b"

                # Đáp án đúng: 1/2 * (n + log_c(a) + log_c(b))
                da_dung = f"\\frac{{1}}{{2}}({n} + {log_part})"

                # Bước 4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = [
                    f"\\frac{{1}}{{2}}({n+1} + {log_part})", # Sai hằng số
                    f"2({n} + {log_part})",                # Sai hệ số ngoài
                    f"{n} + {log_part}",                   # Thiếu 1/2
                    f"\\frac{{1}}{{2}}({n} - {log_part})", # Sai dấu
                    f"\\frac{{1}}{{2}}({n} + \\log_{{{c}}} (ab))", # Tuy đúng về toán học nhưng khác dạng yêu cầu (nếu muốn)
                    f"\\log_{{{c}}} a + \\log_{{{c}}} b - {n}"
                ]

                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Câu hỏi
                noidungcauhoi = ('''Với các số $a, b > 0$ thỏa mãn $a^2 + b^2 = %sab$, tính $\\log_{%s}(a+b)$.'''
                                 %(latex(k), latex(c)))

                # Các đáp án
                da_d = ('\\True $' + da_dung + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$' 
                da_s3 = '$' + str(das3) + '$' 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết lại y hệt cấu trúc bài mẫu)
                loigiai = ('''Ta có: $a^2 + b^2 = %sab \\Leftrightarrow a^2 + b^2 + 2ab = %sab + 2ab \\Leftrightarrow (a+b)^2 = %sab \\ (*)$. \\\\
                             Do $a, b > 0 \\Rightarrow \\begin{cases} ab > 0 \\\\ a+b > 0 \\end{cases}$, lấy logarit cơ số $%s$ hai vế của $(*)$ ta được: \\\\
                             $\\log_{%s}(a+b)^2 = \\log_{%s}(%sab) \\Leftrightarrow 2\\log_{%s}(a+b) = %s + \\log_{%s}a + \\log_{%s}b$ \\\\
                             $\\Leftrightarrow \\log_{%s}(a+b) = \\frac{1}{2}(%s + \\log_{%s}a + \\log_{%s}b)$.'''
                           %(latex(k), latex(k), latex(k+2), 
                             latex(c), 
                             latex(c), latex(c), latex(k+2), latex(c), latex(n), latex(c), latex(c),
                             latex(c), latex(n), latex(c), latex(c)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

