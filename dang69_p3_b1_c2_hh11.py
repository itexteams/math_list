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


def bt_dang69_p3_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo các thiết lập ban đầu
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random độ dài cạnh AB = AC = AD = a
                # Ở đây chọn a là số nguyên dương để tính toán đẹp (1, 2, 3, 4, 5)
                a = random.randint(1, 5)

                # Tính toán các giá trị liên quan
                ab = a
                ac = a
                ad = a

                bc_val = sqrt(ab**2 + ac**2) # Cạnh huyền tam giác vuông ABC
                cd_val = sqrt(ac**2 + ad**2) # Cạnh huyền tam giác vuông ACD

                mn_val = Rational(ab, 2)
                np_val = cd_val / 2

                # AM là đường trung tuyến của tam giác vuông ABC ứng với cạnh huyền BC
                am_val = bc_val / 2
                ap_val = Rational(ad, 2)

                # MP tính trong tam giác vuông PAM (vì AD vuông góc với mặt phẳng ABC)
                mp_sq = ap_val**2 + am_val**2
                mp_val = sqrt(mp_sq)

                # Góc giữa AB và CD là góc giữa MN và NP (vì MN // AB và NP // CD)
                # Ta dùng định lý Cosin trong tam giác MNP: cos(MNP) = (MN^2 + NP^2 - MP^2) / (2 * MN * NP)
                # Với các thông số trên, cos(MNP) luôn bằng 0, góc luôn bằng 90 độ.

                kq_text = "90^\\circ"
                da = "$%s$" % kq_text

                # Các đáp án trắc nghiệm khác
                s = ["$30^\\circ$", "$45^\\circ$", "$60^\\circ$", "$0^\\circ$"]
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = (
                    "Cho tứ diện $ABCD$ có $AB, AC, AD$ đôi một vuông góc với nhau, biết $AB = AC = AD = %s$. "
                    "Số đo góc giữa hai đường thẳng $AB$ và $CD$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị)."
                    % (latex(a))
                )

                # Các đáp án
                da_d = "\\True " + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Vẽ hình bằng TikZ
                tikz_code = (
                    "\\begin{center}\n"
                    "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
                    "\\coordinate (A) at (0,0);\n"
                    "\\coordinate (B) at (-1.5,-1.2);\n"
                    "\\coordinate (C) at (3,0);\n"
                    "\\coordinate (D) at (0,3);\n"
                    "\\coordinate (M) at ($(B)!0.5!(C)$);\n"
                    "\\coordinate (N) at ($(A)!0.5!(C)$);\n"
                    "\\coordinate (P) at ($(A)!0.5!(D)$);\n"
                    "\\draw (D)--(B)--(C)--cycle;\n"
                    "\\draw (D)--(C);\n"
                    "\\draw[dashed] (A)--(B) (A)--(C) (A)--(D) (A)--(M) (A)--(N) (N)--(M);\n"
                    "\\draw[dashed] (P)--(M);\n"
                    "\\draw[dashed] (M)--(N);\n"
                    "\\draw[dashed] (N)--(P);\n"
                    "\\tkzMarkRightAngle[size=0.2](B,A,C)\n"
                    "\\tkzMarkRightAngle[size=0.2](C,A,D)\n"
                    "\\tkzMarkRightAngle[size=0.2](B,A,D)\n"
                    "\\node[below left] at (B) {$B$};\n"
                    "\\node[below] at (A) {$A$};\n"
                    "\\node[right] at (C) {$C$};\n"
                    "\\node[above] at (D) {$D$};\n"
                    "\\node[below right] at (M) {$M$};\n"
                    "\\node[below] at (N) {$N$};\n"
                    "\\node[left] at (P) {$P$};\n"
                    "\\end{tikzpicture}\n"
                    "\\end{center}"    )

                # Lời giải chi tiết
                loigiai = (
                    "Gọi $M, N, P$ lần lượt là trung điểm của các cạnh $BC, AC, AD$. \\\\\n"
                    "Trong $\\triangle ABC$, có $\\begin{cases} MN \\parallel AB \\\\ MN = \\frac{1}{2} AB = \\frac{%s}{2} \\end{cases}$ (Tính chất đường trung bình). \\\\\n"
                    "Trong $\\triangle ACD$, có $\\begin{cases} NP \\parallel CD \\\\ NP = \\frac{1}{2} CD = \\frac{%s}{2} \\end{cases}$ (Tính chất đường trung bình). \\\\\n"
                    "Trong $\\triangle AMP$, có $MP = \\sqrt{AP^2 + AM^2} = \\sqrt{\\left(\\frac{%s}{2}\\right)^2 + \\left(\\frac{%s}{2}\\right)^2} = \\frac{%s}{2}$. \\\\\n"
                    "Ta có $\\begin{cases} MN \\parallel AB \\\\ NP \\parallel CD \\end{cases} \\Rightarrow (AB; CD) = (MN; NP) = \\widehat{MNP}$. \\\\\n"
                    "Áp dụng định lý Cosin cho $\\triangle MNP$, có: \\\\\n"
                    "$\\cos \\widehat{MNP} = \\frac{NP^2 + NM^2 - MP^2}{2NP \\cdot NM} = \\frac{\\left(\\frac{%s}{2}\\right)^2 + \\left(\\frac{%s}{2}\\right)^2 - \\left(\\frac{%s}{2}\\right)^2}{2 \\cdot \\frac{%s}{2} \\cdot \\frac{%s}{2}} = 0 \\Rightarrow \\widehat{MNP} = 90^\\circ$. \\\\\n"
                    "Hay $(AB, CD) = 90^\\circ$."
                    % (latex(ab), latex(cd_val), latex(ad), latex(bc_val), latex(sqrt(mp_sq)*2),
                       latex(cd_val), latex(ab), latex(sqrt(mp_sq)*2), latex(cd_val), latex(ab))
                )
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(90))

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(tikz_code)+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

