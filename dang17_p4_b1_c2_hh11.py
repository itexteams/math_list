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


def bt_dang17_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các bộ số (AB_coeff, CD_coeff, MN_coeff, Angle_deg)
                # AB = k1*a, CD = k2*a, MN = k3*a
                # Hệ thức: 4*MN^2 = AB^2 + CD^2 + 2 * BA . CD
                # => cos(BA, CD) = (4*MN^2 - AB^2 - CD^2) / (2 * AB * CD)

                presets = [
                    (2, 2*sqrt(2), sqrt(5), 45),
                    (2, 2, sqrt(3), 60),
                    (2, 2, sqrt(2), 90),
                    (2, 2*sqrt(3), sqrt(7), 30)
                ]

                chosen = random.choice(presets)
                k1, k2, k3, angle_true = chosen

                # Biến ký hiệu 'a'
                a = symbols('a')
                val_AB = k1 * a
                val_CD = k2 * a
                val_MN = k3 * a

                # Tính toán trung gian cho lời giải
                sq_MN_4 = 4 * (val_MN**2)
                sq_AB = val_AB**2
                sq_CD = val_CD**2
                dot_prod_2 = simplify(sq_MN_4 - sq_AB - sq_CD)
                dot_prod = simplify(dot_prod_2 / 2)

                cos_val = simplify(abs(dot_prod) / (val_AB * val_CD))

                # Đáp án đúng
                kq = str(angle_true) + '^\\circ'
                da_d = '\\True ' + '$' + kq + '$'

                # Tạo các đáp án sai
                angles_fail = {30, 45, 60, 90}
                angles_fail.remove(angle_true)
                list_fail = random.sample(list(angles_fail), 3)

                da_s1 = '$' + str(list_fail[0]) + '^\\circ$'
                da_s2 = '$' + str(list_fail[1]) + '^\\circ$'
                da_s3 = '$' + str(list_fail[2]) + '^\\circ$'

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Hình vẽ TikZ
                tikz_code = """\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                \\coordinate (B) at (0,0);
                \\coordinate (C) at (1.5,-1.2);
                \\coordinate (D) at (4,0);
                \\coordinate (A) at (2,3);
                \\coordinate (M) at ($(B)!0.5!(C)$);
                \\coordinate (N) at ($(A)!0.5!(D)$);
                \\draw (A)--(B)--(C)--(D)--(A)--(C);
                \\draw[dashed] (B)--(D) (M)--(N);
                \\foreach \\p/\\pos in {A/above, B/left, C/below, D/right, M/below left, N/above right} \\fill (\\p) circle (1pt) node[\\pos]{\\p};
                \\end{tikzpicture}"""

                # Câu hỏi
                noidungcauhoi = ("Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm của $BC, AD$. Biết $AB = %s$, $CD = %s$ và $MN = %s$. Tính góc giữa hai đường thẳng $AB$ và $CD$."
                                 % (latex(val_AB), latex(val_CD), latex(val_MN)))

                # Lời giải
                loigiai = ("Ta có: $\\vec{MN} = \\vec{MB} + \\vec{BA} + \\vec{AN}$ và $\\vec{MN} = \\vec{MC} + \\vec{CD} + \\vec{DN}$. \\\\\n"
                           "Cộng hai vế ta được: $2\\vec{MN} = (\\vec{MB} + \\vec{MC}) + (\\vec{BA} + \\vec{CD}) + (\\vec{AN} + \\vec{DN})$. \\\\\n"
                           "Vì $M$ là trung điểm $BC$ và $N$ là trung điểm $AD$ nên $\\vec{MB} + \\vec{MC} = \\vec{0}$ và $\\vec{AN} + \\vec{DN} = \\vec{0}$. \\\\\n"
                           "Suy ra $2\\vec{MN} = \\vec{BA} + \\vec{CD}$. \\\\\n"
                           "Khi đó: $(2\\vec{MN})^2 = (\\vec{BA} + \\vec{CD})^2 \\Leftrightarrow 4\\vec{MN}^2 = \\vec{BA}^2 + \\vec{CD}^2 + 2\\vec{BA}\\cdot\\vec{CD}$. \\\\\n"
                           "Thay số: $4(%s)^2 = (%s)^2 + (%s)^2 + 2\\vec{BA}\\cdot\\vec{CD}$ \\\\\n"
                           "$\\Leftrightarrow %s = %s + %s + 2\\vec{BA}\\cdot\\vec{CD} \\Leftrightarrow 2\\vec{BA}\\cdot\\vec{CD} = %s$. \\\\\n"
                           "Do đó $\\vec{BA}\\cdot\\vec{CD} = %s$. \\\\\n"
                           "Ta có: $\\cos(AB, CD) = \\frac{|\\vec{BA}\\cdot\\vec{CD}|}{|\\vec{BA}| \\cdot |\\vec{CD}|} = \\frac{|%s|}{%s \\cdot %s} = %s$. \\\\\n"
                           "Vậy số đo góc giữa hai đường thẳng $AB$ và $CD$ là $%s$."
                           % (latex(val_MN), latex(val_AB), latex(val_CD),
                              latex(sq_MN_4), latex(sq_AB), latex(sq_CD), latex(dot_prod_2),
                              latex(dot_prod), latex(dot_prod), latex(val_AB), latex(val_CD),
                              latex(cos_val), kq))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + 
                       str(noidungcauhoi) + '\n' +
                       '\\begin{center}\n' + tikz_code + '\n\\end{center}\n' +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

