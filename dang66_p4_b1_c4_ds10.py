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


def bt_dang66_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các thông số (L: khoảng cách, v1: vận tốc tàu 1, v2: vận tốc tàu 2)
                # Chọn các giá trị để kết quả không quá phức tạp
                L = random.randint(4, 12)
                v1 = random.randint(5, 10)
                v2 = random.randint(5, 10)

                # Tính các hệ số của phương trình d^2 = at^2 + bt + c
                a = v1**2 + v2**2
                b = 2 * L * v2
                c = L**2

                # Thời điểm t để d nhỏ nhất: t = b / (2a)
                t_min = Rational(b, 2 * a)

                # Phần dư để hoàn thành bình phương: c - a*(t_min^2)
                phan_du = c - a * (t_min**2)

                # Giá trị d_min = sqrt(phan_du)
                d_min_sq = phan_du
                d_min_tex = latex(sp.sqrt(d_min_sq))

                # Bước 2: Tạo đáp án đúng và các đáp án sai (không trùng nhau)
                da = '$%s$' % latex(t_min)

                s = set()
                while len(s) < 3:
                    # Tạo các phương án sai bằng cách thay đổi tử số hoặc mẫu số
                    sai1 = Rational(random.randint(1, 15), a)
                    sai2 = Rational(L * v1, a)
                    sai3 = Rational(v2, v1 + v2)
                    sai4 = Rational(v1, a)
                    for i in [sai1, sai2, sai3, sai4]:
                        if i != t_min:
                            s.add('$%s$' % latex(i))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Bước 3: Nội dung câu hỏi
                noidungcauhoi = (
                    f"Hai con tàu đang ở cùng một vĩ tuyến và cách nhau ${L}$ hải lý. "
                    f"Đồng thời cả hai con tàu cùng khởi hành, một tàu chạy về hướng nam với ${v1}$ hải lý/giờ, "
                    f"còn tàu kia chạy về vị trí hiện tại của tàu thứ nhất với vận tốc ${v2}$ hải lý/giờ. "
                    f"Tìm thời điểm mà khoảng cách của hai tàu là nhỏ nhất."
                )

                # Bước 4: Nội dung lời giải (theo đúng cấu trúc hình ảnh)
                loigiai = (
                    f"Gọi $d$ là khoảng cách của hai tàu sau khi xuất phát $t$ (giờ), $t > 0$.\\\\ "
                    f"Ta có: $d^2 = AB_1^2 + AA_1^2 = ({L} - {v2}t)^2 + ({v1}t)^2 = {a}t^2 - {b}t + {c}$.\\\\ "
                    f"Suy ra $d = d(t) = \\sqrt{{{a}t^2 - {b}t + {c}}} = \\sqrt{{{a}\\left( t - {latex(t_min)} \\right)^2 + {latex(phan_du)}}} \\ge {d_min_tex}$.\\\\ "
                    f"Khi đó $d_{{min}} = {d_min_tex}$. Dấu \"=\" xảy ra $\\Leftrightarrow t = {latex(t_min)}$.\\\\ "
                    f"Vậy sau ${latex(t_min)}$ giờ xuất phát thì khoảng cách hai tàu là nhỏ nhất."
                )

                # Bước 5: Đóng gói các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

