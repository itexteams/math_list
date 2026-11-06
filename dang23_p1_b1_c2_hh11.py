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


def bt_dang23_p1_b1_c2_hh11(self):
            # Khai báo biến và chọn dạng ngẫu nhiên
            lisdang = ['1', '2', '3']
            dang = random.choice(lisdang)

            # Khởi tạo các giá trị mặc định cho kịch bản
            if dang == '1':
                v1 = '\\vec{BC}'
                v2 = '\\vec{OM}'
                goc_kq = '120^\\circ'
                ve_v1 = '\\vec{OC} - \\vec{OB}'
                tich_vh = '-\\frac{1}{2}OB^2 = -\\frac{a^2}{2}'
                do_dai_v1 = 'a\\sqrt{2}'
                cos_val = '-\\frac{1}{2}'
            elif dang == '2':
                v1 = '\\vec{OA}'
                v2 = '\\vec{OM}'
                goc_kq = '45^\\circ'
                ve_v1 = '\\vec{OA}'
                tich_vh = '\\frac{1}{2}OA^2 = \\frac{a^2}{2}'
                do_dai_v1 = 'a'
                cos_val = '\\frac{\\sqrt{2}}{2}'
            else:
                v1 = '\\vec{OC}'
                v2 = '\\vec{OM}'
                goc_kq = '90^\\circ'
                ve_v1 = '\\vec{OC}'
                tich_vh = '0'
                do_dai_v1 = 'a'
                cos_val = '0'

            # Đáp án đúng
            da_dung = goc_kq

            # Các phương án sai (nhiễu)
            s = ['30^\\circ', '60^\\circ', '135^\\circ', '150^\\circ', '0^\\circ']
            # Loại bỏ đáp án đúng khỏi danh sách nhiễu nếu có
            if da_dung in s: s.remove(da_dung)
            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Câu hỏi
            noidungcauhoi = ('Cho hình chóp $O.ABC$ có ba cạnh $OA, OB, OC$ đôi một vuông góc và $OA = OB = OC = a$. Gọi $M$ là trung điểm cạnh $AB$. Góc tạo bởi hai vectơ $%s$ và $%s$ bằng'
                             % (v1, v2))

            # Các đáp án trắc nghiệm
            da_d = ('\\True $%s$' % da_dung)
            da_s1 = ('$%s$' % das1)
            da_s2 = ('$%s$' % das2)
            da_s3 = ('$%s$' % das3)

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ
            tikz_code = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, line join=round, line cap=round, >=stealth]
                \\coordinate (O) at (0,0);
                \\coordinate (A) at (0,3);
                \\coordinate (B) at (-1.5,-1.5);
                \\coordinate (C) at (4,0);
                \\coordinate (M) at ($(A)!0.5!(B)$);
                \\draw[dashed] (O) -- (C);
                \\draw[dashed] (O) -- (A);
                \\draw[dashed] (O) -- (B);
                \\draw[dashed] (O) -- (M);
                \\draw (A) -- (B) -- (C) -- (A);
                \\fill (O) circle (1pt) node[below left] {$O$};
                \\fill (A) circle (1pt) node[above] {$A$};
                \\fill (B) circle (1pt) node[below left] {$B$};
                \\fill (C) circle (1pt) node[right] {$C$};
                \\fill (M) circle (1pt) node[left] {$M$};
            \\end{tikzpicture}
            \\end{center}''')

            # Nội dung lời giải
            v1_label = v1.replace('\\vec{', '').replace('}', '')
            loigiai = (tikz_code + '''Ta có $M$ là trung điểm của $AB$ nên $\\vec{OM} = \\frac{1}{2}(\\vec{OA} + \\vec{OB})$. \\\\
            Xét tích vô hướng của hai vectơ $%s$ và $%s$: \\\\
            $\\vec{OM} \\cdot %s = \\frac{1}{2}(\\vec{OA} + \\vec{OB}) \\cdot (%s)$. \\\\
            Vì $OA, OB, OC$ đôi một vuông góc nên tích vô hướng của các cặp vectơ đơn vị bằng $0$. 
            Do đó, ta tính được $\\vec{OM} \\cdot %s = %s$. \\\\
            Độ dài các vectơ: $%s = %s$ và $OM = \\frac{a\\sqrt{2}}{2}$. \\\\
            Suy ra: $\\cos(%s, %s) = \\frac{\\vec{OM} \\cdot %s}{OM \\cdot %s} = %s$. \\\\
            Vậy góc giữa hai vectơ bằng $%s$.''' 
                       % (v2, v1, v1, ve_v1, v1, tich_vh, v1_label, do_dai_v1, v2, v1, v1, v1_label, cos_val, da_dung))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

