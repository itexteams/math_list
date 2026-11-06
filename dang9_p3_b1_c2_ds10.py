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


def bt_dang9_p3_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Tập hợp các bộ dữ liệu ngẫu nhiên thực tế và chia hết đẹp mắt
                combos = [
                    {"M": 100000, "PA": 8000, "PB": 15000, "nB": 4, "ans": 5},
                    {"M": 140000, "PA": 10000, "PB": 20000, "nB": 4, "ans": 6},
                    {"M": 120000, "PA": 12000, "PB": 20000, "nB": 3, "ans": 5},
                    {"M": 160000, "PA": 15000, "PB": 25000, "nB": 4, "ans": 4},
                    {"M": 150000, "PA": 15000, "PB": 15000, "nB": 3, "ans": 7},
                    {"M": 200000, "PA": 20000, "PB": 20000, "nB": 5, "ans": 5},
                    {"M": 90000, "PA": 12000, "PB": 10000, "nB": 3, "ans": 5}
                ]

                chosen = random.choice(combos)
                M = chosen["M"]    # Tổng số tiền
                PA = chosen["PA"]  # Giá bánh A
                PB = chosen["PB"]  # Giá bánh B
                nB = chosen["nB"]  # Số lượng bánh B đã mua
                ans = chosen["ans"] # Đáp án đúng (Số bánh A tối đa)
                while PA==PB:
                    chosen = random.choice(combos)
                    M = chosen["M"]    # Tổng số tiền
                    PA = chosen["PA"]  # Giá bánh A
                    PB = chosen["PB"]  # Giá bánh B
                    nB = chosen["nB"]  # Số lượng bánh B đã mua
                    ans = chosen["ans"] # Đáp án đúng (Số bánh A tối đa)

                # Đại lượng tính toán trung gian phục vụ lời giải
                cost_B = PB * nB
                rem_M = M - cost_B

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (ans)]
                da = random.choice(du)

                # Tạo danh sách các đáp án sai xung quanh đáp án đúng
                s = [
                    '$%s$' % (ans + 1),
                    '$%s$' % (ans - 1),
                    '$%s$' % (ans + 2),
                    '$%s$' % (ans - 2),
                    '$%s$' % (ans + 3),
                ]
                # Lọc bỏ giá trị không hợp lệ (nhỏ hơn hoặc bằng 0)
                s = [item for item in s if int(item.replace('$', '')) > 0]

                das1, das2, das3 = random.sample(s, 3)

                # Câu hỏi
                noidungcauhoi = ('''Bạn Bình mang $%s$ đồng đi siêu thị mua 2 loại bánh. Biết rằng giá mỗi túi bánh A là $%s$ đồng, giá mỗi túi bánh B là $%s$ đồng. Bạn Bình có thể mua được tối đa bao nhiêu túi bánh A nếu bạn đã mua $%s$ túi bánh B?'''
                                 % (latex(M), latex(PA), latex(PB), latex(nB)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Giữ nguyên cấu trúc văn phong của hình ảnh mẫu)
                loigiai = ('''Gọi $x, y$ lần lượt là số túi bánh A và số túi bánh B mà bạn Bình có thể mua. ($x, y \\in \\mathbb{{N}}^*$) \\\\
            Theo đề bài ta có: $%sx + %sy \\le %s$ \\\\
            Nếu bạn Bình mua $%s$ túi bánh B, khi đó: $%sx + %s \\cdot %s \\le %s \\Rightarrow %sx \\le %s \\Rightarrow x \\le %s$ \\\\
            Vì $x$ nguyên dương nên số túi bánh A tối đa có thể mua được là $%s$ túi.'''
                           % (latex(PA), latex(PB), latex(M),
                              latex(nB), latex(PA), latex(PB), latex(nB), latex(M), latex(PA), latex(rem_M), latex(ans),
                              latex(ans)))
                dapan='\\shortans[0]{$%s$}\n'%(ans)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

