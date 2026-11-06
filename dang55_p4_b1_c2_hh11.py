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


def bt_dang55_p4_b1_c2_hh11(self):
            # Khai báo biến
            # ta giữ nguyên các góc 60, 90, 120 và thay đổi độ dài cạnh a = AB = AC = AD.
            a_val = random.randint(1, 6) # Ngẫu nhiên cạnh a từ 1 đến 6

            # Các giá trị tính toán dựa trên a
            # BC = a (do tam giác ABC đều)
            # BD = a*sqrt(2) (do tam giác ABD vuông cân tại A)
            # CD = a*sqrt(3) (do tam giác ACD cân tại A có góc 120 độ)
            bc_sq = a_val**2
            bd_sq = 2 * (a_val**2)
            cd_sq = 3 * (a_val**2)

            # Các cạnh tính bằng sympy để xuất latex đẹp
            a = a_val
            bc = a
            bd = sqrt(bd_sq)
            cd = sqrt(cd_sq)

            # Tính toán các đoạn thẳng phụ như trong lời giải
            bi = Rational(a, 2)
            # DI^2 = BD^2 + BI^2 = 2a^2 + a^2/4 = 9a^2/4 => DI = 3a/2
            di = Rational(3*a, 2)
            # IG = 1/3 * DI = a/2
            ig = Rational(a, 2)
            # MG = 1/3 * CD = (a*sqrt(3))/3
            mg = Rational(a, 3) * sqrt(3)
            # IM = 1/3 * IC = 1/3 * (a/2) = a/6
            im = Rational(a, 6)

            # AI là chiều cao tam giác đều ABC cạnh a: AI = a*sqrt(3)/2
            ai = Rational(a, 2) * sqrt(3)

            # AM^2 = AI^2 + IM^2 (do AI vuông góc BC tại I và IM nằm trên BC)
            am_sq = ai**2 + im**2 # (3a^2/4 + a^2/36) = 28a^2/36 = 7a^2/9
            am = sqrt(am_sq)

            # Tính cos(AID) trong tam giác AID
            # cos(AID) = (AI^2 + ID^2 - AD^2) / (2 * AI * ID)
            cos_aid = (ai**2 + di**2 - a**2) / (2 * ai * di)

            # Tính AG^2 bằng định lý cos trong tam giác AIG
            # AG^2 = AI^2 + IG^2 - 2*AI*IG*cos(AID)
            ag_sq = ai**2 + ig**2 - 2 * ai * ig * cos_aid
            ag = sqrt(ag_sq)

            # Tính cos của góc giữa AG và MG (chính là góc giữa AG và CD)
            # cos(AG, MG) = |AG^2 + MG^2 - AM^2| / (2 * AG * MG)
            cos_val = abs(ag_sq + mg**2 - am_sq) / (2 * ag * mg)

            # --- BƯỚC 3 & 4: XỬ LÝ ĐÁP ÁN ---
            kq_dung = '$%s$' % latex(cos_val)

            # Tạo danh sách đáp án sai (tránh trùng đáp án đúng)
            list_sai = []
            candidates = [
                Rational(1, 3), Rational(1, 2), sqrt(3)/3, sqrt(6)/6, 
                Rational(1, 4), sqrt(2)/4, Rational(1, 5)
            ]
            for c in candidates:
                c_tex = '$%s$' % latex(c)
                if c_tex != kq_dung:
                    list_sai.append(c_tex)

            random.shuffle(list_sai)
            da_s1 = list_sai[0]
            da_s2 = list_sai[1]
            da_s3 = list_sai[2]

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (
                'Cho tứ diện $ABCD$ có $AB = AC = AD = %s$; '
                '$\\widehat{BAC} = 60^\\circ$; $\\widehat{BAD} = 90^\\circ$; $\\widehat{DAC} = 120^\\circ$. '
                'Tính cosin của góc tạo bởi hai đường thẳng $AG$ và $CD$, trong đó $G$ là trọng tâm tam giác $BCD$.'
                % (a)
            )

            # --- NỘI DUNG LỜI GIẢI ---
            loigiai = (
                '$\\triangle ABC$ đều $\\Rightarrow BC = %s$.\\\\'
                '$\\triangle ACD$ cân tại $A$ có $CD = \\sqrt{AC^2 + AD^2 - 2AC \\cdot AD \\cdot \\cos 120^\\circ} = %s$.\\\\'
                '$\\triangle ABD$ vuông cân tại $A$ có $BD = %s$.\\\\'
                '$\\triangle BCD$ có $CD^2 = BC^2 + BD^2$ (do $(%s)^2 = %s^2 + (%s)^2$) $\\Rightarrow \\triangle BCD$ vuông tại $B$.\\\\'
                'Dựng đường thẳng $d$ qua $G$ và song song $CD$, cắt $BC$ tại $M$.\\\\'
                'Ta có $MG \\parallel CD \\Rightarrow (AG, CD) = (AG, MG)$.\\\\'
                'Gọi $I$ là trung điểm của $BC$, xét $\\triangle BDI$ vuông tại $B$ có $DI = \\sqrt{BD^2 + BI^2} = %s$.\\\\'
                'Ta có $\\frac{IM}{IC} = \\frac{MG}{CD} = \\frac{IG}{ID} = \\frac{1}{3} \\Rightarrow IM = %s; MG = %s; IG = %s$.\\\\'
                'Xét $\\triangle AIM$ vuông tại $I$ có $AM = \\sqrt{AI^2 + IM^2} = %s$.\\\\'
                '$\\cos \\widehat{AID} = \\frac{AI^2 + ID^2 - AD^2}{2AI \\cdot ID} = %s$.\\\\'
                '$AG = \\sqrt{AI^2 + IG^2 - 2AI \\cdot IG \\cdot \\cos \\widehat{AID}} = %s$.\\\\'
                'Xét $\\triangle AMG$ có: '
                '$\\cos(AG, MG) = |\\cos \\widehat{AGM}| = \\left| \\frac{AG^2 + GM^2 - AM^2}{2 \\cdot AG \\cdot GM} \\right| = %s$.'
                % (
                    latex(bc), latex(cd), latex(bd), latex(cd), latex(bc), latex(bd),
                    latex(di), latex(im), latex(mg), latex(ig),
                    latex(am), latex(cos_aid), latex(ag), latex(cos_val)
                )
            )

            # --- TIKZ DIAGRAM ---
            tikz_code = ('\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]\n'
                '   \\coordinate (A) at (0,3.5);\n'
                '   \\coordinate (B) at (-2,0);\n'
                '   \\coordinate (C) at (-0.5,-1.5);\n'
                '   \\coordinate (D) at (3,0);\n'
                '   \\coordinate (I) at ($(B)!0.5!(C)$);\n'
                '   \\coordinate (G) at ($(B)!1/3!(C)!1/3!(D)$);\n'
                '   \\coordinate (M) at ($(I)!1/3!(C)$);\n'
                '   \\draw[dashed] (B)--(D) (A)--(I) (D)--(I) (A)--(G) (I)--(G) (M)--(G);\n'
                '   \\draw (A)--(B)--(C)--(D)--(A)--(C);\n'
                '   \\foreach \\p/\\pos in {A/above, B/left, C/below, D/right, I/left, G/right, M/below} \n'
                '       \\fill (\\p) node[\\pos] {$\\p$};\n'
                '\\end{tikzpicture}'
                '\\end{center}\n')

            # --- XUẤT NỘI DUNG ---
            list_ans = ['\\True ' + kq_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'
                + str(noidungcauhoi) + '\n'
                '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

