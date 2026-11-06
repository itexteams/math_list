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


def bt_dang55_p3_b2_c5_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Cố định k = 3 màu
                k = 3 

                # Tính toán cho lưới 2x2 (4 ô vuông đơn vị)
                # Bước 1: Ô đầu tiên (4 cạnh mới)
                # Chọn 2 màu: C(3,2) = 3. Hoán vị lặp 4!/(2!2!) = 6.
                buoc1 = math.comb(k, 2) * 6 # 3 * 6 = 18

                # Bước 2: 2 ô tiếp theo (mỗi ô chung 1 cạnh với ô đầu)
                # Mỗi ô có (3-1)*3 = 6 cách tô
                buoc2_don = (k - 1) * 3
                buoc2_tong = buoc2_don**2 # 6^2 = 36

                # Bước 3: Ô cuối cùng (chung 2 cạnh với 2 ô trước)
                # Luôn có 2 cách tô để thỏa mãn quy tắc
                buoc3_don = 2

                # Kết quả cuối cùng cho lưới 2x2
                kq_so = buoc1 * buoc2_tong * buoc3_don # 18 * 36 * 2 = 1296

                # Đáp án đúng dạng số tự nhiên
                da_dung = '$%s$' % (latex(kq_so))

                # Tạo các phương án sai
                s = set()
                while len(s) < 3:
                    sai = kq_so + random.choice([-100, 100, 50, -50, 200, 500, -200])
                    if sai > 0 and sai != kq_so:
                        s.add('$%s$' % (latex(sai)))

                list_ans = ['\\True ' + da_dung] + list(s)
                random.shuffle(list_ans)

                # Câu hỏi (Điều chỉnh thành bảng 2x2)
                noidungcauhoi = ('''Bé Minh có một bảng hình vuông gồm $4$ hình vuông đơn vị ($2 \\times 2$), cố định không xoay như hình vẽ. Bé muốn dùng $%s$ màu để tô tất cả các cạnh của các hình vuông đơn vị, mỗi cạnh tô một lần sao cho mỗi hình vuông đơn vị được tô bởi đúng $2$ màu, trong đó mỗi màu tô đúng $2$ cạnh. Hỏi bé Minh có tất cả bao nhiêu cách tô màu bảng?
            \\\\
            \\begin{center}
            \\begin{tikzpicture}[scale=0.8, line width=1pt]
            \\draw (0,0) grid (2,2);
            \\end{tikzpicture}
            \\end{center}'''
                                 % (latex(k)))

                # Nội dung lời giải chi tiết
                loigiai = ('''Tô màu theo quy tắc:\\\\
            - Bước 1: Tô ô vuông đầu tiên: Chọn $2$ trong $%s$ màu có $C_{%s}^2$ cách, ứng với mỗi cặp màu có $6$ cách tô cạnh. Vậy có $C_{%s}^2 \\cdot 6 = %s$ cách.\\\\
            - Bước 2: Tô $2$ ô vuông tiếp theo (mỗi ô chung $1$ cạnh với ô trước): Với mỗi ô, chọn thêm $1$ màu từ $%s$ màu còn lại và sắp xếp cạnh, có $(%s-1) \\cdot 3 = %s$ cách. Vậy $2$ ô này có $%s^2 = %s$ cách.\\\\
            - Bước 3: Tô ô vuông cuối cùng (chung $2$ cạnh với các ô đã tô): Có $2$ cách tô các cạnh còn lại để thỏa mãn điều kiện. \\\\
            Vậy tổng số cách tô màu bảng là: $%s \\cdot %s \\cdot 2 = %s$ (cách).'''
                           % (latex(k), latex(k), latex(k), latex(buoc1), 
                              latex(k), latex(k), latex(buoc2_don), latex(buoc2_don), latex(buoc2_tong),
                              latex(buoc1), latex(buoc2_tong), latex(kq_so)))

                # Đáp án ngắn (Số tự nhiên)
                dapan = '\\shortans[0]{$%s$}\n' % (latex(kq_so))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

