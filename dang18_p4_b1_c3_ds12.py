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


def bt_dang18_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Random vận tốc đầu v0 từ 50 đến 100 m/s
                v0 = random.randint(50, 95)
                # Random độ cao bắt đầu s0 từ 1 đến 10 m
                s0 = random.randint(1, 10)
                # Random thời điểm t từ 3 đến 8 giây
                t_val = random.randint(3, 8)

                # Hằng số gia tốc trọng trường
                g_acc = 9.8
                g_half = 4.9

                # Tính toán kết quả chính xác
                # Công thức: s(t) = -4.9*t^2 + v0*t + s0
                kq_num = -g_half * (t_val**2) + v0 * t_val + s0

                # Định dạng kết quả dùng dấu phẩy cho số thập phân
                kq_str = str(Decimal(str(kq_num)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

                # --- B4: Điều chỉnh các phương án sai không trùng đáp án đúng ---
                da = f'${kq_str}$'

                s_wrong = set()
                while len(s_wrong) < 3:
                    # Tạo sai số ngẫu nhiên từ -10 đến 10 (không tính 0)
                    offset = random.choice([i for i in range(-15, 16) if i != 0])
                    wrong_val = kq_num + offset
                    # Định dạng phương án sai
                    wrong_str = str(Decimal(str(wrong_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    val_latex = f'${wrong_str}$'
                    if val_latex != da:
                        s_wrong.add(val_latex)

                list_wrong = list(s_wrong)
                das1, das2, das3 = list_wrong[0], list_wrong[1], list_wrong[2]

                # --- B2: Viết lại đề bài và lời giải theo mẫu ---
                # Nội dung câu hỏi
                noidungcauhoi = (
                    f"Một viên đạn được bắn lên trời (phương thẳng đứng) với vận tốc là ${v0} m/s$ bắt đầu từ ${s0} m$. "
                    f"Hãy xác định chiều cao của viên đạn sau thời gian ${t_val} s$ kể từ lúc bắn."
                )

                # Nội dung lời giải (trình bày y hệt hình mẫu)
                loigiai = (
                    f"Ta có vận tốc của viên đạn tại thời điểm $t$ là $v(t) = \\int -9,8 \\text{{d}}t = -9,8t + C_1$. \\\\\n"
                    f"Do $v(0) = {v0}$ nên $v(0) = -9,8 \\cdot 0 + C_1 = {v0} \\Leftrightarrow C_1 = {v0} \\Rightarrow v(t) = -9,8t + {v0}$. \\\\\n"
                    f"Độ cao của viên đạn tại thời điểm $t$ là \\\\\n"
                    f"$s(t) = \\int v(t) \\text{{d}}t = \\int (-9,8t + {v0}) \\text{{d}}t = -4,9t^2 + {v0}t + C_2$. \\\\\n"
                    f"Vì $s(0) = {s0}$ nên $s(0) = -4,9 \\cdot 0^2 + {v0} \\cdot 0 + C_2 = {s0} \\Leftrightarrow C_2 = {s0} \\Rightarrow s(t) = -4,9t^2 + {v0}t + {s0}$. \\\\\n"
                    f"Vậy sau khoảng thời gian ${t_val} s$ kể từ lúc bắn, viên đạn ở độ cao \\\\\n"
                    f"$s({t_val}) = -4,9 \\cdot {t_val}^2 + {v0} \\cdot {t_val} + {s0} = {kq_str} (m)$."
                )

                # Chuẩn bị danh sách đáp án để shuffle
                da_d = '\\True ' + da
                list_ans = [da_d, das1, das2, das3]
                random.shuffle(list_ans)

            # Xuất câu trắc nghiệm theo định dạng Minipage/Ex
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

