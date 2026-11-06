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


def bt_dang19_p4_b2_c6_ds10(self):
            #Khai báo biến
            # B1 & B3: Nghiên cứu đề bài và tìm cách random
            # Thay vì cố định 50 viên bi, ta cho phép tổng số viên bi N chạy từ 40 đến 60.
            N = random.randint(20, 60)

            # Chia các số từ 1 đến N thành 3 nhóm dựa trên số dư khi chia cho 3
            # Nhóm 0: chia hết cho 3
            # Nhóm 1: chia cho 3 dư 1
            # Nhóm 2: chia cho 3 dư 2
            n0 = N // 3
            n1 = N // 3 + (1 if N % 3 >= 1 else 0)
            n2 = N // 3 + (1 if N % 3 >= 2 else 0)

            # B2: Tính toán lời giải
            # Số phần tử không gian mẫu
            omega = binomial(N, 3)

            # Biến cố A: Tổng 3 số chia hết cho 3. Có 2 trường hợp chính:
            # TH1: 3 viên cùng một loại (0+0+0, 1+1+1, 2+2+2 đều chia hết cho 3)
            th1 = binomial(n0, 3) + binomial(n1, 3) + binomial(n2, 3)
            # TH2: Mỗi viên một loại khác nhau (0+1+2 = 3, chia hết cho 3)
            th2 = n0 * n1 * n2

            nA = th1 + th2
            xac_suat = Rational(nA, omega)

            # B4: Điều chỉnh các phương án sai
            da_dung = '$%s$' % latex(xac_suat)

            s = []
            while len(s) < 3:
                # Tạo các phương án nhiễu bằng cách thay đổi tử số hoặc mẫu số một chút
                sai_tu = nA + random.choice([-10, -5, 5, 10, 20, -20, 100, -100])
                # Đảm bảo tử số dương và không tạo ra đáp án đúng
                if sai_tu > 0:
                    ps_sai = Rational(sai_tu, omega)
                    da_sai = '$%s$' % latex(ps_sai)
                    if da_sai != da_dung and da_sai not in s:
                        s.append(da_sai)

            da_d = '\\True ' + da_dung
            da_s1 = s[0]
            da_s2 = s[1]
            da_s3 = s[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Trong một hộp có $%s$ viên bi được đánh số từ $1$ đến $%s$. Chọn ngẫu nhiên $3$ viên trong hộp. '
                'Tính xác suất để tổng ba số trên $3$ viên bi được chọn là một số chia hết cho $3$.'
                % (latex(N), latex(N))
            )

            # Nội dung lời giải chi tiết theo mẫu ảnh
            loigiai = (
                'Không gian mẫu là số cách chọn ngẫu nhiên $3$ viên bi từ hộp chứa $%s$ viên bi. \\\\ '
                'Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^{3} = %s$. \\\\ '
                'Gọi $A$ là biến cố "3 viên bi được chọn là một số chia hết cho 3". Trong $%s$ viên bi được '
                'chia thành ba loại gồm: $%s$ viên bi có số chia hết cho $3$; $%s$ viên bi có số chia cho $3$ dư $1$; '
                '$%s$ viên bi có số chia cho $3$ dư $2$. Để tìm số kết quả thuận lợi cho biến cố $A$, ta xét các trường hợp. \\\\ '
                '+ TH1: 3 viên bi được chọn cùng một loại, có $\\left(C_{%s}^{3} + C_{%s}^{3} + C_{%s}^{3}\\right) = %s$ cách. \\\\ '
                '+ TH2: 3 viên bi được chọn có mỗi viên một loại, có $C_{%s}^{1} \\cdot C_{%s}^{1} \\cdot C_{%s}^{1} = %s$ cách. \\\\ '
                'Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = %s + %s = %s$. \\\\ '
                'Vậy xác suất cần tính $P\\left(A\\right) = \\frac{n\\left(A\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{%s} = %s$.'
                % (
                    latex(N), latex(N), latex(omega),
                    latex(N), latex(n0), latex(n1), latex(n2),
                    latex(n0), latex(n1), latex(n2), latex(th1),
                    latex(n0), latex(n1), latex(n2), latex(th2),
                    latex(th1), latex(th2), latex(nA),
                    latex(nA), latex(omega), latex(xac_suat)
                )
            )

            # Xuất câu trắc nghiệm (không dùng tiền tố r)
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

