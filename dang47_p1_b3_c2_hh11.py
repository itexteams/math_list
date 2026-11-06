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


def bt_dang47_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Cấu trúc: (AC, BC, AA', AB_text, tan_val_text, ket_qua_goc)
            datasets = [
                ('2', '1', '1', '\\sqrt{3}', '\\sqrt{3}', '60^\\circ'),
                ('\\sqrt{5}', '1', '2', '2', '1', '45^\\circ'),
                ('2', '1', '3', '\\sqrt{3}', '\\frac{\\sqrt{3}}{3}', '30^\\circ'),
                ('\\sqrt{2}', '1', '1', '1', '1', '45^\\circ'),
                ('\\sqrt{7}', '2', '\\sqrt{3}', '\\sqrt{3}', '1', '45^\\circ'),
                ('4', '2', '2', '2\\sqrt{3}', '\\sqrt{3}', '60^\\circ')
            ]

            data = random.choice(datasets)
            ac_val = data[0]
            bc_val = data[1]
            aa_val = data[2]
            ab_tex = data[3]
            tan_tex = data[4]
            kq_goc = data[5]

            # Bước 2: Tạo danh sách đáp án
            dap_an_dung = kq_goc
            cac_lua_chon = ['30^\\circ', '45^\\circ', '60^\\circ', '90^\\circ']
            if dap_an_dung not in cac_lua_chon:
                cac_lua_chon[0] = dap_an_dung # Đảm bảo có đáp án đúng nếu dataset mở rộng

            random.shuffle(cac_lua_chon)

            # Bước 3: Nội dung câu hỏi
            noidungcauhoi = ('Cho hình lăng trụ đứng $ABC.A\'B\'C\'$ có đáy $ABC$ là tam giác vuông tại $B$, $AC = ' + ac_val + '$, $BC = ' + bc_val + '$, $AA\' = ' + aa_val + '$. Góc giữa $AB\'$ và mặt phẳng $(BCC\'B\')$ là')

            # Bước 4: Vẽ hình bằng TikZ
            hinh_ve = ('\\begin{center}\n'
                       '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
                       '\\coordinate (B) at (0,3);\n'
                       '\\coordinate (C) at (3,3.5);\n'
                       '\\coordinate (A) at (-1.5,3.5);\n'
                       '\\coordinate (B1) at (0,0);\n'
                       '\\coordinate (C1) at (3,0.5);\n'
                       '\\coordinate (A1) at (-1.5,0.5);\n'
                       '\\draw (A) -- (B) -- (C) -- (A) -- (A1);\n'
                       '\\draw (B) -- (B1) -- (C1) -- (C);\n'
                       '\\draw (A) -- (B1) (A1) -- (B1);\n'
                       '\\draw[dashed] (B1) -- (C1);\n'
                       '\\draw[dashed] (A1) -- (C1);\n'
                       '\\draw (0,2.8) -- (0.2,2.85) -- (0.2,3.05);\n' # Góc vuông tại B
                       '\\node[left] at (A) {$A$};\n'
                       '\\node[above] at (B) {$B$};\n'
                       '\\node[right] at (C) {$C$};\n'
                       '\\node[left] at (A1) {$A\'$};\n'
                       '\\node[below] at (B1) {$B\'$};\n'
                       '\\node[right] at (C1) {$C\'$};\n'
                       '\\end{tikzpicture}\n'
                       '\\end{center}')

            # Bước 5: Lời giải chi tiết
            loigiai = ('Ta có: $\\left. \\begin{array}{l} AB \\perp BC \\\\ AB \\perp BB\' \\end{array} \\right\\} \\Rightarrow AB \\perp (BCC\'B\')$. \\\\\n'
                       'Suy ra $B\'$ là hình chiếu vuông góc của $B\'$ trên mặt phẳng $(BCC\'B\')$ và $B$ là hình chiếu vuông góc của $A$ trên mặt phẳng $(BCC\'B\')$. \\\\\n'
                       'Do đó, $BB\'$ là hình chiếu vuông góc của $AB\'$ trên mặt phẳng $(BCC\'B\')$. \\\\\n'
                       'Vậy góc giữa đường thẳng $AB\'$ và mặt phẳng $(BCC\'B\')$ chính là góc $\\widehat{AB\'B}$. \\\\\n'
                       'Xét tam giác $ABC$ vuông tại $B$, ta có $AB = \\sqrt{AC^2 - BC^2} = \\sqrt{' + ac_val + '^2 - ' + bc_val + '^2} = ' + ab_tex + '$. \\\\\n'
                       'Xét tam giác $ABB\'$ vuông tại $B$ (do $AB \\perp BB\'$), ta có $BB\' = AA\' = ' + aa_val + '$. \\\\\n'
                       'Suy ra $\\tan \\widehat{AB\'B} = \\frac{AB}{BB\'} = \\frac{' + ab_tex + '}{' + aa_val + '} = ' + tan_tex + '$. \\\\\n'
                       'Vậy $\\widehat{AB\'B} = ' + kq_goc + '$.')

            # Bước 6: Xuất nội dung theo mẫu
            list_ans = []
            for option in cac_lua_chon:
                if option == dap_an_dung:
                    list_ans.append('\\True $' + option + '$')
                else:
                    list_ans.append('$' + option + '$')

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + '\n'
                       '\\choice \n'
                       '{' + list_ans[0] + '}\n'
                       '{' + list_ans[1] + '}\n'
                       '{' + list_ans[2] + '}\n'
                       '{' + list_ans[3] + '}\n'
                       '\\loigiai{' + hinh_ve+ loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

