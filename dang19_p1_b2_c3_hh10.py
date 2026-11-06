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


def bt_dang19_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khởi tạo các biến ký hiệu
            x, y = symbols('x y')

            # --- B3: TƯ DUY RANDOM ---
            # Để đảm bảo số đẹp, ta chọn giao điểm M trước
            xm, ym = random.randint(-3, 3), random.randint(-3, 3)
            M = (xm, ym)

            # Chọn các hệ số pháp tuyến của d1 và d2 (đảm bảo không song song)
            while True:
                a1, b1 = random.randint(-3, 3), random.randint(-3, 3)
                a2, b2 = random.randint(-3, 3), random.randint(-3, 3)
                if a1*b2 != a2*b1 and (a1!=0 or b1!=0) and (a2!=0 or b2!=0):
                    break

            # Tính hằng số c1, c2 dựa trên điểm M
            c1 = -(a1*xm + b1*ym)
            c2 = -(a2*xm + b2*ym)

            d1 = a1*x + b1*y + c1
            d2 = a2*x + b2*y + c2

            # --- B2: GIẢI CHI TIẾT ---
            # 1. Tìm giao điểm M (đã có ở trên, nhưng giải hệ để trình bày lời giải)
            # 2. Lấy điểm A trên d1. Cho x_a = xm + một khoảng nào đó để khác M
            xa = xm + random.choice([-2, -1, 1, 2])
            # Giải a1*xa + b1*ya + c1 = 0 => ya
            if b1 != 0:
                ya = Rational(-a1*xa - c1, b1)
            else: # Nếu b1=0 thì d1 là đường thẳng đứng, chọn ya bất kỳ
                xa = Rational(-c1, a1)
                ya = ym + 1
            A = (xa, ya)

            # 3. Tìm đường thẳng AH vuông góc d2 qua A
            # d2: a2*x + b2*y + c2 = 0 => AH: b2(x-xa) - a2(y-ya) = 0
            ah_eq = b2*(x - xa) - a2*(y - ya)

            # 4. Tìm tọa độ H là giao của AH và d2
            sol_h = sp.solve([ah_eq, d2], [x, y])
            xh, yh = sol_h[x], sol_h[y]

            # 5. Tìm B đối xứng A qua H: B = 2H - A
            xb, yb = 2*xh - xa, 2*yh - ya

            # 6. Viết phương trình d3 qua M và B
            # (y - ym)(xb - xm) = (x - xm)(yb - ym)
            d3_raw = (y - ym)*(xb - xm) - (x - xm)*(yb - ym)
            d3 = sp.simplify(d3_raw)

            # Chuẩn hóa phương trình d3: ax + by + c = 0
            coeffs = d3.as_coefficients_dict()
            # Lấy mẫu số chung để đưa về số nguyên
            from sympy import content
            final_d3 = d3 * sp.lcm([sp.denom(val) for val in coeffs.values()])
            # Đảm bảo hệ số x dương cho đẹp
            if final_d3.coeff(x) < 0 or (final_d3.coeff(x) == 0 and final_d3.coeff(y) < 0):
                final_d3 = -final_d3

            # --- TẠO NỘI DUNG ---
            noidungcauhoi = r"Cho hai đường thẳng $d_1: %s = 0$ và $d_2: %s = 0$. Phương trình của đường thẳng $d_3$ đối xứng với $d_1$ qua $d_2$ là" % (latex(d1), latex(d2))

            da_d = r"\True $%s = 0$" % latex(final_d3)
            # Tạo đáp án nhiễu bằng cách đổi dấu hoặc đổi hệ số tự do
            da_s1 = r"$%s = 0$" % latex(final_d3 + random.randint(1, 5))
            da_s2 = r"$%s = 0$" % latex(sp.simplify(final_d3 - 2*final_d3.coeff(x)*x))
            da_s3 = r"$%s = 0$" % latex(final_d3 - random.randint(1, 5))

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            loigiai = r"""Giao điểm $M(x;y)$ của $d_1$ và $d_2$ có tọa độ là nghiệm của hệ:\\
            $\begin{cases} %s = 0 \\ %s = 0 \end{cases} \Leftrightarrow \begin{cases} x = %s \\ y = %s \end{cases} \Rightarrow M(%s;%s)$. \\
            Lấy $A(%s;%s)$ thuộc $d_1$, phương trình đường thẳng $AH$ vuông góc với $d_2$ là:\\
            $%s = 0 \Leftrightarrow %s = 0$. \\
            Tọa độ $H$ là nghiệm của hệ:\\
            $\begin{cases} %s = 0 \\ %s = 0 \end{cases} \Leftrightarrow \begin{cases} x = %s \\ y = %s \end{cases} \Rightarrow H\left(%s;%s\right) \Rightarrow B\left(%s;%s\right)$. \\
            Phương trình đường thẳng $d_3$ đi qua $M$ và $B$ là: $%s = 0$.""" % (
                latex(d1), latex(d2), latex(xm), latex(ym), latex(xm), latex(ym),
                latex(xa), latex(ya), latex(ah_eq), latex(sp.simplify(ah_eq)),
                latex(sp.simplify(ah_eq)), latex(d2), latex(xh), latex(yh), latex(xh), latex(yh), latex(xb), latex(yb),
                latex(final_d3)
            )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

