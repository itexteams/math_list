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


def bt_dang17_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Cố định tên đỉnh theo ảnh: A, B, C, D. Chân đường cao H, trung điểm M.
            a_val = random.randint(2, 10) # Ngẫu nhiên độ dài cạnh tứ diện để lời giải khác biệt

            # Ngẫu nhiên loại hàm lượng giác cần tính: 0: cos, 1: sin, 2: tan
            loai_hieu = random.randint(0, 2)
            ten_hieu = ['\\cos', '\\sin', '\\tan'][loai_hieu]

            # Tính toán giá trị đúng
            if loai_hieu == 0: # cos = BH/AB = sqrt(3)/3
                da_dung = '$\\cos \\varphi = \\frac{\\sqrt{3}}{3}$'
                list_sai = [
                    '$\\cos \\varphi = 0$',
                    '$\\cos \\varphi = \\frac{1}{2}$',
                    '$\\cos \\varphi = \\frac{\\sqrt{2}}{3}$',
                    '$\\cos \\varphi = \\frac{\\sqrt{3}}{2}$'
                ]
            elif loai_hieu == 1: # sin = AH/AB = sqrt(6)/3
                da_dung = '$\\sin \\varphi = \\frac{\\sqrt{6}}{3}$'
                list_sai = [
                    '$\\sin \\varphi = \\frac{1}{3}$',
                    '$\\sin \\varphi = \\frac{\\sqrt{3}}{3}$',
                    '$\\sin \\varphi = \\frac{\\sqrt{2}}{2}$',
                    '$\\sin \\varphi = 1$'
                ]
            else: # tan = AH/BH = sqrt(2)
                da_dung = '$\\tan \\varphi = \\sqrt{2}$'
                list_sai = [
                    '$\\tan \\varphi = \\frac{\\sqrt{2}}{2}$',
                    '$\\tan \\varphi = \\sqrt{3}$',
                    '$\\tan \\varphi = 1$',
                    '$\\tan \\varphi = \\frac{\\sqrt{6}}{2}$'
                ]

            # Trộn đáp án
            da_d = '\\True ' + da_dung
            random.shuffle(list_sai)
            list_4_da = [da_d, list_sai[0], list_sai[1], list_sai[2]]
            random.shuffle(list_4_da)

            # Nội dung câu hỏi
            noidungcauhoi = ('Cho tứ diện đều $ABCD$ có cạnh bằng $%s$. Gọi $\\varphi$ là góc giữa đường thẳng $AB$ và mặt phẳng $\\left(BCD\\right)$. Giá trị $%s \\varphi$ bằng'
                             % (latex(a_val), ten_hieu))

            # Hình vẽ TikZ (cố định đỉnh, nét vẽ 1pt)
            hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[line cap=round,line join=round,scale=0.8]
                \\coordinate (B) at (0,0);
                \\coordinate (C) at (1.5,-1.5);
                \\coordinate (D) at (4,0);
                \\coordinate (M) at ($(C)!0.5!(D)$);
                \\coordinate (H) at ($(B)!2/3!(M)$);
                \\coordinate (A) at ($(H)+(0,4)$);
                \\draw [line width=1pt, dash pattern=on 3pt off 3pt] (B)--(D) (B)--(M) (A)--(H);
                \\draw [line width=1pt] (A)--(B)--(C)--(D)--(A)--(C);
                \\begin{small}
                    \\draw [fill=red] (A)  node[above]{$A$};
                    \\draw [fill=red] (B)  node[left]{$B$};
                    \\draw [fill=red] (C)  node[below]{$C$};
                    \\draw [fill=red] (D)  node[right]{$D$};
                    \\draw [fill=red] (H)  node[below left]{$H$};
                    \\draw [fill=red] (M)  node[right]{$M$};
                \\end{small}
            \\end{tikzpicture}
            \\end{center}''')

            # Tính toán các giá trị trung gian cho lời giải dựa trên a_val
            bm_val = latex(Rational(a_val, 2)) + '\\sqrt{3}'
            bh_val = latex(Rational(a_val, 3)) + '\\sqrt{3}'
            ah_val = latex(Rational(a_val, 3)) + '\\sqrt{6}'

            # B2: Nội dung lời giải chi tiết
            if loai_hieu == 0:
                buoc_cuoi = '$\\cos \\varphi = \\cos \\widehat{ABM} = \\frac{BH}{AB} = \\frac{\\frac{%s\\sqrt{3}}{3}}{%s} = \\frac{\\sqrt{3}}{3}$' % (latex(a_val), latex(a_val))
            elif loai_hieu == 1:
                buoc_cuoi = '$\\sin \\varphi = \\sin \\widehat{ABM} = \\frac{AH}{AB} = \\frac{\\frac{%s\\sqrt{6}}{3}}{%s} = \\frac{\\sqrt{6}}{3}$' % (latex(a_val), latex(a_val))
            else:
                buoc_cuoi = '$\\tan \\varphi = \\tan \\widehat{ABM} = \\frac{AH}{BH} = \\frac{\\frac{%s\\sqrt{6}}{3}}{\\frac{%s\\sqrt{3}}{3}} = \\sqrt{2}$' % (latex(a_val), latex(a_val))

            loigiai = (hinh_ve +
                       'Gọi $M$ là trung điểm của $CD$. Ta có $BM = \\frac{AB\\sqrt{3}}{2} = \\frac{%s\\sqrt{3}}{2}$. \\\\ ' % (latex(a_val)) +
                       'Gọi $H$ là chân đường cao hạ từ $A$ xuống mặt phẳng $\\left(BCD\\right)$ thì $H \\in BM$ và ' +
                       '$BH = \\frac{2}{3}BM = \\frac{%s\\sqrt{3}}{3}$. \\\\ ' % (latex(a_val)) +
                       'Góc giữa đường thẳng $AB$ và mặt phẳng $\\left(BCD\\right)$ là $\\widehat{ABM}$. \\\\ ' +
                       'Ta có ' + buoc_cuoi + '.')

            # B4: Xuất câu trắc nghiệm đúng cấu trúc
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_4_da[0]) + '}\n'
                       '{' + str(list_4_da[1]) + '}\n'
                       '{' + str(list_4_da[2]) + '}\n'
                       '{' + str(list_4_da[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

