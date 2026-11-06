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


def bt_dang34_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Hàm số có dạng y = sqrt(x - m) + sqrt(a*x - (m + b)) trên khoảng (k; +inf)
                # Trong đề gốc: a=2, b=1, k=0
                a = random.randint(2, 4)
                b = random.randint(1, 5)
                k = random.randint(-2, 3)

                # Tính toán các giá trị mấu chốt
                # m_zero là giá trị m mà tại đó m = (m+b)/a <=> m(a-1) = b
                m_zero = Rational(b, a - 1)

                # Kết quả đúng dựa trên logic: m <= a*k - b
                res_val = a * k - b

                # Đáp án đúng
                da_dung = f'm \\le {res_val}'

                # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s_options = [
                    f'm < {res_val}',
                    f'm \\le {res_val + 1}',
                    f'm \\le {res_val - 1}',
                    f'm \\ge {res_val}',
                    f'm < {res_val + 2}',
                    f'm \\le {k}'
                ]

                random.shuffle(s_options)
                selected_s = []
                for opt in s_options:
                    if opt != da_dung and len(selected_s) < 3:
                        selected_s.append(opt)

                # B2: Viết lại bài toán và lời giải theo mẫu
                # Câu hỏi
                noidungcauhoi = (r'''Tìm giá trị $m$ để hàm số $y = \sqrt{x - m} + \sqrt{%sx - m - %s}$ xác định với mọi $x$ thuộc khoảng $(%s; +\infty)$.'''
                                 %(latex(a), latex(b), latex(k)))

                # Các đáp án
                da_d = ('\\True $' + da_dung + '$')
                da_s1 = f'${selected_s[0]}$'
                da_s2 = f'${selected_s[1]}$'
                da_s3 = f'${selected_s[2]}$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Hàm số xác định khi $\begin{cases} x - m \ge 0 \\ %sx - m - %s \ge 0 \end{cases} \Leftrightarrow \begin{cases} x \ge m \\ x \ge \frac{m + %s}{%s} \end{cases} (*)$. \\
                           Nếu $m \ge \frac{m + %s}{%s} \Leftrightarrow m \ge %s$ thì $(*)$ trở thành $x \ge m$. \\
                           Khi đó tập xác định là $D = [m; +\infty)$. \\
                           Yêu cầu bài toán $\Leftrightarrow (%s; +\infty) \subset [m; +\infty) \Leftrightarrow m \le %s$. \\
                           Kết hợp điều kiện $m \ge %s$, trường hợp này có $m \in %s$. \\
                           Nếu $m \le \frac{m + %s}{%s} \Leftrightarrow m \le %s$ thì $(*)$ trở thành $x \ge \frac{m + %s}{%s}$. \\
                           Khi đó tập xác định là $D = \left[\frac{m + %s}{%s}; +\infty \right)$. \\
                           Yêu cầu bài toán $\Leftrightarrow (%s; +\infty) \subset \left[\frac{m + %s}{%s}; +\infty \right) \Leftrightarrow \frac{m + %s}{%s} \le %s \Leftrightarrow m \le %s$. \\
                           Kết hợp điều kiện $m \le %s$, ta được $m \le %s$. \\
                           Vậy $m \le %s$ là giá trị cần tìm.'''
                           %(latex(a), latex(b), latex(b), latex(a), 
                             latex(b), latex(a), latex(m_zero), 
                             latex(k), latex(k), 
                             latex(m_zero), r'\emptyset' if k < m_zero else f'[{m_zero}; {k}]',
                             latex(b), latex(a), latex(m_zero), latex(b), latex(a),
                             latex(b), latex(a),
                             latex(k), latex(b), latex(a), latex(b), latex(a), latex(k), latex(res_val),
                             latex(m_zero), latex(res_val),
                             latex(res_val)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

