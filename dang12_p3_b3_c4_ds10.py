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


def bt_dang12_p3_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 & B3: Khởi tạo giá trị ngẫu nhiên
                # Giả sử khoảng nghiệm yêu cầu là [a, b]
                a = randint(2, 5)
                b = a + randint(2, 4)

                # Phạm vi của tham số m: [0, m_max]
                m_max = randint(2000, 2025)

                # Theo logic bài toán: x^2 - (m+1)x + m <= 0 <=> (x-1)(x-m) <= 0
                # Nghiệm luôn có x=1. Để [a, b] là nghiệm và a > 1, thì m phải >= b.
                # Tập hợp các giá trị m nguyên thỏa mãn là {b, b+1, ..., m_max}

                so_gia_tri = m_max - b + 1

                # Đáp án đúng
                da_dung = '$%s$' % (so_gia_tri)

                # B4: Tạo các phương án sai không trùng đáp án đúng
                s_set = set()
                while len(s_set) < 3:
                    sai = so_gia_tri + random.choice([-2, -1, 1, 2, 3])
                    if sai != so_gia_tri and sai > 0:
                        s_set.add('$%s$' % (sai))

                list_sai = list(s_set)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # B2: Nội dung câu hỏi
                noidungcauhoi = ('''Có tất cả bao nhiêu giá trị nguyên của tham số $m \\in [0; %s]$ để mọi $x \\in [%s; %s]$ đều là nghiệm bất phương trình $x^2 - (m+1)x + m \\le 0$?'''
                                 % (latex(m_max), latex(a), latex(b)))

                # Các đáp án
                da_d = '\\True ' + str(da_dung)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết theo nội dung ảnh
                loigiai = ('''Ta có: $x^2 - (m+1)x + m \\le 0 \\Leftrightarrow (x-1)(x-m) \\le 0 \\quad (*)$. \\\\
                           Trường hợp 1: $m=1$. Khi đó $(*)$ trở thành: $(x-1)(x-1) \\le 0 \\Leftrightarrow (x-1)^2 \\le 0 \\Leftrightarrow x=1$. \\\\
                           Do đó $m=1$ không thỏa mãn vì không chứa khoảng $[%s; %s]$. \\\\
                           Trường hợp 2: $m > 1$. Khi đó $(*)$ có tập nghiệm là $1 \\le x \\le m$. \\\\
                           Yêu cầu bài toán thỏa mãn khi $[%s; %s] \\subseteq [1; m]$, tức là $m \\ge %s$. Kết hợp điều kiện $m > 1$ ta có $m \\ge %s$. \\\\
                           Trường hợp 3: $m < 1$. Khi đó $(*)$ có tập nghiệm là $m \\le x \\le 1$. \\\\
                           Không có giá trị $m$ thỏa mãn bởi vì $[%s; %s] \\not\\subset [m; 1]$ (do $%s > 1$). \\\\
                           Vậy $m \\ge %s$ là điều kiện cần tìm. Mặt khác $\\begin{cases} m \\in \\mathbb{Z} \\\\ m \\in [0; %s] \\end{cases}$ nên $m \\in \\{%s; %s; \\dots; %s\\}$. \\\\
                           Do đó có $%s$ giá trị nguyên của $m$.'''
                           % (latex(a), latex(b), 
                              latex(a), latex(b), latex(b), latex(b),
                              latex(a), latex(b), latex(a),
                              latex(b), latex(m_max), latex(b), latex(b+1), latex(m_max),
                              latex(so_gia_tri)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(so_gia_tri))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

