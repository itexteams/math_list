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


def bt_dang31_p3_b1_c2_hh11(self):
            # Khai báo biến
            # Với AB = CD = 2*k*a, MN = MN_he_so * a
            list_du_lieu = [
                (1, sqrt(3), 'a\\sqrt{3}', '60^\\circ'),
                (1, sqrt(2), 'a\\sqrt{2}', '90^\\circ'),
                (1, 1, 'a', '60^\\circ'),
                (2, 2*sqrt(3), '2a\\sqrt{3}', '60^\\circ'),
                (2, 2*sqrt(2), '2a\\sqrt{2}', '90^\\circ'),
                (3, 3*sqrt(3), '3a\\sqrt{3}', '60^\\circ')
            ]

            # Chọn ngẫu nhiên một bộ dữ liệu
            data = random.choice(list_du_lieu)
            k = data[0]
            mn_val = data[1]
            mn_latex = data[2]
            da_dung = data[3]

            # Tính toán các giá trị cho lời giải
            ab_val = 2 * k
            mp_val = k # PM = AB/2

            # Tính cos của góc MPN trong tam giác MPN
            # Định lý cosin: MN^2 = PM^2 + PN^2 - 2*PM*PN*cos(MPN)
            # => cos(MPN) = (PM^2 + PN^2 - MN^2) / (2*PM*PN)
            tu_so = mp_val**2 + mp_val**2 - mn_val**2
            mau_so = 2 * mp_val * mp_val
            cos_mpn = tu_so / mau_so

            # Xác định góc giữa hai đường thẳng
            angle_rad = math.acos(float(abs(cos_mpn)))
            angle_deg = round(math.degrees(angle_rad))
            da_dung = '$%s^\\circ$' % angle_deg

            # Tạo danh sách các phương án nhiễu
            cac_goc = ['30^\\circ', '45^\\circ', '60^\\circ', '90^\\circ']
            if str(angle_deg) + '^\\circ' in cac_goc:
                cac_goc.remove(str(angle_deg) + '^\\circ')
            random.shuffle(cac_goc)

            da_s1 = '$' + cac_goc[0] + '$'
            da_s2 = '$' + cac_goc[1] + '$'
            da_s3 = '$' + cac_goc[2] + '$'

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho tứ diện $ABCD$ có $AB = CD = %sa$. Gọi $M, N$ lần lượt là trung điểm của $AD$ và $BC$. Biết $MN = %s$, góc giữa hai đường thẳng $AB$ và $CD$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'
                % (latex(ab_val), mn_latex)
            )

            # TikZ code cho hình vẽ
            tikz_code = r'''\begin{center}
            \begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round]
                \coordinate (A) at (1,3);
                \coordinate (B) at (0,0);
                \coordinate (C) at (2,-1);
                \coordinate (D) at (4,0.5);
                \coordinate (M) at ($(A)!0.5!(D)$);
                \coordinate (N) at ($(B)!0.5!(C)$);
                \coordinate (P) at ($(A)!0.5!(C)$);
                \coordinate (Q) at ($(B)!0.5!(D)$);
                \draw (A)--(B)--(C)--(D)--(A)--(C) (P)--(N) (P)--(M);
                \draw[dashed] (B)--(D) (M)--(N) (M)--(Q) (N)--(Q);
                \foreach \p/\pos in {A/above, B/left, C/below, D/right, M/right, N/left, P/left, Q/below}
                    \fill (\p) node[\pos] {$\p$};
            \end{tikzpicture}
            \end{center}'''

            # Nội dung lời giải chi tiết
            h1=angle_deg
            number = Decimal(float(h1))  # Số cần làm tròn
            kqz = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            loigiai = (
                'Gọi $P, Q$ lần lượt là trung điểm của $AC$ và $BD$. Khi đó ta có: \\\\'
                '$\\begin{cases} PM // NQ // CD \\\\ PM = NQ = \\frac{CD}{2} \\end{cases} \\Rightarrow PMQN$ là hình bình hành. \\\\'
                'Ta cũng có $MQ // NP // AB, MQ = NP = \\frac{AB}{2}$. \\\\'
                'Do $AB = CD = %sa \\Rightarrow PM = MQ = QN = NP = %sa$. \\\\'
                'Gọi $(AB, CD) = \\alpha \\Rightarrow \\cos \\alpha = |\\cos(\\widehat{MPN})|$. \\\\ Áp dụng định lí Côsin trong tam giác $MPN$ ta có: \\\\'
                '$MN^2 = PM^2 + PN^2 - 2PM \\cdot PN \\cdot \\cos(\\widehat{MPN})$ \\\\'
                '$\\Leftrightarrow (%s)^2 = (%sa)^2 + (%sa)^2 - 2 \\cdot %sa \\cdot %sa \\cdot \\cos(\\widehat{MPN})$ \\\\'
                '$\\Leftrightarrow %s a^2 = %s a^2 - %s a^2 \\cdot \\cos(\\widehat{MPN})$ \\\\'
                '$\\Leftrightarrow \\cos(\\widehat{MPN}) = %s$. \\\\'
                'Nên $\\cos \\alpha = \\left|%s \\right| = %s \\Rightarrow (AB, CD) =$ %s $\\approx %s$.'
                % (latex(ab_val), latex(mp_val), mn_latex, latex(mp_val), latex(mp_val), 
                   latex(mp_val), latex(mp_val), latex(mn_val**2), latex(2*mp_val**2), 
                   latex(2*mp_val**2), latex(Rational(tu_so, mau_so)), 
                   latex(Rational(tu_so, mau_so)), latex(abs(Rational(tu_so, mau_so))), da_dung, str(kqz))
            )

            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(kqz)
            # Trộn đáp án
            list_ans = ['\\True ' + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Xuất câu trắc nghiệm theo mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + str(dapan)+
                '\\loigiai{' +    tikz_code + '\n'+ loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

