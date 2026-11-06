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


def bt_dang42_p4_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng đoàn viên n sao cho tỉ lệ k là số hữu tỉ đẹp
                # k = 24 / ((n-4)*(n-5)*(n-6))
                # n=7 -> k=4
                # n=8 -> k=1
                # n=9 -> k=2/5
                # n=10 -> k=1/5
                list_n = [7, 8, 9, 10]
                n_val = random.choice(list_n)

                # Tính tỉ lệ k tương ứng
                mau_k = (n_val - 4) * (n_val - 5) * (n_val - 6)
                tu_k = 24
                ti_le = Rational(tu_k, mau_k)

                # Chuyển tỉ lệ sang latex để hiển thị
                if ti_le.q == 1:
                    str_tile = str(ti_le.p)
                else:
                    str_tile = "\\frac{%s}{%s}" % (latex(ti_le.p), latex(ti_le.q))

                # Đáp án đúng
                kq = n_val

                # Các đáp án trắc nghiệm
                s = [kq + 1, kq + 2, kq + 3, kq - 1, kq - 2, kq - 3]
                # Lọc các giá trị n >= 7 để bài toán có nghĩa
                s = [i for i in s if i >= 7]

                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Câu hỏi
                noidungcauhoi = ("Một Chi đoàn có 3 đoàn viên nữ và một số đoàn viên nam. Cần lập một đội thanh niên tình nguyện (TNTN) gồm 4 người. Biết xác suất để trong 4 người được chọn có 3 nữ bằng $%s$ lần xác suất 4 người được chọn toàn nam. Tìm số đoàn viên của chi đoàn."
                                 %(str_tile))

                # Các đáp án
                da_d = ("\\True $%s$" % (latex(kq)))
                da_s1 = ("$%s$" % (latex(das1)))
                da_s2 = ("$%s$" % (latex(das2)))
                da_s3 = ("$%s$" % (latex(das3)))

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ("Gọi số đoàn viên trong chi đoàn đó là $n \\left( n \\geq 7, n \\in \\mathbb{N}^* \\right)$. \\\\ "
                           "Suy ra số đoàn viên nam trong chi đoàn là $n-3$. \\\\ "
                           "Số cách chọn 4 người từ $n$ người là $C_n^4$. \\\\ "
                           "Số cách chọn 4 người có 3 nữ (và 1 nam) là $C_3^3 \\cdot C_{n-3}^1 = C_{n-3}^1$. \\\\ "
                           "Xác suất để lập đội TNTN có 3 nữ là $P_1 = \\frac{C_3^3 \\cdot C_{n-3}^1}{C_n^4}$. \\\\ "
                           "Số cách chọn 4 người toàn nam là $C_{n-3}^4$. \\\\ "
                           "Xác suất để lập đội TNTN toàn nam là $P_2 = \\frac{C_{n-3}^4}{C_n^4}$. \\\\ "
                           "Theo giả thiết, ta có: $P_1 = %s \\cdot P_2$ \\\\ "
                           "$\\Leftrightarrow \\frac{C_3^3 \\cdot C_{n-3}^1}{C_n^4} = %s \\cdot \\frac{C_{n-3}^4}{C_n^4}$ \\\\ "
                           "$\\Leftrightarrow C_{n-3}^1 = %s \\cdot C_{n-3}^4$ \\\\ "
                           "$\\Leftrightarrow n-3 = %s \\cdot \\frac{(n-3)(n-4)(n-5)(n-6)}{24}$ \\\\ "
                           "$\\Leftrightarrow 1 = %s \\cdot \\frac{(n-4)(n-5)(n-6)}{24}$ \\\\ "
                           "$\\Leftrightarrow (n-4)(n-5)(n-6) = %s$. \\\\ "
                           "Giải phương trình trên với $n \\in \\mathbb{N}^*$, ta được $n = %s$. \\\\ "
                           "Vậy chi đoàn có $%s$ đoàn viên."
                           %(str_tile, str_tile, str_tile, str_tile, str_tile, latex(mau_k), latex(kq), latex(kq)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

