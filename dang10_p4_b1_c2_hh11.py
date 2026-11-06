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


def bt_dang10_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các kịch bản random kết quả
                # Mỗi kịch bản gồm: (Vectơ 1, Vectơ 2, Kết quả góc, Lời giải tương ứng)
                scenarios = [
                    {
                        "v1": "\\overrightarrow{BC}",
                        "v2": "\\overrightarrow{OM}",
                        "kq": 120,
                        "ve_v1": "\\overrightarrow{OC} - \\overrightarrow{OB}",
                        "tich_vh": "-\\frac{1}{2}OB^2 = -\\frac{a^2}{2}",
                        "do_dai_v1": "a\\sqrt{2}",
                        "cos_val": "-\\frac{1}{2}"
                    },
                    {
                        "v1": "\\overrightarrow{OA}",
                        "v2": "\\overrightarrow{OM}",
                        "kq": 45,
                        "ve_v1": "\\overrightarrow{OA}",
                        "tich_vh": "\\frac{1}{2}OA^2 = \\frac{a^2}{2}",
                        "do_dai_v1": "a",
                        "cos_val": "\\frac{\\sqrt{2}}{2}"
                    },
                    {
                        "v1": "\\overrightarrow{OC}",
                        "v2": "\\overrightarrow{OM}",
                        "kq": 90,
                        "ve_v1": "\\overrightarrow{OC}",
                        "tich_vh": "0",
                        "do_dai_v1": "a",
                        "cos_val": "0"
                    }
                ]

                # Chọn ngẫu nhiên 1 kịch bản
                case = random.choice(scenarios)
                goc_kq = case["kq"]

                # Tạo các phương án nhiễu (không được trùng với goc_kq)
                pool_sai = [30, 45, 60, 90, 120, 135, 150]
                if goc_kq in pool_sai:
                    pool_sai.remove(goc_kq)
                random.shuffle(pool_sai)

                da_dung = '$' + str(goc_kq) + '^\\circ$'
                da_s1 = '$' + str(pool_sai[0]) + '^\\circ$'
                da_s2 = '$' + str(pool_sai[1]) + '^\\circ$'
                da_s3 = '$' + str(pool_sai[2]) + '^\\circ$'

                # Câu hỏi
                noidungcauhoi = (
                    'Cho hình chóp $O.ABC$ có ba cạnh $OA, OB, OC$ đôi một vuông góc và $OA = OB = OC = a$. '
                    'Gọi $M$ là trung điểm cạnh $AB$. Tính góc tạo bởi hai vectơ $' + case["v1"] + '$ và $' + case["v2"] + '$.'
                )

             # Vẽ hình bằng TikZ
                hinh_ve = (
                    '\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=1, line join=round, line cap=round, >=stealth]\n'
                    '   \\coordinate (O) at (0,0);\n'
                    '   \\coordinate (A) at (0,3);\n'
                    '   \\coordinate (B) at (-1.5,-1.5);\n'
                    '   \\coordinate (C) at (4,0);\n'
                    '   \\coordinate (M) at ($(A)!0.5!(B)$);\n'
                    '   \\draw[dashed] (O) -- (C);\n'
                    '   \\draw[dashed] (O) -- (A);\n'
                    '   \\draw[dashed] (O) -- (B);\n'
                    '   \\draw[dashed] (O) -- (M);\n'
                    '   \\draw (A) -- (B) -- (C) -- (A);\n'
                    '   \\fill (O) node[below left] {$O$};\n'
                    '   \\fill (A) node[above] {$A$};\n'
                    '   \\fill (B) node[below left] {$B$};\n'
                    '   \\fill (C) node[right] {$C$};\n'
                    '   \\fill (M) node[left] {$M$};\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}')

                # Nội dung lời giải chi tiết (điều chỉnh theo kịch bản)
                loigiai = (
                    'Ta có $M$ là trung điểm của $AB$ nên $\\overrightarrow{OM} = \\frac{1}{2}(\\overrightarrow{OA} + \\overrightarrow{OB})$.\\\\\n'
                    'Xét tích vô hướng của hai vectơ $' + case["v1"] + '$ và $' + case["v2"] + '$:\\\\\n'
                    '$\\overrightarrow{OM} \\cdot ' + case["v1"] + ' = \\frac{1}{2}(\\overrightarrow{OA} + \\overrightarrow{OB}) \\cdot (' + case["ve_v1"] + ')$.\\\\\n'
                    'Vì $OA, OB, OC$ đôi một vuông góc nên tích vô hướng của các cặp vectơ đơn vị bằng $0$. '
                    'Do đó, ta tính được $\\overrightarrow{OM} \\cdot ' + case["v1"] + ' = ' + case["tich_vh"] + '.$\\\\\n'
                    'Độ dài các vectơ: $' + case["v1"].replace("\\overrightarrow{","").replace("}","") + ' = ' + case["do_dai_v1"] + ' $'
                    'và $OM = \\frac{1}{2}AB = \\frac{a\\sqrt{2}}{2}$.\\\\\n'
                    'Suy ra: $\\cos(' + case["v2"] + ', ' + case["v1"] + ') = '
                    '\\frac{' + case["v2"] + ' \\cdot ' + case["v1"] + '}{OM \\cdot ' + case["v1"].replace("\\overrightarrow{","").replace("}","") + '} '
                    '= ' + case["cos_val"] + '.$\\\\\n'
                    'Vậy góc giữa hai vectơ bằng $' + str(goc_kq) + '^\\circ$.'
                )

                # Trộn đáp án
                list_ans = [('\\True ' + da_dung), da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Xuất nội dung
                content = (
                    '\\begin{minipage}{\\textwidth}\n'
                    '\\begin{ex}\n'
                    + str(noidungcauhoi) + '\n'
                    + str(hinh_ve) + '\n'
                    '\\loigiai{' + str(loigiai) + '}\n'
                    '\\end{ex}\n'
                    '\\end{minipage}\n\n')
            return content

