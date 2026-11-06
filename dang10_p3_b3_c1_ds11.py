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


def bt_dang10_p3_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Biên độ của hàm số cos (A > 0) và hằng số cộng thêm B
                A = random.randint(2, 5)
                B = random.randint(10, 15)

                # Random thời điểm đáp án đúng sao cho t là số nguyên dương hợp lý trong ngày (0 < t <= 24)
                # Để biểu thức đơn giản, ta chọn t sao cho góc bằng 2*pi (k = 1)
                # Chọn ngẫu nhiên mẫu số m của pi*t/m, ví dụ m = 6, 8, 12
                m = random.choice([6, 8, 12])

                # Chọn đáp án đúng t_dung (ví dụ từ 10 đến 22)
                t_dung = random.randint(10, 22)

                # Tính tử số của phân số pha ban đầu: phi = 2*pi - pi*t_dung/m = pi*(2*m - t_dung)/m
                # Để đảm bảo phân số pha ban đầu đẹp và nhỏ hơn 2*pi, ta có tử số là (2*m - t_dung)
                # Do đó, ta cần chọn bộ (m, t_dung) sao cho tử số dương.
                while (2 * m - t_dung) <= 0:
                    m = random.choice([6, 8, 12])
                    t_dung = random.randint(10, 20)

                tu_so_phi = 2 * m - t_dung

                # Tạo phân số tối giản cho pha ban đầu bằng SymPy
                pha_ban_dau = Rational(tu_so_phi, m)

                # Giá trị đáp án đúng
                da = '$t = %s$ (giờ)' % (latex(t_dung))

                # Khởi tạo tập hợp các phương án sai xung quanh t_dung
                s_set = set()
                while len(s_set) < 3:
                    sai = t_dung + random.choice([-3, -2, -1, 1, 2, 3, 4])
                    if 0 < sai <= 24 and sai != t_dung:
                        s_set.add(sai)

                s_list = list(s_set)
                das1 = '$t = %s$ (giờ)' % (latex(s_list[0]))
                das2 = '$t = %s$ (giờ)' % (latex(s_list[1]))
                das3 = '$t = %s$ (giờ)' % (latex(s_list[2]))

                # Câu hỏi
                noidungcauhoi = ('''Hằng ngày mực nước của con kênh lên xuống theo thủy triều. Độ sâu $h$ (mét) của mực nước trong kênh được tính tại thời điểm $t$ (giờ) trong một ngày bởi công thức $h = %s\\cos\\left(\\frac{\\pi t}{%s} + \\frac{%s\\pi}{%s}\\right) + %s$. Mực nước của kênh cao nhất tại thời điểm bằng bao nhiêu?'''
                                 % (latex(A), latex(m), latex(pha_ban_dau.p), latex(pha_ban_dau.q), latex(B)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Mực nước của kênh cao nhất khi $h$ lớn nhất \\\\
                           $\\Leftrightarrow \\cos\\left(\\frac{\\pi t}{%s} + \\frac{%s\\pi}{%s}\\right) = 1 \\Leftrightarrow \\frac{\\pi t}{%s} + \\frac{%s\\pi}{%s} = k2\\pi$ với $0 < t \\le 24$ và $k \\in \\mathbb{Z}$. \\\\
                           Lần lượt thay các đáp án, ta được phương án thỏa mãn \\\\
                           Vì với $t = %s \\Rightarrow \\frac{\\pi \\cdot %s}{%s} + \\frac{%s\\pi}{%s} = 2\\pi$ (đúng với $k = 1 \\in \\mathbb{Z}$). \\\\
                           Vậy mực nước của kênh cao nhất tại thời điểm $%s$ giờ.'''
                           % (latex(m), latex(pha_ban_dau.p), latex(pha_ban_dau.q),
                              latex(m), latex(pha_ban_dau.p), latex(pha_ban_dau.q),
                              latex(t_dung), latex(t_dung), latex(m), latex(pha_ban_dau.p), latex(pha_ban_dau.q),
                              latex(t_dung)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(t_dung))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

