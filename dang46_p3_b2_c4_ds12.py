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


def bt_dang46_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lượng bi trong các hộp (Giới hạn hợp lý để vẽ hình đẹp)
                r1 = random.randint(3, 5) # Đỏ hộp 1
                b1 = random.randint(4, 6) # Xanh hộp 1
                r2 = random.randint(2, 4) # Đỏ hộp 2
                b2 = random.randint(3, 5) # Xanh hộp 2

                n1 = r1 + b1
                n2 = r2 + b2

                # Tính toán các tổ hợp
                c_r1_2 = math.comb(r1, 2)
                c_b1_2 = math.comb(b1, 2)
                c_r1_1 = math.comb(r1, 1)
                c_b1_1 = math.comb(b1, 1)
                c_n1_2 = math.comb(n1, 2)

                # Tính xác suất các biến cố H (chuyển bi)
                pH1 = frac(c_r1_2, c_n1_2)
                pH2 = frac(c_b1_2, c_n1_2)
                pH3 = frac(c_r1_1 * c_b1_1, c_n1_2)

                # Tính xác suất biến cố A (rút bi đỏ) với điều kiện H
                pA_H1 = frac(r2 + 2, n2 + 2)
                pA_H2 = frac(r2, n2 + 2)
                pA_H3 = frac(r2 + 1, n2 + 2)

                # Tính xác suất toàn phần P(A)
                term1 = pH1 * pA_H1
                term2 = pH2 * pA_H2
                term3 = pH3 * pA_H3

                pA = term1 + term2 + term3

                # Tính xác suất hậu nghiệm P(H3|A)
                ans_frac = term3 / pA

                # Định dạng kết quả số thập phân làm tròn 2 chữ số
                ans_float = float(ans_frac)
                ans_dec = Decimal(str(ans_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                ans_str = str(ans_dec).replace('.', ',')

                # Sinh phương án sai (không trùng đáp án đúng)
                s_options = set([
                    str(Decimal(str(float(ans_frac) + 0.12)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    str(Decimal(str(float(ans_frac) - 0.05)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    str(Decimal(str(float(ans_frac) + 0.08)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    str(Decimal(str(float(ans_frac) + 0.15)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    str(Decimal(str(float(ans_frac) - 0.11)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
                ])
                if ans_str in s_options:
                    s_options.remove(ans_str)
                s_list = list(s_options)

                du = ['$%s$' % ans_str]
                da = du[0]
                das1 = '$%s$' % s_list[0]
                das2 = '$%s$' % s_list[1]
                das3 = '$%s$' % s_list[2]

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = ['\\True ' + da, das1, das2, das3]
                random.shuffle(list_1)

                # Hàm sinh mã TikZ tự động cho các viên bi trong hộp
                def get_tikz_balls(r, b, offset_x):
                    tikz = ""
                    positions = [
                        (-0.6, 0.2), (-0.2, 0.2), (0.2, 0.2), (0.6, 0.2),
                        (-0.8, 0.6), (-0.4, 0.6), (0.0, 0.6), (0.4, 0.6), (0.8, 0.6),
                        (-0.6, 1.0), (-0.2, 1.0), (0.2, 1.0), (0.6, 1.0)
                    ]
                    colors = ['red'] * r + ['blue'] * b
                    for i in range(len(colors)):
                        x, y = positions[i]
                        if colors[i] == 'red':
                            fill_col = 'red!30'
                            draw_col = 'red'
                        else:
                            fill_col = 'blue!30'
                            draw_col = 'blue'
                        tikz += "\\filldraw[fill=%s, draw=%s, line width=1pt] (%s, %s) circle (0.15);" % (fill_col, draw_col, offset_x + x, y)
                    return tikz

                tikz_urn1 = get_tikz_balls(r1, b1, -2.5)
                tikz_urn2 = get_tikz_balls(r2, b2, 2.5)

                # Nội dung câu hỏi
                noidungcauhoi = '''Có hai hộp đựng bi: Hộp I đựng $%s$ viên bi gồm $%s$ viên màu đỏ và $%s$ viên màu xanh. Hộp II đựng $%s$ viên bi gồm $%s$ viên màu đỏ và $%s$ viên màu xanh.
            \\begin{center}
            \\begin{tikzpicture}[scale=1, >=stealth]
            \\node at (-2.5, 1.8) {\\textbf{Hộp I}};
            \\draw[blue, line width=1pt] (-3.5,0) -- (-1.5,0) -- (-1.1, 1.5) -- (-3.9, 1.5) -- cycle;
            %s
            \\node at (2.5, 1.8) {\\textbf{Hộp II}};
            \\draw[blue, line width=1pt] (1.5,0) -- (3.5,0) -- (3.9, 1.5) -- (1.1, 1.5) -- cycle;
            %s
            \\end{tikzpicture}
            \\end{center}
            Lấy ngẫu nhiên $2$ viên bi từ hộp I bỏ sang hộp II. Sau khi trộn đều, người ta lấy ngẫu nhiên $1$ viên bi từ hộp II ra. Biết rằng viên bi lấy ra từ hộp II là bi màu đỏ. Xác suất để $2$ viên bi đã chuyển từ hộp I sang hộp II có màu khác nhau bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).''' % (n1, r1, b1, n2, r2, b2, tikz_urn1, tikz_urn2)

                # Nội dung lời giải
                loigiai = '''Gọi $A$ là biến cố "Viên bi lấy ra từ hộp II là màu đỏ".\\\\
            Gọi $H_1$ là biến cố "Lấy $2$ viên từ hộp I sang hộp II là màu đỏ" thì $P(H_1) = \\frac{C_{%s}^2}{C_{%s}^2} = \\frac{%s}{%s}$.\\\\
            Gọi $H_2$ là biến cố "Lấy $2$ viên từ hộp I sang hộp II là màu xanh" thì $P(H_2) = \\frac{C_{%s}^2}{C_{%s}^2} = \\frac{%s}{%s}$.\\\\
            Gọi $H_3$ là biến cố "Lấy $2$ viên từ hộp I sang hộp II là $1$ đỏ và $1$ xanh" thì $P(H_3) = \\frac{C_{%s}^1 \\cdot C_{%s}^1}{C_{%s}^2} = \\frac{%s}{%s}$.\\\\
            Sau khi chuyển $2$ viên bi từ hộp I sang thì hộp II sẽ có tổng cộng $%s$ viên bi.\\\\
            Nếu $H_1$ xảy ra thì hộp II có $%s + 2 = %s$ đỏ $\\Rightarrow P(A|H_1) = \\frac{%s}{%s}$.\\\\
            Nếu $H_2$ xảy ra thì hộp II có $%s + 0 = %s$ đỏ $\\Rightarrow P(A|H_2) = \\frac{%s}{%s}$.\\\\
            Nếu $H_3$ xảy ra thì hộp II có $%s + 1 = %s$ đỏ $\\Rightarrow P(A|H_3) = \\frac{%s}{%s}$.\\\\
            Ta có:
            $$P(A) = P(H_1)P(A|H_1) + P(H_2)P(A|H_2) + P(H_3)P(A|H_3) = \\frac{%s}{%s} \\cdot \\frac{%s}{%s} + \\frac{%s}{%s} \\cdot \\frac{%s}{%s} + \\frac{%s}{%s} \\cdot \\frac{%s}{%s} = \\frac{%s}{%s}$$
            Vậy xác suất cần tìm là: 
            $$P(H_3|A) = \\frac{P(H_3)P(A|H_3)}{P(A)} = \\frac{\\frac{%s}{%s} \\cdot \\frac{%s}{%s}}{\\frac{%s}{%s}} = \\frac{%s}{%s} \\approx %s.$$''' % (
                    r1, n1, c_r1_2, c_n1_2,
                    b1, n1, c_b1_2, c_n1_2,
                    r1, b1, n1, c_r1_1 * c_b1_1, c_n1_2,
                    n2 + 2,
                    r2, r2 + 2, r2 + 2, n2 + 2,
                    r2, r2, r2, n2 + 2,
                    r2, r2 + 1, r2 + 1, n2 + 2,
                    c_r1_2, c_n1_2, r2 + 2, n2 + 2, c_b1_2, c_n1_2, r2, n2 + 2, c_r1_1 * c_b1_1, c_n1_2, r2 + 1, n2 + 2, pA.numerator, pA.denominator,
                    c_r1_1 * c_b1_1, c_n1_2, r2 + 1, n2 + 2, pA.numerator, pA.denominator, ans_frac.numerator, ans_frac.denominator, ans_str
                )
                dapan='\\shortans[0]{$%s$}\n'%(ans_str)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

