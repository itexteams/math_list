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


def bt_dang31_p3_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu cho Sympy
            t = symbols('t')

            # Danh sách dạng (để mở rộng sau này)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM ---
                # Chọn k sao cho k chia hết cho 6 để số luôn nguyên và đẹp
                k = 6 * random.randint(1, 3)  # k có thể là 6, 12, 18

                # Thời điểm t0 và vận tốc v0 tại đó
                t0 = random.randint(1, 3)
                v0 = random.randint(15, 30)

                # Khoảng thời gian tính quãng đường [t1, t2]
                t1 = random.randint(1, 4)
                t2 = random.randint(5, 10)

                # --- TÍNH TOÁN LỜI GIẢI ---
                # 1. Tìm v(t) = nguyên hàm a(t) = (k/2)*t^2 + C
                # v(t0) = v0 => C = v0 - (k/2)*t0^2
                C_val = v0 - (k//2) * (t0**2)

                def v_func(time):
                    return (k//2) * (time**2) + C_val

                # 2. Tính quãng đường s = tích phân v(t) từ t1 đến t2
                # s = [ (k/6)*t^3 + C*t ] từ t1 đến t2
                integral_v = (k//6) * (t**3) + C_val * t
                s_t1 = (k//6) * (t1**3) + C_val * t1
                s_t2 = (k//6) * (t2**3) + C_val * t2
                kq_dung = s_t2 - s_t1

                # --- BƯỚC 4: TẠO PHƯƠNG ÁN SAI (KHÔNG TRÙNG ĐÁP ÁN ĐÚNG) ---
                s_sai = set()
                while len(s_sai) < 3:
                    sai = kq_dung + random.choice([-20, -10, 10, 20, 15, -15, 5, -5])
                    if sai != kq_dung and sai > 0:
                        s_sai.add(f'${sai}$ m')

                list_sai = list(s_sai)
                da_dung = f'${kq_dung}$ m'

                # --- NỘI DUNG CÂU HỎI (BƯỚC 2) ---
                noidungcauhoi = (
                    f'Một vật chuyển động với gia tốc $a(t) = {k}t$ m/s$^2$. '
                    f'Vận tốc của vật tại thời điểm $t = {t0}$ giây là ${v0}$ m/s. '
                    f'Quãng đường vật đó đi được trong khoảng thời gian từ thời điểm $t = {t1}$ giây '
                    f'đến thời điểm $t = {t2}$ giây là'
                )

                # --- NỘI DUNG LỜI GIẢI (BƯỚC 2) ---
                loigiai = (
                    f'Từ giả thiết suy ra $v\'(t) = a(t) \\Rightarrow v(t) = \\int a(t) \\text{{d}}t = \\int {k}t \\text{{d}}t = {k//2}t^2 + C$. \\\\'
                    f'Mặt khác $v({t0}) = {v0}$ nên ${k//2} \\cdot {t0}^2 + C = {v0} \\Rightarrow C = {C_val}$. '
                    f'Do đó $v(t) = {k//2}t^2 + {C_val}$ (nếu $C < 0$ code cần xử lý dấu, ở đây chọn t0, v0 để $C > 0$). \\\\'
                    f'Quãng đường vật đó đi được trong khoảng thời gian từ thời điểm $t = {t1}$ giây đến thời điểm $t = {t2}$ giây là: \\\\'
                    f'$s = \\int_{{{t1}}}^{{{t2}}} v(t) \\text{{d}}t = \\int_{{{t1}}}^{{{t2}}} ({k//2}t^2 + {C_val}) \\text{{d}}t = ({k//6}t^3 + {C_val}t) \\Big|_{{{t1}}}^{{{t2}}} = {s_t2} - {s_t1} = {kq_dung}$ m.'
                )
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_dung))

                # Trộn đáp án
                list_all = ['\\True ' + da_dung, list_sai[0], list_sai[1], list_sai[2]]
                random.shuffle(list_all)

            # --- XUẤT KẾT QUẢ ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

