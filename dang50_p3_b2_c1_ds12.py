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


def bt_dang50_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random bán kính R (chọn các bội số của 6 để hệ số phương trình đạo hàm nguyên đẹp)
                R_list = [6, 12, 18, 24, 30]
                R = random.choice(R_list)

                # Tính toán các hệ số
                R_sq = R**2
                k = R // 3
                c1 = (5 * R) // 2
                c2 = 2 * R_sq
                a_max_coef = 4 * R
                V_max_coef = 4 * (R**3)

                # Tính giá trị max volume và làm tròn
                V_max_num = (V_max_coef * math.sqrt(15)) / 125
                kq3 = Decimal(float(V_max_num)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq = int(kq3)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % kq]
                da = du[0]

                # Sinh các phương án sai ngẫu nhiên (không trùng lặp)
                s_set = set()
                offsets = [1, -1, 2, -2, 3, -3, 5, -5, 10, -10]
                for off in offsets:
                    dist_val = kq + off
                    if dist_val > 0:
                        s_set.add('$%s$' % dist_val)

                if da in s_set:
                    s_set.remove(da)

                s = list(s_set)
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Code TikZ Hình 1 (Cho đề bài)
                tikz_img1 = ('''\\begin{tikzpicture}[scale=0.8, line width=1pt]
                    \\def\\R{2.5}
                    \\def\\d{0.45}
                    \\coordinate (O) at (0,0);
                    \\draw[blue, thick] (O) circle (\\R);
                    \\coordinate (H1) at (0,-\\R);
                    \\coordinate (H2) at ({-cos(30)*\\R}, {sin(30)*\\R});
                    \\coordinate (H3) at ({cos(30)*\\R}, {sin(30)*\\R});
                    \\coordinate (A1) at ({\\d*sqrt(3)}, -\\d);
                    \\coordinate (A2) at ({-\\d*sqrt(3)}, -\\d);
                    \\coordinate (A3) at (0, {2*\\d});
                    \\draw[red, thick] (A1) -- (A2) -- (A3) -- cycle;
                    \\draw[red, thick] (A1) -- (H1) -- (A2);
                    \\draw[red, thick] (A2) -- (H2) -- (A3);
                    \\draw[red, thick] (A3) -- (H3) -- (A1);
                    \\fill (O) circle (1.5pt);
                    \\fill (H1) circle (1.5pt);
                    \\fill (H2) circle (1.5pt);
                    \\fill (H3) circle (1.5pt);
                    \\fill (A1) circle (1.5pt);
                    \\fill (A2) circle (1.5pt);
                    \\fill (A3) circle (1.5pt);
                \\end{tikzpicture}''')

                # Code TikZ Hình 2 (Cho lời giải)
                tikz_img2 = ('''\\begin{center}
                \\begin{tikzpicture}[scale=0.8, line width=1pt]
                    \\def\\R{2.5}
                    \\def\\d{0.45}
                    \\coordinate (O) at (0,0);
                    \\draw[blue, thick] (O) circle (\\R);
                    \\coordinate (H) at (0,-\\R);
                    \\coordinate (H2) at ({-cos(30)*\\R}, {sin(30)*\\R});
                    \\coordinate (H3) at ({cos(30)*\\R}, {sin(30)*\\R});
                    \\coordinate (A) at ({\\d*sqrt(3)}, -\\d);
                    \\coordinate (A2) at ({-\\d*sqrt(3)}, -\\d);
                    \\coordinate (A3) at (0, {2*\\d});
                    \\coordinate (B) at (0,-\\d);
                    \\draw[red, thick] (A) -- (A2) -- (A3) -- cycle;
                    \\draw[red, thick] (A) -- (H) -- (A2);
                    \\draw[red, thick] (A2) -- (H2) -- (A3);
                    \\draw[red, thick] (A3) -- (H3) -- (A);
                    \\draw[dashed] (A3) -- (H);
                    \\node at (-0.25, 0.1) {$O$};
                    \\node at (-0.25, -\\d - 0.2) {$B$};
                    \\node at ({\\d*sqrt(3) + 0.3}, -\\d) {$A$};
                    \\node at (0, -\\R - 0.3) {$H$};
                    \\node at ({\\d*sqrt(3)/2 + 0.2}, {\\d/2}) {$a$};
                    \\node at ({\\d*sqrt(3)/2 + 0.3}, {-\\R/2 - \\d/2}) {$b$};
                    \\fill (O) circle (1.5pt);
                    \\fill (H) circle (1.5pt);
                    \\fill (H2) circle (1.5pt);
                    \\fill (H3) circle (1.5pt);
                    \\fill (A) circle (1.5pt);
                    \\fill (A2) circle (1.5pt);
                    \\fill (A3) circle (1.5pt);
                    \\fill (B) circle (1.5pt);
                \\end{tikzpicture}
                \\end{center}''')

                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một miếng bìa hình tròn tâm $O$ có bán kính bằng $%s$ cm. Ta cắt tấm bìa như hình vẽ rồi ghép thành hình chóp tam giác đều. Thể tích lớn nhất thu được của khối chóp tam giác bằng bao nhiêu centimet khối? (Kết quả làm tròn đến hàng đơn vị).}{%s}''' % (R, tikz_img1))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''%s
                Ta có: $OB = \\frac{1}{3} \\cdot \\frac{a\\sqrt{3}}{2} = \\frac{a\\sqrt{3}}{6} \\Rightarrow BH = %s - \\frac{a\\sqrt{3}}{6} \\Rightarrow OH = \\sqrt{BH^2 - OB^2} = ... = \\sqrt{%s - %sa\\sqrt{3}}$\\\\
                Suy ra thể tích $V = \\frac{1}{3} \\cdot OH \\cdot S_{\\Delta} = \\frac{1}{3} \\cdot \\sqrt{%s - %sa\\sqrt{3}} \\cdot \\frac{a^2\\sqrt{3}}{4}$ với $0 \\le a \\le %s\\sqrt{3}$.\\\\
                Xét hàm số $V(a) = \\frac{1}{3} \\sqrt{%s - %sa\\sqrt{3}} \\cdot \\frac{a^2\\sqrt{3}}{4}$ trên đoạn $\\left[ 0 ; %s\\sqrt{3} \\right]$\\\\
                Ta có: $V'(a) = \\frac{1}{3} \\cdot \\frac{ -%sa^2 + %sa\\sqrt{3} }{ 4\\sqrt{%s - %sa\\sqrt{3}} } = 0 \\Leftrightarrow \\left[ \\begin{array}{l} a=0 \\\\ a = \\frac{%s\\sqrt{3}}{5} \\in \\left[ 0 ; %s\\sqrt{3} \\right] \\end{array} \\right.$ và $V''\\left( \\frac{%s\\sqrt{3}}{5} \\right) < 0$\\\\
                Suy ra: $\\max V = \\max_{\\left[ 0 ; %s\\sqrt{3} \\right]} V(a) = V\\left( \\frac{%s\\sqrt{3}}{5} \\right) = \\frac{%s\\sqrt{15}}{125} \\approx %s$.'''
                % (tikz_img2, R, R_sq, k, R_sq, k, R, R_sq, k, R, c1, c2, R_sq, k, a_max_coef, R, a_max_coef, R, a_max_coef, V_max_coef, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

