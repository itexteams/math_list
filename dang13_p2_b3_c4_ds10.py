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


def bt_dang13_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')

            # --- BƯỚC 1: Random số liệu ---
            # Ta thiết lập: h(t) = a(t - t1)(t - t2)
            # Trong đó t2 là thời điểm chạm đất (nghiệm dương), t1 là nghiệm âm.
            # Để h(0) = c_val (độ cao ban đầu), ta tính a = c_val / (t1 * t2)

            t_cham_dat = random.choice([4, 5, 6, 8, 10])  # Thời điểm chạm đất (nghiệm dương)
            t1 = random.choice([-0.5, -1, -2])            # Nghiệm âm để parabol cắt trục tung tại c > 0
            c_val = random.choice([1.2, 1.5, 1.6, 2.0])   # Độ cao ban đầu

            # Tính hệ số a = c / (t1 * t2)
            a_val = float(simplify(c_val / (t1 * t_cham_dat)))
            # Khai triển h(t) = a(t^2 - (t1+t_cham_dat)t + t1*t_cham_dat)
            b_val = float(simplify(-a_val * (t1 + t_cham_dat)))

            # Tính tọa độ đỉnh
            t_dinh = float(simplify(-(b_val) / (2 * a_val)))
            t_limit = float(simplify(t_cham_dat + t1)) # Khoảng h(t) > c_val là (0, t1+t2)

            # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy
            def fmt(val):
                return latex(val).replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một quả bóng được đá lên từ độ cao $%s$ mét so với mặt đất. Biết quỹ đạo của quả bóng là một đường parabol trong mặt phẳng tọa độ $Oxy$ có phương trình $h(t)=%st^2 + %st + %s$ trong đó $t$ là thời gian (tính bằng giây) kể từ khi quả bóng được đá lên và $h$ là độ cao (tính bằng mét) của quả bóng.''' 
                             %(fmt(c_val), fmt(a_val), fmt(b_val), fmt(c_val)))

            ########################################################################
            # Khẳng định a: Thời điểm chạm đất (h(t) = 0)
            da_a_d = '\\True Quả bóng chạm mặt đất khi $t = %s$ giây' % (fmt(t_cham_dat))
            da_a_s = 'Quả bóng chạm mặt đất khi $t = %s$ giây' % (fmt(t_cham_dat + 1)) 
            list_da_a = [da_a_d, da_a_s]

            loigiai_a = ('''Quả bóng chạm đất khi $h(t)=0 \\Leftrightarrow %st^2 + %st + %s = 0$. Giải phương trình ta được $t = %s$ (nhận) hoặc $t = %s$ (loại). Vậy quả bóng chạm đất tại thời điểm $t = %s$ giây.''' 
                         %(fmt(a_val), fmt(b_val), fmt(c_val), fmt(t_cham_dat), fmt(t1), fmt(t_cham_dat)))

            ########################################################################
            # Khẳng định b: Tổng thời gian có độ cao lớn hơn h(0)
            da_b_d = '\\True Quả bóng có độ cao lớn hơn $%s$ mét so với mặt đất trong khoảng thời gian là $%s$ giây' % (fmt(c_val), fmt(t_limit))
            da_b_s = 'Quả bóng có độ cao lớn hơn $%s$ mét so với mặt đất trong thời gian là $%s$ giây' % (fmt(c_val), fmt(t_cham_dat))
            list_da_b = [da_b_d, da_b_s]

            loigiai_b = ('''Quả bóng ở độ cao lớn hơn $%s$ m khi $h(t) > %s \\Leftrightarrow %st^2 + %st + %s > %s \\Leftrightarrow %st^2 + %st > 0 \\Leftrightarrow 0 < t < %s$. Khoảng thời gian này kéo dài $%s - 0 = %s$ giây.''' 
                         %(fmt(c_val), fmt(c_val), fmt(a_val), fmt(b_val), fmt(c_val), fmt(c_val), fmt(a_val), fmt(b_val), fmt(t_limit), fmt(t_limit), fmt(t_limit)))

            ########################################################################
            # Khẳng định c: Thời điểm đạt độ cao lớn nhất
            da_c_d = '\\True Quả bóng đạt độ cao lớn nhất khi $t = %s$ giây' % (fmt(t_dinh))
            da_c_s = 'Quả bóng đạt độ cao lớn nhất khi $t = %s$ giây' % (fmt(t_dinh + 0.5))
            list_da_c = [da_c_d, da_c_s]

            loigiai_c = ('''Hàm số $h(t) = %st^2 + %st + %s$ đạt giá trị lớn nhất tại đỉnh của parabol có hoành độ $t = -\\frac{b}{2a} = -\\frac{%s}{2 \\cdot (%s)} = %s$.''' 
                         %(fmt(a_val), fmt(b_val), fmt(c_val), fmt(b_val), fmt(a_val), fmt(t_dinh)))

            ########################################################################
            # Khẳng định d: Khoảng thời gian cụ thể
            da_d_d = '\\True Quả bóng có độ cao lớn hơn $%s$ mét so với mặt đất trong khoảng thời gian $0 < t < %s$' % (fmt(c_val), fmt(t_limit))
            da_d_s = 'Quả bóng có độ cao lớn hơn $%s$ mét so với mặt đất trong khoảng thời gian $0 < t < %s$' % (fmt(c_val), fmt(t_cham_dat))
            list_da_d = [da_d_d, da_d_s]

            loigiai_d = ('''Dựa trên bất phương trình $h(t) > %s$ đã giải ở câu b, ta có quả bóng ở độ cao trên $%s$ mét khi $0 < t < %s$.''' % (fmt(c_val), fmt(c_val), fmt(t_limit)))

            # --- BƯỚC 2: Kiểm soát số lượng câu Đúng/Sai ---
            def count_true(ans_list):
                return sum('\\True' in a for a in ans_list)

            while True:
                a_final = random.choice(list_da_a)
                b_final = random.choice(list_da_b)
                c_final = random.choice(list_da_c)
                d_final = random.choice(list_da_d)

                if 1 <= count_true([a_final, b_final, c_final, d_final]) <= 3:
                    break

            # --- BƯỚC 3: Xuất nội dung ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(a_final) + '}\n'
                '{' + str(b_final) + '}\n'
                '{' + str(c_final) + '}\n'
                '{' + str(d_final) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

