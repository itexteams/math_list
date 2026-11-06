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


def bt_dang20_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo ngẫu nhiên điểm cực tiểu x1 và điểm cực đại x2 (số nguyên đẹp)
                x1 = randint(2, 4)       # Điểm doanh thu bắt đầu tăng trở lại (ngàn sản phẩm)
                x2 = x1 + randint(3, 6)  # Điểm cực đại của doanh thu

                # Tính các hệ số nguyên cho hàm số R(x) = -2x^3 + b*x^2 + c*x + d
                coeff_a = -2
                coeff_b = 3 * (x1 + x2)
                coeff_c = -6 * x1 * x2
                D_val = randint(80, 200)

                # Kết quả đúng đổi ra đơn vị sản phẩm: x1 * 1000
                kq_num = x1 * 1000
                kq = str(kq_num)

                # Các đáp án trắc nghiệm
                du = ['$%s$ sản phẩm' % (kq)]
                da = random.choice(du)

                # Tạo danh sách các phương án nhiễu (sai) không trùng đáp án đúng
                s_candidates = [
                    (x1 + 1) * 1000,
                    x2 * 1000,
                    (x2 - x1) * 1000,
                    abs(x1 - 1) * 1000 if x1 > 1 else 500,
                    (x2 + 1) * 1000
                ]

                s = []
                for val in s_candidates:
                    s.append('$%s$ sản phẩm' % (str(val)))

                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Định dạng dấu hiển thị cho các hệ số trong đa thức
                sign_b = '+' if coeff_b >= 0 else ''
                sign_c = '+' if coeff_c >= 0 else ''
                sign_d = '+' if D_val >= 0 else ''

                ham_so_latex = '%s x^3 %s %s x^2 %s %s x %s %s' % (latex(coeff_a), sign_b, latex(coeff_b), sign_c, latex(coeff_c), sign_d, latex(D_val))
                ham_so_latex = ' '.join(ham_so_latex.split())

                # Câu hỏi
                noidungcauhoi = ('''Một công ty sản xuất sản phẩm và doanh thu (đơn vị: triệu đồng) từ việc bán sản phẩm được mô tả bởi hàm số $R(x) = %s$. Trong đó, $x$ là số lượng sản phẩm được bán ra (tính bằng ngàn sản phẩm). Hỏi số lượng sản phẩm tối thiểu phải bán ra để doanh thu bắt đầu tăng là bao nhiêu sản phẩm? (Kết quả làm tròn đến hàng đơn vị)'''
                                 % (ham_so_latex))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Phục vụ hiển thị đạo hàm trong lời giải
                der_a = 3 * coeff_a
                der_b = 2 * coeff_b
                der_c = coeff_c
                sign_der_b = '+' if der_b >= 0 else ''
                sign_der_c = '+' if der_c >= 0 else ''

                dao_ham_latex = '%s x^2 %s %s x %s %s' % (latex(der_a), sign_der_b, latex(der_b), sign_der_c, latex(der_c))
                dao_ham_latex = ' '.join(dao_ham_latex.split())

                # Lời giải chi tiết kèm lập bảng biến thiên bằng TikZ, độ dày nét 1pt
                loigiai = ('''Xét hàm số doanh thu $R(x) = %s$ trên nửa khoảng $[0; +\\infty)$.\\\\
                           Ta có đạo hàm của hàm số là:\\\\
                           $R\'(x) = %s$.\\\\
                           Cho $R\'(x) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow \\left[\\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned}\\right.$.\\\\
                           Ta lập bảng biến thiên của hàm số $R(x)$ trên nửa khoảng $[0; +\\infty)$ như sau:\\\\
                           \\begin{center}
                           \\begin{tikzpicture}[scale=1]
                           \\draw[line width=1pt] (0,3) -- (10,3);
                           \\draw[line width=1pt] (0,2) -- (10,2);
                           \\draw[line width=1pt] (2,0) -- (2,4);
                           \\node at (1,3.5) {$x$};
                           \\node[anchor=west] at (2,3.5) {$[0$};
                           \\node at (4.5,3.5) {$%s$};
                           \\node at (7.2,3.5) {$%s$};
                           \\node at (9.5,3.5) {$+\\infty$};
                           \\node at (1,2.5) {$R\'(x)$};
                           \\node at (3.25,2.5) {$-$};
                           \\node at (4.5,2.5) {$0$};
                           \\node at (5.85,2.5) {$+$};
                           \\node at (7.2,2.5) {$0$};
                           \\node at (8.5,2.5) {$-$};
                           \\node at (1,1) {$R(x)$};
                           \\draw[->,line width=1pt] (2.4,1.7) -- (4.2,0.3);
                           \\draw[->,line width=1pt] (4.8,0.3) -- (6.9,1.7);
                           \\draw[->,line width=1pt] (7.5,1.7) -- (9.3,0.3);
                           \\end{tikzpicture}
                           \\end{center}
                           Dựa vào bảng biến thiên, ta thấy trên khoảng $[0; %s)$, đạo hàm $R\'(x) < 0$ nên hàm số nghịch biến (doanh thu giảm).\\\\
                           Trên khoảng $(%s; %s)$, đạo hàm $R\'(x) > 0$ nên hàm số đồng biến, tức là doanh thu bắt đầu tăng từ điểm cực tiểu $x = %s$ (ngàn sản phẩm).\\\\
                           Đổi ra đơn vị sản phẩm ta được:\\\\
                           $%s \\cdot 1000 = %s \\text{ sản phẩm}$.\\\\
                           Vậy số lượng sản phẩm tối thiểu phải bán ra để doanh thu bắt đầu tăng là $%s$ sản phẩm.'''
                           % (ham_so_latex, dao_ham_latex, dao_ham_latex, latex(x1), latex(x2),
                              latex(x1), latex(x2),
                              latex(x1), latex(x1), latex(x2), latex(x1),
                              latex(x1), latex(kq), latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

