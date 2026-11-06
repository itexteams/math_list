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


def bt_dang35_p1_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Chọn hệ số a chia hết cho 3 để nghiệm t_max = a/3 là số nguyên đẹp
                # Đồng thời vận tốc lớn nhất v_max = a^2 / 3 cũng là số nguyên đẹp
                a = random.choice([3, 6, 9, 12, 15])

                t_max = a // 3
                v_max = (a**2) // 3

                # Tạo chuỗi hiển thị quy luật S = a*t^2 - t^3
                quy_luat_S = "%s t^2 - t^3" % a

                # Đáp án đúng (thời điểm t)
                da = "$%s$ (s)" % t_max

                # Tạo danh sách các phương án nhiễu logic từ bài toán
                s = [
                    "$%s$ (s)" % v_max,
                    "$%s$ (s)" % a,
                    "$%s$ (s)" % (2 * t_max),
                    "$%s$ (s)" % (t_max + 1),
                    "$%s$ (s)" % (t_max + 2)
                ]

                # Lọc trùng và loại bỏ đáp án đúng khỏi danh sách nhiễu
                s = list(set(s))
                if da in s:
                    s.remove(da)

                # SỬA LỖI: Kiểm tra và bổ sung thêm nhiễu nếu danh sách s không đủ 3 phần tử
                while len(s) < 3:
                    # Sinh thêm một số ngẫu nhiên từ 1 đến 20 (hoặc tùy bạn chọn khoảng)
                    new_s = "$%s$ (s)" % random.randint(1, 20)
                    if new_s != da and new_s not in s:
                        s.append(new_s)

                # Lấy ngẫu nhiên 3 phương án nhiễu khác nhau bằng random.sample
                das1, das2, das3 = random.sample(s, 3)

                # Câu hỏi
                noidungcauhoi = ('''Một chất điểm chuyển động theo quy luật $S = %s$, vận tốc $v$ (m/s) của chuyển động đạt giá trị lớn nhất tại thời điểm $t$ (s) bằng''' % quy_luat_S)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết sử dụng đạo hàm
                loigiai = ('''Vận tốc của chất điểm là đạo hàm bậc nhất của quãng đường theo thời gian:\\\\
                           $v(t) = S'(t) = (%s t^2 - t^3)' = %s t - 3t^2$ (m/s).\\\\
                           Để tìm thời điểm vận tốc đạt giá trị lớn nhất, ta xét hàm số $v(t)$ với $t > 0$.\\\\
                           Tính đạo hàm của vận tốc theo thời gian: $v'(t) = %s - 6t$.\\\\
                           Cho $v'(t) = 0 \\Leftrightarrow %s - 6t = 0 \\Leftrightarrow t = %s$ (s).\\\\
                           Vì hàm số $v(t)$ là một hàm số bậc hai có hệ số của $t^2$ âm (parabol có bề lõm quay xuống dưới) nên đồ thị đạt giá trị lớn nhất tại đỉnh.\\\\
                           Do đó, vận tốc đạt giá trị lớn nhất tại thời điểm $t = %s$ (s).'''
                           % (a, 2 * a, 2 * a, 2 * a, t_max, t_max))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

