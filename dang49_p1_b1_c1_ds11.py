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


def bt_dang49_p1_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập random bài toán
                # Số điểm biểu diễn cho họ nghiệm x = alpha + k * (2*pi / N) trên đường tròn là N điểm.
                # Trong đề gốc: k*2*pi/3 -> N = 3.
                # Ta chọn ngẫu nhiên N từ 3 đến 8 để bài toán thay đổi phong phú.
                da_dung = randint(3, 8)

                # Chọn ngẫu nhiên mẫu số cho số hạng đầu (ví dụ: pi/2, pi/3, pi/4, pi/6)
                mau_so_dau = random.choice([2, 3, 4, 6])

                # Đáp án đúng dạng chuỗi số nguyên
                da = '$%d$' % da_dung
                da_chon = da

                # B4: Điều chỉnh các phương án sai không được trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = da_dung + random.choice([-3, -2, -1, 1, 2, 3, 4])
                    if sai > 1 and sai != da_dung:
                        s.add('$%d$' % sai)

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Có bao nhiêu điểm $M$ trên đường tròn định hướng gốc $A$ thỏa mãn $\\curvearrowright\\hspace{-0.3cm}AM = \\frac{\\pi}{%s} + \\frac{k2\\pi}{%s}, k \\in \\mathbb{Z}$'''
                                 % (latex(mau_so_dau), latex(da_dung)))

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết, đầy đủ từng bước phân tích chu kỳ để tìm ra số điểm biểu diễn nguyên
                loigiai = ('''Họ các cung lượng giác có số đo dạng $\\alpha = \\alpha_0 + \\frac{k2\\pi}{N}$ ($k \\in \\mathbb{Z}$, $N$ là số nguyên dương) được biểu diễn bởi đúng $N$ điểm chia đều đường tròn lượng giác. \\\\
            Áp dụng vào bài toán, ta có số đo cung lượng giác là: \\\\
            $\\curvearrowright\\hspace{-0.3cm}AM = \\frac{\\pi}{%s} + k \\cdot \\frac{2\\pi}{%s}, k \\in \\mathbb{Z}$. \\\\
            Ở đây, bước nhảy của hệ số sau mỗi giá trị $k$ tăng lên là $\\frac{2\\pi}{%s}$. \\\\
            Để các điểm bắt đầu trùng nhau, ta giải phương trình dịch chuyển trọn một hoặc nhiều vòng quay ($m2\\pi$ với $m \\in \\mathbb{Z}$): \\\\
            $k \\cdot \\frac{2\\pi}{%s} = m2\\pi \\Leftrightarrow k = %s \\cdot m$. \\\\
            Các giá trị nguyên của $k$ không trùng nhau về vị trí hình học tương ứng với các số dư khi chia $k$ cho $%s$, tức là $k \\in \\{0, 1, 2, \\dots, %d\\}$. \\\\
            Vậy có tất cả $%d$ điểm $M$ thỏa mãn điều kiện bài toán trên đường tròn định hướng.'''
                           % (latex(mau_so_dau), latex(da_dung), latex(da_dung), latex(da_dung), latex(da_dung), latex(da_dung), da_dung - 1, da_dung))

            # Xuất câu trắc nghiệm định dạng minipage TeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

