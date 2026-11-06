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


def bt_dang26_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng bài
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Random hệ số của a để bài toán thay đổi thông số nhưng giữ nguyên bản chất
                he_so = random.choice([1, 2, 3, 5])
                if he_so == 1:
                    val_a = 'a'
                else:
                    val_a = f'{he_so}a'

                # Góc giữa AB và OI trong cấu trúc này luôn là 60 độ
                da_dung = '60^\\circ'

                # Bước 4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s = ['30^\\circ', '45^\\circ', '90^\\circ', '120^\\circ', '150^\\circ']
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (B2 - Viết lại y hệt đề bài)
                noidungcauhoi = ('''Cho tứ diện $OABC$ có $OA = OB = OC = %s$, $OA, OB, OC$ vuông góc với nhau từng đôi một. Gọi $I$ là trung điểm của $BC$. Tính góc giữa hai đường thẳng $AB$ và $OI$.'''
                                 % (val_a))

                # Mã TikZ cho hình vẽ
                hinh_ve = r'''\begin{center}
            \begin{tikzpicture}[scale=0.8, font=\footnotesize, line join=round, line cap=round, >=stealth]
                \coordinate (O) at (0,0);
                \coordinate (B) at (-1.2,-1.5);
                \coordinate (C) at (3.5,0);
                \coordinate (D) at ($(B)+(C)-(O)$);
                \coordinate (A) at (0,3.5);
                \coordinate (M) at ($(A)+(B)-(O)$);
                \coordinate (P) at ($(A)+(C)-(O)$);
                \coordinate (N) at ($(A)+(D)-(O)$);
                \coordinate (I) at ($(B)!0.5!(C)$);
                \draw[dashed] (O)--(C) (O)--(A) (O)--(B) (B)--(C) (O)--(D) (O)--(I) (A)--(B) (N)--(B) (A)--(C);
                \draw (A)--(M)--(B)--(D)--(N)--(P)--(A) (M)--(N) (P)--(C)--(D) (A)--(N) ; 
                \foreach \p/\pos in {O/left, B/below left, C/right, D/below, A/above left, M/left, N/right, P/above, I/below}
                    \fill (\p)  node[\pos] {$\p$};
            \end{tikzpicture}
            \end{center}'''

                # Nội dung lời giải chi tiết (B2 - Viết lại y hệt lời giải)
                loigiai = ('''%s
            Vì tứ diện $OABC$ có $OA = OB = OC = %s$, $OA, OB, OC$ vuông góc với nhau từng đôi một nên ta có thể dựng hình lập phương $AMNP.OBDC$ như hình vẽ với $I$ là trung điểm $BC$ nên $\\{I\\} = OD \\cap BC$.\\\\
            Cạnh của hình lập phương trên bằng $%s$ nên $AB = AN = NB = %s\\sqrt{2}$ vậy tam giác $ABN$ đều.\\\\
            Dễ thấy $OI \\parallel AN$ nên góc giữa hai đường thẳng $AB$ và $OI$ bằng góc giữa $AB$ và $AN$ bằng $60^\\circ$.'''
                           % (hinh_ve, val_a, val_a, val_a))

                # Các đáp án
                da_d = ('\\True $' + da_dung + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm (B2 - Đúng cấu trúc mẫu)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

