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


def bt_dang26_p1_b1_c2_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random cạnh của hình vuông từ 1 đến 10
                a = random.randint(1, 20)

                # Tính độ dài thực tế của MN
                val = (a * math.sqrt(13)) / 2

                # Làm tròn đến hàng phần chục
                kq_dec = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_dec).replace('.', ',')
                kq_float = float(kq_dec)

                # Xử lý chuỗi toán học theo a (SymPy giúp hiển thị latex phân số chuẩn)
                # Độ dài AM
                if a % 2 == 0:
                    am_str = str(a // 2)
                    am_sq_str = "%s^2" % am_str
                else:
                    am_str = "\\frac{%s}{2}" % a
                    am_sq_str = "\\left(\\frac{%s}{2}\\right)^2" % a

                # DM^2 và DM
                dm_sq_val = sp.Rational(5 * a**2, 4)
                str_dm_sq = latex(dm_sq_val)
                if a % 2 == 0:
                    str_dm = "%s\\sqrt{5}" % (a // 2) if (a // 2) != 1 else "\\sqrt{5}"
                else:
                    str_dm = "\\frac{%s\\sqrt{5}}{2}" % a if a != 1 else "\\frac{\\sqrt{5}}{2}"

                # PM
                if a % 2 == 0:
                    pm_str = str(a + a // 2)
                    pm_sq_str = "%s^2" % pm_str
                else:
                    pm_str = "\\frac{%s}{2}" % (3 * a)
                    pm_sq_str = "\\left(\\frac{%s}{2}\\right)^2" % (3 * a)

                # MN^2 và MN
                mn_sq_val = sp.Rational(13 * a**2, 4)
                str_mn_sq = latex(mn_sq_val)
                if a % 2 == 0:
                    str_mn = "%s\\sqrt{13}" % (a // 2) if (a // 2) != 1 else "\\sqrt{13}"
                else:
                    str_mn = "\\frac{%s\\sqrt{13}}{2}" % a if a != 1 else "\\frac{\\sqrt{13}}{2}"

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu bằng cách cộng/trừ 0.1, 0.2, 0.3
                s = [
                    '$%s$' % str(Decimal(str(kq_float + 0.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(str(kq_float + 0.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(str(kq_float + 0.3)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(str(kq_float - 0.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(str(kq_float - 0.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(str(kq_float - 0.3)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                str_a = str(a)
                noidungcauhoi = ('''Cho hình vuông $ABCD$ tâm $O$ cạnh bằng $%s$. Gọi $M$ là trung điểm của $AB$, $N$ là điểm đối xứng với $C$ qua $D$. Độ dài của vectơ $\\overrightarrow{MN}$ bằng bao nhiêu? \\textit{Kết quả làm tròn đến hàng phần chục.}''' % str_a)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Mã TikZ vẽ hình học khớp với tỉ lệ bài toán
                code_hinh = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1.2, >=stealth]
            \\coordinate (P) at (0,0);
            \\coordinate (A) at (2,0);
            \\coordinate (M) at (3,0);
            \\coordinate (B) at (4,0);
            \\coordinate (N) at (0,2);
            \\coordinate (D) at (2,2);
            \\coordinate (C) at (4,2);
            \\coordinate (O) at (3,1);
            \\draw[thick] (P) -- (B) -- (C) -- (N) -- cycle;
            \\draw[thick] (A) -- (D);
            \\draw (A) -- (C);
            \\draw (B) -- (D);
            \\draw (N) -- (M);
            \\draw (D) -- (M);
            \\node[below] at (P) {$P$};
            \\node[below] at (A) {$A$};
            \\node[below] at (M) {$M$};
            \\node[below] at (B) {$B$};
            \\node[above] at (N) {$N$};
            \\node[above] at (D) {$D$};
            \\node[above] at (C) {$C$};
            \\node[below] at (3.1,0.95) {$O$};
            \\end{tikzpicture}
            \\end{center}''')

                # Nội dung lời giải
                loigiai = ('''%s
            Áp dụng định lý Pytago trong tam giác vuông $MAD$ ta có:\\\\
            $DM^2 = AM^2 + AD^2 = %s + %s^2 = %s \\Rightarrow DM = %s$.\\\\
            Qua $N$ kẻ đường thẳng song song với $AD$ cắt $AB$ tại $P$.\\\\
            Khi đó tứ giác $ADNP$ là hình vuông và $PM = PA + AM = %s + %s = %s$.\\\\
            Áp dụng định lý Pytago trong tam giác vuông $NPM$ ta có:\\\\
            $MN^2 = NP^2 + PM^2 = %s^2 + %s = %s \\Rightarrow MN = %s$.\\\\
            Suy ra $\\left| \\overrightarrow{MN} \\right| = MN = %s \\approx %s$.''' % (
                code_hinh, 
                am_sq_str, a, str_dm_sq, str_dm,
                a, am_str, pm_str,
                a, pm_sq_str, str_mn_sq, str_mn,
                str_mn, kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

