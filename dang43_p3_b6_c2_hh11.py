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


def bt_dang43_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            # Chúng ta sẽ random hệ số 'n' của cạnh AC = n
            n_val = random.randint(1, 4) 

            # Tính toán các giá trị theo n
            ac = n_val
            ab = 2 * n_val

            # BC = sqrt(AB^2 - AC^2) = n*sqrt(3)
            bc_sq = ab**2 - ac**2
            bc_val = math.sqrt(bc_sq)

            # Diện tích đáy ABC = 1/2 * AC * BC
            s_abc = 0.5 * ac * bc_val

            # Kẻ CH vuông góc AB. BH = BC^2 / AB = (3n^2) / (2n) = 1.5n
            bh = 1.5 * n_val

            # CH = sqrt(BC^2 - BH^2)
            ch_sq = bc_sq - (bh**2)
            ch_val = math.sqrt(ch_sq)

            # Góc CKH = 60 độ. HK = CH * cot(60)
            hk = ch_val * (1 / math.sqrt(3))

            # BK = sqrt(BH^2 - HK^2)
            bk_sq = bh**2 - hk**2
            bk_val = math.sqrt(bk_sq)

            # Tam giác SAB đồng dạng HKB => SA = (AB * HK) / BK
            sa = (ab * hk) / bk_val

            # Thể tích V = 1/3 * SA * S_abc
            v_final = (1/3) * sa * s_abc

            # Làm tròn kết quả đến hàng phần chục
            kq_float = round(v_final, 1)
            kq_str = str(kq_float).replace('.', ',')

            # Các phương án sai (tạo số thập phân ngẫu nhiên quanh kết quả)
            pa_sai1 = str(round(kq_float * 1.5, 1)).replace('.', ',')
            pa_sai2 = str(round(kq_float * 0.7, 1)).replace('.', ',')
            pa_sai3 = str(round(kq_float + 2.3, 1)).replace('.', ',')

            list_ans = ["\\True " + kq_str, pa_sai1, pa_sai2, pa_sai3]
            random.shuffle(list_ans)

            # Nội dung câu hỏi (Đã loại bỏ 'a')
            noidungcauhoi = ("Cho hình chóp $S.ABC$ có đáy là tam giác $ABC$ vuông tại $C$, $AB=%s$, $AC=%s$ và $SA$ vuông góc với mặt phẳng $\\left( ABC \\right)$. Biết góc giữa hai mặt phẳng $\\left( SAB \\right)$ and $\\left( SBC \\right)$ bằng $60^\\circ$. Thể tích của khối chóp $S.ABC$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)."
                             % (latex(ab), latex(ac)))

            # Lời giải chi tiết (Đã loại bỏ 'a')
            loigiai = ("Trong $\\Delta ABC$ kẻ $CH \\perp AB \\Rightarrow CH \\perp \\left( SAB \\right) \\Rightarrow CH \\perp SB$.\\\\ "
                       "$BC = \\sqrt{AB^2 - AC^2} = %s$.\\\\ "
                       "$BH \\cdot BA = BC^2 \\Rightarrow BH = %s$, $CH = \\sqrt{BC^2 - BH^2} = %s$.\\\\ "
                       "Trong $\\Delta SAB$ kẻ $HK \\perp SB \\Rightarrow CK \\perp SB$.\\\\ "
                       "Góc giữa hai mặt phẳng $\\left( SAB \\right)$ và $\\left( SBC \\right)$ là $\\widehat{CKH} = 60^\\circ$.\\\\ "
                       "Trong tam giác vuông $\\Delta CKH$ có $HK = CH \\cdot \\cot 60^\\circ = %s$, $BK = \\sqrt{BH^2 - HK^2} = %s$.\\\\ "
                       "$\\Delta SAB \\sim \\Delta HKB$ nên $\\frac{SA}{HK} = \\frac{AB}{BK} \\Rightarrow SA = %s$.\\\\ "
                       "Thể tích hình chóp $S.ABC$ là $V = \\frac{1}{3} \\cdot SA \\cdot S_{\\Delta ABC} \\approx %s$."
                       % (round(bc_val, 2), round(bh, 2), round(ch_val, 2), round(hk, 2), round(bk_val, 2), round(sa, 2), kq_str))

            dapan = '\\shortans[0]{%s}\n' % kq_str

            # TikZ Code
            tikz_code = ("\\begin{center} \\begin{tikzpicture}[line cap=round,line join=round,x=1.0cm,y=1.0cm, scale=0.8, line width=1pt]\n"
                         "\\coordinate (A) at (0,0); \n"
                         "\\coordinate (B) at (5,0); \n"
                         "\\coordinate (C) at (2,-1.5); \n"
                         "\\coordinate (S) at (0,5); \n"
                         "\\coordinate (H) at ($(A)!0.25!(B)$); \n"
                         "\\coordinate (K) at ($(B)!0.4!(S)$); \n"
                         "\\draw [dashed] (A)--(B) (C)--(H) (H)--(K);\n"
                         "\\draw (S)--(A) (S)--(B) (S)--(C) (A)--(C) (C)--(B) (C)--(K);\n"
                         "\\draw (0.2,0) -- (0.2,0.2) -- (0,0.2);\n"
                         "\\draw (1.8,-1.3) -- (1.95,-1.45) -- (2.1,-1.3);\n"
                         "\\begin{scriptsize}\n"
                         "\\draw (S) node[above left] {$S$};\n"
                         "\\draw (A) node[left] {$A$};\n"
                         "\\draw (B) node[right] {$B$};\n"
                         "\\draw (C) node[below] {$C$};\n"
                         "\\draw (H) node[above left] {$H$};\n"
                         "\\draw (K) node[above right] {$K$};\n"
                         "\\draw (1.8,0.3) node {$60^\\circ$};\n"
                         "\\end{scriptsize}\n"
                         "\\draw (H)++(0.1,0.03) -- ++(0.05,0.15) -- ++(-0.1,0); \n"
                         "\\draw (K)++(-0.1,-0.1) -- ++(-0.1,0.1) -- ++(0.1,0.1); \n"
                         "\\end{tikzpicture} \\end{center}")

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +str(dapan)+
                       '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

