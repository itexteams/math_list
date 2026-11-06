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


def bt_dang21_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Để đảm bảo sau 3s xe chưa dừng hẳn: v0 - a*3 > 0 => v0 > 3a
            a = random.randint(2, 4) # Hệ số gia tốc (m/s^2)
            v0 = random.randint(3*a + 5, 25) # Vận tốc ban đầu

            t = symbols('t')
            v_func = v0 - a*t

            # Tính quãng đường s(t) = tích phân v(t)dt với s(0) = 0
            s_func = v0*t - Rational(a, 2)*t**2

            # Tính giá trị tại 1s, 2s, 3s
            s1 = s_func.subs(t, 1)
            s2 = s_func.subs(t, 2)
            s3 = s_func.subs(t, 3)

            # Đáp án đúng
            kq_dung = f"{s1}m, {s2}m, {s3}m"

            # --- Tạo các phương án sai ---
            # Cách tạo: Thay đổi nhẹ các giá trị kết quả
            s_options = []
            offsets = [(-1, 1, 2), (1, -1, -2), (2, 2, 2), (-2, -2, -2), (1, 2, 3)]
            random.shuffle(offsets)

            for off in offsets:
                w1, w2, w3 = s1 + off[0], s2 + off[1], s3 + off[2]
                opt = f"{w1}m, {w2}m, {w3}m"
                if opt != kq_dung:
                    s_options.append(opt)

            # Lấy 3 đáp án sai
            das1 = s_options[0]
            das2 = s_options[1]
            das3 = s_options[2]

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (r'''Một ô tô đang chạy với tốc độ $%s m/s$ thì hãm phanh và chuyển động chậm dần đều với tốc độ $v(t) = %s - %st (m/s)$. Kể từ khi hãm phanh, quãng đường ô tô đi được sau $1$ giây, $2$ giây, $3$ giây lần lượt là bao nhiêu?'''
                            %(latex(v0), latex(v0), latex(a)))

            # --- Nội dung lời giải ---
            loigiai = (r'''Gọi $s(t)$ là quãng đường ô tô đi được kể từ khi hãm phanh cho đến thời điểm $t$ giây. \\
                        Do $s'(t) = v(t)$, nên: \\
                        $s(t) = \int v(t) \text{d}t = \int (%s - %st) \text{d}t = %st - %st^2 + C$. \\
                        Mặt khác, do mốc thời gian được tính kể từ khi hãm phanh, nên $s(0) = 0 \Rightarrow C = 0$. \\
                        Vậy $s(t) = %st - %st^2$. \\
                        Quãng đường ô tô đi được sau 1 giây: $s(1) = %s(1) - %s(1)^2 = %s(m)$. \\
                        Quãng đường ô tô đi được sau 2 giây: $s(2) = %s(2) - %s(2)^2 = %s(m)$. \\
                        Quãng đường ô tô đi được sau 3 giây: $s(3) = %s(3) - %s(3)^2 = %s(m)$.'''
                        %(latex(v0), latex(a), latex(v0), latex(Rational(a, 2)), 
                          latex(v0), latex(Rational(a, 2)),
                          latex(v0), latex(Rational(a, 2)), latex(s1),
                          latex(v0), latex(Rational(a, 2)), latex(s2),
                          latex(v0), latex(Rational(a, 2)), latex(s3)
                        ))

            # --- Trình bày các đáp án ---
            da_d = r'\True $' + kq_dung + '$'
            list_1 = [da_d, f'${das1}$', f'${das2}$', f'${das3}$']
            random.shuffle(list_1)

            # --- Xuất kết quả ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

